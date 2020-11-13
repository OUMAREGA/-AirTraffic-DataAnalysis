import React from 'react';
import axios from 'axios';

export default class PlaneNumber extends React.Component {
  state = {
    result: {}
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:5000/plane-number`)
      .then(res => {
        console.log("res",res)
        const result = res
        this.setState({ result });
      })
  }

  render() {
    return (
      <ul>
        <li>ici</li>
      </ul>
    )
  }
}