TABLES = {
        "airlines": {
            "columns": [
                { "name": "carrier" ,"structure" : {"type": "CHAR", "length": "2","options" : ["PRIMARY KEY"] }},
                { "name": "name" ,"structure" : {"type": "VARCHAR", "length": "100","options": ["NOT NULL"] }}
            ]
        },
        "airports": {
            "columns": [
                {"name": "faa" ,"structure" : { "type": "CHAR", "length": "3", "options":["PRIMARY KEY"], "special_rule": "[A-Z]+" }},
                {"name": "name" ,"structure" : { "type": "VARCHAR", "length": "100", "options":["NOT NULL"] }},
                {"name": "lat" ,"structure" : {"type": "FLOAT", "options": ["NOT NULL"] }},
                {"name": "lon" ,"structure" : { "type": "FLOAT", "options": ["NOT NULL"]}},
                {"name": "alt" ,"structure" : { "type": "SMALLINT", "options": ["NOT NULL"]}},
                {"name": "tz" ,"structure" : { "type": "TINYINT", "options": ["NOT NULL"]}},
                {"name": "dst" ,"structure" : { "type": "CHAR", "length": "1", "options": ["NOT NULL"] }},
                {"name": "tzone" ,"structure" : { "type": "VARCHAR", "length": "100" }}
            ]
        },
        "flights": {
            "columns": [
                {"name": "year" ,"structure" : {"type": "YEAR", "length": "4", "options": ["NOT NULL"], "unique": True }},
                {"name": "month" ,"structure" : {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"], "unique": True }},
                {"name": "day" ,"structure" : {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"], "unique": True }},
                {"name": "dep_time" ,"structure" : {"type": "TIME"}, "concat": "00"},
                {"name": "sched_dep_time" ,"structure" : {"type": "TIME"}, "concat": "00"},
                {"name": "dep_delay" ,"structure" : { "type": "SMALLINT" }},
                {"name": "arr_delay" ,"structure" : { "type": "SMALLINT" }},
                {"name": "arr_time" ,"structure" : { "type": "TIME", "options": ["NOT NULL"] }, "concat": "00"},
                {"name": "sched_arr_time" ,"structure" : {"type": "TIME"}, "concat": "00"},
                {"name": "carrier" ,"structure" : {"type": "CHAR", "length": "2", "options": ["NOT NULL"] }},
                {"name": "flight" ,"structure" : {"type": "SMALLINT UNSIGNED", "unique": True }},
                {"name": "tailnum" ,"structure" : {"type": "CHAR", "length": "6"}},
                {"name": "origin" ,"structure" : {"type":"CHAR", "length": "3", "options": ["NOT NULL"], "references": {"table": "airports", "index": "faa"} }},
                {"name": "dest" ,"structure" : {"type": "CHAR", "length": "3", "options": ["NOT NULL"], "references": {"table": "airports", "index": "faa"}}},
                {"name": "air_time" ,"structure" : {"type": "SMALLINT UNSIGNED"}},
                {"name": "distance" ,"structure" : {"type": "SMALLINT UNSIGNED", "options": ["NOT NULL"] }},
                {"name": "hour" ,"structure" : {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"], "unique": True }},
                {"name": "minute" ,"structure" : {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"] }},
                {"name": "time_hour" ,"structure" : {"type": "DATETIME", "options": ["NOT NULL"]}}
            ],
            "constraints": [
                "PRIMARY KEY (`year`,`month`,`day`,hour,flight)",
                "FOREIGN KEY (origin) REFERENCES airports(faa) ON DELETE CASCADE",
                "FOREIGN KEY (dest) REFERENCES airports(faa) ON DELETE CASCADE"
            ]
        },
        "planes": {
            "columns": [
                {"name": "tailnum" ,"structure" : {"type": "CHAR", "length": "6", "options": ["PRIMARY KEY"] }},
                {"name": "year" ,"structure" : {"type": "YEAR"}},
                {"name": "type" ,"structure" : {"type": "VARCHAR", "length": "50", "options": ["NOT NULL"]}},
                {"name": "manufacturer" ,"structure" : {"type": "VARCHAR", "length": "50", "options": ["NOT NULL"]}},
                {"name": "model" ,"structure" : {"type": "VARCHAR", "length": "50", "options": ["NOT NULL"]}},
                {"name": "engines" ,"structure" : {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"]}},
                {"name": "seats" ,"structure" : {"type": "SMALLINT UNSIGNED", "options": ["NOT NULL"]}},
                {"name": "speed" ,"structure" : {"type": "SMALLINT UNSIGNED"}},
                {"name": "engine" ,"structure" : {"type": "VARCHAR", "length": "20", "options": ["NOT NULL"]}}
            ]   
        },
        "weather": {
            "columns": [
                {"name": "origin" ,"structure" : {"type": "CHAR", "length": "3", "options": ["NOT NULL"], "unique": True }},
                {"name": "year" ,"structure" : {"type": "YEAR", "length": "4", "options": ["NOT NULL"], "unique": True }},
                {"name": "month" ,"structure" : {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"], "unique": True }},
                {"name": "day" ,"structure" : {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"], "unique": True }},
                {"name": "hour" ,"structure" : {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"], "unique": True }},
                {"name": "temp" ,"structure" : {"type": "FLOAT UNSIGNED", "options": ["NOT NULL"]}},
                {"name": "dewp" ,"structure" : {"type": "FLOAT", "options": ["NOT NULL"]}},
                {"name": "humid" ,"structure" : {"type": "FLOAT UNSIGNED" }},
                {"name": "wind_dir" ,"structure" : {"type": "TINYINT UNSIGNED", "options": ["NOT NULL"]}},
                {"name": "wind_speed" ,"structure" : {"type": "FLOAT" }},
                {"name": "wind_gust" ,"structure" : {"type": "FLOAT UNSIGNED" }},
                {"name": "precip" ,"structure" : {"type": "FLOAT UNSIGNED", "options": ["NOT NULL"] }},
                {"name": "pressure" ,"structure" : {"type": "FLOAT UNSIGNED", "options": ["NOT NULL", "DEFAULT 0"] }},
                {"name": "visib" ,"structure" : {"type": "FLOAT UNSIGNED", "options": ["NOT NULL"] }},
                {"name": "time_hour" ,"structure" : {"type": "DATETIME", "options": ["NOT NULL"] }}
            ],
            "constraints": [
                "PRIMARY KEY (origin,`year`,`month`,`day`,hour)"
            ]
        }
    
}
