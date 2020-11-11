import os
import util
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
        """
            Méthode retournant l'objet MySQLConnection
            afin de pouvoir manipuler la base de données
            MariaDB/MySQL
        """
        connection = db.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )

        return connection


    def create(self,table_name:str):
        """
            Méthode permettant de créer une table SQL
            en s'appuyant sur le dictionnaire tables dans util

            Parameters
            ----------
                table_name (str) : nom de la table
        """
        if table_name in util.tables:
            columns = ""
            for index,column in enumerate(util.tables[table_name]["columns"]):
                column_dict: dict = column
                column_name = list(column_dict.keys()).pop()
                column_data = column_dict[column_name]
                columns = columns + column_name + " " + column_data["type"] + " "
                if "options" in column_data:
                    columns = columns + (" ".join(column_data["options"]))
                if not index:
                    columns = columns + ","
            if "constraints" in util.tables[table_name]:
                columns = columns + "," + ",".join(util.tables[table_name]["constraints"])
            query = f"CREATE TABLE IF NOT EXISTS {table_name}({columns})"
            print(query)
        else:
            raise Exception("Table à créer non répertoriée")

    # MÉTHODE TEMPORAIRE AVANT INTERPRÉTATION DES FICHIERS CSV
    # POUR RESPECTER LA COHÉRENCE DES TYPES DANS LA BASE DE DONNÉES

    def load_csv_data(self,table_name:str,csv_file:str):
        """
            Méthode permettant de charger des données
            CSV dans une table

            Parameters
            ----------
                table_name (str) : nom de la table qui doit recevoir les données
                csv_file (str) : nom du fichier CSV
        """
        self.cursor.execute(f"""
            LOAD DATA INFILE '/csv_data/{csv_file}'
            INTO TABLE {table_name}
            FIELDS TERMINATED BY ',' ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
        """)
        self.db.commit()

c = Connection()
c.create("flights")