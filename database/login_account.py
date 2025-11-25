from database.database import database, cursor


class LoginAccount:
    def __init__(self, account:int, password:int):
        self.account = account
        self.__password = password
    
    def login_account(self):
        try:
            get_password_query = """SELECT PASSWORD FROM ACCOUNTS 
                                    WHERE ACCOUNT = %s;"""
            
            cursor.execute(get_password_query, (self.account,))
            db_password = cursor.fetchall()[0][0]
            
            print("This is from database/login_account.py:", db_password, type(db_password))
            if db_password:
                if db_password == self.__password:
                    return True
                else:
                    return False
            else: 
                return False
        except Exception as e:
            return f"Someting wrong in amt/database/login_account.py"
        