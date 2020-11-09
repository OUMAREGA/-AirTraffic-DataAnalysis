import mysql.connector

#connect to database

mydb = mysql.connector.connect(
  host="91.171.69.177",
  port="26550",
  user="oumarm",
  password="oumarmarega",
  database="avions"
)

mycursor = mydb.cursor()

mycursor.execute(
  "CREATE TABLE planes"
  "(tailnum INT AUTO_INCREMENT PRIMARY KEY,"
  "year INT(4),"
  "yype VARCHAR(50),"
  "manufacturer VARCHAR(20),"
  "model VARCHAR(20),"
  "engines INT(4),"
  "spped INT(4),"
  "engine VARCHAR(20))"
)
