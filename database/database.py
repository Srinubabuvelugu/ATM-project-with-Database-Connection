import mysql.connector as SQLC
# importing tables creation file
# from tables import tables_creation
database = SQLC.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'bank'
)

cursor = database.cursor()
# print("Loaded database.py →", dir())

# calling tables creating 
# tables_creation()

