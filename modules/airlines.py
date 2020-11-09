import mysql.connector as db #import de mysql

#connexion à la bdd
mydb = mysql.connector.connect(
  host="91.171.69.177",
  port="26550",
  user="oumarh",
  password="oumarhaidara"
)

#nom de variable : mycursor, type : mysql.connector.cursor.MySQLCursor
mycursor = mydb.cursor()

#Création de la table airlines avec les champs : carrier et name
#mycursor.execute("CREATE TABLE IF NOT EXISTS airlines (carrier CHAR(2) PRIMARY KEY, name VARCHAR(100))")