import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()

    def get_information(self):
        sql = "SELECT Name, Survived FROM data ORDER BY random()"
        return self.__select_data(sql)
    
    
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
