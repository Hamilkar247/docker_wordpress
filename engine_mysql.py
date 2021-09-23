import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1:3310", user="db_user", password="db_pass", database="db_name"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
