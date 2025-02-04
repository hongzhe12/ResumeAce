# -*- encoding=utf8 -*-
__author__ = "hongzhe"

import logging
import sys

from PySide6.QtCore import QThread, Signal, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from drawermenu import DrawerMenu
from ui_main_window import Ui_MainWindow

# 配置日志输出到文件
log_file = "task_log.txt"
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


def add_task(task):
    """
    向任务队列添加任务
    """
    task_queue.append(task)
    logger.info(f"任务已添加到队列: {task.__name__}")


def execute_task(task):
    """
    执行任务并处理异常
    """
    try:
        logger.info(f"开始执行任务: {task.__name__}")
        task()  # 执行任务
        logger.info(f"任务执行成功: {task.__name__}")
    except Exception as e:
        logger.error(f"任务执行失败: {task.__name__} - 错误: {e}")
        rollback_task(task)  # 回滚操作
        return False
    return True


def rollback_task(task):
    """
    任务失败时的回滚操作
    这里你可以根据任务的类型来定义回滚操作
    """
    logger.info(f"任务失败，开始回滚: {task.__name__}")
    swipe_left()


def swipe_left():
    """
    向左滑动
    """
    tv_job_name = poco("com.hpbr.bosszhipin:id/tv_job_name", type="android.widget.TextView")
    tv_job_name.swipe([-0.9, -0.1], duration=0.1)


def parse_page():
    """
    解析工作详情页
    """
    try:
        tv_job_name = poco("com.hpbr.bosszhipin:id/tv_job_name", type="android.widget.TextView")
        tv_description = poco("com.hpbr.bosszhipin:id/tv_description").attr('text') if poco(
            "com.hpbr.bosszhipin:id/tv_description").exists() else "暂无描述"
        btn_chat = poco("com.hpbr.bosszhipin:id/btn_chat")
    except Exception as e:
        logger.error(f"控件查找失败: {e}")
        return None, None

    if btn_chat:
        job_name = tv_job_name.get_text() if tv_job_name else ''
        return tv_description, btn_chat, job_name

    return None, None, None


def filter_job_title(job_name, job_key):
    """
    根据用户提供的筛选规则对职位标题进行筛选
    返回 True 表示符合筛选条件，False 表示不符合
    """
    for key in job_key:
        if key in job_name:
            return True
    return False


def task_job(job_key):
    """
    任务：解析页面内容并执行聊天操作
    """
    content, btn_chat, job_name = parse_page()
    if content and btn_chat and job_name:
        logger.info(f"职位名称：: {job_name}")
        logger.info(f"岗位描述: {content}")
    if content and job_name:
        if filter_job_title(job_name, job_key):  # 筛选标题是否符合条件
            logger.info(f"职位标题符合筛选条件: {job_name}")
            logger.info(f"解析到内容: {content}")
            btn_chat.click()  # 打招呼
            time.sleep(0.5)  # 等待页面加载
            keyevent("BACK")  # 返回详情页
            time.sleep(0.1)  # 等待页面加载
            swipe_left()  # 向左滑动
            time.sleep(1.5)  # 等待页面加载
        else:
            logger.info(f"职位标题不符合筛选条件，跳过: {job_name}")
            swipe_left()
    else:
        logger.error("找不到控件，任务失败")  # 如果没有找到控件，任务失败
        raise Exception("找不到控件，任务失败")


# PySide6界面部分
class TaskWorker(QThread):
    """
    后台任务线程类，用于处理任务队列
    """
    task_completed = Signal(str)  # 任务完成信号
    task_failed = Signal(str)  # 任务失败信号
    progress_updated = Signal(int)  # 进度更新信号

    def __init__(self, job_key, num_tasks):
        super().__init__()
        self.job_key = job_key
        self.num_tasks = num_tasks

    def run(self):
        # 执行队列中的任务
        for i in range(self.num_tasks):
            add_task(lambda: task_job(self.job_key))
            if execute_task(task_queue[i]):
                self.task_completed.emit(f"任务 {i + 1} 执行成功")
            else:
                self.task_failed.emit(f"任务 {i + 1} 执行失败")
            self.progress_updated.emit((i + 1) * 100 // self.num_tasks)


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        # 创建 UI 类的实例
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 设置 UI 布局

        # 连接信号和槽
        self.ui.add_task_button.clicked.connect(self.add_task)
        self.ui.start_button.clicked.connect(self.start_tasks)
        self.ui.open_log_button.clicked.connect(self.open_log_file)
        self.ui.stop_button.clicked.connect(self.stop_tasks)
        self.ui.add_group.clicked.connect(self.add_group)

        # 创建抽屉式菜单
        self.drawer_menu = DrawerMenu(self)

        # 追加样式
        current_stylesheet = self.drawer_menu.styleSheet()

        # 向侧边栏添加按钮
        self.button1 = QPushButton("主页")

        self.button1.setMinimumSize(180, 50)
        self.button2 = QPushButton("设置")
        self.button3 = QPushButton("关于")
        self.button1.setStyleSheet("""   QPushButton {
       border-width: 0px;
       border-style: none;
       border-color: transparent;
	   border-radius:8px;
	   color: rgb(255, 255, 255);
	   background-color: rgb(65, 168, 99);
   }""")
        self.drawer_menu.add_widget(self.button1)
        self.drawer_menu.add_widget(self.button2)
        self.drawer_menu.add_widget(self.button3)






    def add_group(self):
        """浏览器跳转打开加群链接"""
        url = QUrl("https://qm.qq.com/q/Xdw4VIAIAo")
        QDesktopServices.openUrl(url)

    def stop_tasks(self):
        """
        停止后台任务
        """
        if hasattr(self, 'worker') and self.worker.isRunning():
            self.worker.terminate()  # 停止任务线程
            self.ui.log_output.append("任务已停止")
        else:
            self.ui.log_output.append("没有正在运行的任务")

    def open_log_file(self):
        """
        打开日志文件
        """
        # 读取日志文件并在文本框中显示
        try:
            with open(log_file, 'r', encoding='utf-8') as file:
                log_content = file.read()
            self.ui.log_output.setPlainText(log_content)
        except Exception as e:
            self.ui.log_output.append(f"无法打开日志文件: {e}")


    def add_task(self):
        """
        向队列添加任务
        """
        filter_text = self.ui.filter_input.text()
        job_key = filter_text.split(" ") if filter_text else []
        num_tasks = self.ui.num_tasks_input.value()

        for _ in range(num_tasks):
            add_task(lambda: task_job(job_key))

        self.ui.log_output.append(f"已添加 {num_tasks} 个任务，筛选规则: {job_key}")

    def start_tasks(self):
        """
        启动后台任务线程
        """
        filter_text = self.ui.filter_input.text()

        job_key = filter_text.split(",") if filter_text else []
        num_tasks = self.ui.num_tasks_input.value()

        self.worker = TaskWorker(job_key, num_tasks)
        self.worker.task_completed.connect(self.on_task_completed)
        self.worker.task_failed.connect(self.on_task_failed)
        self.worker.progress_updated.connect(self.update_progress)

        # 在开始执行任务之前初始化Poco
        auto_setup(__file__)  # 初始化Poco
        global poco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

        self.worker.start()

    def on_task_completed(self, message):
        self.ui.log_output.append(f"任务完成: {message}")

    def on_task_failed(self, message):
        self.ui.log_output.append(f"任务失败: {message}")

    def update_progress(self, progress):
        self.ui.progress_bar.setValue(progress)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
