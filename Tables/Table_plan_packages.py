from Tables.DatabaseContextManager import DatabaseContextManager


def create_table_plan_packages():
    query = """CREATE TABLE IF NOT EXISTS Plan_packages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        television_id INTEGER,
        plan_id INTEGER,
        price FLOAT,
        date_of_purchase DATE,
        FOREIGN KEY (television_id) REFERENCES Television(id),
        FOREIGN KEY (plan_id) REFERENCES Plan(id)
        )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_plan_packages(television_id: int, plan_id: int, price: float, date_of_purchase: dict):
    query = """INSERT INTO Plan_packages(channel_type, channel_list, exclusives) VALUES(?,?,?,?)"""
    parameters = [television_id, plan_id, price, date_of_purchase]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_plan_packages():
    query = """SELECT * FROM Plan_packages"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_plan_packages(old_price: float, new_price: float):
    query = """UPDATE Plan_packages
                SET price = ?
                WHERE price = ?"""
    parameters = [new_price, old_price]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_plan_packages(date_of_purchase: dict):
    query = """DELETE FROM Plan_packages
                WHERE date_of_purchase = ?"""
    parameters = [date_of_purchase]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_payer_plan_packages():
    query = """SELECT * FROM Plan_packages
                JOIN Payer
                    ON Plan_packages.id = Payer.plan_packages_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
