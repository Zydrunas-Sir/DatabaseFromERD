import sqlite3


class DatabaseContextManager(object):
    """This class exists for us to use less lines of code than necessary for queries.
        __init__: used to set database file name.
        __enter__: opens connection and creates cursor.
        __exit__: commits the changes to database file and closes connection."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

def create_table_moketojas():
    query = """CREATE TABLE IF NOT EXISTS moketojas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asmensKodas TEXT,)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

