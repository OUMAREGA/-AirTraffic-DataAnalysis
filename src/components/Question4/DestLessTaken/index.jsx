import React from 'react';
import axios from 'axios';

export default class DestLesstaken extends React.Component {

  state = {
    result: {}
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:5000/dest-less-taken`)
      .then(res => {
        const result = res.data
        this.setState({ result });
        console.log(res.data)
      })
  }

  render() {
    return (
      <div style={{ margin: "auto", textAlign: "center" }}>
        <table style={{border: "1px solid black", textAlign: "center", padding: "5px", width: "50%", margin:"auto" }}>
        <tr style={{border: "1px solid black", textAlign: "center", padding: "10px"}}>
          <th>alt</th>
          <th>faa</th>
          <th>lat</th>
          <th>lon</th>
          <th>Nom</th>
          <th>Timezone</th>
        </tr>
        {
          this.state.result.length > 0 ? 
          this.state.result.map((object,i) => (
          <tr key={i}>
              <td>{object.alt}</td>
              <td>{object.dst}</td>
              <td>{object.lat}</td>
              <td>{object.lon}</td>
              <td>{object.name}</td>
              <td>{object.tz}</td>
          </tr>)) : <h2 class="title">Récupération des données..."</h2>
        
        }
        </table>
      </div>
    )
  }
}