import React from 'react';
import axios from 'axios';


export default class AirportNumber extends React.Component {
  state = {
    result: {}
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:5000/airport-number`)
      .then(res => {
        const result = res.data
        this.setState({ result });
      })
  }

  render() {
    return (
      <div className="title">
        { this.state.result.airport_number ? <h2>Il y a en tout { this.state.result.airport_number } aéroports</h2> : <h2 className='title'><h2 className='title'>Récupération des données...</h2></h2> }
      </div>
    )
  }
}