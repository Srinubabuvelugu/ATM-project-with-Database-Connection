## list of tuple to set of accounts
def list_tuple_accounts_to_set_account(accounts_list:list[tuple]):
    accounts = {}
    for tup in accounts_list:
        if type(tup) == tuple:
            accounts.add(tup[0])
    return accounts

# get amount 
def get_amount(amount_list:list[tuple])->int:
    return amount_list[0][0]