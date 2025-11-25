from database.database import database, cursor

class Register:
    def __init__(self,account:int, password:str, email:str, amount:int):
        self.account = account
        self._email = email
        self.__password = password
        self.__amount= amount
    def register_account(self)-> bool:
        try:
            # checking weather user is exists or not
            account_check = f"SELECT COUNT(ACCOUNT) FROM ACCOUNTS WHERE {self.account} = ACCOUNT;"
            cursor.execute(account_check)
            res = cursor.fetchall()
            
            
            if res[0][0] == 0:
                # if user not exist in account table add user to account table and users table
                # adding user to account table
                insert_user = "INSERT INTO ACCOUNTS(ACCOUNT, PASSWORD) VALUES(%s, %s)"
                values = (self.account, self.__password)
                cursor.execute(insert_user, values)
                # add user to users table
                insert_amount = 'INSERT INTO USERS(ACCOUNT,USERNAME, EMAIL, AMOUNT) VALUES (%s, %s, %s, %s)'
                amount_value = (self.account, self._email,self._email, self.__amount)
                cursor.execute(insert_amount, amount_value)
                
                database.commit()
                return "User added successfully and run again and login"

            else:
                return "Account already exist Try to check your account"
            
        except Exception as e:
            return f"Something wrong in atm/database/register.py :{e}" 