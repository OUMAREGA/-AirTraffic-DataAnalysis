import React from 'react';
import { NavLink } from 'react-router-dom';
import { ReactSVG } from 'react-svg';
import Logo from '../../assets/img/logo.svg';

// Transformer les A en navLink

const Header = () => <header>
    <ReactSVG 
        src={Logo}
        className="logo-header"
    />
    <div id="navbar">
        <ul>
        <li className="dropdown">
            <NavLink to="/home" className="dropbtn">Accueil</NavLink>
        </li>
        <li className="dropdown">
            <NavLink to="#" className="dropbtn">Aéroports</NavLink>
            <div className="dropdown-content">
            <NavLink to="/airport-number">Nombre d'aéroports</NavLink>
            <NavLink to="/most-emprunted-airport">Aéroport de départ le plus emprunté</NavLink>
            <NavLink to="/dest-desserved-carrier-origin">Aéroport d’origine desservie par chaque compagnie</NavLink>
            </div>
        </li>
        <li className="dropdown">
            <NavLink to="#" className="dropbtn">Compagnies</NavLink>
            <div className="dropdown-content">
            <NavLink to="/carrier-number">Nombre de compagnies</NavLink>
            <NavLink to="/flights-to-sea-carrier">Compagnies desservant la destination Seattle</NavLink>
            <NavLink to="/carrier-no-orgin-airports">Compagnies qui n'opèrent pas sur tous les aéroports d’origine</NavLink>
            <NavLink to="/carrier-desserv-all-destinations">Compagnies qui desservent l’ensemble de destination</NavLink>
            <NavLink to="/table-for-dest">Tableau où l’on récupère l’ensemble des origines et des destinations pour les compagnies</NavLink>
            </div>
        </li>
        <li className="dropdown">
            <NavLink to="#" className="dropbtn">Destinations <span className="fa fa-caret-down"></span></NavLink>
            <div className="dropdown-content">
            <NavLink to="/destination-number">Nombre de destinations</NavLink>
            <NavLink to="/timezone-number">Nombre de fuseaux horaire</NavLink>
            <NavLink to="/summer-hour-usa">Zones USA où on ne passe pas à l’heure d’été</NavLink>
            <NavLink to="/dest-less-token">10 destinations les moins prisées</NavLink>
            <NavLink to="/dest-desserved-carrier">Destinations desservies par chaque compagnie</NavLink>
            <NavLink to="/exclusive-destinations-for-carrier">Destinations qui sont exclusives à certaines compagnies</NavLink>
            </div>
        </li>
        <li className="dropdown">
            <NavLink to="#" className="dropbtn">Avions</NavLink>
            <div className="dropdown-content">
                <NavLink to="/plane-number">Nombre d'avions</NavLink>
                <NavLink to="/planes-less-boarding">10 avions qui ont le moins décollés</NavLink>
                <NavLink to="/flights-to-sea-unic-plane">Avions “uniques" qui desservent la destination Seattle</NavLink>
            </div>
        </li>
        <li className="dropdown"><NavLink to="#" className="dropbtn">Vols</NavLink>
            <div className="dropdown-content">
            <NavLink to="/flight-hou">Les vols ayant atterri à Houston (IAH ou HOU)</NavLink>
            <NavLink to="/flight-to-sea">Les vols qui partent de NYC airports vers Seattle (SEA)</NavLink>
            <NavLink to="/number-flights-unic">le nombre de vols unique par destination, aéroport d’origine et la compagnie dans un ordre alphabétique croissant</NavLink>
            <NavLink to="/united-flight">Les vols exploités par United, American ou Delta</NavLink>
            </div>
        </li>
        <li className="dropdown">
            <NavLink to="/grafics" className="dropbtn">Graphiques</NavLink>
        </li>
        </ul>
    </div>
</header>

export default Header;