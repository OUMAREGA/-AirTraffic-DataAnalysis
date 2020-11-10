import mysql.connector as db #import de mysql

#connexion à la bdd
mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="30000",
  user="root",
  password="root",
  database="avions"
)

#nom de variable : mycursor, type : mysql.connector.cursor.MySQLCursor
mycursor = mydb.cursor()

#Création de la table airlines avec les champs : carrier et name
mycursor.execute("CREATE TABLE IF NOT EXISTS airlines (carrier CHAR(2) PRIMARY KEY, name VARCHAR(100) NOT NULL)")