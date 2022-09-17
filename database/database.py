import sqlite3
from data.configs import DBNAME

class DataBase:
    def __init__(self):
        self.database = sqlite3.connect(DBNAME, check_same_thread=False)

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False):
        with self.database as db:
            cursor = db.cursor()
            print(args)
            cursor.execute(sql, args)
            if commit:
                result = db.commit()
            if fetchone:
                result = cursor.fetchone()
            if fetchall:
                result = cursor.fetchall()
            return result

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS translate(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id VARCHAR(20),
            original_text TEXT,
            src TEXT,
            dest TEXT,
            translated_text TEXT
        )'''
        self.manager(sql, commit=True)

    def insert_into_db(self, telegram_id, original_text, src, dest, translated_text):
        sql = '''INSERT INTO translate(telegram_id, original_text, src, dest, translated_text)
        VALUES (?,?,?,?,?)
        '''
        self.manager(sql, telegram_id, original_text, src, dest, translated_text, commit=True)
