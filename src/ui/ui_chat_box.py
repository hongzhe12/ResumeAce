# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_box.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ChatBox(object):
    def setupUi(self, ChatBox):
        if not ChatBox.objectName():
            ChatBox.setObjectName(u"ChatBox")
        ChatBox.resize(600, 400)
        self.gridLayout = QGridLayout(ChatBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scroll_area = QScrollArea(ChatBox)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setWidgetResizable(True)
        self.chat_container = QWidget()
        self.chat_container.setObjectName(u"chat_container")
        self.chat_container.setGeometry(QRect(0, 0, 568, 380))
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setObjectName(u"chat_layout")
        self.scroll_area.setWidget(self.chat_container)

        self.gridLayout.addWidget(self.scroll_area, 0, 0, 1, 1)


        self.retranslateUi(ChatBox)

        QMetaObject.connectSlotsByName(ChatBox)
    # setupUi

    def retranslateUi(self, ChatBox):
        ChatBox.setWindowTitle(QCoreApplication.translate("ChatBox", u"\u804a\u5929\u6846", None))
    # retranslateUi

