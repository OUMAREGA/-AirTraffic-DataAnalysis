from modules.Connection import Connection

c = Connection()

c.create('airplanes')
c.load_csv_data('airplanes','csv_data/airplanes.csv')

c.create("planes")
c.load_csv_data('flights',"csv_data/planes.csv")

c.create('airports')
c.load_csv_data('airports',"csv_data/airports.csv")

c.create("flights")
c.load_csv_data('flights',"csv_data/flights.csv")

c.create("weather")
c.load_csv_data('weather',"csv_data/weather.csv")