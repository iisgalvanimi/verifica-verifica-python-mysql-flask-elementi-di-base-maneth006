import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="verifica"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS verifica")
mycursor.execute("USE verifica")


mycursor.execute("SELECT * FROM musica")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)