import React from 'react';
import axios from 'axios';

export default class DestDesservedCarrierOrigin extends React.Component {
    state = {
      result: {}
    }
    
    componentDidMount() {
      axios.get(`http://127.0.0.1:5000/dest-desserved-carrier-origin`)
        .then(res => {
          const result = res.data
          this.setState({ result });
          console.log(result)
          
        })
    }
  
    render() {
      return (
        <div style={{ margin: "auto" }}>
          <table style={{border: "1px solid black", textAlign: "center", padding: "5px", width: "50%", margin:"auto" }}>
          <tr style={{border: "1px solid black", textAlign: "center", padding: "10px"}}>
            <th>carrier</th>
            <th>nom</th>
            <th>nombre de fois</th>
          </tr>
          {
            this.state.result.length > 0 ? 
            this.state.result.map((object,i) => (
            <tr key={i}>
                <td>{object.carrier}</td>
                <td>{object.name}</td>
                <td>{object.nbr_origin}</td>
            </tr>)) : "Récupération des données..."
          
          }
          </table>
        </div>
      )
    }
};

