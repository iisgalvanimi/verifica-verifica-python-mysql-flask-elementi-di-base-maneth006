import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="verifica"
)

risp_id3 = int(input("Inserisci l'id dell'album che vuoi modificare:  ")) 
artista = input("Inserisci il artista: ")
album = input("Inserisci la album: ")
genere = input("Inserisci la genere: ")
while True:
      try:
                Anno_pubblicazione = int(input("Inserisci l'anno: "))  # Età come intero
                break
      except ValueError:
                print("Errore: inserisci un numero intero valido per l'anno.")
Etichetta_discografica = input("Inserisci la Etichetta discografica: ")
queryupdate = "UPDATE musica SET Artista, Album, Genere, Anno_pubblicazione, Etichetta_discografica) VALUES (%s, %s, %s, %s, %s)"
valori = (artista, album, genere, Anno_pubblicazione, Etichetta_discografica)
mycursor.execute(queryupdate, valori)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

'''
while True:
  risp = int(input("Inserisci l'id dell'album che vuoi eliminare: "))
  controllo = "SELECT COUNT(*) FROM musica WHERE id = %s"
  mycursor.execute(controllo, (risp,))
  lista = mycursor.fetchone()[0]

  if lista == 0:
      print("L'ID inserito non esiste nella tabella.")
  else:
      # Se l'ID esiste, procedi con l'eliminazione
      elimina = "DELETE FROM musica WHERE id = %s"
      mycursor.execute(elimina, (risp,))
      mydb.commit()
      print("Album eliminato con successo.")
'''



'''
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
  '''

