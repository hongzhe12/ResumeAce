import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QHBoxLayout
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtCore import Qt, QTimer

# 假设 ui_chat_box 模块和 Ui_ChatBox 类已经定义好
from ui_chat_box import Ui_ChatBox


class ChatBox(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ChatBox()
        self.ui.setupUi(self)
        self.current_message_timer = None
        self.current_message_chars = 0

    def send_message(self, is_sender,message):
        if message:
            self.add_message(message, is_sender)

    def add_message(self, message, is_sender):
        # 清理之前的定时器和计数器
        if self.current_message_timer:
            self.current_message_timer.stop()
        self.current_message_chars = 0

        if self.ui.chat_layout.count() > 1:
            self.ui.chat_layout.takeAt(self.ui.chat_layout.count() - 1)

        message_label = QLabel()
        font = QFont("Microsoft YaHei UI", 12)
        message_label.setFont(font)
        message_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        text_max_width = 250
        elided_text = self.wrap_text(message, font, text_max_width)
        message_label.setMaximumWidth(text_max_width + 50)

        message_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

        message_layout = QHBoxLayout()

        if is_sender:
            message_label.setAlignment(Qt.AlignLeft)
            message_label.setStyleSheet("""
                QLabel {
                    background-color: #dcf8c6;
                    color: #333;
                    padding: 10px;
                    border-radius: 10px;
                    margin: 5px;
                }
            """)
            message_layout.addStretch()
            message_layout.addWidget(message_label)
        else:
            message_label.setAlignment(Qt.AlignLeft)
            message_label.setStyleSheet("""
                QLabel {
                    background-color: #f1f1f1;
                    color: #333;
                    padding: 10px;
                    border-radius: 10px;
                    margin: 5px;
                }
            """)
            message_layout.addWidget(message_label)
            message_layout.addStretch()

        self.ui.chat_layout.addLayout(message_layout)
        self.ui.chat_layout.addStretch()

        # 开始逐字显示文本
        self.current_message_timer = QTimer(self)
        self.current_message_timer.timeout.connect(lambda: self.show_next_char(message_label, elided_text))
        self.current_message_timer.start(25)  # 设置字符间的延迟时间

    def show_next_char(self, label, message):
        self.current_message_chars += 1
        label.setText(message[:self.current_message_chars])
        if self.current_message_chars >= len(message):
            self.current_message_timer.stop()
            self.scroll_to_bottom()

    def scroll_to_bottom(self):
        scroll_bar = self.ui.scroll_area.verticalScrollBar()
        QTimer.singleShot(100, lambda: scroll_bar.setValue(scroll_bar.maximum()))

    def wrap_text(self, message, font, max_width):
        font_metrics = QFontMetrics(font)
        lines = []
        current_line = ""

        for char in message:
            test_line = current_line + char
            text_line_width = font_metrics.horizontalAdvance(test_line)
            if text_line_width > max_width:
                lines.append(current_line.strip())
                current_line = char
            else:
                current_line = test_line

        if current_line:
            lines.append(current_line.strip())

        wrapped_text = "\n".join(lines)
        return wrapped_text


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_box = ChatBox()
    chat_box.show()
    sys.exit(app.exec())