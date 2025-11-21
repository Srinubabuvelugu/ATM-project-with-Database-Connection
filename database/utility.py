## list of tuple to set of accounts
def list_tuple_accounts_to_set_account(accounts_list:list[tuple]):
    try:
        accounts = {}
        for tup in accounts_list:
            if type(tup) == tuple:
                accounts.add(tup[0])
        return accounts
    except Exception as e:
        return f"Something wrong in atm/database/utility.py:{e}"

# get amount 
def get_amount(amount_list:list[tuple])->int:
    try: 
        return amount_list[0][0]
    except Exception as e:
        return f"Something wrong atm/database/utility.py:{e}"