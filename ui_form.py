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
    QProgressBar, QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(498, 750)
        Form.setStyleSheet(u"/* \u4e3b\u7a97\u53e3\u6837\u5f0f */\n"
"QWidget {\n"
"    background-color: white; /* \u4e3b\u7a97\u53e3\u80cc\u666f\u989c\u8272 */\n"
"    color: #333333; /* \u4e3b\u7a97\u53e3\u6587\u5b57\u989c\u8272 */\n"
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
"    outline: none; /* \u53bb\u9664\u9ed8\u8ba4\u7684\u7126\u70b9\u8f6e\u5ed3 */\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761\u6837\u5f0f */\n"
""
                        "QScrollBar:vertical {\n"
"    background: #F0F0F0; /* \u5782\u76f4\u6eda\u52a8\u6761\u80cc\u666f\u989c\u8272 */\n"
"    width: 12px; /* \u5782\u76f4\u6eda\u52a8\u6761\u5bbd\u5ea6 */\n"
"    margin: 12px 0 12px 0; /* \u5782\u76f4\u6eda\u52a8\u6761\u5916\u8fb9\u8ddd */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #B0B0B0; /* \u5782\u76f4\u6eda\u52a8\u6761\u6ed1\u5757\u80cc\u666f\u989c\u8272 */\n"
"    min-height: 20px; /* \u5782\u76f4\u6eda\u52a8\u6761\u6ed1\u5757\u6700\u5c0f\u9ad8\u5ea6 */\n"
"    border-radius: 6px; /* \u5782\u76f4\u6eda\u52a8\u6761\u6ed1\u5757\u5706\u89d2 */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #909090; /* \u9f20\u6807\u60ac\u505c\u65f6\u5782\u76f4\u6eda\u52a8\u6761\u6ed1\u5757\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 12px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
""
                        "    border: none;\n"
"    background: none;\n"
"    height: 12px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #F0F0F0; /* \u6c34\u5e73\u6eda\u52a8\u6761\u80cc\u666f\u989c\u8272 */\n"
"    height: 12px; /* \u6c34\u5e73\u6eda\u52a8\u6761\u9ad8\u5ea6 */\n"
"    margin: 0 12px 0 12px; /* \u6c34\u5e73\u6eda\u52a8\u6761\u5916\u8fb9\u8ddd */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #B0B0B0; /* \u6c34\u5e73\u6eda\u52a8\u6761\u6ed1\u5757\u80cc\u666f\u989c\u8272 */\n"
"    min-width: 20px; /* \u6c34\u5e73\u6eda\u52a8\u6761\u6ed1\u5757\u6700\u5c0f\u5bbd\u5ea6 */\n"
"    border-radius: 6px; /* \u6c34\u5e73\u6eda\u52a8\u6761\u6ed1\u5757\u5706\u89d2 */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #909090; /* \u9f20\u6807\u60ac\u505c\u65f6\u6c34\u5e73\u6eda\u52a8\u6761\u6ed1\u5757\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    back"
                        "ground: none;\n"
"    width: 12px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 12px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

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

        self.gridLayout.addWidget(self.progress_bar, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.num_tasks_label_2 = QLabel(Form)
        self.num_tasks_label_2.setObjectName(u"num_tasks_label_2")
        font = QFont()
        self.num_tasks_label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.num_tasks_label_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(32, 32))
        self.label.setPixmap(QPixmap(u":/icons/images/\u9519\u8bef.svg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.connect_button = QPushButton(Form)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(10)
        self.connect_button.setFont(font1)
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
        self.add_task_button.setFont(font1)
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
        self.start_button.setFont(font1)
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
        self.stop_button.setFont(font1)
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


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7b80\u5386\u52a9\u624bv1.5.2", None))
        self.label_2.setText("")
        self.num_tasks_label_2.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5\u72b6\u6001\uff1a", None))
        self.label.setText("")
        self.connect_button.setText("")
        self.add_task_button.setText("")
        self.start_button.setText("")
        self.stop_button.setText("")
    # retranslateUi

