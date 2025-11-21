from database.database import database, cursor
from database.amount_fetch import AmountFetch
from exception import InvalidAccountError, InsufficientBalanceError, InvalidAmountError

class ReduceAmount:
    def __init__(self, account:int,withdraw_amount:int):
        self.account = account
        self.withdraw_amount = withdraw_amount

    # reduce amount method
    def reduce_amount(self):
        try:
            obj_af = AmountFetch(self.account)
            current_amount = obj_af.amountFetch()
            if current_amount >= self.withdraw_amount:
                # updating the amount in database
                update_amount = current_amount - self.withdraw_amount
                update_amount_query = f"UPDATE USERS SET AMOUNT = {update_amount} WHERE ACCOUNT = {self.account};"
                cursor.execute(update_amount_query)
                database.commit()
                return f"Withdrawal successful and current balence is {update_amount}"
            else:
                raise InvalidAmountError("Insufficient funds for this transaction.")

        except Exception as e:
            return f"Something wrong in atm/database/reduce_amount.py :{e}"
            
            