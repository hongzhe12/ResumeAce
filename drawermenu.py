from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QWidget, QSizePolicy
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QSize
from PySide6.QtGui import QIcon
import resources_rc

class DrawerMenu(QFrame):
    def __init__(self, parent, width=200, button_icon_path=":/icons/images/菜单.svg"):
        super().__init__(parent)
        self.parent = parent
        self.width = width
        self.is_expanded = False  # 用于跟踪侧边栏的展开状态
        self.initUI(button_icon_path)
        self.parent.resizeEvent = self.on_parent_resize

    def initUI(self, button_icon_path):
        # 设置侧边栏样式
        self.setStyleSheet("background-color: #DCDCDC;")
        self.setGeometry(-self.width, 0, self.width, self.parent.height())  # 初始位置在视图外面
        self.layout = QVBoxLayout(self)

        # 创建一个垂直方向起间隔作用的QWidget（本质利用其空白占位达到间隔效果）
        verticalSpacerWidget = QWidget()
        verticalSpacerWidget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addWidget(verticalSpacerWidget)

        # 创建一个按钮，用于切换侧边栏
        self.toggle_button = QPushButton("", self.parent)
        self.update_button_position()


        self.toggle_button.setStyleSheet("""
            QPushButton {
                border: none;  /* 去掉边框 */
                background: transparent;  /* 背景透明 */
                background-position: center;  /* 图标居中显示 */
                padding: 0px 0px; /* 按钮内边距 */
            }
            QPushButton:hover {
                background-color: #E0E0E0;  /* 鼠标悬停时背景颜色 */
            }
            QPushButton:pressed {
                background-color: #C0C0C0;  /* 鼠标按下时背景颜色 */
            }
        """)
        self.toggle_button.setIconSize(QSize(32, 32))
        self.toggle_button.setIcon(QIcon(button_icon_path))
        self.toggle_button.clicked.connect(self.toggle_drawer)

        # 创建动画效果
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

    def add_widget(self, widget):
        """向侧边栏添加控件"""
        # 在间隔控件之前添加新控件
        index = self.layout.count() - 1
        self.layout.insertWidget(index, widget)
        # 绑定收起事件
        if hasattr(widget, 'clicked'):
            widget.clicked.connect(self.toggle_drawer)

    def toggle_drawer(self):
        """切换侧边栏的展开和收起"""
        if self.is_expanded:
            self.collapse_drawer()
        else:
            self.expand_drawer()
        self.is_expanded = not self.is_expanded

    def expand_drawer(self):
        """展开侧边栏"""
        self.animation.setStartValue(QRect(-self.width, 0, self.width, self.parent.height()))
        self.animation.setEndValue(QRect(0, 0, self.width, self.parent.height()))
        self.animation.start()

    def collapse_drawer(self):
        """收起侧边栏"""
        self.animation.setStartValue(QRect(0, 0, self.width, self.parent.height()))
        self.animation.setEndValue(QRect(-self.width, 0, self.width, self.parent.height()))
        self.animation.start()

    def update_button_position(self):
        button_x = self.parent.width() - 50
        self.toggle_button.setGeometry(button_x-32-5, 0 + 10, 50, 50)

    # def update_button_position(self):
    #     parent_width = self.parent.width()
    #     parent_height = self.parent.height()
    #     button_width = 50
    #     button_height = 50
    #     margin = 10  # 距离父窗口边缘的间距
    #
    #     button_x = parent_width - button_width - margin
    #     button_y = parent_height - button_height - margin
    #
    #     self.toggle_button.setGeometry(button_x, button_y, button_width, button_height)

    def on_parent_resize(self, event):
        self.update_button_position()
        self.setGeometry(-self.width, 0, self.width, self.parent.height())
        event.accept()