from database import DatabaseContextManager


def create_table_payer_profile():
    query = """CREATE TABLE IF NOT EXISTS Payer_profile(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        last_name TEXT,
        address TEXT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_payer_profile(name: str, last_name: str, address: str):
    query = """INSERT INTO Payer_profile(name, last_name, address) VALUES(?,?,?)"""
    parameters = [name, last_name, address]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_payer_profile():
    query = """SELECT * FROM Payer_profile"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_Payer_profile_address(old_address: str, new_address: str):
    query = """UPDATE Payer_profile
                SET address = ?
                WHERE address = ?"""
    parameters = [new_address, old_address]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_Payer_profile(last_name: str):
    query = """DELETE FROM Payer_profile
                WHERE last_name = ?"""
    parameters = [last_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_payer_profile_payers():
    query = """SELECT * FROM Payer_profile
                JOIN Payer
                    ON Payer_profile.id = Payer.payer_profile_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
