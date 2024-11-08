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

rispUtente1 = int(input('Quante album vorresti inserire: '))
for _ in range(rispUtente1):
  Artista = input("Nome dell'artista della canzone: ")
  Album = input("Quale album vorresti inserire: ")
  Genere = input("Genere dell'artista della canzone: ")
  Anno_pubblicazione = input("Anno di pubblicazione dell'album: ")
  Etichetta_discografica = input("Nome dell'etichetta discografica: ")
  sql = "INSERT INTO musica (Artista, Album, Genere, Anno_pubblicazione, Etichetta_discografica) VALUES (%s, %s, %s, %s, %s)"
  val = (Artista, Album, Genere, Anno_pubblicazione, Etichetta_discografica)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "inserito")   
