from .database import cusror, database
def tables_creation():
    accounts = """
            CREATE TABLE IF NOT EXISTS ACCOUNTS(
            ACCOUNT BIGINT NOT NULL,
            PASSWORD VARCHAR(30) NOT NULL,
            PRIMARY KEY(ACCOUNT));"""

    cusror.execute(accounts)



    users_table = """
                CREATE TABLE IF NOT EXISTS USERS(
                Account BIGINT NOT NULL,
                USERNAME VARCHAR(50) NOT NULL,
                EMAIL VARCHAR(50) NOT NULL UNIQUE,
                AMOUNT DOUBLE(10,2),
                FOREIGN KEY(ACCOUNT) REFERENCES ACCOUNTS(ACCOUNT)   
                );"""
    cusror.execute(users_table)
    transesaction_table = """
                    CREATE TABLE IF NOT EXISTS TRANSESACTION(
                    TRANSESATION_ID BIGINT NOT NULL,
                    ACCOUNT BIGINT NOT NULL UNIQUE,
                    TRANSESACTION_TYPE VARCHAR(20) NOT NULL,
                    AMOUNT INT NOT NULL)"""

    cusror.execute(transesaction_table)
    database.commit()
    return True