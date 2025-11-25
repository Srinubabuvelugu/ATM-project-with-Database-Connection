from database.database import cursor, database
from database.history import MiniStatement

def get_mini_statement(account:int):
    try:
        obj_ms = MiniStatement()
        transactions = obj_ms.mini_statement(account=account)
        if transactions:
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions found.")
        
        
    except Exception as e:
        return f"Something wrong in atm/database/history.py:{e}"