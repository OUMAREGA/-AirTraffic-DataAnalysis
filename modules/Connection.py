import mysql.connector as db

class Connection:
    def __init__(self):
        self.host="localhost",
        self.port="30000",
        self.user='root',
        self.password='root',
        self.database='avions'
        self.mydb = self.connection()

    
    def connection(self):
        connection = db.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )

        return connection


    def create_airlines(self):
        mycursor = self.mydb.cursor()


        mycursor.execute("CREATE TABLE IF NOT EXISTS airlines (carrier CHAR(2) PRIMARY KEY, name VARCHAR(100) NOT NULL)")

        mycursor.execute("""
            LOAD DATA INFILE '/csv_data/airlines.csv'
            INTO TABLE airlines
            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
        """)
        self.mydb.commit()

    def create_airports(self):
        mycursor = self.connection()
        
        mycursor.execute("CREATE TABLE IF NOT EXISTS airports (faa CHAR(4) PRIMARY KEY, name VARCHAR(100) NOT NULL, lat FLOAT NOT NULL, lon FLOAT NOT NULL, alt SMALLINT NOT NULL, tz TINYINT NOT NULL, dst CHAR(1) NOT NULL, tzone VARCHAR(100) NOT NULL) ")

        mycursor.execute("""
            LOAD DATA INFILE '/csv_data/airports.csv'
            INTO TABLE airports
            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
        """)
        
        self.mydb.commit()


    def create_planes(self):
        mycursor = self.connection()

        mycursor.execute(
            "CREATE TABLE planes (tailnum CHAR(6) PRIMARY KEY,"
            "YEAR YEAR(4) NOT NULL ,"
            "type VARCHAR(50)  NOT NULL ,"
            "manufacturer VARCHAR(20)  NOT NULL ,"
            "model VARCHAR(20)  NOT NULL ,"
            "engines TINYINT UNSIGNED  NOT NULL ,"
            "seats TINYINT UNSIGNED  NOT NULL,"
            "speed TINYINT UNSIGNED ,"
            "engine VARCHAR(20)  NOT NULL)"
        )

        mycursor.execute("""
                 LOAD DATA INFILE '/csv_data/planes.csv'
                 INTO TABLE planes
                 FIELDS TERMINATED BY ',' ENCLOSED BY '"'
                 LINES TERMINATED BY '\n'
                 IGNORE 1 ROWS
             """)

        self.mydb.commit()

    def create_flights(self):
        mycursor = self.connection()

        mycursor.execute("""
            CREATE TABLE flights(
                year YEAR(4) NOT NULL,
                month TINYINT UNSIGNED NOT NULL,
                day TINYINT UNSIGNED NOT NULL,
                dep_time TIME,
                sched_dep_time TIME,
                dep_delay SMALLINT,
                arr_delay SMALLINT,
                arr_time TIME NOT NULL,
                sched_arr_time TIME,
                carrier CHAR(2) NOT NULL,
                flight SMALLINT UNSIGNED,
                tailnum CHAR(6),
                origin CHAR(3) NOT NULL,
                dest CHAR(3) NOT NULL,
                air_time SMALLINT UNSIGNED,
                distance SMALLINT UNSIGNED NOT NULL,
                hour TINYINT UNSIGNED NOT NULL,
                minute TINYINT UNSIGNED NOT NULL,
                time_hour DATETIME NOT NULL,
                PRIMARY KEY (year,month,day,hour,flight),
                FOREIGN KEY (origin) REFERENCES airports(faa),
                FOREIGN KEY (dest) REFERENCES airports(faa)
            )
        """)

        mycursor.execute("""
            LOAD DATA INFILE '/csv_data/flights.csv'
            INTO TABLE flights
            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
        """)

        self.mydb.commit()

        self.mydb.commit()


    def create_weather(self):
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

        self.mydb.commit()
