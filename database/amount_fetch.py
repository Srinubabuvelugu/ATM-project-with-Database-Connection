from database.database import database, cursor
from database.utility import list_tuple_accounts_to_set_account, get_amount

class AmountFetch:
    def __init__(self, account):
        self.account = account

    def amountFetch(self):
        try:
            accounts_query = "SELECT 1 FROM ACCOUNTS WHERE ACCOUNT = %s;"
            cursor.execute(accounts_query,(self.account,))
            res_account = cursor.fetchall()
            # accounts = list_tuple_accounts_to_set_account(accounts_list=res_account)
            # print(accounts)
            if res_account:# self.account in accounts:
                amount_query = f"SELECT AMOUNT FROM USERS WHERE ACCOUNT =%s;"
                cursor.execute(amount_query, (self.account,))
                res_amount = cursor.fetchall()
                # print(res_amount)
                amount = get_amount(amount_list=res_amount)
                return amount
            else:
                print("Account not found")
        except Exception as e:
            return f"Something wrong in database/amount_fetch.py:{e}"
