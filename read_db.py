import pandas as pd
import pyodbc

connection_data = "Driver={SQLite3 ODBC Driver};Server=localhost;Database=chinook.db"
connection = pyodbc.connect(connection_data)
print("Connection successful")

cursor = connection.cursor()

cursor.execute(
    """
SELECT * FROM customers
"""
)

values = (
    cursor.fetchall()
)  # Pega as informações do cursor e armazena na variável as informações em um formato de lista de tuplas.
description = cursor.description
columns = [tuple[0] for tuple in description]
table_client = pd.DataFrame.from_records(values, columns=columns)
print(table_client)

cursor.close()
connection.close()
print("Connection finalized")
