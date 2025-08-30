import mysql.connector

# Try to connect
conn = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="1234",
    port=3307
)

print("Connected?", conn.is_connected())
cur = conn.cursor()


db_name = "Student"

cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
print(f"Database ready: {db_name}")


cur.execute(f"USE {db_name}")

cur.close()
conn.close()
