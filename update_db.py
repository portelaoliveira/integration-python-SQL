import pyodbc

connection_data = "Driver={SQLite3 ODBC Driver};Server=localhost;Database=chinook.db"
connection = pyodbc.connect(connection_data)
print("Connection successful")

cursor = connection.cursor()

new_email = input("Novo E-mail: ")
old_email = input("Informe seu E-mail atual: ")

cursor.execute(
    f"""
    UPDATE customers SET Email="{new_email}" WHERE Email="{old_email}"
"""
)

cursor.commit()

cursor.close()
connection.close()
print("Connection finalized")
