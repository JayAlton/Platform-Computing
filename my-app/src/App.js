import logo from './logo.svg';
import './App.css';
import AboutMeHTML from './AboutMeHTML';

function App() {
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
    </div>
  );
}

export default App;
