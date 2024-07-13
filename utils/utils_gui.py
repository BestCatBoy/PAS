from PyQt5 import QtCore, QtGui, QtWidgets
import utils_other

from sys import path
path.insert(0, '../core')
from core import table
path.pop()

def checkUser(login, password):
    usersData = table('personnel')
    users = usersData.getData()

    hashPassword = utils_other.getHash(password)

    for user in users:
        if (user['login'] == login) and (user['password'] == hashPassword):
            return user['permissions']

    return False

def login(object):
    login = object.usernameLine.text()
    password = object.passwordLine.text()

    user = checkUser(login, password)
    if user is not False:
        permissions = user

        object.mainWindowShow(permissions)
        object.loginWindow.close()

    else: message("Неверные логин или пароль")

def fillTable(object):
    for key in object.gettedId.keys():
        object.gettedId[key] = []

    students = table('students')
    data = students.getData()

    if len(data) > 0:
        for student in data:
            object.gettedId['students'].append(student['id'])

        __addItems(data, object.studentsTable)

    if object.permissions == 'Администратор':
        personnel = table('personnel')
        data = personnel.getData()

        for personnel in data:
            object.gettedId['personnel'].append(personnel['id'])

        __addItems(data, object.personnelTable)

def __cleanTable(tableObject):
    for row in range(tableObject.rowCount()):
        tableObject.removeRow(0)

def updateTable(object):
    __cleanTable(object.studentsTable)

    if object.permissions == 'Администратор':
        __cleanTable(object.personnelTable)

    object.fillTable()

def __addItems(data, tableObject):
    dataKeys = list(data[0].keys())

    if len(dataKeys) > 4:
        columns = dataKeys[1:7]
        columns.append(dataKeys[-1])

    else: columns = dataKeys[1::]

    for row in range(len(data)):
        tableObject.insertRow(row)

        for column_db, column_table in zip(columns, range(len(columns))):
            tableObject.setItem(
                row, column_table, QtWidgets.QTableWidgetItem(data[row][column_db]))

def onChangedTab(object, index):
    object.activeTableName = object.tables[index]
    object.activeTable = table(object.activeTableName)
    object.currentTable = object.tableWidgets[object.activeTableName]

def addRow(object):
    rowIndex = object.currentTable.rowCount()
    object.currentTable.insertRow(rowIndex)

def saveAll(object):
    try:
        __saveStudents(object)
        __savePersonnel(object)

    except: message("Поля заполнены неверно")

def __saveStudents(object):
    students = table('students')

    for student in students.getData():
        __delData(students, student)

    rowIndex = object.studentsTable.rowCount()
    if rowIndex > 0:

        exportData = __getExportStudentsData(object.studentsTable, rowIndex)
        for data in exportData:
            __addStudent(students, data)

def __savePersonnel(object):
    if object.permissions == 'Администратор':
        personnel = table('personnel')
        gettedData = personnel.getData()

        rowIndex = object.personnelTable.rowCount()
        if rowIndex > 0:
            dataIndex = len(gettedData)

            exportData = __getExportPersonnelData(
                object.personnelTable, rowIndex, dataIndex, gettedData)

        for personnel_i in gettedData:
            __delData(personnel, personnel_i)

        for data in exportData:
            __addPersonnel(personnel, data)

def __addStudent(tableObject, data):
    tableObject.addData(
        fullName = data['fullName'],
        dateOfBirth = data['dateOfBirth'],
        address = data['address']
    )

def __getExportStudentsData(tableWidget, rowIndex):
    exportData = []

    for i in range(rowIndex):
        localDict = {
            'fullName':     tableWidget.item(i, 0).text(),
            'dateOfBirth':  tableWidget.item(i, 1).text(),
            'address':      tableWidget.item(i, 2).text()
        }

        exportData.append(localDict)

    return exportData

def __addPersonnel(tableObject, data):
    tableObject.addData(
        fullName = data['fullName'],
        dateOfBirth = data['dateOfBirth'],
        number = data['number'],
        mail = data['mail'],
        address = data['address'],
        passport = data['passport'],
        login = data['login'],
        password = data['password'],
        permissions = data['permissions']
    )

def __getExportPersonnelData(tableWidget, rowIndex, dataIndex, data):
    exportData = []

    for i in range(rowIndex):
        login = utils_other.getRandomUserData()
        password = utils_other.getRandomUserData()
        permissions = tableWidget.item(i, 6).text()

        if i < dataIndex:
            login = data[i]['login']
            password = data[i]['password']
            permissions = data[i]['permissions']

        else:
            mail = tableWidget.item(i, 3).text()
            fullName = tableWidget.item(i, 0).text()

            __sendMail(mail, login, password, fullName)

            password = utils_other.getHash(password)

        localDict = {
            'fullName':     tableWidget.item(i, 0).text(),
            'dateOfBirth':  tableWidget.item(i, 1).text(),
            'number':       tableWidget.item(i, 2).text(),
            'mail':         tableWidget.item(i, 3).text(),
            'address':      tableWidget.item(i, 4).text(),
            'passport':     tableWidget.item(i, 5).text(),
            'login':        login,
            'password':     password,
            'permissions':  permissions
        }

        exportData.append(localDict)

    return exportData

def __delData(tableObject, row):
    id_del = row['id']
    tableObject.delData(
        column = 'id',
        data = id_del
    )

def __sendMail(mail, login, password, fullName):
    msg = (
        f"Здравствуйте, {fullName}.\n"
        "Вы были успешно зарегистированы в системе PAS.\n"
        "Ваши личные данные для входа в систему:\n"
        f"Логин:\t  {login}\nПароль:\t{password}"
    )

    utils_other.sendMail(
        recipient = mail,
        header = 'Логин и пароль для входа в систему PAS',
        content = msg
    )

def delRow(object):
    row = object.currentTable.currentRow()
    object.currentTable.removeRow(row)

def message(messageType):
    messageWindow = QtWidgets.QMessageBox()
    messageWindow.setWindowTitle("PAS")
    messageWindow.setText(messageType)

    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap("../img/logo.ico"),
        QtGui.QIcon.Normal,
        QtGui.QIcon.Off
    )
    messageWindow.setWindowIcon(icon)

    messageWindow.exec_()