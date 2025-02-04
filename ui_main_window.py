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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(409, 664)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #4CAF50;\n"
"                color: white;\n"
"                border: 1px solid #4CAF50;\n"
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
        self.log_output.setReadOnly(True)

        self.gridLayout.addWidget(self.log_output, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")

        self.verticalLayout_2.addWidget(self.progress_bar)

        self.filter_label = QLabel(self.centralwidget)
        self.filter_label.setObjectName(u"filter_label")

        self.verticalLayout_2.addWidget(self.filter_label)

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

        self.verticalLayout_2.addWidget(self.filter_input)

        self.num_tasks_label = QLabel(self.centralwidget)
        self.num_tasks_label.setObjectName(u"num_tasks_label")

        self.verticalLayout_2.addWidget(self.num_tasks_label)

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

        self.verticalLayout_2.addWidget(self.num_tasks_input)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_task_button = QPushButton(self.centralwidget)
        self.add_task_button.setObjectName(u"add_task_button")
        self.add_task_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.add_task_button)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.start_button)

        self.open_log_button = QPushButton(self.centralwidget)
        self.open_log_button.setObjectName(u"open_log_button")
        self.open_log_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.open_log_button)

        self.stop_button = QPushButton(self.centralwidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.stop_button)

        self.add_group = QPushButton(self.centralwidget)
        self.add_group.setObjectName(u"add_group")
        self.add_group.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.add_group)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 409, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7b80\u5386\u6295\u9012(\u5f00\u6e90\u514d\u8d39\u4ec5\u7528\u4e8e\u5b66\u4e60\u4ea4\u6d41)", None))
        self.filter_label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u7b5b\u9009\u89c4\u5219\uff08\u4ee5\u7a7a\u683c\u5206\u9694\uff09:", None))
        self.num_tasks_label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4efb\u52a1\u6570\u91cf:", None))
        self.add_task_button.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4efb\u52a1", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4efb\u52a1", None))
        self.open_log_button.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u65e5\u5fd7\u6587\u4ef6", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u4efb\u52a1", None))
        self.add_group.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u7fa4\u4ea4\u6d41", None))
    # retranslateUi

