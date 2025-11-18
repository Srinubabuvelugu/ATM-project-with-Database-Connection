import data as d
from database.amount_fetch import AmountFetch
def balance(account:int):
    obj_af = AmountFetch(account=account)
    curr_amount = obj_af.amountFetch()

    return f"Current balance is {curr_amount}"
    