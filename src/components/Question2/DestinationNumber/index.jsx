import React from 'react';
import axios from 'axios';

export default class DestinationNumber extends React.Component {
  state = {
    result: {}
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:5000/destination-number`)
      .then(res => {
        const result = res.data
        this.setState({ result });
      })
  }

  render() {
    return (
      <ul>
        <li>Il y a en tout { this.state.result.dest_number } destinations desservies</li>
      </ul>
    )
  }
}