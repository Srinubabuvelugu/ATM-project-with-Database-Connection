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
                        AMOUNT DOUBLE(10,2) default 0,
                        FOREIGN KEY(ACCOUNT) REFERENCES ACCOUNTS(ACCOUNT)   
                        );"""
        cursor.execute(users_table)
        transaction_table = """
                CREATE TABLE IF NOT EXISTS TRANSACTIONS(
                TRANSACTION_ID BIGINT NOT NULL AUTO_INCREMENT,
                ACCOUNT BIGINT NOT NULL,
                TRANSACTION_TYPE VARCHAR(20) NOT NULL,
                AMOUNT DOUBLE(10,2) NOT NULL,
                PRIMARY KEY(TRANSACTION_ID),
                FOREIGN KEY(ACCOUNT) REFERENCES ACCOUNTS(ACCOUNT)
            );
        """
        cursor.execute(transaction_table)
        database.commit()
        return True
    except Exception as e:
        return f"Something wrong in atm/database/tables.py :{e}"