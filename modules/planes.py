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
  "YEAR YEAR(4) NOT NULL ,"
  "type VARCHAR(50)  NOT NULL ,"
  "manufacturer VARCHAR(20)  NOT NULL ,"
  "model VARCHAR(20)  NOT NULL ,"
  "engines TINYINT UNSIGNED  NOT NULL ,"
  "seats TINYINT UNSIGNED  NOT NULL,"
  "speed TINYINT UNSIGNED  NOT NULL,"
  "engine VARCHAR(20)  NOT NULL)"
)
