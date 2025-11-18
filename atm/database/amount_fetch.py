from .database import database, cusror
from utility import list_tuple_accounts_to_set_account, get_amount

class AmountFetch:
    def __init__(self, account):
        self.account = account

    def amountFetch(self):
        try:
            accounts_query = """ SELECT ACCOUNT FROM ACCOUNTS"""
            cusror.execute(accounts_query)
            res_account = cusror.fetchall()
            accounts = list_tuple_accounts_to_set_account(accounts_list=res_account)
            if self.account in accounts:
                amount_query = f"SELECT AMOUNT FROM USERS WHERE ACCOUNT = {self.account}"
                cusror.execute(amount_query)
                res_amount = cusror.fetchall()
                amount = get_amount(amount_list=res_amount)
                return amount
        except Exception as e:
            return f"Something wrong in database/amount_fetch.py:{e}"
