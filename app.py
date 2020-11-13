from flask import Flask,jsonify
from modules.Connection import Connection
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] =  'Content-Type'

conn = Connection()

@app.route('/', methods=['GET'])
def index():
    return jsonify(conn.query("SELECT * FROM airports"))


@app.route('/airport-number', methods=['GET'])
def AirportNumber():
    return conn.query("SELECT COUNT(faa) as `airport_number` FROM airports",multiple=False)

@app.route('/carrier-number', methods=['GET'])
def CarrierNumber():
    return conn.query("SELECT COUNT(DISTINCT(carrier)) as `carrier_number` FROM airlines", multiple=False)

@app.route('/destination-number', methods=['GET'])
def DestinationNumber():
    return conn.query("SELECT COUNT(DISTINCT(dest)) as `dest_number` FROM flights",multiple=False)

@app.route('/plane-number', methods=['GET'])
def PlaneNumber():
    return conn.query("SELECT COUNT(tailnum) as `plane_number` FROM planes", multiple=False)

@app.route('/timezone-number', methods=['GET'])
def TimezoneNumber():
    return conn.query("SELECT COUNT(DISTINCT(tzone)) as `tzone_number` FROM airports", multiple=False)

@app.route('/summer-hour-usa', methods=['GET'])
def SummerHourUSA():
    return jsonify(conn.query("SELECT * FROM airports WHERE (tzone LIKE 'America%' OR tzone LIKE 'Pacific%') AND dst='N'"))

@app.route('/dest-less-taken', methods=['GET'])
def DestLessTaken():
    return jsonify(conn.query("SELECT dest, COUNT(dest) as Nbr FROM flights GROUP BY dest ORDER BY Nbr ASC LIMIT 10"))

@app.route('/dest-more-taken', methods=['GET'])
def DestMoreTaken():
    return jsonify(conn.query("SELECT dest, COUNT(dest) as Nbr FROM flights GROUP BY dest ORDER BY Nbr DESC LIMIT 10"))

@app.route('/most-emprunted-airport', methods=['GET'])
def MostEmpruntedAirport():
    return jsonify(conn.query("SELECT COUNT(origin) as Nbr, dest FROM `flights` GROUP BY dest ORBER BY Nbr DESC LIMIT 10"))

@app.route('/planes-less-boarding', methods=['GET'])
def PlanesLessBoarding():
    return jsonify(conn.query("SELECT tailnum as `avion`,tailnum FROM flights GROUP BY tailnum ORDER BY `avion` ASC LIMIT 10"))

@app.route('/dest-desserved-carrier', methods=['GET'])
def DestDesservedCarrier():
    return jsonify(conn.query("SELECT COUNT(f.dest) as `nbr_dest`, a.carrier, a.name FROM flights `f` INNER JOIN airlines `a` ON f.carrier = a.carrier GROUP BY a.carrier"))

@app.route('/dest-desserved-carrier-origin', methods=['GET'])
def DestDesservedCarrierOrigin():
    return jsonify(conn.query("SELECT COUNT(f.origin) as `nbr_origin`, a.carrier, a.name FROM flights `f` INNER JOIN airlines `a` ON f.carrier = a.carrier GROUP BY a.carrier"))

# @app.route('/grafics', methods=['GET'])
# def Grafics():
#     return jsonify(conn.query("SELECT * FROM airports"))

@app.route('/flight-hou', methods=['GET'])
def FlightHou():
    return jsonify(conn.query("SELECT * FROM flights WHERE dest='HOU' OR dest='IAH' "))

@app.route('/flight-to-sea', methods=['GET'])
def FlightsToSEA():
    return jsonify(conn.query("SELECT COUNT(dest) FROM `flights` WHERE origin in ('JFK', 'EWR', 'LGA') AND dest = 'SEA'"))

@app.route('/flights-to-sea-carrier', methods=['GET'])
def FlightsToSeaCarrier():
    return jsonify(conn.query('SELECT COUNT(DISTINCT carrier) FROM `flights` WHERE origin in (\'JFK\', \'EWR\', \'LGA\') AND dest = "SEA"'))

@app.route('/flights-to-sea-unic-plane', methods=['GET'])
def FlightsToSeaUnicPlane():
    return jsonify(conn.query('SELECT COUNT(DISTINCT tailnum) FROM `flights` WHERE origin in (\'JFK\', \'EWR\', \'LGA\') AND dest = "SEA"'))

@app.route('/number-flights-unic', methods=['GET'])
def NumberFlightsUnic():
    return jsonify(conn.query('SELECT airports.name, COUNT(DISTINCT flights.flight) as nb_vol_unique FROM flights INNER JOIN airports ON flights.dest = airports.faa GROUP BY flights.dest ORDER BY nb_vol_unique DESC'))

@app.route('/exclusive-destinations-for-carrier', methods=['GET'])
def ExclusiveDestinationsForCarrier():
    return jsonify(conn.query('select dest, count(dest) AS \'nb_dest\', carrier from flights group by dest, carrier'))

@app.route('/carrier-desserv-all-destinations', methods=['GET'])
def CarrierDesservAllDestinations():
    return jsonify(conn.query('select dest, count(dest) AS \'nb_dest\', carrier from flights group by dest, carrier'))

@app.route('/carrier-no-orgin-airports', methods=['GET'])
def CarrierNotOriginAirports():
    return jsonify(conn.query("SELECT * FROM airports"))

@app.route('/united-flight', methods=['GET'])
def UnitedFlight():
    return jsonify(conn.query('select * from flights where carrier in ("AA","UA","DL")'))

@app.route('/table-for-dest', methods=['GET'])
def TableForDest():
    return jsonify(conn.query("SELECT * FROM airports"))


if __name__ == "__main__":
    app.run(debug=True)