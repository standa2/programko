import sqlite3

conn = sqlite3.connect("hokus.db")
cursor = conn.cursor()

input_name = input("Add name of a lab: ")

cursor.execute(
    "INSERT INTO labs (name) VALUES (?)", (input_name,)
)

conn.commit()

cursor.execute("SELECT * FROM labs")
rows = cursor.fetchall()

for row in rows:
    print(row[1])
 
conn.close()
