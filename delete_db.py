import pyodbc

connection_data = "Driver={SQLite3 ODBC Driver};Server=localhost;Database=chinook.db"
connection = pyodbc.connect(connection_data)
print("Connection successful")

cursor = connection.cursor()

cursor.execute(
    """
    DELETE FROM albums WHERE AlbumId=2
"""
)

cursor.commit()

cursor.close()
connection.close()
print("Connection finalized")
