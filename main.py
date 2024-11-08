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
mycursor.execute("CREATE TABLE IF NOT EXISTS musica (id INT PRIMARY KEY AUTO_INCREMENT, Artista VARCHAR(255), Album VARCHAR(255), Genere VARCHAR(255), Anno_pubblicazione INT, Etichetta_discografica VARCHAR(255))")
sql = "INSERT INTO musica (id, Artista, Album, Genere, Anno_pubblicazione, Etichetta_discografica) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
('01', 'The Beatles', 'Abbey Road', 'Rock', 1969, 'Apple Records'),
('02', 'Queen', 'A Night at the Opera', 'Rock', 1975, 'EMI'),
('03', 'Michael Jackson', 'Thriller', 'Pop', 1982, 'Epic Records'),
('04', 'Pink Floyd', 'The Dark Side of the Moon', 'Progressive Rock', 1973, 'Harvest Records'),
('05', 'Nirvana', 'Nevermind', 'Grunge', 1991, 'DGC Records'),
('06', 'Led Zeppelin', 'IV', 'Rock', 1971, 'Atlantic Records'),
('07', 'Metallica', 'Master of Puppets', 'Heavy Metal', 1986, 'Elektra Records'),
('08', 'Beyoncé', 'Lemonade', 'R&B', 2016, 'Columbia Records'),
('09', 'Eminem', 'The Marshall Mathers LP', 'Hip Hop', 2000, 'Interscope Records'),
('10', 'Bob Marley & The Wailers', 'Legend', 'Reggae', 1984, 'Island Records')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")