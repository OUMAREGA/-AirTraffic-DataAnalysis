import mysql.connector as db
from os.path import dirname, join

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


    def launch_script(self,script_name:str):
        mycursor = self.mydb.cursor()
        try:
            racine = dirname(dirname(__file__))
            chemin_scripts_sql = join(racine, 'sql')
            file = open(chemin_scripts_sql+f"/{script_name}.sql")
            mycursor.execute(file.read())
            self.mydb.commit()
        except Exception as e:
            raise e
        finally:
            file.close()

