import pandas as pd
import sqlite3

connection = sqlite3.connect("chinook.db")
table_client = pd.read_sql("SELECT * FROM customers", connection)
print(table_client)
connection.close()
