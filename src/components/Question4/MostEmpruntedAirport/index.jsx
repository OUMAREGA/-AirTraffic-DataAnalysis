import React from 'react';
import axios from 'axios';

export default class MostEmpruntedAirport extends React.Component {
  
  state = {
    result: {}
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:5000/most-emprunted-airport`)
      .then(res => {
        const result = res.data
        this.setState({ result });
      })
  }

  render() {
    return (
      <div style={{ margin: "auto", textAlign: "center" }}>
        <table style={{border: "1px solid black", textAlign: "center", padding: "5px", width: "50%", margin:"auto" }}>
        <tr style={{border: "1px solid black", textAlign: "center", padding: "10px"}}>
          <th>Nombre de fois</th>
          <th>Aéroport de départ</th>
        </tr>
        {
          this.state.result.length > 0 ? 
          this.state.result.map((object,i) => (
          <tr key={i}>
              <td>{object.Nbr}</td>
              <td>{object.dest}</td>
          </tr>)) : "Récupération des données..."
        
        }
        </table>
      </div>
    )
  }

}
