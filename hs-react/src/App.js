import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Historical Searchengine</h1>
        <input type="text" id="hs-input" placeholder="Such was.." />
      </div>
    );
  }
}

export default App;
