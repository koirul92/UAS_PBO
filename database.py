import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("dataUAS.db")
        self.cursor = self.conn.cursor()

    def query(self, query, param=""):
        self.cursor.execute(query, param)
        self.conn.commit()

    def resultOne(self):
        return self.cursor.fetchone()

    def resultAll(self):
        return self.cursor.fetchall()
