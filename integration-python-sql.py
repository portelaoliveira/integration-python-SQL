import pyodbc

# print(pyodbc.drivers())

connection_data = (
    "Driver={SQLite3 ODBC Driver};Server=localhost;Database=salarios.sqlite"
)
connection = pyodbc.connect(connection_data)
print("Connection successful")

cursor = connection.cursor()
cursor.execute("SELECT * FROM Salaries")

values = cursor.fetchall()
print(values[:10])

cursor.close()
connection.close()
print("Connection finalized")
