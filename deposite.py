
from database.database import database, cursor
from database.add_amount import AddAmount

#deposite function definition
def deposite(account:int,amount:int):
    try:
        obj_am = AddAmount(account=account, deposite_amount= amount)
        return obj_am.add_amount()
    except Exception as e:
        return f"Something wrong in atm/deposite.py :{e}"