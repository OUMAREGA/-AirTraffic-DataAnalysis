from os.path import dirname, join
racine = dirname(dirname(__file__))
chemin_scripts_sql = join(racine, 'sql')
file = open(chemin_scripts_sql+f"/flights.sql")
print(file.read())
file.close()