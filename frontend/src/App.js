import logo from './logo.svg';
import './App.css';
import {useEffect} from 'react'

function App() {
  
  // J'ai rien toucher dans le frontend et je te laisse explorer la librairie et son fonctionnement toi même sauf l'exemple qui suit.
  // Va lire la doc de react mais en gros un useEffect prends deux chose, une arrow function de ce qu'il a à faire, puis un tableau
  // Le tableau comporte les variables que si ces variables changent, il doit recharger la page.
  // Par contre, si ton tableau est vide, il va faire l'action en loadant la page.
  useEffect(() => {
    const data = {
      key: "Value"
    };
    fetch('http://127.0.0.1:5000/api/produit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
    });
  }, [])
  
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
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
