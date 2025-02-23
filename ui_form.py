# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 600)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"/* \u5168\u5c40\u5b57\u4f53\u8bbe\u7f6e */\n"
"* {\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* \u7a97\u53e3\u80cc\u666f */\n"
"QWidget {\n"
"    background-color: white;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"/* \u6309\u94ae\u6837\u5f0f */\n"
"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d8b40;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u6837\u5f0f */\n"
"QLabel {\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* \u6587\u672c\u6846\u6837\u5f0f */\n"
"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
""
                        "/* \u7ec4\u5408\u6846\u6837\u5f0f */\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #cccccc;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/images/\u5411\u4e0b.svg);\n"
"}\n"
"\n"
"/* \u590d\u9009\u6846\u6837\u5f0f */\n"
"QCheckBox {\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 3px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #4CAF50;\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
"/* \u5355\u9009\u6846\u6837\u5f0f */\n"
"QRadioButton {\n"
""
                        "    color: #333333;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 8px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4CAF50;\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761\u6837\u5f0f */\n"
"QScrollBar:vertical {\n"
"    background-color: #f0f0f0;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #cccccc;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: #f0f0f0;\n"
"    height: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:h"
                        "orizontal {\n"
"    background-color: #cccccc;\n"
"    min-width: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/* \u8fdb\u5ea6\u6761\u6837\u5f0f */\n"
"QProgressBar {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* \u83dc\u5355\u680f\u6837\u5f0f */\n"
"QMenuBar {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #f0f0f0;\n"
""
                        "    border: 1px solid #cccccc;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 5px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u5de5\u5177\u680f\u6837\u5f0f */\n"
"QToolBar {\n"
"    background-color: #f0f0f0;\n"
"    border: none;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #3d8b40;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* \u72b6\u6001\u680f\u6837\u5f0f */\n"
"QStatusBar {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    /* \u6574\u4f53\u80cc\u666f\u989c\u8272\uff0c\u91c7\u7528\u6d45\u7070\u8272\uff0c\u8425\u9020\u67d4\u548c\u6c1b\u56f4 */\n"
"    background-color: #F2F2F2;\n"
"    /* \u6587\u5b57\u989c\u8272\u4e3a\u6df1\u7070\u8272\uff0c\u4fdd\u8bc1\u53ef\u8bfb\u6027 */\n"
"    color: #333333;\n"
"    /* \u8fb9\u6846\u6837\u5f0f\uff0c\u8bbe\u7f6e 1 \u50cf\u7d20\u5bbd\u7684\u6d45\u7070\u8272\u8fb9\u6846\uff0c\u589e\u52a0\u8fb9\u754c\u611f */\n"
"    border: 1px solid #CCCCCC;\n"
"    /* \u8fb9\u6846\u5706\u89d2\u4e3a 5 \u50cf\u7d20\uff0c\u4f7f\u7ec4\u4ef6\u8fb9\u89d2\u66f4\u5706\u6da6 */\n"
"    border-radius: 5px;\n"
"    /* \u5185\u8fb9\u8ddd\u8bbe\u7f6e\uff0c\u8ba9\u6587\u5b57\u4e0e\u8fb9\u6846\u6709\u4e00\u5b9a\u95f4\u8ddd */\n"
"    padding: 5px;\n"
"    /* \u5b57\u4f53\u5927\u5c0f\u8bbe\u7f6e\u4e3a 14 \u50cf\u7d20 */\n"
"    font-size: 14px;\n"
"    /* \u5b57\u4f53\u8bbe\u7f6e\u4e3a\u5fae\u8f6f\u96c5\u9ed1\uff0c\u8fd9\u662f\u5e38\u89c1\u7684\u7b80\u6d01\u5b57\u4f53 */\n"
"    font-family: \"Microsoft "
                        "YaHei\";\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u6837\u5f0f */\n"
"QTextEdit:hover {\n"
"    /* \u9f20\u6807\u60ac\u505c\u65f6\uff0c\u8fb9\u6846\u989c\u8272\u53d8\u4e3a\u84dd\u8272\uff0c\u63d0\u793a\u7528\u6237\u53ef\u4ea4\u4e92 */\n"
"    border: 1px solid #0084FF;\n"
"}\n"
"\n"
"/* \u83b7\u5f97\u7126\u70b9\u65f6\u7684\u6837\u5f0f */\n"
"QTextEdit:focus {\n"
"    /* \u83b7\u5f97\u7126\u70b9\u65f6\uff0c\u8fb9\u6846\u989c\u8272\u53d8\u4e3a\u84dd\u8272\uff0c\u7a81\u51fa\u5f53\u524d\u64cd\u4f5c\u7ec4\u4ef6 */\n"
"    border: 1px solid #0084FF;\n"
"    /* \u7126\u70b9\u72b6\u6001\u4e0b\u6dfb\u52a0\u84dd\u8272\u7684\u9634\u5f71\uff0c\u589e\u5f3a\u89c6\u89c9\u6548\u679c */\n"
"    outline: none;\n"
"    box-shadow: 0 0 5px rgba(0, 132, 255, 0.5);\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761\u6837\u5f0f */\n"
"QTextEdit QScrollBar:vertical {\n"
"    /* \u5782\u76f4\u6eda\u52a8\u6761\u7684\u5bbd\u5ea6 */\n"
"    width: 8px;\n"
"    /* \u6eda\u52a8\u6761\u80cc\u666f\u989c\u8272 */\n"
"    background: #E5E5E5;\n"
""
                        "    /* \u6eda\u52a8\u6761\u8fb9\u6846\u6837\u5f0f */\n"
"    border: none;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical {\n"
"    /* \u6eda\u52a8\u6761\u6ed1\u5757\u7684\u80cc\u666f\u989c\u8272 */\n"
"    background: #B3B3B3;\n"
"    /* \u6ed1\u5757\u7684\u5706\u89d2 */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical:hover {\n"
"    /* \u9f20\u6807\u60ac\u505c\u5728\u6ed1\u5757\u4e0a\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"    background: #808080;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::add-line:vertical,\n"
"QTextEdit QScrollBar::sub-line:vertical {\n"
"    /* \u6eda\u52a8\u6761\u4e0a\u4e0b\u7bad\u5934\u533a\u57df\u7684\u9ad8\u5ea6 */\n"
"    height: 0;\n"
"    /* \u9690\u85cf\u4e0a\u4e0b\u7bad\u5934 */\n"
"    subcontrol-opacity: 0;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::add-page:vertical,\n"
"QTextEdit QScrollBar::sub-page:vertical {\n"
"    /* \u6eda\u52a8\u6761\u7a7a\u767d\u533a\u57df\u7684\u80cc\u666f\u989c\u8272 */\n"
"    background: none;\n"
"}")

        self.verticalLayout.addWidget(self.textEdit)

        self.progress_bar = QProgressBar(Form)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMinimumSize(QSize(0, 0))
        self.progress_bar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid grey;\n"
"    border-radius: 5px;\n"
"	background-color: rgb(243, 243, 243);\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #007BFF;\n"
"    width: 20px;\n"
"    margin: 0.5px;\n"
"}")
        self.progress_bar.setValue(0)

        self.verticalLayout.addWidget(self.progress_bar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.connect_button = QPushButton(Form)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        self.connect_button.setFont(font)
        self.connect_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"    border-radius: 5px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/\u8fde\u63a5.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.connect_button.setIcon(icon)
        self.connect_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.connect_button)

        self.add_task_button = QPushButton(Form)
        self.add_task_button.setObjectName(u"add_task_button")
        self.add_task_button.setMinimumSize(QSize(0, 0))
        self.add_task_button.setFont(font)
        self.add_task_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"    border-radius: 5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/\u7b5b\u9009.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_task_button.setIcon(icon1)
        self.add_task_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.add_task_button)

        self.start_button = QPushButton(Form)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 0))
        self.start_button.setFont(font)
        self.start_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"    border-radius: 5px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/\u5f00\u59cb.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_button.setIcon(icon2)
        self.start_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.start_button)

        self.stop_button = QPushButton(Form)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 0))
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"    border-radius: 5px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/\u505c\u6b62.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_button.setIcon(icon3)
        self.stop_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.stop_button)

        self.person_info = QPushButton(Form)
        self.person_info.setObjectName(u"person_info")
        self.person_info.setMinimumSize(QSize(0, 0))
        self.person_info.setFont(font)
        self.person_info.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"    border-radius: 5px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/\u4e2a\u4eba\u4fe1\u606f.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.person_info.setIcon(icon4)
        self.person_info.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.person_info)

        self.show_rank_btn = QPushButton(Form)
        self.show_rank_btn.setObjectName(u"show_rank_btn")
        self.show_rank_btn.setMinimumSize(QSize(0, 0))
        self.show_rank_btn.setFont(font)
        self.show_rank_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"    border-radius: 5px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/\u6392\u884c\u699c.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_rank_btn.setIcon(icon5)
        self.show_rank_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.show_rank_btn)

        self.chat = QPushButton(Form)
        self.chat.setObjectName(u"chat")
        self.chat.setMinimumSize(QSize(0, 0))
        self.chat.setFont(font)
        self.chat.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"    border-radius: 5px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/\u4eba\u5de5\u667a\u80fd.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chat.setIcon(icon6)
        self.chat.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.chat)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7b80\u5386\u52a9\u624bv1.8", None))
        self.label_2.setText("")
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u60a8\u7684\u95ee\u9898", None))
        self.connect_button.setText("")
        self.add_task_button.setText("")
        self.start_button.setText("")
        self.stop_button.setText("")
        self.person_info.setText("")
        self.show_rank_btn.setText("")
        self.chat.setText("")
    # retranslateUi

