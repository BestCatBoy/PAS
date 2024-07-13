# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10

from PyQt5 import QtCore, QtGui, QtWidgets

from sys import path
path.insert(0, '../core')
from core import table

path.insert(0, '../utils')
import utils_gui
import utils_other

class Ui_MainWindow(object):

    tables = ['students', 'personnel']
    activeTableName = tables[0]
    activeTable = table(activeTableName)
    gettedId = {
        'students': [],
        'personnel': []
    }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 600)
        MainWindow.setMaximumSize(QtCore.QSize(1020, 600))
        MainWindow.setMinimumSize(QtCore.QSize(1020, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1020, 550))
        self.tabWidget.setObjectName("tabWidget")
        self.students = QtWidgets.QWidget()
        self.students.setObjectName("students")
        self.studentsTable = QtWidgets.QTableWidget(self.students)
        self.studentsTable.setGeometry(QtCore.QRect(0, 0, 1020, 525))
        self.studentsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.studentsTable.setObjectName("studentsTable")
        self.studentsTable.setColumnCount(3)
        self.studentsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setHorizontalHeaderItem(2, item)
        self.studentsTable.horizontalHeader().setDefaultSectionSize(323)
        self.tabWidget.addTab(self.students, "")
        self.personnel = QtWidgets.QWidget()
        self.personnel.setObjectName("personnel")
        self.personnelTable = QtWidgets.QTableWidget(self.personnel)
        self.personnelTable.setGeometry(QtCore.QRect(0, 0, 1020, 525))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.personnelTable.setFont(font)
        self.personnelTable.setObjectName("personnelTable")
        self.personnelTable.setColumnCount(7)
        self.personnelTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.personnelTable.setHorizontalHeaderItem(6, item)
        self.personnelTable.horizontalHeader().setDefaultSectionSize(138)
        self.tabWidget.addTab(self.personnel, "")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(5, 555, 111, 41))
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.addButton.setObjectName("addButton")
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(120, 555, 111, 41))
        self.delButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delButton.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.delButton.setObjectName("delButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(350, 555, 111, 41))
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.saveButton.setObjectName("saveButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(905, 555, 111, 41))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.exitButton.setObjectName("exitButton")
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(235, 555, 111, 41))
        self.updateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.updateButton.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.updateButton.setObjectName("updateButton")
        MainWindow.setCentralWidget(self.centralwidget)

        if self.permissions != 'Администратор':
            self.tabWidget.removeTab(1)

        self.tabWidget.tabBarClicked.connect(self.onChangedTab)
        self.addButton.clicked.connect(self.addRow)
        self.saveButton.clicked.connect(self.saveAll)
        self.delButton.clicked.connect(self.delRow)
        self.updateButton.clicked.connect(self.updateTable)

        self.tableWidgets = {
            'students':     self.studentsTable,
            'personnel':    self.personnelTable
        }

        self.currentTable = self.tableWidgets[self.activeTableName]
        self.exitButton.clicked.connect(MainWindow.close)
        self.fillTable()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PAS: МАОУ \"Ичалковская средняя школа\""))
        item = self.studentsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.studentsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.studentsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Адрес"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.students), _translate("MainWindow", "Ученики"))
        item = self.personnelTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.personnelTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.personnelTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Телефон"))
        item = self.personnelTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Почта"))
        item = self.personnelTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Адрес"))
        item = self.personnelTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Паспорт"))
        item = self.personnelTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Права"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.personnel), _translate("MainWindow", "Персонал"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.delButton.setText(_translate("MainWindow", "Удалить"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.updateButton.setText(_translate("MainWindow", "Обновить"))

    fillTable = utils_gui.fillTable
    onChangedTab = utils_gui.onChangedTab
    addRow = utils_gui.addRow
    saveAll = utils_gui.saveAll
    delRow = utils_gui.delRow
    updateTable = utils_gui.updateTable

    def __init__(self, permissions):
        self.permissions = permissions

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())