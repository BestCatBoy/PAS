import pymysql
from typing import Final

host:           Final[str] = 'maouicvt.beget.tech'
user:           Final[str] = 'maouicvt_school'
password:       Final[str] = 'Dpjuy74m200324'
db:             Final[str] = 'maouicvt_school'
mailLogin:      Final[str] = 'maou.ichalkovskaya.school@yandex.ru'
mailPassword:   Final[str] = 'dvchjetkezzjepce'

def connect():
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db,
        cursorclass = pymysql.cursors.DictCursor
    )

    return connection