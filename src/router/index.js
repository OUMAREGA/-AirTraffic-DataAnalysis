import Home from '../components/Home';

import AirportNumber from '../components/Question2/AirportNumber';
import CarrierNumber from '../components/Question2/CarrierNumber';
import DestinationNumber from '../components/Question2/DestinationNumber';
import PlaneNumber from '../components/Question2/PlaneNumber';
import TimezoneNumber from '../components/Question2/TimezoneNumber';
import SummerHourUSA from '../components/Question3/SummerHourUSA';
import DestLessToken from '../components/Question4/DestLessToken';
import MostEmpruntedAirport from '../components/Question4/MostEmpruntedAirport';
import PlanesLessBoarding from '../components/Question4/PlanesLessBoarding';
import DestDesservedCarrier from '../components/Question5/DestDesservedCarrier';
import DestDesservedCarrierOrigin from '../components/Question5/DestDesservedCarrierOrigin';
import Grafics from '../components/Question5/Grafics';
import FlightHou from '../components/Question6/FlightHou';
import FlightsToSEA from '../components/Question6/FlightsToSEA';
import FlightsToSeaCarrier from '../components/Question6/FlightsToSeaCarrier';
import FlightsToSeaUnicPlane from '../components/Question6/FlightsToSeaUnicPlane';
import NumberFlightsUnic from '../components/Question7/NumberFlightsUnic';
import CarrierDesservAllDestinations from '../components/Question8/CarrierDesservAllDestinations';
import CarrierNotOriginAirports from '../components/Question8/CarrierNotOriginAirports';
import ExclusiveDestinationsForCarrier from '../components/Question9/ExclusiveDestinationsForCarrier';
import UnitedFlight from '../components/Question10/UnitedFlight';
import TableForDest from '../components/Question8/TableForDest';
import DestLessTaken from '../components/Question4/DestLessTaken';

export const router = [
    { pathname: "/home",                                name: "Home",                               components: Home },
    { pathname: "/airport-number",                      name: "AirportNumber",                      components: AirportNumber },
    { pathname: "/carrier-number",                      name: "CarrierNumber",                      components: CarrierNumber },
    { pathname: "/destination-number",                  name: "DestinationNumber",                  components: DestinationNumber },
    { pathname: "/plane-number",                        name: "PlaneNumber",                        components: PlaneNumber },
    { pathname: "/timezone-number",                     name: "TimezoneNumber",                     components: TimezoneNumber },
    { pathname: "/summer-hour-usa",                     name: "SummerHourUSA",                      components: SummerHourUSA },
    { pathname: "/dest-less-taken",                     name: "DestLessTaken",                      components: DestLessTaken },
    { pathname: "/most-emprunted-airport",              name: "MostEmpruntedAirport",               components: MostEmpruntedAirport },
    { pathname: "/planes-less-boarding",                name: "PlanesLessBoarding",                 components: PlanesLessBoarding },
    { pathname: "/dest-desserved-carrier",              name: "DestDesservedCarrier",               components: DestDesservedCarrier },
    { pathname: "/dest-desserved-carrier-origin",       name: "DestDesservedCarrierOrigin",         components: DestDesservedCarrierOrigin },
    { pathname: "/grafics",                             name: "Grafics",                            components: Grafics },
    { pathname: "/flight-hou",                          name: "FlightHou",                          components: FlightHou },
    { pathname: "/flight-to-sea",                       name: "FlightsToSEA",                       components: FlightsToSEA },
    { pathname: "/flights-to-sea-carrier",              name: "FlightsToSeaCarrier",                components: FlightsToSeaCarrier },
    { pathname: "/flights-to-sea-unic-plane",           name: "FlightsToSeaUnicPlane",              components: FlightsToSeaUnicPlane },
    { pathname: "/number-flights-unic",                 name: "NumberFlightsUnic",                  components: NumberFlightsUnic },
    { pathname: "/exclusive-destinations-for-carrier",  name: "ExclusiveDestinationsForCarrier",    components: ExclusiveDestinationsForCarrier },
    { pathname: "/carrier-desserv-all-destinations",    name: "CarrierDesservAllDestinations",      components: CarrierDesservAllDestinations },
    { pathname: "/carrier-no-orgin-airports",           name: "CarrierNotOriginAirports",           components: CarrierNotOriginAirports },
    { pathname: "/united-flight",                       name: "UnitedFlight",                       components: UnitedFlight },
    { pathname: "/table-for-dest",                      name: "TableForDest",                       components: TableForDest },
    
    { redirect: true, path: "/", to:"/home", name: "Home" }
]