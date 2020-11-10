import mysql.connector as db

#Se connecter à la BDD
mydb = db.connect(
  host="localhost",
  port="30000",
  user="root",
  database="avions",
  password="root"
)
#Nom de variable : mycursor, type : mysql.connector.cursor.MySQLCursor
mycursor = mydb.cursor()

#Création de la table airports
mycursor.execute("CREATE TABLE IF NOT EXISTS airports (faa CHAR(4) PRIMARY KEY, name VARCHAR(100), lat FLOAT NOT NULL, lon FLOAT NOT NULL, alt VARCHAR(7), tz VARCHAR(4), dst CHAR(1), tzone VARCHAR(100)) ")