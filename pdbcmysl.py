import mysql.connector
conn = mysql.connector.connect(
host="localhost",
user="root",
password="Prudhvi12@",
database="mysql_db"
)
cursor = conn.cursor()
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS students ( 
id INT PRIMARY KEY, 
name VARCHAR(100) NOT NULL, 
age INT, 
grade VARCHAR(2) 
) 
""")
# cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s)", (1, "Alice", 14, "A"))
# cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s)", (2, "Bob", 15, "B"))
# cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s)", (3, "Charlie", 14, "A"))
# conn.commit()
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
  print(row)
cursor.execute("UPDATE students SET grade = %s WHERE name = %s", ("A+", "Bob"))
conn.commit()
cursor.execute("DELETE FROM students WHERE id = %s", (3,))
conn.commit()
cursor.close()
conn.close()