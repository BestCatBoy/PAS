import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import hashlib
import string
from random import choice

def getHash(string):
    hash256 = hashlib.new('sha256')
    hash256.update(string.encode())

    return hash256.hexdigest()

def getRandomUserData():
    symbols = string.printable[:62]
    userData = ""

    for i in range(12):
        userData += choice(symbols)

    return userData

from core import table

password = getRandomUserData()
table('personnel').addData(
    fullName = "Марьина Юлия Максимовна",
    dateOfBirth = "15.02.1987",
    number = "89200886542",
    mail = "maryinaum1987@yandex.ru",
    address = "Ул. Набережная, д. 8, кв. 91",
    passport = "2207 656785",
    login = getRandomUserData(),
    password = getHash(password),
    permissions = "Завуч")
