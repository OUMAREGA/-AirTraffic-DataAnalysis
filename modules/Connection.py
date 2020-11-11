import os
import mysql.connector as db
from dotenv import load_dotenv
from os.path import dirname, join

racine = dirname(dirname(__file__))

class Connection:
   
    def __init__(self):

        load_dotenv(racine+"/.env")
        
        self.host = os.environ.get("DB_HOST")
        self.database= os.environ.get("DB_NAME")
        self.port = os.environ.get("DB_PORT")
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PWD")
        self.db = self.connection()
        self.cursor = self.db.cursor()
    
    def connection(self):
        connection = db.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )

        return connection


    def launch_script(self,script_name:str):
        try:
            chemin_scripts_sql = join(racine, 'sql')
            file = open(chemin_scripts_sql+f"/{script_name}.sql")
            self.cursor.execute(file.read())
            self.db.commit()
        except Exception as e:
            raise e
        finally:
            file.close()

    def load_csv_data(self,table_name:str,csv_file:str):
        self.cursor.execute(f"""
            LOAD DATA INFILE '/csv_data/{csv_file}'
            INTO TABLE {table_name}
            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
        """)
        self.db.commit()

