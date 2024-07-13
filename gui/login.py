# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10

from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_MainWindow

from sys import path
path.insert(0, '../utils')
import utils_gui
import utils_other

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(500, 500)
        loginWindow.setMinimumSize(QtCore.QSize(500, 500))
        loginWindow.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.bgLabel.setMinimumSize(QtCore.QSize(500, 500))
        self.bgLabel.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(10)
        self.bgLabel.setFont(font)
        self.bgLabel.setStyleSheet("background-image: url(:/image/img/logo.jpg);")
        self.bgLabel.setText("")
        self.bgLabel.setObjectName("bgLabel")
        self.blurLabel = QtWidgets.QLabel(self.centralwidget)
        self.blurLabel.setGeometry(QtCore.QRect(75, 125, 350, 250))
        self.blurLabel.setStyleSheet("background-image: url(:/image/img/logo_blur.jpg);\n""\n""")
        self.blurLabel.setText("")
        self.blurLabel.setObjectName("blurLabel")
        self.padLabel = QtWidgets.QLabel(self.centralwidget)
        self.padLabel.setGeometry(QtCore.QRect(75, 125, 350, 250))
        self.padLabel.setStyleSheet("background-color: rgba(0, 0, 0, 45);\n""\n""\n""")
        self.padLabel.setText("")
        self.padLabel.setObjectName("padLabel")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(187, 290, 126, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet("background-color: rgb(97, 170, 238);\n""color: rgb(255, 255, 255);")
        self.loginButton.setObjectName("loginButton")
        self.usernameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLine.setGeometry(QtCore.QRect(132, 190, 236, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLine.sizePolicy().hasHeightForWidth())
        self.usernameLine.setSizePolicy(sizePolicy)
        self.usernameLine.setSizeIncrement(QtCore.QSize(0, 0))
        self.usernameLine.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.usernameLine.setFont(font)
        self.usernameLine.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.usernameLine.setWhatsThis("")
        self.usernameLine.setText("")
        self.usernameLine.setMaxLength(24)
        self.usernameLine.setDragEnabled(False)
        self.usernameLine.setClearButtonEnabled(True)
        self.usernameLine.setObjectName("usernameLine")
        self.passwordLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLine.setGeometry(QtCore.QRect(132, 240, 236, 36))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.passwordLine.setFont(font)
        self.passwordLine.setText("")
        self.passwordLine.setMaxLength(24)
        self.passwordLine.setClearButtonEnabled(True)
        self.passwordLine.setObjectName("passwordLine")
        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setGeometry(QtCore.QRect(80, 140, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(16)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.loginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginLabel.setObjectName("loginLabel")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(370, 461, 126, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.exitButton.setFont(font)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.exitButton.setObjectName("exitButton")
        loginWindow.setCentralWidget(self.centralwidget)

        self.loginButton.clicked.connect(self.login)
        self.exitButton.clicked.connect(loginWindow.close)
        self.loginWindow = loginWindow

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "PAS: Вход в систему"))
        self.loginButton.setText(_translate("loginWindow", "Войти"))
        self.usernameLine.setPlaceholderText(_translate("loginWindow", "Логин"))
        self.passwordLine.setPlaceholderText(_translate("loginWindow", "Пароль"))
        self.loginLabel.setText(_translate("loginWindow", "Вход в систему"))
        self.exitButton.setText(_translate("loginWindow", "Выход"))

    def mainWindowShow(self, permissions):
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(permissions)
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()

    login = utils_gui.login

import bg_rc
import blur_bg_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())