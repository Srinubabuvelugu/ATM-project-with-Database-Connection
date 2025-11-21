from database.database import database, cursor
from database.amount_fetch import AmountFetch


class AddAmount:
    def __init__(self, account:int, deposite_amount:int):
        self.account = account
        self._amount = deposite_amount
    
    # add amount to account
    def add_amount(self):
        try:
            obj_af = AmountFetch(account=self.account)
            current_amount = obj_af.amountFetch()
            update_amount = current_amount + self._amount
            update_amount_query = f"UPDATE USERS SET AMOUNT = {update_amount} WHERE ACCOUNT = {self.account};"
            cursor.execute(update_amount_query)
            database.commit()
            return f"Withdrawal successful and current balence is {update_amount}"
        except Exception as e:
            return f"Something wrong in atm/database/add_amount.py:{e}"
