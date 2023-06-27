import sqlite3

import pandas as pd

connection = sqlite3.connect("chinook.db")
table_client = pd.read_sql("SELECT * FROM customers", connection)
print(table_client)
connection.close()
