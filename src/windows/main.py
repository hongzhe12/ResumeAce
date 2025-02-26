# -*- encoding=utf8 -*-
__author__ = "hongzhe"

import json
import logging
import re
import socket
import subprocess
import sys
import webbrowser
from datetime import datetime
from typing import List, Union, Any

import requests
from PySide6.QtCore import QThread, QUrl, QSize, QTimer, QEvent
from PySide6.QtCore import Qt
from PySide6.QtGui import QDesktopServices, QClipboard, QIcon
from PySide6.QtGui import QPixmap
from PySide6.QtSql import QSqlQuery, QSqlDatabase
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, \
    QTextEdit, QDialog
from PySide6.QtWidgets import QMessageBox
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.proxy import UIObjectProxy
from sparkai.core.outputs import LLMResult
from sparkai.llm.llm import ChunkPrintHandler

from src.api import get_xinghuo_response
from src.core import ChatBox, ElWindow, DrawerMenu, InputFormDialog,ElTitleBar
from ui_form import Ui_Form


# 配置日志输出到文件
log_file = "../../log/task_log.txt"
logger = logging.getLogger("airtest")
logger.setLevel(logging.DEBUG)  # 设置日志级别为 DEBUG

# 创建文件处理器，日志写入到文件
file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 添加处理器到日志器
logger.addHandler(file_handler)

# 任务队列
task_queue = []

global poco
poco = None

ADB_PATH = "adb"  # 开发环境

# ADB_PATH = r"..\python-embed\Lib\site-packages\airtest\core\android\static\adb\windows\adb.exe"

# 定义按钮样式表
btn_style = '''/* 按钮样式 */
QPushButton {
    background-color: #1296db; /* 按钮背景颜色 */
    color: white; /* 按钮文字颜色 */
    border: none; /* 去除边框 */
    border-radius: 5px; /* 按钮圆角 */
    padding: 8px 10px; /* 按钮内边距 */
    min-width: 80px; /* 按钮最小宽度 */
}

QPushButton:hover {
    background-color: #0d7ab4; /* 鼠标悬停时按钮背景颜色 */
}

QPushButton:pressed {
    background-color: #0a608e; /* 按钮按下时背景颜色 */
}'''


# 连接到 SQLite 数据库
def create_connection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db_path = "../db/user_info.db"
    db.setDatabaseName(db_path)
    if not db.open():
        print("无法打开数据库")
        return False
    # 创建用户信息表（如果不存在）
    query = QSqlQuery()
    query.exec('''
        CREATE TABLE IF NOT EXISTS user_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT
        )
    ''')
    return True


# 获取存储的用户名
def get_stored_username():
    query = QSqlQuery()
    query.exec('SELECT username FROM user_info ORDER BY id DESC LIMIT 1')
    if query.next():
        return query.value(0)
    return None


# 保存用户名到数据库
def save_username(username):
    query = QSqlQuery()
    query.prepare('INSERT INTO user_info (username) VALUES (:username)')
    query.bindValue(':username', username)
    if not query.exec():
        print("保存用户名失败")


from PySide6.QtCore import QObject, Signal


class ExcThread(QObject):
    # 定义信号
    is_finish = Signal(bool)

    def __init__(self):
        super().__init__()

    def run(self):
        if not is_scrcpy_running():
            # 使用 subprocess.Popen 非阻塞地启动 scrcpy.exe
            subprocess.Popen([os.path.join("scrcpy-win64-v3.1", "scrcpy.exe")],
                             creationflags=subprocess.CREATE_NO_WINDOW)
            self.is_finish.emit(True)


class StreamingChunkHandler(ChunkPrintHandler):
    def __init__(self, signal):
        self.signal = signal
        super().__init__()

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.signal.emit(token)


class ChatThread(QObject):
    # 定义信号
    result = Signal(str)

    def __init__(self, message):
        super().__init__()
        self.message = message

    def run(self):
        # 调用星火大模型接口
        res = get_xinghuo_response(self.message)

        # 从结果中提取回复文本
        if isinstance(res, LLMResult):
            # 通常 generations 是一个二维列表，这里假设取第一个生成结果
            first_generation = res.generations[0][0]
            reply_text = first_generation.text
            self.result.emit(reply_text)
        else:
            print("结果不是 LLMResult 类型")
            self.result.emit("不好意思，正在学习中...")


import psutil


def is_scrcpy_running():
    # 遍历所有正在运行的进程
    for proc in psutil.process_iter(['name']):
        try:
            # 检查进程名称是否为 scrcpy.exe
            if proc.info['name'] == 'scrcpy.exe':
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def is_range_within(range1, range2):
    # range1 岗位薪资
    # range2 筛选薪资

    raw_range1 = range1  # 复制一份，后续做判断

    res1 = re.search('\d+\-\d+', range1)
    if res1:
        range1 = res1.group(0)

    if "K" in raw_range1 or 'k' in raw_range1:
        temp = [f'{int(range1.split("-")[0]) * 1000}', f'{int(range1.split("-")[1]) * 1000}']
        range1 = "-".join(temp)

    # 解析第一个范围
    try:
        min1, max1 = map(int, range1.split('-'))
    except ValueError:
        print(f"输入的范围 {range1} 格式不正确，请使用 '最小值-最大值' 的格式。")
        return False

    # 解析第二个范围
    try:
        min2, max2 = map(int, range2.split('-'))
    except ValueError:
        print(f"输入的范围 {range2} 格式不正确，请使用 '最小值-最大值' 的格式。")
        return False

    # 判断第一个范围是否在第二个范围内
    return min2 <= min1 and max1 <= max2


def check_android_connection() -> bool:
    """检查Android设备是否连接"""
    try:
        result = subprocess.run(
            [ADB_PATH, 'devices'],
            capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
        )

        output = result.stdout

        # 解析输出，判断是否有设备连接
        lines = output.strip().split('\n')[1:]  # 去掉第一行标题

        return any(line.strip() and 'device' in line for line in lines)
    except Exception as e:
        logger.error(f"检查连接时出错: {e}")
        return False


def add_task(task):
    """向任务队列添加任务"""
    task_queue.append(task)


def execute_task(task) -> bool:
    """执行任务并处理异常"""
    try:
        task()  # 执行任务
        return True
    except Exception as e:
        logger.error(f"任务执行失败: {task.__name__} - 错误: {e}")
        rollback_task(task)  # 回滚操作
        return False


def rollback_task(task):
    """任务失败时的回滚操作"""
    logger.info(f"任务失败，开始回滚: {task.__name__}")
    swipe_left()


def swipe_left():
    """向左滑动"""
    tv_job_name = poco("com.hpbr.bosszhipin:id/tv_job_name", type="android.widget.TextView")
    tv_job_name.swipe([-0.9, -0.1], duration=0.1)


def parse_page() -> Union[tuple[None, None, None], tuple[Union[str, Any], UIObjectProxy, str, str, str, str]]:
    """解析工作详情页"""
    try:
        tv_job_name = poco("com.hpbr.bosszhipin:id/tv_job_name", type="android.widget.TextView")
        tv_description = poco("com.hpbr.bosszhipin:id/tv_description").attr('text') if poco(
            "com.hpbr.bosszhipin:id/tv_description").exists() else "暂无描述"
        btn_chat = poco("com.hpbr.bosszhipin:id/btn_chat")

        job_salary = poco("com.hpbr.bosszhipin:id/tv_job_salary").get_text()
        location = poco("com.hpbr.bosszhipin:id/tv_required_location").get_text()
        boss_name = poco("com.hpbr.bosszhipin:id/tv_boss_name").get_text()


    except Exception as e:
        logger.error(f"控件查找失败: {e}")
        return None, None, None

    if btn_chat:
        job_name = tv_job_name.get_text() if tv_job_name else ''
        return tv_description, btn_chat, job_name, job_salary, location, boss_name

    return None, None, None


def filter_job_title(job_name: str, job_key: List[str]) -> bool:
    """根据用户提供的筛选规则对职位标题进行筛选"""
    return any(key in job_name for key in job_key)


def filter_job(content: str, job_key: List[str]) -> bool:
    """根据用户提供的筛选规则对职位标题进行筛选"""
    return any(key in content for key in job_key)


import csv


def append_to_csv(file_path, data: list, header=None) -> None:
    """
    该函数用于将数据追加写入到指定的 CSV 文件中。

    :param file_path: 要写入的 CSV 文件的路径
    :param data: 要写入的数据，应为可迭代对象，如列表或元组，其中每个元素代表一行数据
    :param header: 可选参数，CSV 文件的表头，为列表或元组类型
    """
    try:
        file_exists = os.path.exists(file_path)
        # 以追加模式打开 CSV 文件，使用 newline='' 避免在 Windows 系统下出现多余的空行
        with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
            # 创建一个 CSV 写入器对象
            writer = csv.writer(csvfile)
            # 如果文件不存在且提供了表头，则写入表头
            if not file_exists and header:
                writer.writerow(header)
            writer.writerow(data)
    except Exception as e:
        print(f"写入 CSV 文件时出现错误: {e}")


def task_job(job_key: List[str], job_key_2: str):
    """任务：解析页面内容并执行聊天操作"""
    content, btn_chat, job_name, job_salary, location, boss_name = parse_page()

    if content and btn_chat and job_name:
        logger.info(f"职位名称：: {job_name}")
        logger.info(f"岗位描述: {content}")
        logger.info(f"岗位薪资: {job_salary}")
        logger.info(f"工作地点: {location}")
        logger.info(f"招聘者姓名: {boss_name}")

    if content and job_name:

        if filter_job_title(job_name, job_key) and is_range_within(job_salary, job_key_2):  # 筛选标题是否符合条件
            logger.info(f"职位标题符合筛选条件: {job_name}")
            logger.info(f"解析到内容: {content}")
            btn_chat.click()  # 打招呼
            time.sleep(0.5)  # 等待页面加载
            keyevent("BACK")  # 返回详情页
            time.sleep(0.1)  # 等待页面加载
            swipe_left()  # 向左滑动
            time.sleep(1.5)  # 等待页面加载

            # 获取当前日期
            current_date = datetime.now().strftime("%Y-%m-%d")
            # 生成文件名
            file_path = f"{current_date}已投名单.csv"
            append_to_csv(file_path, [job_name, content, job_salary, location, boss_name],
                          header=["岗位名称", "工作内容", "薪水", "位置", "招聘者姓名"])
        else:
            logger.info(f"职位标题不符合筛选条件，跳过: {job_name}")

            swipe_left()
    else:
        logger.error("找不到控件，任务失败")  # 如果没有找到控件，任务失败
        raise Exception("找不到控件，任务失败")


# 获取简历投递信息
def get_resume_info():
    poco(text="我的").click()
    time.sleep(0.3)
    contacts_number = poco('com.hpbr.bosszhipin:id/tv_geek_contacts_number').get_text()
    post_resume_number = poco('com.hpbr.bosszhipin:id/tv_geek_post_resume_number').get_text()
    interview_count = poco('com.hpbr.bosszhipin:id/tv_interview_count').get_text()
    return contacts_number, post_resume_number, interview_count


# 更新用户数据到排行榜
def push_resume_rank():
    # api域名
    BASE_URL = 'http://47.113.186.186'
    # 用户昵称
    # 连接到 SQLite 数据库
    create_connection()
    username = get_stored_username()

    if username is None:
        username = socket.gethostname()
    # 沟通数量、已投简历、待面试
    contacts_number, post_resume_number, interview_count = get_resume_info()
    # 头像
    avatar = 'static/images/t1.jpg'
    # 趋势
    trend = 0

    # 更新用户数据
    update_url = f'{BASE_URL}/api/user/{username}/update'
    update_data = {
        "chat_count": contacts_number,
        "resume_count": post_resume_number,
        "interview_count": interview_count
    }
    try:
        update_response = requests.put(update_url, json=update_data)
        update_response.raise_for_status()  # 检查请求是否成功
        print("\n更新用户数据:")
        print(json.dumps(update_response.json(), ensure_ascii=False, indent=2))

        # 刷新榜单
        refresh_url = f'{BASE_URL}/api/rankings/refresh'
        refresh_response = requests.post(refresh_url)
        refresh_response.raise_for_status()  # 检查请求是否成功
        print("\n刷新榜单:")
        print(json.dumps(refresh_response.json(), ensure_ascii=False, indent=2))
    except requests.RequestException as e:
        print(f"请求出错: {e}")
    except ValueError:
        print("响应数据不是有效的JSON格式")


class LogDisplayWindow(QWidget):
    def __init__(self, log_content):
        super().__init__()
        self.setWindowTitle("日志显示窗口")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        # 创建一个 QTextEdit 用于显示日志内容
        self.log_text_edit = QTextEdit()
        self.log_text_edit.setReadOnly(True)
        self.log_text_edit.setPlainText(log_content)
        layout.addWidget(self.log_text_edit)

        # 创建一个关闭按钮
        close_button = QPushButton("关闭")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button, alignment=Qt.AlignRight)

        self.setLayout(layout)

        # 将窗口移动到屏幕中间
        self.move_to_center()

    def move_to_center(self):
        # 获取屏幕的几何信息
        screen_geometry = QApplication.primaryScreen().geometry()
        # 获取窗口的几何信息
        window_geometry = self.frameGeometry()
        # 计算窗口居中时左上角的坐标
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        # 移动窗口到计算好的位置
        self.move(window_geometry.topLeft())


class TaskWorker(QThread):
    """后台任务线程类，用于处理任务队列"""
    task_completed = Signal(str)  # 任务完成信号
    task_failed = Signal(str)  # 任务失败信号
    progress_updated = Signal(int)  # 进度更新信号

    def __init__(self, num_tasks: int):
        super().__init__()
        self.num_tasks = num_tasks

    def run(self):

        auto_setup(__file__)  # 初始化Poco
        global poco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

        # 执行队列中的任务
        for i in range(self.num_tasks):
            if execute_task(task_queue[i]):
                self.task_completed.emit(f"任务 {i + 1} 执行成功")
            else:
                self.task_failed.emit(f"任务 {i + 1} 执行失败")
            self.progress_updated.emit((i + 1) * 100 // self.num_tasks)


class RankWorker(QThread):
    """后台任务线程类，用于处理任务队列"""
    task_completed = Signal(bool)  # 任务完成信号

    def __init__(self):
        super().__init__()

    def run(self):
        global poco
        if check_android_connection():
            print("连接正常！")
            auto_setup(__file__)  # 初始化Poco
            poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

        # 非阻塞执行ADB命令
        start_app("com.hpbr.bosszhipin")
        time.sleep(0.5)
        # 更新排行榜
        push_resume_rank()
        self.task_completed.emit(True)


class EnterKeyFilter(QObject):
    def __init__(self, target, callback):
        super().__init__()
        self.target = target
        self.callback = callback

    def eventFilter(self, obj, event):
        if obj == self.target and event.type() == QEvent.KeyPress:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                # 触发回调函数
                self.callback()
                # 阻止事件继续传播
                return True
        # 其他事件正常处理
        return super().eventFilter(obj, event)


class MyWidget(ElWindow):
    def __init__(self):
        super().__init__()

        # 创建 UI 类的实例
        self.rw = None
        self.chat = None
        self.num_tasks = None
        self.is_chat_show = False
        self.ui = Ui_Form()

        self.ui.setupUi(self)  # 设置 UI 布局

        # 创建菜单
        self.open_log_button = QPushButton()
        self.open_log_button.setMinimumSize(QSize(0, 40))
        self.open_log_button.setText("查看日志")

        self.add_group = QPushButton()
        self.add_group.setMinimumSize(QSize(0, 40))
        self.add_group.setText("加群交流")

        self.open_csv = QPushButton()
        self.open_csv.setMinimumSize(QSize(0, 40))
        self.open_csv.setText("打开文件")

        self.show_path = QPushButton()
        self.show_path.setMinimumSize(QSize(0, 40))
        self.show_path.setText("获取更新路径")

        self.open_log_button.setStyleSheet(btn_style)
        self.add_group.setStyleSheet(btn_style)
        self.open_csv.setStyleSheet(btn_style)
        self.show_path.setStyleSheet(btn_style)

        # 创建抽屉式菜单
        self.drawer_menu = DrawerMenu(self)

        # 向侧边栏添加按钮

        self.drawer_menu.add_widget(self.open_log_button)
        self.drawer_menu.add_widget(self.add_group)
        self.drawer_menu.add_widget(self.open_csv)
        self.drawer_menu.add_widget(self.show_path)

        # 连接信号和槽
        self.ui.add_task_button.clicked.connect(self.add_task)
        self.ui.start_button.clicked.connect(self.start_tasks)
        self.ui.stop_button.clicked.connect(self.stop_tasks)
        self.ui.connect_button.clicked.connect(self.connect_phone)

        # 绑定菜单按钮的槽函数
        self.open_log_button.clicked.connect(self.open_log_file)
        self.add_group.clicked.connect(self.add_group_func)
        self.open_csv.clicked.connect(self.open_excel_file)
        self.show_path.clicked.connect(self.start_update)

        # 创建一个 QTimer 对象
        self.timer = QTimer(self)
        # 设置定时器每 3 秒触发一次
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(2000)

        # 获取布局对象
        layout = self.ui.verticalLayout
        self.cb = ChatBox()

        # 将 ChatBox 实例添加到布局的最上面
        self.ui.verticalLayout.removeWidget(self.ui.label_2)
        self.ui.verticalLayout.insertWidget(0, self.cb)
        layout.setStretchFactor(self.cb, 4)

        # 调整层级关系，将 ChatBox 放在 other_widget 后面
        self.cb.stackUnder(self.drawer_menu)
        # 初始化欢迎语句
        self.cb.send_message(False, "欢迎！连接手机后请先点击筛选输入条件！")

        # 初始化线程和工作对象
        self.thread = None
        self.wk = None

        # 隐藏输入框
        self.ui.textEdit.hide()
        # 绑定chat按钮
        self.ui.chat.clicked.connect(self.clicked_chat)
        # 创建事件过滤器实例
        self.enter_filter = EnterKeyFilter(self.ui.textEdit, self.handle_enter_press)
        # 为 QTextEdit 安装事件过滤器
        self.ui.textEdit.installEventFilter(self.enter_filter)

        # 挂载标题栏即可
        self.title_bar = ElTitleBar(self, window_title="简历助手")

        # 使用 raise_() 方法将 drawer_menu 提升到前面的层级
        self.drawer_menu.raise_()

        # 个人信息信号槽
        self.ui.person_info.clicked.connect(self.show_person_info_edit)
        # 排行榜信号槽
        self.ui.show_rank_btn.clicked.connect(self.show_rank)

    def show_rank(self):
        # 打开网站
        webbrowser.open("http://47.113.186.186/")

    def update_rank(self):
        # 弹窗确认
        reply = QMessageBox.information(self, "提示", "确认更新排行榜吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return

        # 检查线程是否存在且正在运行
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()

        # 发送消息
        self.cb.send_message(False, "正在查找app位置...")

        # 创建工作线程和工作对象
        self.rw = RankWorker()
        self.thread = QThread()

        # 将工作对象移动到线程中
        self.rw.moveToThread(self.thread)

        # 连接信号和槽
        self.thread.started.connect(self.rw.run)
        self.rw.task_completed.connect(self.update_rank_completed)

        # 启动线程
        self.thread.start()

    def update_rank_completed(self):
        self.cb.send_message(False, "成功更新排行榜！")

    # 个人信息槽函数
    def show_person_info_edit(self):
        # 连接到 SQLite 数据库
        create_connection()
        username = get_stored_username()

        import socket

        # 获取计算机名称
        computer_name = socket.gethostname()

        form_structure = [
            {"label": "姓名（用于排行榜）", "type": "text", "default": username if username else computer_name},
        ]
        dialog = InputFormDialog(form_structure, self)
        if dialog.exec() == QDialog.Accepted:
            values = dialog.get_input_values()
            new_name = values[0]
            save_username(new_name)

        self.update_rank()

    # 隐藏布局控件
    def hide_all_widgets(self, layout):
        # 遍历水平布局中的所有组件
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget:
                widget.hide()

    def handle_enter_press(self):
        # 获取用户输入
        message = self.ui.textEdit.toPlainText()
        # 清空输入框
        self.ui.textEdit.clear()
        # 发送消息到聊天框
        self.cb.send_message(True, message)

        # 检查线程是否存在且正在运行
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()

        # 创建工作线程和工作对象
        self.chat = ChatThread(message)
        self.thread = QThread()

        # 将工作对象移动到线程中
        self.chat.moveToThread(self.thread)

        # 连接信号和槽
        self.thread.started.connect(self.chat.run)
        self.chat.result.connect(self.receive_chat)

        # 线程结束时进行清理
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.chat.deleteLater)

        # 启动线程
        self.thread.start()

    def receive_chat(self, content):

        self.cb.send_message(False, content)

    def clicked_chat(self):
        if not self.is_chat_show:
            # 隐藏进度条
            self.ui.progress_bar.hide()
            # 显示输入框
            self.ui.textEdit.show()

            self.is_chat_show = True
        else:
            # 显示进度条
            self.ui.progress_bar.show()
            # 隐藏输入框
            self.ui.textEdit.hide()

            self.is_chat_show = False

    def start_update(self):
        # 显示文件所在路径
        path = os.path.dirname(os.path.abspath(__file__))
        clipboard = QClipboard()
        clipboard.setText(path)
        # 弹出复制成功
        QMessageBox.information(self, "复制成功", "路径已复制到剪贴板")

    def open_excel_file(self):
        # 获取当前日期
        current_date = datetime.now().strftime("%Y-%m-%d")
        # 生成文件名
        file_path = f"{current_date}已投名单.csv"
        os.startfile(file_path)

    def connect_phone(self):
        # 自定义数据结构，用于描述表单字段
        form_structure = [
            {"label": "IP地址和端口", "type": "text"},
        ]
        dialog = InputFormDialog(form_structure, self)
        if dialog.exec() == QDialog.Accepted:
            values = dialog.get_input_values()

            # 获取用户输入的IP
            ipaddress = values[0]

            result = subprocess.run(
                [ADB_PATH, 'connect', ipaddress],
                capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )

    def on_timeout(self):

        # 每次定时器触发时更新标签内容
        if check_android_connection():
            # 加载图像
            # pixmap = QPixmap(":/icons/images/正常.png")
            # pixmap = pixmap.scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio)
            # self.ui.label.setPixmap(pixmap)
            # self.ui.label.setFixedSize(16, 16)
            # self.ui.label.setAlignment(Qt.AlignCenter)

            # 检查线程是否存在且正在运行
            if self.thread and self.thread.isRunning():
                return

            # 创建工作线程和工作对象
            self.wk = ExcThread()
            self.thread = QThread()

            # 将工作对象移动到线程中
            self.wk.moveToThread(self.thread)

            # 连接信号和槽
            self.thread.started.connect(self.wk.run)
            self.wk.is_finish.connect(lambda res: print("打开成功") if res else print("打开失败"))

            # 启动线程
            self.thread.start()

        else:
            # 加载图像
            pixmap = QPixmap(":/icons/images/err.png")
            pixmap = pixmap.scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio)
            # self.ui.label.setPixmap(pixmap)
            # self.ui.label.setFixedSize(16, 16)
            # self.ui.label.setAlignment(Qt.AlignCenter)

        # self.ui.label.update()  # 或使用 repaint()

    def check_connection(self):
        """检查Android设备连接状态"""
        if check_android_connection():
            self.ui.statusbar.showMessage("已连接到 Android 设备", 5000)
        else:
            self.ui.statusbar.showMessage("未连接到 Android 设备", 5000)

    def add_group_func(self):
        """浏览器跳转打开加群链接"""
        url = QUrl("https://qm.qq.com/q/Xdw4VIAIAo")
        QDesktopServices.openUrl(url)

    def stop_tasks(self):
        """停止后台任务"""
        if hasattr(self, 'worker') and self.worker.isRunning():
            self.worker.terminate()  # 停止任务线程
            # self.ui.log_output.append("任务已停止")  # 待修改
            self.cb.send_message(False, "任务已停止")

        else:
            # self.ui.log_output.append("没有正在运行的任务") # 待修改
            self.cb.send_message(False, "没有正在运行的任务")

    def open_log_file(self):
        """打开日志文件"""
        try:
            with open(log_file, 'r', encoding='utf-8') as file:
                log_content = file.read()
            # self.ui.log_output.setPlainText(log_content) # 待修改

            # 创建并显示日志显示窗口
            self.log_window = LogDisplayWindow(log_content)
            self.log_window.show()

        except Exception as e:
            # self.ui.log_output.append(f"无法打开日志文件: {e}") # 待修改
            error_message = f"无法打开日志文件: {e}"
            self.log_window = LogDisplayWindow(error_message)
            self.log_window.show()

    def add_task(self):
        """向队列添加任务"""
        # filter_text = self.ui.filter_input.text()
        # filter_text_2 = self.ui.filter_input_2.text()
        # num_tasks = self.ui.num_tasks_input.value()

        # 自定义数据结构，用于描述表单字段
        form_structure = [
            {"label": "筛选标题(多个关键词空格隔开)", "type": "text"},
            {"label": "筛选薪水(例如5000-10000)", "type": "text", "default": "5000-10000"},
            {"label": "任务数量", "type": "spinbox", "default": 100},
        ]
        dialog = InputFormDialog(form_structure, self)
        if dialog.exec() == QDialog.Accepted:
            values = dialog.get_input_values()
            # 标题
            filter_text = values[0]
            # 薪水
            filter_text_2 = values[1]
            # 任务数量
            self.num_tasks = values[2]

            job_key = filter_text.split(" ") if filter_text else []
            job_key_2 = filter_text_2 if filter_text_2 else None
        else:
            return

        task_queue.clear()
        for _ in range(self.num_tasks):
            add_task(lambda: task_job(job_key, job_key_2))

        # self.ui.log_output.append(f"已添加 {num_tasks} 个任务，标题: {job_key}，薪水：{job_key_2}") # 待修改
        self.cb.send_message(False, f"已添加 {self.num_tasks} 个任务，标题: {'、'.join(job_key)}，薪水：{job_key_2}")

    def start_tasks(self):
        """启动后台任务线程"""
        num_tasks = self.num_tasks

        self.worker = TaskWorker(num_tasks)
        self.worker.task_completed.connect(self.on_task_completed)
        self.worker.task_failed.connect(self.on_task_failed)
        self.worker.progress_updated.connect(self.update_progress)

        self.worker.start()
        # self.ui.statusbar.showMessage("等待大约30秒，正在初始化...", 5000)
        self.cb.send_message(True, f"任务开始启动，请等待大约30秒，正在初始化...")

    def on_task_completed(self, message):
        """任务完成时的处理"""
        # self.ui.log_output.append(f"任务完成: {message}") # 待修改
        self.cb.send_message(False, f"任务完成: {message}")

    def on_task_failed(self, message):
        """任务失败时的处理"""
        # self.ui.log_output.append(f"任务失败: {message}") # 待修改
        self.cb.send_message(False, f"任务失败: {message}")

    def update_progress(self, progress):
        """更新进度条"""
        self.ui.progress_bar.setValue(progress)


def show_disclaimer():
    disclaimer_text = """免责声明：\n  本程序仅供学习和参考使用，作者不对因使用本程序而产生的任何直接或间接损失负责。继续使用本程序即表示您同意此免责声明。"""
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle("免责声明")
    msg_box.setText(disclaimer_text)
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg_box.setDefaultButton(QMessageBox.Ok)

    # 将 OK 按钮的文本修改为“同意”
    ok_button = msg_box.button(QMessageBox.Ok)
    ok_button.setText("同意")

    # 将 Cancel 按钮的文本修改为“不同意”
    cancel_button = msg_box.button(QMessageBox.Cancel)
    cancel_button.setText("不同意")

    # 设置按钮的固定大小
    ok_button.setFixedSize(100, 30)  # 设置"同意"按钮的大小
    cancel_button.setFixedSize(100, 30)  # 设置"不同意"按钮的大小

    result = msg_box.exec()
    if result == QMessageBox.Ok:
        return True
    else:
        return False


if __name__ == "__main__":
    # 调试：C:\Users\hongz\Downloads\简历助手\python-embed\python.exe C:\Users\hongz\Downloads\简历助手\src\main.py
    # 通过 Get-ChildItem 命令获取当前目录下所有 .py 文件，再使用 ForEach-Object 对每个文件执行 pyarmor gen 命令
    # Get-ChildItem -Filter *.py | ForEach-Object { pyarmor gen $_.FullName }

    try:
        from ctypes import windll  # Only exists on Windows.

        myappid = 'mycompany.myproduct.subproduct.version'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../../resources/images/月亮.png"))
    if show_disclaimer():
        window = MyWidget()
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit()
