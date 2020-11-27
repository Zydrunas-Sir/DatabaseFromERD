from Tables.DatabaseContextManager import DatabaseContextManager


def create_table_plan():
    query = """CREATE TABLE IF NOT EXISTS Plan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_type TEXT,
        channel_list TEXT,
        exclusives TEXT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_plan(channel_type: str, channel_list: str, exclusives: str):
    query = """INSERT INTO Plan(channel_type, channel_list, exclusives) VALUES(?,?,?)"""
    parameters = [channel_type, channel_list, exclusives]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_plan():
    query = """SELECT * FROM Plan"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_Plan_exclusives(old_exclusives: str, new_exclusives: str):
    query = """UPDATE Plan
                SET exclusives = ?
                WHERE exclusives = ?"""
    parameters = [new_exclusives, old_exclusives]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_plan(channel_type: str):
    query = """DELETE FROM Plan
                WHERE channel_type = ?"""
    parameters = [channel_type]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_plan_packages_plan():
    query = """SELECT * FROM Plan
                JOIN Plan_packages
                    ON Plan.id = Plan_packages.plan_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
