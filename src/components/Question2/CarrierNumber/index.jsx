import React from 'react';
import axios from 'axios';


export default class CarriertNumber extends React.Component {
  state = {
    result: {}
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:5000/carrier-number`)
      .then(res => {
        const result = res.data
        this.setState({ result });
      })
  }

  render() {
    return (
      <div className="title">
        { this.state.result.carrier_number ? <h2>Il y a en tout compagnies { this.state.result.carrier_number } aériennes</h2> : "Récupération en cours..." }
      </div>
    )
  }
}