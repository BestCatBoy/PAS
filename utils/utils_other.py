import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import hashlib
import string
from random import choice

from sys import path
path.insert(0, '../core')
from config import mailLogin, mailPassword

def sendMail(recipient, header, content):
    charset = 'utf-8'

    msg = MIMEText(f'{content}', 'plain', charset)
    msg['Subject'] = Header(header, charset)
    msg['From'] = mailLogin
    msg['To'] = recipient

    smtp = smtplib.SMTP('smtp.yandex.ru', 587, timeout = 10)

    try:
        smtp.starttls()
        smtp.login(mailLogin, mailPassword)
        smtp.sendmail(msg['From'], recipient, msg.as_string())

    except:
        raise ConnectionError("Не удалось отправить данные на указанный email адрес")

    finally:
        smtp.quit()

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