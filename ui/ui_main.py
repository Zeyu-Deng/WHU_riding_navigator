################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 810)
        MainWindow.setStyleSheet(u"#MainWindow {\n"
"	background-color: #fff8eb;\n"
"}\n"
"QLineEdit, QComboBox {\n"
"	font-size: 18px;\n"
"	font-family: consolas, \u9ed1\u4f53;\n"
"	border: 1px solid #965d00;\n"
"	border-radius: 4px;\n"
"	background-color: #fffeef;\n"
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
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(MainWindow)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout.addWidget(self.titleLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.srcEdit = QLineEdit(MainWindow)
        self.srcEdit.setObjectName(u"srcEdit")
        self.srcEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.srcEdit)

        self.srcButton = QPushButton(MainWindow)
        self.srcButton.setObjectName(u"srcButton")

        self.horizontalLayout.addWidget(self.srcButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dstEdit = QLineEdit(MainWindow)
        self.dstEdit.setObjectName(u"dstEdit")
        self.dstEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.dstEdit)

        self.dstButton = QPushButton(MainWindow)
        self.dstButton.setObjectName(u"dstButton")

        self.horizontalLayout_2.addWidget(self.dstButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.algBox = QComboBox(MainWindow)
        self.algBox.addItem("")
        self.algBox.addItem("")
        self.algBox.setObjectName(u"algBox")

        self.horizontalLayout_3.addWidget(self.algBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.navButton = QPushButton(MainWindow)
        self.navButton.setObjectName(u"navButton")
        self.navButton.setMinimumSize(QSize(70, 0))
        self.navButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.navButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 3)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayout_3.setStretch(5, 2)
        self.horizontalLayout_3.setStretch(6, 1)
        self.horizontalLayout_3.setStretch(7, 1)
        self.horizontalLayout_3.setStretch(8, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.web = QWebEngineView(MainWindow)
        self.web.setObjectName(u"web")

        self.verticalLayout.addWidget(self.web)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 15)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6b66\u6c49\u5927\u5b66\u5bfc\u822a\u7cfb\u7edf", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u" \u6b66\u6c49\u5927\u5b66\u6821\u56ed\u5bfc\u822a\u7cfb\u7edf", None))
        self.srcEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u8d77\u70b9", None))
        self.srcButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.dstEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u7ec8\u70b9", None))
        self.dstButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.algBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.algBox.setItemText(1, QCoreApplication.translate("MainWindow", u"A*", None))

        self.navButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5bfc\u822a", None))
    # retranslateUi

