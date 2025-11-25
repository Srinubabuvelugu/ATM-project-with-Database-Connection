from exception import InvalidAccountError, AuthenticationError
from database.login_account import LoginAccount


def login(account: int, password: str):
    try:
        obj_la = LoginAccount(account= account, password=password)
        print("This is from atm/login.py:",obj_la.login_account())
        return obj_la.login_account()
    except Exception as e:
        return f"Something wrong in atm/login.py"

