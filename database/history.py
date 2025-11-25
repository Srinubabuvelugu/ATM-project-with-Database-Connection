from database.database import database, cursor


class MiniStatement:
    def mini_statement(self, account):
        try:
            mini_statement_query = """SELECT AMOUNT, TRANSACTION_TYPE FROM TRANSACTIONS 
                                     WHERE ACCOUNT = %s LIMIT 10;"""
            cursor.execute(mini_statement_query, (account,))
            transactions = cursor.fetchall()
            return transactions
        except Exception as e:
            return f"Something wrong in atm/database/history.py:{e}"