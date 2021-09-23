import mysql.connector

import mysql.connector
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path(".")
load_dotenv(dotenv_path=env_path)


mydb = mysql.connector.connect(
  host="localhost",
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  port=os.getenv("MYSQL_PORT"),
  database=os.getenv("DB_NAME")
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
