import enum
from dataclasses import dataclass

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPaintEvent
from PySide6.QtWidgets import QApplication, QWidget


# 边缘类型枚举
class Edge(enum.Flag):
    NoEdge: Qt.Edge = 0  # 不在边缘地带

    TopEdge: Qt.Edge = 1  # 顶部边缘
    LeftEdge: Qt.Edge = 2  # 左部边缘
    RightEdge: Qt.Edge = 3.  # 右部边缘
    BottomEdge: Qt.Edge = 4  # 底部边缘

    LeftTopEdge: Qt.Edge = 5  # 左顶部边缘
    RightTopEdge: Qt.Edge = 6  # 右顶部边缘
    LeftBottomEdge: Qt.Edge = 7  # 左底部边缘
    RightBottomEdge: Qt.Edge = 8  # 右底部边缘


# 边缘按下区域类型
@dataclass
class EdgePress:
    leftEdgePress: bool = False
    rightEdgePress: bool = False
    topEdgePress: bool = False
    bottomEdgePress: bool = False
    leftTopEdgePress: bool = False
    rightBottomEdgePress: bool = False
    leftBottomEdgePress: bool = False
    rightTopEdgePress: bool = False
    moveEdgePress: bool = False
    # 点击时的窗口初始位置
    movePosition = None


class ElWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.resize(100, 100)
        self.setWindowFlags(
            Qt.Window
            | Qt.FramelessWindowHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        )
        # 设置窗体透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 窗体边缘尺寸（出现缩放标记的范围）
        self.edge_size = 5
        # 窗体圆角X半径
        self.xRadius = 5
        # 窗体圆角Y半径
        self.yRadius = 5
        # 窗体的最小宽度
        self.min_width = 50
        # 窗体的最小高度
        self.min_height = 50
        # 拖放标记
        self.edge_press = EdgePress()
        # 顶部可移动窗口高度
        self.move_event_height = 40

    # 设置边框圆角
    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 设置抗锯齿，不然边框会有明显锯齿
        painter.setBrush(Qt.white)  # 设置窗体颜色
        painter.drawRoundedRect(self.rect(), self.xRadius, self.yRadius)
        super().paintEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.NoButton:
            # 没有鼠标按钮按下，检查鼠标位置并更新窗口光标
            pos = event.globalPosition().toPoint() - self.pos()
            edges = self._get_edges(pos)

            if edges == Edge.LeftEdge or edges == Edge.RightEdge:
                self.setCursor(Qt.SizeHorCursor)
            elif edges == Edge.TopEdge or edges == Edge.BottomEdge:
                self.setCursor(Qt.SizeVerCursor)
            elif edges == Edge.LeftTopEdge or edges == Edge.RightBottomEdge:
                self.setCursor(Qt.CursorShape.SizeFDiagCursor)
            elif edges == Edge.LeftBottomEdge or edges == Edge.RightTopEdge:
                self.setCursor(Qt.CursorShape.SizeBDiagCursor)
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)
        elif event.buttons() == Qt.MouseButton.LeftButton:
            if self.edge_press.moveEdgePress:
                """移动窗口"""
                self.move(event.globalPosition().toPoint() - self.edge_press.movePosition)  # 更改窗口位置
            elif self._get_edge_press() is not Edge.NoEdge:
                """缩放窗口"""
                self._resize_window(event.globalPosition().toPoint() - self.pos())

    def mousePressEvent(self, event) -> None:

        pos = event.globalPosition().toPoint() - self.pos()
        edges = self._get_edges(pos)
        if edges == Edge.LeftEdge:
            self.edge_press.leftEdgePress = True
        elif edges == Edge.RightEdge:
            self.edge_press.rightEdgePress = True
        elif edges == Edge.TopEdge:
            self.edge_press.topEdgePress = True
        elif edges == Edge.BottomEdge:
            self.edge_press.bottomEdgePress = True
        elif edges == Edge.LeftTopEdge:
            self.edge_press.leftTopEdgePress = True
        elif edges == Edge.RightBottomEdge:
            self.edge_press.rightBottomEdgePress = True
        elif edges == Edge.LeftBottomEdge:
            self.edge_press.leftBottomEdgePress = True
        elif edges == Edge.RightTopEdge:
            self.edge_press.rightTopEdgePress = True
        else:
            # 移动事件
            if self._get_move_edges(pos):
                self.edge_press.moveEdgePress = True
                self.edge_press.movePosition = event.globalPosition().toPoint() - self.pos()
                self.setCursor(Qt.CursorShape.OpenHandCursor)

    def mouseReleaseEvent(self, event) -> None:
        self.edge_press.leftEdgePress = False
        self.edge_press.rightEdgePress = False
        self.edge_press.topEdgePress = False
        self.edge_press.bottomEdgePress = False
        self.edge_press.leftTopEdgePress = False
        self.edge_press.rightBottomEdgePress = False
        self.edge_press.leftBottomEdgePress = False
        self.edge_press.rightTopEdgePress = False
        self.edge_press.moveEdgePress = False
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def _get_move_edges(self, pos):
        """获取移动窗口事件标记"""
        in_move_edge: bool = pos.y() <= self.move_event_height  # 是否在可移动区域内
        not_in_edges: bool = self._get_edges(pos) == Edge.NoEdge  # 是否在非缩放区域内
        return in_move_edge and not_in_edges

    def _get_edges(self, pos):
        """获取边缘类型"""
        edges = Edge.NoEdge

        in_left_edge: bool = pos.x() <= self.edge_size  # 左
        in_right_edge: bool = pos.x() >= (self.width() - self.edge_size)  # 右
        in_top_edge: bool = pos.y() <= self.edge_size  # 上
        in_bottom_edge: bool = pos.y() >= (self.height() - self.edge_size)  # 下

        size = len([i for i in [in_left_edge, in_right_edge, in_top_edge, in_bottom_edge] if i])

        if size == 0:
            return edges
        if size == 1:
            if in_left_edge:
                return Edge.LeftEdge
            if in_right_edge:
                return Edge.RightEdge
            if in_top_edge:
                return Edge.TopEdge
            if in_bottom_edge:
                return Edge.BottomEdge
        if size == 2:
            if in_left_edge and in_top_edge:
                return Edge.LeftTopEdge
            if in_left_edge and in_bottom_edge:
                return Edge.LeftBottomEdge
            if in_right_edge and in_top_edge:
                return Edge.RightTopEdge
            if in_right_edge and in_bottom_edge:
                return Edge.RightBottomEdge

    def _get_edge_press(self):
        """
         边缘按下区域类型
        """
        if self.edge_press.leftEdgePress:
            return Edge.LeftEdge
        elif self.edge_press.rightEdgePress:
            return Edge.RightEdge
        elif self.edge_press.topEdgePress:
            return Edge.TopEdge
        elif self.edge_press.bottomEdgePress:
            return Edge.BottomEdge
        elif self.edge_press.leftTopEdgePress:
            return Edge.LeftTopEdge
        elif self.edge_press.rightBottomEdgePress:
            return Edge.RightBottomEdge
        elif self.edge_press.leftBottomEdgePress:
            return Edge.LeftBottomEdge
        elif self.edge_press.rightTopEdgePress:
            return Edge.RightTopEdge
        else:
            return Edge.NoEdge

    def _resize_window(self, pos):

        """缩放窗口"""
        # 判断按下时的区域是哪一块
        edges = self._get_edge_press()
        # 获取窗口的初始大小和位置
        geo = self.frameGeometry()
        x, y, width, height = geo.x(), geo.y(), geo.width(), geo.height()
        if edges is Edge.LeftEdge:
            width -= pos.x()
            if width <= self.min_width:
                return
            else:
                x += pos.x()
        elif edges is Edge.RightEdge:
            width = pos.x()
            if width <= self.min_width:
                return
        elif edges is Edge.TopEdge:
            height -= pos.y()
            if height <= self.min_height:
                return
            else:
                y += pos.y()
        elif edges is Edge.BottomEdge:
            height = pos.y()
            if height <= self.min_height:
                return
        elif edges is Edge.LeftTopEdge:
            width -= pos.x()
            if width <= self.min_width:
                width = geo.width()
            else:
                x += pos.x()
            height -= pos.y()
            if height <= self.min_height:
                height = geo.height()
            else:
                y += pos.y()
        elif edges is Edge.LeftBottomEdge:
            width -= pos.x()
            if width <= self.min_width:
                width = geo.width()
            else:
                x += pos.x()
            height = pos.y()
            if height <= self.min_height:
                height = geo.height()
        elif edges is Edge.RightTopEdge:
            width = pos.x()
            if width <= self.min_width:
                width = geo.width()
            height -= pos.y()
            if height <= self.min_height:
                height = geo.height()
            else:
                y += pos.y()
        elif edges is Edge.RightBottomEdge:
            width = pos.x()
            if width <= self.min_width:
                width = geo.width()
            height = pos.y()
            if height <= self.min_height:
                height = geo.height()
        self.setGeometry(x, y, width, height)

    def resizeEvent(self, event):
        # 处理窗口大小更改事件
        self.setCursor(Qt.CursorShape.ArrowCursor)
