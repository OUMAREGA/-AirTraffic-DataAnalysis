import mysql.connector as db

class Connection:
    def __init__(self):
        self.host="localhost",
        self.port="30000",
        self.user='root',
        self.password='root',
        self.database='avions'

    
    def connection():
        connection = db.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )

        return connection.cursor()


    def create_airlines():
        mycursor = self.connection()

        mycursor.execute("CREATE TABLE IF NOT EXISTS airlines (carrier CHAR(2) PRIMARY KEY, name VARCHAR(100) NOT NULL)")

        mycursor.execute("""
            LOAD DATA INFILE '/csv_data/airlines.csv'
            INTO TABLE airlines
            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
        """)

    def create_airports():
        mycursor = self.connection()


    def create_planes():
        mycursor = self.connection()


    def create_flights():
        mycursor = self.connection()


    def create_weather():
        mycursor = self.connection()
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
                wind_dir TINYINT UNSIGNED NOT NULL,
                wind_speed FLOAT,
                wind_gust FLOAT UNSIGNED,
                precip FLOAT UNSIGNED NOT NULL,
                pressure FLOAT UNSIGNED DEFAULT 0,
                visib FLOAT UNSIGNED NOT NULL,
                time_hour DATETIME NOT NULL,
                PRIMARY KEY (origin,year,month,day,hour)
            )
        """)

        mycursor.execute("""
            LOAD DATA INFILE '/csv_data/weather.csv'
            INTO TABLE weather
            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
        """)
