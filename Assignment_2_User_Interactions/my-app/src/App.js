import React, { useEffect, useState } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import AboutMeHTML from './AboutMeHTML';

function App() {
  const [metrics, setMetrics] = useState('');

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const response = await axios.get('http://localhost:3001/get-metrics');
        setMetrics(response.data); // Update state with metrics data
      } catch (error) {
        console.error('Error fetching metrics:', error);
      }
    };

    fetchMetrics();
  }, []); // Empty dependency array ensures useEffect runs only once on component mount
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          CSE 4500
        </a>
      </header>
      <AboutMeHTML />
      {/* Display metrics in a separate div */}
      <div>
        <h2>Metrics:</h2>
        <pre>{metrics}</pre>
      </div>
    </div>
  );
}

export default App;

