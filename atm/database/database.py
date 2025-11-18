import mysql.connector as SQLC
# importing tables creation file
from .tables import tables_creation
database = SQLC.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'bank'
)

cusror = database.cursor()
# calling tables creating 
tables_creation()

