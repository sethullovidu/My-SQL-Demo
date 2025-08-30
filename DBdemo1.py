import mysql.connector

# Try to connect
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # replace if you use another user
    password="YOUR_PASSWORD"  # replace with your real MySQL password
)

print("Connection Successful?", conn.is_connected())

# Close connection
conn.close()
