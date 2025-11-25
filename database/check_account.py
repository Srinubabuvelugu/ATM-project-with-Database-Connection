from database.database import database, cursor
class CheckAccount:
    def check_account_in_database(self, account):
        try:
            accounts_query = "SELECT 1 FROM ACCOUNTS WHERE ACCOUNT = %s;"
            cursor.execute(accounts_query,(account,))
            account_status = cursor.fetchall()
            if account_status:
                return True
            else:
                return False
        except Exception as e:
            return f"Something error in database/check_account.py {e}"