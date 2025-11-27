
from database.reduce_amount import ReduceAmount


from exception import InvalidAccountError, InsufficientBalanceError, InvalidAmountError

def withdraw(account: int, amount: int):
    try:
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")
        obj_ra = ReduceAmount(account=account, withdraw_amount=amount)
        
        

        return obj_ra.reduce_amount()
    except Exception as e:
        return f"Something wrong in atm/withdrawal.py :{e}"
