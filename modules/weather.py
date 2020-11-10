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
        temp FLOAT NOT NULL,
        dewp FLOAT NOT NULL,
        humid FLOAT NOT NULL,
        wind_dir TINYINT UNSIGNED NOT NULL,
        wind_speed FLOAT NOT NULL,
        wind_gust FLOAT NOT NULL,
        precip TINYINT NOT NULL DEFAULT 0,
        pressure FLOAT NOT NULL,
        visib TINYINT NOT NULL,
        time_hour DATETIME NOT NULL,
        PRIMARY KEY (origin,year,month,day,hour)
    )
""")