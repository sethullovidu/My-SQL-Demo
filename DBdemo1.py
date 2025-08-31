import mysql.connector 
DB_NAME = "school" 
conn = mysql.connector.connect( 
host="localhost", 
user="root", 
password="1234", 
port=3307,
database=DB_NAME 
) 
cur = conn.cursor() 
cur.execute(""" 
CREATE TABLE IF NOT EXISTS students ( 
id INT AUTO_INCREMENT PRIMARY KEY, 
name VARCHAR(50) NOT NULL, 
age INT 
) ENGINE=InnoDB 
""") 
print("Table ready: students") 
cur.close() 
conn.close() 