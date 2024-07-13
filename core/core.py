from config import connect

class table():

    def getData(self):
        dbObject = connect()

        with dbObject.cursor() as cursor:
            cursor.execute(f'SELECT * FROM {self.tableName}')
            data = [row for row in cursor.fetchall()]

        dbObject.close()

        return data

    def addData(self, **kwargs):
        dbObject = connect()

        columns = [arg for arg in kwargs.keys()]
        columns = ", ".join(columns)

        data = [f'"{arg}"' for arg in kwargs.values()]
        data = ", ".join(data)

        with dbObject.cursor() as cursor:
            cursor.execute(
                f'INSERT INTO {self.tableName}({columns}) values({data})')
            dbObject.commit()

        dbObject.close()

    def delData(self, column, data):
        dbObject = connect()

        with dbObject.cursor() as cursor:
            cursor.execute(f'DELETE FROM {self.tableName} WHERE {column} = "{data}"')
            dbObject.commit()

        dbObject.close()

    def __init__(self, tableName):
        self.tableName = tableName