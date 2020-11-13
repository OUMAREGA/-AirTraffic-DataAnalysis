from modules.Connection import Connection

c = Connection()


c.create("planes")
c.load_csv_data('flights',"csv_data/planes.csv")

c.create("flights")
c.load_csv_data('flights',"csv_data/flights.csv")

c.create("weather")
c.load_csv_data('weather',"csv_data/weather.csv")