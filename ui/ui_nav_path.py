################################################################################
## Form generated from reading UI file 'nav_path.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_PathWindow(object):
    def setupUi(self, PathWindow):
        if not PathWindow.objectName():
            PathWindow.setObjectName(u"PathWindow")
        PathWindow.resize(1440, 810)
        PathWindow.setStyleSheet(u"#PathWindow {\n"
"	background-color: #fff8eb;\n"
"}\n"
"QLabel {\n"
"	font-size: 20px;\n"
"	font-family: consolas, \u9ed1\u4f53;\n"
"}\n"
"QPushButton{\n"
"	padding: 2px 12px 2px 12px;\n"
"	font-family: \u5fae\u8f6f\u96c5\u9ed1;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"    background-color: rgb(222,184,135);\n"
"    border: 2px solid rgb(205,133,63);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(210,174,137);\n"
"}\n"
"#titleLabel{\n"
"	background-color: rgb(161, 117, 15);\n"
"	color: white;\n"
"	font-size: 36px;\n"
"	font-family: \u534e\u6587\u884c\u6977;\n"
"	padding: 10px auto 5px 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(PathWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(PathWindow)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout.addWidget(self.titleLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.srcLabel = QLabel(PathWindow)
        self.srcLabel.setObjectName(u"srcLabel")

        self.horizontalLayout.addWidget(self.srcLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.dstLabel = QLabel(PathWindow)
        self.dstLabel.setObjectName(u"dstLabel")

        self.horizontalLayout.addWidget(self.dstLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.algLabel = QLabel(PathWindow)
        self.algLabel.setObjectName(u"algLabel")

        self.horizontalLayout.addWidget(self.algLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.returnButton = QPushButton(PathWindow)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setMinimumSize(QSize(70, 0))
        self.returnButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.returnButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 2)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(7, 1)
        self.horizontalLayout.setStretch(8, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.web = QWebEngineView(PathWindow)
        self.web.setObjectName(u"web")

        self.verticalLayout.addWidget(self.web)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 15)

        self.retranslateUi(PathWindow)

        QMetaObject.connectSlotsByName(PathWindow)
    # setupUi

    def retranslateUi(self, PathWindow):
        PathWindow.setWindowTitle(QCoreApplication.translate("PathWindow", u"\u6b66\u6c49\u5927\u5b66\u5bfc\u822a\u7cfb\u7edf", None))
        self.titleLabel.setText(QCoreApplication.translate("PathWindow", u" \u6b66\u6c49\u5927\u5b66\u6821\u56ed\u5bfc\u822a\u7cfb\u7edf", None))
        self.srcLabel.setText(QCoreApplication.translate("PathWindow", u"\u8d77\u70b9\uff1a\u6e56\u6ee8\u5341\u4e00\u820d", None))
        self.dstLabel.setText(QCoreApplication.translate("PathWindow", u"\u7ec8\u70b9\uff1a\u6587\u7406\u5b66\u90e8\u7b2c\u4e94\u6559\u5b66\u697c", None))
        self.algLabel.setText(QCoreApplication.translate("PathWindow", u"\u7b97\u6cd5\uff1aDijkstra", None))
        self.returnButton.setText(QCoreApplication.translate("PathWindow", u"\u8fd4\u56de", None))
    # retranslateUi

