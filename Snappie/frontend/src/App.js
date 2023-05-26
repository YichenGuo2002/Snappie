import logo from './static/logo.png'
import './App.css';
import React from 'react';

function App() {
  return (
    <div className="App w-full min-h-screen">
      <div className = "topBar h-32 flex flex-row justify-between pt-8 pb-8 pl-32 pr-32">
        <img src={logo} className = "h-full object-contain object-center align-middle" alt="logo"/>
        <p>Hi</p>
      </div>

      <nav className = "navBar border border-black w-1/4">
        <p>History</p>
      </nav>

      <div className = "chat">
        <p>Hi</p>
      </div>

    </div>
  );
}

export default App;
