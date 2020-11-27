from Tables.DatabaseContextManager import DatabaseContextManager


def create_table_electricity():
    query = """CREATE TABLE IF NOT EXISTS Electricity(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kWh FLOAT,
        bill FLOAT
        )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_electricity(kwh: float, bill: float):
    query = """INSERT INTO Electricity(kWh, bill) VALUES(?,?)"""
    parameters = [kwh, bill]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_electricity():
    query = """SELECT * FROM Electricity"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_electricity_kWh(old_kwh: float, new_kwh: float):
    query = """UPDATE Electricity
                SET kWh = ?
                WHERE kWh = ?"""
    parameters = [new_kwh, old_kwh]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_electricity(kwh: float):
    query = """DELETE FROM Electricity
                WHERE kWh = ?"""
    parameters = [kwh]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_payer_electricity():
    query = """SELECT * FROM Electricity
                JOIN Payer
                    ON Electricity.id = Payer.electricity_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
