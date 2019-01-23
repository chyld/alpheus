import React, { Component } from "react";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.append = this.append.bind(this);
  }

  async append() {
    const val = parseInt(this.in_val.value);
    const url = `http://localhost:5000/append/${val}`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  }

  render() {
    return (
      <div className="App">
        <input ref={input => (this.in_val = input)} type="text" />
        <button onClick={this.append}>Append</button>
      </div>
    );
  }
}

export default App;
