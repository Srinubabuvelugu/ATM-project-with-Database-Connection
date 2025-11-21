from database.database import cursor, database
def tables_creation():
    try:
        accounts = """
                CREATE TABLE IF NOT EXISTS ACCOUNTS(
                ACCOUNT BIGINT NOT NULL,
                PASSWORD VARCHAR(30) NOT NULL,
                PRIMARY KEY(ACCOUNT));"""

        cursor.execute(accounts)



        users_table = """
                        CREATE TABLE IF NOT EXISTS USERS(
                        Account BIGINT NOT NULL,
                        USERNAME VARCHAR(50) NOT NULL,
                        EMAIL VARCHAR(50) NOT NULL UNIQUE,
                        AMOUNT DOUBLE(10,2),
                        FOREIGN KEY(ACCOUNT) REFERENCES ACCOUNTS(ACCOUNT)   
                        );"""
        cursor.execute(users_table)
        transesaction_table = """
                        CREATE TABLE IF NOT EXISTS TRANSESACTION(
                        TRANSESATION_ID BIGINT NOT NULL,
                        ACCOUNT BIGINT NOT NULL UNIQUE,
                        TRANSESACTION_TYPE VARCHAR(20) NOT NULL,
                        AMOUNT INT NOT NULL)"""

        cursor.execute(transesaction_table)
        database.commit()
        return True
    except Exception as e:
        return f"Something wrong in atm/database/tables.py :{e}"