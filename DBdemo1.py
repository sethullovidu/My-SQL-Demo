import mysql.connector

# Try to connect
conn = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="1234",
    port= 3307
)

print("Connection Successful?", conn.is_connected())

# Close connection
conn.close()
