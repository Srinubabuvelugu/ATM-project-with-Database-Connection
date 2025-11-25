from database.database import database, cursor


class LoginAccount:
    def __init__(self, account:int, password:int):
        self.account = account
        self.__password = password
    
    def login_account(self):
        try:
            get_password_query = f"""SELECT PASSWORD FROM ACCOUNTS 
                                    WHERE ACCOUNT = {self.account};"""
            
            cursor.execute(get_password_query)
            db_password = int(cursor.fetchall()[0][0])
            if db_password:
                if db_password == self.__password:
                    return True
                else:
                    return False
            else: 
                return False
        except Exception as e:
            return f"Someting wrong in amt/database/login_account.py"
        