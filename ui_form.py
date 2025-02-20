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
        Form.setStyleSheet(u"/* \u4e3b\u7a97\u53e3\u6837\u5f0f */\n"
"QWidget {\n"
"    background-color: white; /* \u4e3b\u7a97\u53e3\u80cc\u666f\u989c\u8272 */\n"
"    color: #333333; /* \u4e3b\u7a97\u53e3\u6587\u5b57\u989c\u8272 */\n"
"	border-radius: 10px; /* \u6587\u672c\u6846\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u6837\u5f0f */\n"
"QLabel {\n"
"    font-size: 14px; /* \u6807\u7b7e\u6587\u5b57\u5927\u5c0f */\n"
"    padding: 5px; /* \u6807\u7b7e\u5185\u8fb9\u8ddd */\n"
"}\n"
"\n"
"/* \u6587\u672c\u6846\u6837\u5f0f */\n"
"QLineEdit {\n"
"    background-color: white; /* \u6587\u672c\u6846\u80cc\u666f\u989c\u8272 */\n"
"    border: 1px solid #cccccc; /* \u6587\u672c\u6846\u8fb9\u6846 */\n"
"    border-radius: 3px; /* \u6587\u672c\u6846\u5706\u89d2 */\n"
"    padding: 5px; /* \u6587\u672c\u6846\u5185\u8fb9\u8ddd */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #1296db; /* \u6587\u672c\u6846\u83b7\u5f97\u7126\u70b9\u65f6\u8fb9\u6846\u989c\u8272 */\n"
"    outline: none; /* \u53bb\u9664\u9ed8\u8ba4\u7684\u7126\u70b9\u8f6e\u5ed3"
                        " */\n"
"}\n"
"QScrollBar:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgb(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-top:12px;   /*\u4e0a\u9884\u7559\u4f4d\u7f6e*/\n"
"    padding-bottom:12px;    /*\u4e0b\u9884\u7559\u4f4d\u7f6e*/\n"
"}\n"
" \n"
"/*\u6eda\u52a8\u6761\u4e2d\u6ed1\u5757\u7684\u6837\u5f0f*/\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgb(0,0,0,25%);\n"
"    border-radius:4px;\n"
"    min-height:20px;\n"
"}\n"
" \n"
"/*\u9f20\u6807\u89e6\u53ca\u6ed1\u5757\u6837\u5f0f*/\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"    width:9px;\n"
"    background:rgb(0,0,0,50%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
" \n"
"/*\u8bbe\u7f6e\u4e0b\u7bad\u5934*/\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    height:12px;\n"
"    width:10px;\n"
"    border-image:url(:/KeyManager/images/icon_pull-down.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
" \n"
"/*\u8bbe\u7f6e\u4e0a\u7bad\u5934*/\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    h"
                        "eight:12px;\n"
"    width:10px;\n"
"    border-image:url(:/KeyManager/images/icon_pull-up.png);\n"
"    subcontrol-position:top;\n"
"}\n"
" \n"
"/*\u8bbe\u7f6e\u4e0b\u7bad\u5934:\u60ac\u6d6e\u72b6\u6001*/\n"
"QScrollBar::add-line:vertical:hover\n"
"{\n"
"    height:12px;\n"
"    width:10px;\n"
"    border-image:url(:/KeyManager/images/icon_pull-down2.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
" \n"
"/*\u8bbe\u7f6e\u4e0a\u7bad\u5934\uff1a\u60ac\u6d6e\u72b6\u6001*/\n"
"QScrollBar::sub-line:vertical:hover\n"
"{\n"
"    height:12px;\n"
"    width:10px;\n"
"    border-image:url(:/KeyManager/images/icon_pull-up2.png);\n"
"    subcontrol-position:top;\n"
"}\n"
" \n"
"/*\u5f53\u6eda\u52a8\u6761\u6eda\u52a8\u7684\u65f6\u5019\uff0c\u4e0a\u9762\u7684\u90e8\u5206\u548c\u4e0b\u9762\u7684\u90e8\u5206*/\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
"{\n"
"    background:rgb(0,0,0,10%);\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 8px;  /* \u8bbe\u7f6e\u6eda"
                        "\u52a8\u6761\u9ad8\u5ea6 */\n"
"    background: rgb(0, 0, 0, 0%);  /* \u80cc\u666f\u900f\u660e */\n"
"    margin: 0px;  /* \u5916\u8fb9\u8ddd */\n"
"    padding-left: 12px;  /* \u5de6\u9884\u7559\u4f4d\u7f6e */\n"
"    padding-right: 12px;  /* \u53f3\u9884\u7559\u4f4d\u7f6e */\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761\u4e2d\u6ed1\u5757\u7684\u6837\u5f0f */\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    height: 8px;  /* \u8bbe\u7f6e\u6ed1\u5757\u9ad8\u5ea6 */\n"
"    background: rgb(0, 0, 0, 25%);  /* \u6ed1\u5757\u80cc\u666f\u989c\u8272\u53ca\u900f\u660e\u5ea6 */\n"
"    border-radius: 4px;\n"
"    min-width: 20px;  /* \u6700\u5c0f\u5bbd\u5ea6 */\n"
"}\n"
"\n"
"/* \u9f20\u6807\u89e6\u53ca\u6ed1\u5757\u6837\u5f0f */\n"
"QScrollBar::handle:horizontal:hover\n"
"{\n"
"    height: 9px;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6ed1\u5757\u9ad8\u5ea6\u53d8\u5316 */\n"
"    background: rgb(0, 0, 0, 50%);\n"
"    border-radius: 4px;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u53f3\u7bad\u5934 */\n"
"QScrollBar::add"
                        "-line:horizontal\n"
"{\n"
"    width: 12px;\n"
"    height: 10px;\n"
"    border-image: url(:/KeyManager/images/icon_pull-right.png);  /* \u5bf9\u5e94\u53f3\u7bad\u5934\u56fe\u7247\uff0c\u9700\u786e\u4fdd\u8d44\u6e90\u8def\u5f84\u6b63\u786e */\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u5de6\u7bad\u5934 */\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    width: 12px;\n"
"    height: 10px;\n"
"    border-image: url(:/KeyManager/images/icon_pull-left.png);  /* \u5bf9\u5e94\u5de6\u7bad\u5934\u56fe\u7247 */\n"
"    subcontrol-position: left;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u53f3\u7bad\u5934:\u60ac\u6d6e\u72b6\u6001 */\n"
"QScrollBar::add-line:horizontal:hover\n"
"{\n"
"    width: 12px;\n"
"    height: 10px;\n"
"    border-image: url(:/KeyManager/images/icon_pull-right2.png);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u5de6\u7bad\u5934\uff1a\u60ac\u6d6e\u72b6\u6001 */\n"
"QScrollBar::sub-line:horizontal:hover\n"
"{\n"
"    width: 12px;\n"
"    height: 10px;\n"
"    bo"
                        "rder-image: url(:/KeyManager/images/icon_pull-left2.png);\n"
"    subcontrol-position: left;\n"
"}\n"
"\n"
"/* \u5f53\u6eda\u52a8\u6761\u6eda\u52a8\u7684\u65f6\u5019\uff0c\u5de6\u8fb9\u7684\u90e8\u5206\u548c\u53f3\u8fb9\u7684\u90e8\u5206 */\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: rgb(0, 0, 0, 10%);\n"
"    border-radius: 4px;\n"
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
        font.setPointSize(10)
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/\u4eba\u5de5\u667a\u80fd.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chat.setIcon(icon4)
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
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7b80\u5386\u52a9\u624bv1.6", None))
        self.label_2.setText("")
        self.connect_button.setText("")
        self.add_task_button.setText("")
        self.start_button.setText("")
        self.stop_button.setText("")
        self.chat.setText("")
    # retranslateUi

