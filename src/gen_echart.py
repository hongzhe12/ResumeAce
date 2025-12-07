import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# --------------------------
# 1. 基础设置与数据读取
# --------------------------
# 设置中文字体（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取CSV数据文件
df = pd.read_csv('2025-12-08_jobs.csv')
print(f"数据读取完成，共{df.shape[0]}行数据，{df.shape[1]}列字段")


# --------------------------
# 2. 薪资数据解析函数
# --------------------------
def parse_salary(salary_str):
    """
    解析薪资字符串（如"8-12K·13薪"、"10-15K"）
    返回：最低薪资、最高薪资、平均薪资、薪资单位
    """
    # 移除"·13薪"等福利后缀，只保留核心薪资范围
    salary_str = re.sub(r'·\d+薪', '', salary_str)

    # 匹配"8-12K"格式的薪资范围
    range_match = re.search(r'(\d+)-(\d+)K', salary_str)
    if range_match:
        min_sal = int(range_match.group(1))
        max_sal = int(range_match.group(2))
        avg_sal = (min_sal + max_sal) / 2
        return min_sal, max_sal, avg_sal, 'K'

    # 匹配"10K"格式的单一薪资
    single_match = re.search(r'(\d+)K', salary_str)
    if single_match:
        sal = int(single_match.group(1))
        return sal, sal, sal, 'K'

    # 解析失败返回空值
    return None, None, None, None


# 应用解析函数，新增薪资字段
salary_parsed = df['salary'].apply(parse_salary)
df[['min_salary', 'max_salary', 'avg_salary', 'salary_unit']] = pd.DataFrame(
    salary_parsed.tolist(), index=df.index
)

# 过滤无效薪资数据（仅保留解析成功的记录）
df_salary_valid = df.dropna(subset=['avg_salary'])
print(f"薪资解析完成，有效数据{df_salary_valid.shape[0]}条")


# --------------------------
# 3. 图表1：薪资分布直方图
# --------------------------
def create_salary_histogram(data, save_path):
    """生成薪资分布直方图，展示薪资整体分布趋势"""
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']

    # 绘制直方图
    n, bins, patches = ax.hist(
        data['avg_salary'],
        bins=10,
        color=colors[0],
        alpha=0.7,
        edgecolor='white',
        linewidth=1.2
    )

    # 计算关键统计值并添加参考线
    mean_sal = data['avg_salary'].mean()
    median_sal = data['avg_salary'].median()
    ax.axvline(mean_sal, color=colors[1], linestyle='--', linewidth=2.5,
               label=f'平均薪资: {mean_sal:.1f}K')
    ax.axvline(median_sal, color=colors[2], linestyle='-.', linewidth=2.5,
               label=f'薪资中位数: {median_sal:.1f}K')

    # 图表样式设置
    ax.set_title('Java相关岗位薪资分布直方图', fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('平均薪资（K）', fontsize=14, fontweight='bold')
    ax.set_ylabel('岗位数量', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_axisbelow(True)
    ax.tick_params(axis='both', labelsize=12)
    ax.legend(fontsize=12, loc='upper right', framealpha=0.9)

    # 添加统计信息文本框
    stats_text = (f'样本总数: {len(data)}个岗位\n'
                  f'薪资范围: {data["avg_salary"].min():.1f}K - {data["avg_salary"].max():.1f}K\n'
                  f'标准差: {data["avg_salary"].std():.1f}K')
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # 保存图表
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"薪资分布直方图已保存至: {save_path}")


# 调用函数生成图表
create_salary_histogram(df_salary_valid, '薪资分布直方图.png')


# --------------------------
# 4. 图表2：薪资范围箱线图
# --------------------------
def create_salary_boxplot(data, save_path):
    """生成薪资箱线图，展示薪资离散程度与分布对比"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']

    # 左图：平均薪资箱线图
    box1 = ax1.boxplot(
        data['avg_salary'],
        patch_artist=True,
        notch=True,
        showmeans=True,
        meanprops=dict(marker='o', markerfacecolor=colors[3], markersize=8, markeredgecolor='white'),
        medianprops=dict(color=colors[1], linewidth=2.5),
        boxprops=dict(facecolor=colors[0], alpha=0.7, edgecolor='white', linewidth=1.5),
        whiskerprops=dict(color=colors[2], linewidth=2),
        capprops=dict(color=colors[2], linewidth=2)
    )

    # 左图样式与统计信息
    q1 = data['avg_salary'].quantile(0.25)
    q3 = data['avg_salary'].quantile(0.75)
    iqr = q3 - q1
    ax1.set_title('Java相关岗位平均薪资分布箱线图', fontsize=16, fontweight='bold', pad=20)
    ax1.set_ylabel('平均薪资（K）', fontsize=14, fontweight='bold')
    ax1.set_xticklabels(['平均薪资'], fontsize=12)
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.set_axisbelow(True)
    stats_text1 = (f'Q1 (25%): {q1:.1f}K\n'
                   f'中位数 (50%): {data["avg_salary"].median():.1f}K\n'
                   f'Q3 (75%): {q3:.1f}K\n'
                   f'四分位距: {iqr:.1f}K')
    ax1.text(0.02, 0.98, stats_text1, transform=ax1.transAxes, fontsize=11,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # 右图：最低/最高薪资对比箱线图
    salary_data = [data['min_salary'], data['max_salary']]
    box2 = ax2.boxplot(
        salary_data,
        patch_artist=True,
        notch=True,
        showmeans=True,
        meanprops=dict(marker='o', markerfacecolor=colors[3], markersize=8, markeredgecolor='white'),
        medianprops=dict(color=colors[1], linewidth=2.5),
        boxprops=dict(facecolor=colors[0], alpha=0.7, edgecolor='white', linewidth=1.5),
        whiskerprops=dict(color=colors[2], linewidth=2),
        capprops=dict(color=colors[2], linewidth=2)
    )

    # 为两个箱子设置不同颜色
    box_colors = [colors[0], colors[2]]
    for patch, color in zip(box2['boxes'], box_colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    # 右图样式与统计信息
    min_mean = data['min_salary'].mean()
    max_mean = data['max_salary'].mean()
    salary_gap = max_mean - min_mean
    ax2.set_title('Java相关岗位薪资范围分布对比', fontsize=16, fontweight='bold', pad=20)
    ax2.set_ylabel('薪资（K）', fontsize=14, fontweight='bold')
    ax2.set_xticklabels(['最低薪资', '最高薪资'], fontsize=12)
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_axisbelow(True)
    stats_text2 = (f'最低薪资均值: {min_mean:.1f}K\n'
                   f'最高薪资均值: {max_mean:.1f}K\n'
                   f'平均薪资差距: {salary_gap:.1f}K')
    ax2.text(0.02, 0.98, stats_text2, transform=ax2.transAxes, fontsize=11,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # 保存图表
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"薪资范围箱线图已保存至: {save_path}")


# 调用函数生成图表
create_salary_boxplot(df_salary_valid, '薪资范围箱线图.png')


# --------------------------
# 5. 图表3：各薪资区间岗位数量柱状图
# --------------------------
def create_salary_range_bar(data, save_path):
    """生成薪资区间柱状图，展示各区间岗位数量分布"""
    # 定义薪资区间与标签
    salary_bins = [5, 8, 11, 14, 17, 20]
    salary_labels = ['5-8K', '8-11K', '11-14K', '14-17K', '17-20K']

    # 划分薪资区间并统计数量
    data['salary_range'] = pd.cut(
        data['avg_salary'],
        bins=salary_bins,
        labels=salary_labels,
        include_lowest=True
    )
    range_count = data['salary_range'].value_counts().sort_index()
    range_percent = (range_count / range_count.sum() * 100).round(1)

    # 创建图表
    fig, ax = plt.subplots(figsize=(14, 9))
    colors_gradient = ['#2E86AB', '#4A9FCE', '#6BB6E0', '#8CCDF2', '#AED6F4']

    # 绘制柱状图
    bars = ax.bar(
        range_count.index,
        range_count.values,
        color=colors_gradient,
        alpha=0.8,
        edgecolor='white',
        linewidth=1.5,
        width=0.6
    )

    # 在柱子上添加数值与百分比标签
    for bar, count, percent in zip(bars, range_count.values, range_percent.values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height + 0.3,
                f'{count}个\n({percent}%)',
                ha='center', va='bottom', fontsize=12, fontweight='bold')

    # 图表样式设置
    ax.set_title('Java相关岗位各薪资区间岗位数量分布', fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('薪资区间', fontsize=14, fontweight='bold')
    ax.set_ylabel('岗位数量', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_axisbelow(True)
    ax.set_ylim(0, max(range_count.values) * 1.2)
    ax.tick_params(axis='both', labelsize=12)

    # 添加总结文本框
    max_range = range_count.idxmax()
    max_count = range_count.max()
    max_percent = range_percent[max_range]
    summary_text = (f'薪资区间分布总结：\n'
                    f'• 最多岗位集中在 {max_range} 区间\n'
                    f'• 该区间共 {max_count} 个岗位，占比 {max_percent}%\n'
                    f'• 11-14K 为薪资主流区间\n'
                    f'• 5-8K 低薪区间岗位较少')
    ax.text(0.02, 0.98, summary_text, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # 保存图表
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    # 输出统计结果
    print("\n各薪资区间统计：")
    for range_name, count in range_count.items():
        print(f"{range_name}: {count}个岗位 ({range_percent[range_name]}%)")
    print(f"各薪资区间柱状图已保存至: {save_path}")


# 调用函数生成图表
create_salary_range_bar(df_salary_valid, '各薪资区间岗位数量柱状图.png')

print("\n所有薪资相关图表生成完成！")