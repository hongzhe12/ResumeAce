# job_scraper.py
import csv
from datetime import datetime
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from src.simpe_log import logger


def create_poco():
    """初始化Poco"""
    auto_setup(__file__)
    return AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def parse_job_page(poco):
    """解析工作详情页并截图"""
    try:
        # 获取岗位信息
        job_name = poco("com.hpbr.bosszhipin:id/tv_job_name").get_text()
        job_salary = poco("com.hpbr.bosszhipin:id/tv_job_salary").get_text()
        location = poco("com.hpbr.bosszhipin:id/tv_required_location").get_text()
        boss_name = poco("com.hpbr.bosszhipin:id/tv_boss_name").get_text()
        description = poco("com.hpbr.bosszhipin:id/tv_description").attr('text') if \
            poco("com.hpbr.bosszhipin:id/tv_description").exists() else "暂无描述"

        # 截图并保存
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_filename = f"screenshot/screenshot_{timestamp}.png"
        snapshot(screenshot_filename)

        # 记录时间和日志
        log_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(log_timestamp + " " + "".join([job_name, job_salary, location, boss_name, description]))

        return {
            'job_name': job_name,
            'salary': job_salary,
            'location': location,
            'boss_name': boss_name,
            'description': description,
            'screenshot': screenshot_filename
        }
    except Exception as e:
        print(f"解析页面失败: {e}")
        return None


# 更新 save_to_csv 函数以包含截图列
def save_to_csv(data):
    """保存数据到CSV文件"""
    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{current_date}_jobs.csv"

    # 检查文件是否存在
    file_exists = False
    try:
        with open(filename, 'r', encoding='utf-8'):
            file_exists = True
    except FileNotFoundError:
        pass

    # 写入数据
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['job_name', 'salary', 'location', 'boss_name', 'description', 'screenshot']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 如果文件不存在，写入表头
        if not file_exists:
            writer.writeheader()

        # 写入数据行
        writer.writerow(data)

    print(f"数据已保存到 {filename}")


def swipe_to_next(poco):
    """滑动到下一个岗位"""
    try:
        tv_job_name = poco("com.hpbr.bosszhipin:id/tv_job_name")
        tv_job_name.swipe([-0.9, -0.1], duration=0.1)
        time.sleep(0.7)
    except Exception as e:
        print(f"滑动失败: {e}")


def scrape_jobs(num_jobs=10):
    """爬取指定数量的岗位数据"""
    # 初始化
    poco = create_poco()
    start_app("com.hpbr.bosszhipin")

    for i in range(num_jobs):
        print(f"正在爬取第 {i + 1} 个岗位...")

        # 解析当前页面
        job_data = parse_job_page(poco)

        if job_data:
            # 保存数据
            save_to_csv(job_data)
            print(f"已爬取岗位: {job_data['job_name']}")
        else:
            print("未能获取岗位信息")

        # 滑动到下一个岗位
        swipe_to_next(poco)


if __name__ == "__main__":

    def cleanup_screenshots_and_csv():
        """
        清理截图文件夹中的所有文件，并删除指定的CSV文件
        """
        # 搜索路径下全部的csv文件
        csv_files = [f for f in os.listdir(r'C:\Users\canway\PycharmProjects\ResumeAce\src') if f.endswith(".csv")]

        for i in csv_files:
            # 删除CSV文件
            if os.path.exists(i):
                try:
                    os.remove(i)
                    print(f"已删除文件: {i}")
                except Exception as e:
                    print(f"删除CSV文件时出错: {e}")
            else:
                print(f"CSV文件不存在: {i}")


    cleanup_screenshots_and_csv()

    # 爬取100个岗位数据
    scrape_jobs(50)
    # 连接手机 "C:/Users/canway/PycharmProjects/ResumeAce/.venv/Lib/site-packages/airtest/core/android/static/adb/windows/adb.exe" connect 192.168.0.104:41125
