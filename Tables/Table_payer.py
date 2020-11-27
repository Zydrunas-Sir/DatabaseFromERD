from Tables.DatabaseContextManager import DatabaseContextManager


def create_table_payer():
    query = """CREATE TABLE IF NOT EXISTS Payer(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        identification_number TEXT,
        payer_profile_id INTEGER,
        internet_id INTEGER,
        electricity_id INTEGER,
        heating_id INTEGER,
        plan_packages_id INTEGER,
        FOREIGN KEY (payer_profile_id) REFERENCES Payer_profile(id),
        FOREIGN KEY (internet_id) REFERENCES Internet(id),
        FOREIGN KEY (electricity_id) REFERENCES Electricity(id),
        FOREIGN KEY (heating_id) REFERENCES Heating(id),
        FOREIGN KEY (plan_packages_id) REFERENCES Plan_packages(id)
        )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_payer(identification_number: int, payer_profile: int, internet_id: int, electricity_id: int,
                 heating_id: int, plan_packages_id: int):
    query = """INSERT INTO Payer(identification_number, payer_profile, internet_id, electricity_id, heating_id,
    plan_packages_id) VALUES(?,?,?,?,?,?)"""
    parameters = [identification_number, payer_profile, internet_id, electricity_id, heating_id,
                  plan_packages_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_payer():
    query = """SELECT * FROM Payer"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_payer_identification_number(old_identification_number: int, new_identification_number: int):
    query = """UPDATE Payer
                SET identification_number = ?
                WHERE identification_number = ?"""
    parameters = [new_identification_number, old_identification_number]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_payer(identification_number: str):
    query = """DELETE FROM Payer
                WHERE identification_number = ?"""
    parameters = [identification_number]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
