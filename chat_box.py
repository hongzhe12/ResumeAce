import sys
from pprint import pprint
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QHBoxLayout
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtCore import Qt, QTimer

from ui_chat_box import Ui_ChatBox


class ChatBox(QWidget):
    def __init__(self):
        super().__init__()
        self.is_reply_complete = False
        self.streaming_reply = ''
        self.current_label = None  # 用于存储当前的消息气泡
        self.ui = Ui_ChatBox()
        self.ui.setupUi(self)

    def send_message(self, is_sender, message):
        if is_sender:
            if message:
                self.add_message(message, is_sender)
        else:
            if message:
                self.add_message(message, is_sender)

    def add_message(self, message, is_sender):
        if self.ui.chat_layout.count() > 1:
            self.ui.chat_layout.takeAt(self.ui.chat_layout.count() - 1)

        message_label = QLabel()
        message_label.setWordWrap(False)
        font = QFont("Microsoft YaHei UI", 12)
        message_label.setFont(font)
        message_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        text_max_width = 250
        message_label_max_width = text_max_width + 50
        message_label.setMaximumWidth(message_label_max_width)

        font_metrics = QFontMetrics(font)
        text_width = font_metrics.horizontalAdvance(message)
        print("文本宽度:", text_width)

        elided_text = self.wrap_text(message, font, text_max_width)
        message_label.setText(elided_text)

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
        self.scroll_to_bottom()

        if not is_sender:
            self.current_label = message_label  # 保存当前的消息气泡



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
            print("当前字符:", char, "当前文本宽度:", text_line_width)
            if text_line_width > max_width:
                lines.append(current_line.strip())
                current_line = char
            else:
                current_line = test_line

        if current_line:
            lines.append(current_line.strip())

        pprint(lines)
        wrapped_text = "\n".join(lines)
        print("换行后文本:", wrapped_text)
        return wrapped_text

    def handle_streaming_response(self, token):
        """处理流式响应的新片段"""
        self.streaming_reply += token
        if self.current_label:
            current_text = self.current_label.text()
            new_text = current_text + token
            elided_text = self.wrap_text(new_text, self.current_label.font(), 250)
            self.current_label.setText(elided_text)
            self.scroll_to_bottom()

        # 这里可以添加一些逻辑判断是否回复结束，比如根据特定标识等
        # 假设没有特殊标识，简单延迟后展示完整内容
        # QTimer.singleShot(500, self.show_complete_reply)

    def show_complete_reply(self):
        """展示完整的回复"""
        if self.streaming_reply:
            self.add_message(self.streaming_reply, False)
            self.streaming_reply = ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_box = ChatBox()
    chat_box.show()
    sys.exit(app.exec())