import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="db_user",
  password="db_pass",
  port="3310",
  database="db_name"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
