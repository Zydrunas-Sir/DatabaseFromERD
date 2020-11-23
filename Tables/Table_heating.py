from database import DatabaseContextManager


def create_table_heating():
    query = """CREATE TABLE IF NOT EXISTS Heating(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        heating_costs FLOAT
        )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_heating(heating_costs: float):
    query = """INSERT INTO Heating(heating_costs) VALUES(?)"""
    parameters = [heating_costs]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_heating():
    query = """SELECT * FROM Heating"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_heating_costs(old_heating_costs: float, new_heating_costs: float):
    query = """UPDATE Heating
                SET heating_costs = ?
                WHERE heating_costs = ?"""
    parameters = [new_heating_costs, old_heating_costs]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_electricity(heating_costs: float):
    query = """DELETE FROM Heating
                WHERE heating_costs = ?"""
    parameters = [heating_costs]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_payer_heating():
    query = """SELECT * FROM Heating
                JOIN Payer
                    ON Heating.id = Payer.heating_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
