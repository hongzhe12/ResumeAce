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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTextEdit, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(460, 644)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #4CAF50;\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                padding: 10px 20px;\n"
"                font-size: 14px;\n"
"                font-weight: bold;\n"
"                transition: background-color 0.3s, border-color 0.3s;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #45a049;\n"
"                border-color: #45a049;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #3e8e41;\n"
"                border-color: #3e8e41;\n"
"            }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.log_output = QTextEdit(self.centralwidget)
        self.log_output.setObjectName(u"log_output")
        font = QFont()
        font.setFamilies([u"\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53"])
        font.setPointSize(16)
        self.log_output.setFont(font)
        self.log_output.setReadOnly(True)

        self.gridLayout.addWidget(self.log_output, 0, 0, 1, 1)

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")

        self.gridLayout.addWidget(self.progress_bar, 1, 0, 1, 1)

        self.filter_label = QLabel(self.centralwidget)
        self.filter_label.setObjectName(u"filter_label")
        font1 = QFont()
        font1.setFamilies([u"\u534e\u6587\u884c\u6977"])
        font1.setPointSize(14)
        self.filter_label.setFont(font1)

        self.gridLayout.addWidget(self.filter_label, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filter_input = QLineEdit(self.centralwidget)
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

        self.horizontalLayout.addWidget(self.filter_input)

        self.add_task_button = QPushButton(self.centralwidget)
        self.add_task_button.setObjectName(u"add_task_button")
        self.add_task_button.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"\u534e\u6587\u884c\u6977"])
        font2.setBold(True)
        self.add_task_button.setFont(font2)

        self.horizontalLayout.addWidget(self.add_task_button)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.num_tasks_label = QLabel(self.centralwidget)
        self.num_tasks_label.setObjectName(u"num_tasks_label")
        self.num_tasks_label.setFont(font1)

        self.gridLayout.addWidget(self.num_tasks_label, 4, 0, 1, 1)

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

        self.gridLayout.addWidget(self.num_tasks_input, 5, 0, 1, 1)

        self.filter_label_2 = QLabel(self.centralwidget)
        self.filter_label_2.setObjectName(u"filter_label_2")
        self.filter_label_2.setFont(font1)

        self.gridLayout.addWidget(self.filter_label_2, 6, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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

        self.horizontalLayout_2.addWidget(self.ip)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(16, 16))
        self.label.setPixmap(QPixmap(u":/icons/images/err.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.connect_button = QPushButton(self.centralwidget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setMinimumSize(QSize(0, 40))
        self.connect_button.setFont(font2)
        self.connect_button.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.connect_button)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 40))
        self.start_button.setFont(font2)
        self.start_button.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.start_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.stop_button = QPushButton(self.centralwidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 40))
        self.stop_button.setFont(font2)

        self.horizontalLayout_3.addWidget(self.stop_button)


        self.gridLayout.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 460, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7b80\u5386\u52a9\u624b(\u5f00\u6e90\u514d\u8d39\u4ec5\u7528\u4e8e\u5b66\u4e60\u4ea4\u6d41)", None))
        self.log_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.filter_label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u7b5b\u9009\u89c4\u5219\uff08\u4ee5\u7a7a\u683c\u5206\u9694\uff09:", None))
        self.add_task_button.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4efb\u52a1", None))
        self.num_tasks_label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4efb\u52a1\u6570\u91cf:", None))
        self.filter_label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u65e0\u7ebf\u8c03\u8bd5\u5730\u5740", None))
        self.ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4f8b\u5982\uff1a192.168.1.5:8888", None))
        self.label.setText("")
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u624b\u673a", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4efb\u52a1", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4efb\u52a1", None))
    # retranslateUi

