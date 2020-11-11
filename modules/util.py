tables = {
    "airlines": {
        "columns": [
           { "carrier": {"type": "CHAR(2)","options" : ["PRIMARY KEY"] }},
           { "name": {"type": "VARCHAR(100)","options": ["NOT NULL"] }}
        ]
    },
    "airports": {
        "columns": [
            {"faa": { "type": "CHAR(4)", "options":["PRIMARY KEY"] }},
            {"name": { "type": "VARCHAR(100)", "options":["NOT NULL"] }},
            {"lat": {"type": "FLOAT", "options": ["NOT NULL"] }},
            {"lon": { "type": "FLOAT", "options": ["NOT NULL"]}},
            {"alt": { "type": "SMALLINT", "options": ["NOT NULL"]}},
            {"tz": { "type": "TINYINT", "options": ["NOT NULL"]}},
            {"dst": { "type": "CHAR(1)", "options": ["NOT NULL"] }},
            {"tzone": { "type": "VARCHAR(100)", "options":["NOT NULL"] }}
        ]
    },
    "flights": {
        "columns": [
            {"year": {"type": "YEAR(4)", "options": ["NOT NULL"] }},
            {"month": {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"]}},
            {"dep_time": {"type": "TIME"}},
            {"sched_dep_time": {"type": "TIME"}},
            {"dep_delay": { "type": "SMALLINT" }},
            {"arr_delay": { "type": "SMALLINT" }},
            {"arr_time": { "type": "TIME", "options": ["NOT NULL"] }},
            {"sched_arr_time": {"type": "TIME"}},
            {"carrier": {"type": "CHAR(2)", "options": ["NOT NULL"] }},
            {"flight": {"type": "SMALLINT UNSIGNED" }},
            {"tailnum": {"type": "CHAR(6)"}},
            {"origin": {"type":"CHAR(3)", "options": ["NOT NULL"] }},
            {"dest": {"type": "CHAR(3)", "options": ["NOT NULL"]}},
            {"air_time": {"type": "SMALLINT UNSIGNED"}},
            {"distance": {"type": "SMALLINT UNSIGNED", "options": ["NOT NULL"] }},
            {"hour": {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"] }},
            {"minute": {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"] }},
            {"time_hour": {"type": "DATETIME", "options": ["NOT NULL"]}}
        ],
        "constraints": [
            "PRIMARY KEY (`year`,`month`,`day`,hour,flight)",
            "FOREIGN KEY (origin) REFERENCES airports(faa))"
        ]
    },
    "planes": {
        "columns": [
            {"tailnum": {"type": "CHAR(6)", "options": ["PRIMARY KEY"] }},
            {"year": {"type": "YEAR", "options": ["NOT NULL"]}},
            {"type": {"type": "VARCHAR(50)", "options": ["NOT NULL"]}},
            {"manufacturer": {"type": "VARCHAR(50)", "options": ["NOT NULL"]}},
            {"model": {"type": "VARCHAR(50)", "options": ["NOT NULL"]}},
            {"engines": {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"]}},
            {"seats": {"type": "SMALLINT UNSIGNED", "options": ["NOT NULL"]}},
            {"speed": {"type": "TINYINT UNSIGNED"}},
            {"engine": {"type": "VARCHAR(20)", "options": ["NOT NULL"]}}
        ]
    },
    "weather": {
        "columns": [
            {"origin": {"type": "CHAR(3)", "options": ["NOT NULL"] }},
            {"year": {"type": "YEAR(4)", "options": ["NOT NULL"]}},
            {"month": {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"]}},
            {"day": {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"]}},
            {"temp": {"type": "FLOAT UNSIGNED", "options": ["NOT NULL"]}},
            {"dewp": {"type": "FLOAT", "options": ["NOT NULL"]}},
            {"humid": {"type": "FLOAT UNSIGNED" }},
            {"wind_dir": {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"]}},
            {"wind_speed": {"type": "FLOAT" }},
            {"wind_gust": {"type": "FLOAT UNSIGNED" }},
            {"precip": {"type": "FLOAT UNSIGNED", "options": ["NOT NULL"] }},
            {"pressure": {"type": "FLOAT UNSIGNED", "options": ["NOT NULL", "DEFAULT 0"] }},
            {"visib": {"type": "FLOAT UNSIGNED", "options": ["NOT NULL"] }},
            {"time_hour": {"type": "DATETIME", "options": ["NOT NULL"] }},
        ],
        "constraints": [
            "PRIMARY KEY (origin,`year`,`month`,`day`,hour)"
        ]
    }
 
}