from database.amount_fetch import AmountFetch
from database.database import cursor, database
from database.add_amount import AddAmount
from database.reduce_amount import ReduceAmount
from database.check_account import CheckAccount
#Transfer function definition
def transfer(account:int,to_account:int,amount:int):
    try:
        obj_cka = CheckAccount()
        if obj_cka.check_account_in_database(account=account):
            if obj_cka.check_account_in_database(to_account):
                obj_fa = AmountFetch(account=account)
                curr_amount = obj_fa.amountFetch()
                if curr_amount >= amount:
                    obj_ra = ReduceAmount(account=account, withdraw_amount=amount)
                    reduce_amount_status = obj_ra.reduce_amount(transfer_type="transfer")
                    obj_add_amount = AddAmount(account=to_account, deposite_amount=amount)
                    obj_add_amount.add_amount()
                    return reduce_amount_status
                else:
                    return "Insufficient Balance"
            else:
                return "Reciver account not found"
        else:
            return "Sender account not found"
    except Exception as e:
        return f"Something wrong in atm/transfer.py:{e}"
                    
                    
                    

                    


                     
        
