from database import DatabaseContextManager


def create_table_television():
    query = """CREATE TABLE IF NOT EXISTS Television(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        display_diagonal INTEGER,
        display_technology TEXT,
        resolution TEXT,
        HD_type TEXT
        )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_television(display_diagonal: int, display_technology: str, resolution: str, hd_type: str):
    query = """INSERT INTO Payer_profile(display_diagonal, display_technology,
                resolution, HD_type) VALUES(?,?,?,?)"""
    parameters = [display_diagonal, display_technology, resolution, hd_type]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_television():
    query = """SELECT * FROM Television"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_television_resolution(old_resolution: str, new_resolution: str):
    query = """UPDATE Television
                SET resolution = ?
                WHERE resolution = ?"""
    parameters = [new_resolution, old_resolution]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_television(hd_type: str):
    query = """DELETE FROM Television
                WHERE HD_type = ?"""
    parameters = [hd_type]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_plan_packages_television():
    query = """SELECT * FROM Television
                JOIN Plan_packages
                    ON Television.id = Plan_packages.television_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
