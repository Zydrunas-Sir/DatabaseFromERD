from database import DatabaseContextManager


def create_table_internet():
    query = """CREATE TABLE IF NOT EXISTS Internet(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        IP TEXT,
        bill FLOAT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_internet(ip: str, bill: float):
    query = """INSERT INTO Internet(IP, bill) VALUES(?,?)"""
    parameters = [ip, bill]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_internet():
    query = """SELECT * FROM Internet"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_internet_ip(old_ip: str, new_ip: str):
    query = """UPDATE Internet
                SET IP = ?
                WHERE IP = ?"""
    parameters = [new_ip, old_ip]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_Internet(ip: str):
    query = """DELETE FROM Internet
                WHERE IP = ?"""
    parameters = [ip]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_payer_internet():
    query = """SELECT * FROM Internet
                JOIN Payer
                    ON Internet.id = Payer.internet_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
