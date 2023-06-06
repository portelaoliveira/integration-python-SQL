import pyodbc

connection_data = "Driver={SQLite3 ODBC Driver};Server=localhost;Database=chinook.db"
connection = pyodbc.connect(connection_data)
print("Connection successful")

cursor = connection.cursor()
cursor.execute(
    """
INSERT INTO albums (Title, ArtistId)
VALUES
('Lira Rock', 4)
"""
)
cursor.commit()
cursor.close()
connection.close()
print("Connection finalized")
