from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QApplication



# 自定义标题栏
class ElTitleBar:
    def __init__(self, window: QtWidgets, window_title: str = ""):
        self.window = window
        # 默认标题栏高度 必须设
        self.DEFAULT_TITILE_BAR_HEIGHT = 40
        # 存储父类的双击事件
        self.mouseDoubleClickEvent_parent = self.window.mouseDoubleClickEvent
        # 将本类的双击事件赋值给将父类的双击事件
        self.window.mouseDoubleClickEvent = self.mouseDoubleClickEvent

        # 存储父类的窗口大小改变事件
        self.resizeEvent_parent = self.window.resizeEvent
        # 将本类的窗口大小改变事件赋值给将父类的窗口大小改变事件
        self.window.resizeEvent = self.resizeEvent

        # 设置ui文件里main_layout上边距，以免遮挡标题栏
        self.window.setContentsMargins(0, self.DEFAULT_TITILE_BAR_HEIGHT, 0, 0)

        # 1.设置无边框 和 透明背景 无边框必须设置全，不然会导致点击任务栏不能最小化窗口
        self.window.setWindowFlags(
            Qt.Window
            | Qt.FramelessWindowHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        )
        # self.window.setAttribute(Qt.WA_TranslucentBackground)
        # 2.添加自定义的标题栏到最顶部
        self.title = QLabel(window_title, self.window)
        self.title.setFont(QFont("Microsoft YaHei UI", 20))
        # 3.设置标题栏样式
        self.setStyle()
        # 4.添加按钮
        # 添加关闭按钮
        self.close_btn = QPushButton("", self.window)
        self.close_btn.setGeometry(self.window.width() - 33, 10, 20, 20)
        # 添加最大化按钮
        self.max_btn = QPushButton("", self.window)
        self.max_btn.setGeometry(self.window.width() - 66, 10, 20, 20)
        # 添加最小化按钮
        self.min_btn = QPushButton("", self.window)
        self.min_btn.setGeometry(self.window.width() - 99, 10, 20, 20)
        # 设置三个按钮的鼠标样式
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.max_btn.setCursor(Qt.PointingHandCursor)
        self.min_btn.setCursor(Qt.PointingHandCursor)
        # 设置三个按钮的样式
        self.close_btn.setStyleSheet(
            "QPushButton{border-image:url('./images/close.png');background:#ff625f;border-radius:10px;}"
            "QPushButton:hover{background:#eb4845;}"
        )
        self.max_btn.setStyleSheet(
            "QPushButton{border-image:url('./images/max.png');background:#ffbe2f;border-radius:10px;}"
            "QPushButton:hover{background:#ecae27;}"
        )
        self.min_btn.setStyleSheet(
            "QPushButton{border-image:url('./images/min.png');background:#29c941;border-radius:10px;}"
            "QPushButton:hover{background:#1ac033;}"
        )

        # 5.添加工具栏按钮事件
        # 关闭按钮点击绑定窗口关闭事件
        self.close_btn.clicked.connect(self.window.close)
        # 最大化按钮绑定窗口最大化事件
        self.max_btn.clicked.connect(self.setMaxEvent)
        # 最小化按钮绑定窗口最小化事件
        self.min_btn.clicked.connect(self.window.showMinimized)
        # 6.记录全屏窗口的大小-ps非常有用
        self.window_max_size = None
        # 7.设置标题栏鼠标跟踪 鼠标移入触发，不设置，移入标题栏不触发
        self.title.setMouseTracking(True)

    def setMaxEvent(self, flag=False):
        """
        @description  最大化按钮绑定窗口最大化事件和事件 拿出来是因为拖动标题栏时需要恢复界面大小
        @param flag 是否是拖动标题栏 bool
        @return
        """
        if flag:
            if self.window.isMaximized():
                self.window.showNormal()
                self.max_btn.setStyleSheet(
                    "QPushButton{border-image:url('./images/max.png');background:#ffbe2f;border-radius:10px;}"
                    "QPushButton:hover{background:#ecae27;}"
                )
                return self.window_max_size
            return None
        else:
            if self.window.isMaximized():
                self.window.showNormal()
                self.max_btn.setStyleSheet(
                    "QPushButton{border-image:url('./images/max.png');background:#ffbe2f;border-radius:10px;}"
                    "QPushButton:hover{background:#ecae27;}"
                )
            else:
                self.window.showMaximized()
                self.max_btn.setStyleSheet(
                    "QPushButton{border-image:url('./images/restore.png');background:#ffbe2f;border-radius:10px;}"
                    "QPushButton:hover{background:#ecae27;}"
                )
                # 记录最大化窗口的大小  用于返回最大化时拖动窗口恢复前的大小 这个程序循环帧会取不到恢复前的宽度
                self.window_max_size = QSize(self.window.width(), self.window.height())

    def setStyle(self, style: str = ""):
        """
        @description 设置自定义标题栏样式
        @param
        @return
        """
        # 想要边框 加上border:1px solid #cccccc;
        DEFAULT_STYLE = """
                            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #fafafa,stop:1 #d1d1d1);
                            color:#333333;padding:10px;border:1px solid #c6c6c6;
                            border-top-left-radius:4px;
                            border-top-right-radius:4px;
                        """
        self.title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # 设置样式
        self.title.setStyleSheet(DEFAULT_STYLE if not style else DEFAULT_STYLE + style)
        # 设置大小
        self.title.setGeometry(0, 0, self.window.width(), self.DEFAULT_TITILE_BAR_HEIGHT)

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        @description 鼠标双击事件
        @param
        @return
        """
        # 如果双击的是鼠标左键 且在标题栏范围内 则放大缩小窗口
        if a0.button() == Qt.MouseButton.LeftButton and a0.position().y() < self.title.height():
            self.setMaxEvent()
        return self.mouseDoubleClickEvent_parent(a0)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        """
        @description  窗口缩放事件
        @param
        @return
        """
        # 最大化最小化的时候，需要去改变按钮组位置
        self.close_btn.move(self.window.width() - 33, 10)
        self.max_btn.move(self.window.width() - 66, 10)
        self.min_btn.move(self.window.width() - 99, 10)
        self.title.resize(self.window.width(), self.DEFAULT_TITILE_BAR_HEIGHT)
        return self.resizeEvent_parent(a0)
