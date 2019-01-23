import React, { Component } from "react";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.append = this.append.bind(this);
    this.prepend = this.prepend.bind(this);
    this.delete = this.delete.bind(this);
    this.clear = this.clear.bind(this);
    this.reverse = this.reverse.bind(this);
  }

  async append() {
    const val = parseInt(this.in_val.value);
    const url = `http://localhost:5000/append/${val}`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  }

  async prepend() {
    const val = parseInt(this.in_val.value);
    const url = `http://localhost:5000/prepend/${val}`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  }

  async delete() {
    const val = parseInt(this.in_val.value);
    const url = `http://localhost:5000/delete/${val}`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  }

  async clear() {
    const url = `http://localhost:5000/clear`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  }

  async reverse() {
    const url = `http://localhost:5000/reverse`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  }

  render() {
    return (
      <div className="App">
        <input ref={input => (this.in_val = input)} type="text" />
        <button onClick={this.append}>Append</button>
        <button onClick={this.prepend}>Prepend</button>
        <button onClick={this.delete}>Delete</button>
        <button onClick={this.clear}>Clear</button>
        <button onClick={this.reverse}>Reverse</button>
      </div>
    );
  }
}

export default App;
