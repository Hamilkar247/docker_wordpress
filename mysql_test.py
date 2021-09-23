import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="db_user",
  password="db_pass",
  port="3310",
  database="db_name"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
