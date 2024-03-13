import logo from './logo.svg';
import './App.css';
import AboutMeHTML from './AboutMeHTML';

function App() {
  
  return (
    <div className="App">
      <header className="App-header">
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
      
    </div>
  );
}

export default App;

