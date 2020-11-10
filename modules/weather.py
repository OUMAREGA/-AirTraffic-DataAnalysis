import mysql.connector as db

connection = db.connect(
    host="localhost",
    port="30000",
    user='root',
    password='root',
    database='avions'
)

mycursor = connection.cursor()

mycursor.execute("""
    CREATE TABLE weather(
        origin CHAR(3) NOT NULL,
        year YEAR(4) NOT NULL,
        month TINYINT UNSIGNED NOT NULL,
        day TINYINT UNSIGNED NOT NULL,
        hour TINYINT UNSIGNED NOT NULL,
        temp FLOAT UNSIGNED NOT NULL,
        dewp FLOAT NOT NULL,
        humid FLOAT UNSIGNED NOT NULL,
        wind_dir TINYINT UNSIGNED,
        wind_speed FLOAT UNSIGNED,
        wind_gust FLOAT UNSIGNED,
        precip FLOAT UNSIGNED NOT NULL,
        pressure FLOAT UNSIGNED DEFAULT 0,
        visib FLOAT UNSIGNED NOT NULL,
        time_hour DATETIME NOT NULL,
        PRIMARY KEY (origin,year,month,day,hour)
    )
""")