import mysql.connector

#connect to database

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="30000",
  user="root",
  password="root",
  database="avions"
)

mycursor = mydb.cursor()

mycursor.execute(
  "CREATE TABLE planes (tailnum CHAR(6) PRIMARY KEY,"
  "YEAR YEAR(4),"
  "type VARCHAR(50),"
  "manufacturer VARCHAR(20),"
  "model VARCHAR(20),"
  "engines SMALLINT ,"
  "seats SMALLINT ,"
  "speed SMALLINT ,"
  "engine VARCHAR(20))"
)
