# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTextEdit,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setStyleSheet(u"/* \u6574\u4f53\u7a97\u53e3\u80cc\u666f\u8272 */\n"
"QWidget {\n"
"    background - color: #f0f0f0;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u6837\u5f0f */\n"
"QLabel {\n"
"    color: #333333;\n"
"    font - size: 12pt;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* \u8f93\u5165\u6846\u6837\u5f0f */\n"
"QLineEdit {\n"
"    background - color: white;\n"
"    border: 1px solid #ccc;\n"
"    border - radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background - color: #45a049; /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background - color: #388e3c; /* \u6309\u4e0b\u65f6\u7684\u989c\u8272 */\n"
"}\n"
"\n"
"/* \u8fdb\u5ea6\u6761\u6837\u5f0f */\n"
"QProgressBar {\n"
"    border: 1px solid #ccc;\n"
"    border - radius: 3px;\n"
"    background - color: white;\n"
"    text - align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background - color: #007bff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.log_output = QTextEdit(self.centralwidget)
        self.log_output.setObjectName(u"log_output")
        font = QFont()
        font.setPointSize(12)
        self.log_output.setFont(font)
        self.log_output.setReadOnly(True)

        self.gridLayout.addWidget(self.log_output, 0, 0, 1, 1)

        self.progress_bar = QProgressBar(self.centralwidget)
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

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.filter_label = QLabel(self.groupBox)
        self.filter_label.setObjectName(u"filter_label")
        self.filter_label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.filter_label)

        self.filter_input = QLineEdit(self.groupBox)
        self.filter_input.setObjectName(u"filter_input")
        self.filter_input.setMinimumSize(QSize(0, 31))
        self.filter_input.setStyleSheet(u"QLineEdit {\n"
"    padding: 5px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4CAF50;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.filter_input)

        self.filter_label_3 = QLabel(self.groupBox)
        self.filter_label_3.setObjectName(u"filter_label_3")
        self.filter_label_3.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.filter_label_3)

        self.filter_input_2 = QLineEdit(self.groupBox)
        self.filter_input_2.setObjectName(u"filter_input_2")
        self.filter_input_2.setMinimumSize(QSize(0, 31))
        self.filter_input_2.setStyleSheet(u"QLineEdit {\n"
"    padding: 5px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4CAF50;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.filter_input_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.add_task_button = QPushButton(self.groupBox)
        self.add_task_button.setObjectName(u"add_task_button")
        self.add_task_button.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.add_task_button.setFont(font1)

        self.horizontalLayout.addWidget(self.add_task_button)


        self.formLayout.setLayout(2, QFormLayout.SpanningRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)

        self.num_tasks_label = QLabel(self.centralwidget)
        self.num_tasks_label.setObjectName(u"num_tasks_label")
        self.num_tasks_label.setFont(font)

        self.gridLayout.addWidget(self.num_tasks_label, 3, 0, 1, 1)

        self.num_tasks_input = QSpinBox(self.centralwidget)
        self.num_tasks_input.setObjectName(u"num_tasks_input")
        self.num_tasks_input.setMinimumSize(QSize(0, 31))
        self.num_tasks_input.setStyleSheet(u"QLineEdit {\n"
"    padding: 5px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4CAF50;\n"
"}")
        self.num_tasks_input.setMinimum(1)
        self.num_tasks_input.setMaximum(1000)
        self.num_tasks_input.setValue(100)

        self.gridLayout.addWidget(self.num_tasks_input, 4, 0, 1, 1)

        self.filter_label_2 = QLabel(self.centralwidget)
        self.filter_label_2.setObjectName(u"filter_label_2")
        self.filter_label_2.setFont(font)

        self.gridLayout.addWidget(self.filter_label_2, 5, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ip = QLineEdit(self.centralwidget)
        self.ip.setObjectName(u"ip")
        self.ip.setMinimumSize(QSize(0, 31))
        self.ip.setStyleSheet(u"QLineEdit {\n"
"    padding: 5px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4CAF50;\n"
"}")

        self.horizontalLayout_3.addWidget(self.ip)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(16, 16))
        self.label.setPixmap(QPixmap(u":/icons/images/err.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.connect_button = QPushButton(self.centralwidget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setMinimumSize(QSize(0, 40))
        self.connect_button.setFont(font1)
        self.connect_button.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.connect_button)


        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 40))
        self.start_button.setFont(font1)
        self.start_button.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.start_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.stop_button = QPushButton(self.centralwidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 40))
        self.stop_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.stop_button)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7b80\u5386\u52a9\u624b(\u4ec5\u7528\u4e8e\u5b66\u4e60\u4ea4\u6d41)", None))
        self.log_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53'; font-size:16pt;\"><br /></span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u89c4\u5219", None))
        self.filter_label.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009\u6807\u9898", None))
        self.filter_input.setInputMask("")
        self.filter_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4f8b\u5982\uff1ajava \u5f00\u53d1\uff08\u4ee5\u7a7a\u683c\u5206\u9694\uff09", None))
        self.filter_label_3.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009\u85aa\u6c34", None))
        self.filter_input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4f8b\u5982\uff1a1000-2000", None))
        self.add_task_button.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u6dfb\u52a0", None))
        self.num_tasks_label.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u6570\u91cf:", None))
        self.filter_label_2.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u7ebf\u8c03\u8bd5\u5730\u5740\uff08\u6709\u7ebf\u4e0d\u9700\u8981\uff09", None))
        self.ip.setText("")
        self.ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4f8b\u5982\uff1a192.168.1.5:8888", None))
        self.label.setText("")
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u624b\u673a", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4efb\u52a1", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4efb\u52a1", None))
    # retranslateUi

