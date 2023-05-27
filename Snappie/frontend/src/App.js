import logo from './static/logo.png'
import './App.css';
import React from 'react';

function App() {
  return (
    <div className="App w-full min-h-screen">
      <div className = "topBar h-24 flex flex-row justify-start pt-8 pb-8 pl-32 pr-32">
        <img src={logo} className = "h-full object-contain object-center align-middle" alt="logo"/>
      </div>

      <div className = "flex flex-row ">
        <nav className = "navBar min-h-menu w-1/4 flex flex-col p-8">
          <p>My Dashboard</p>
          <p>Snappie Activity</p>
          <p>FAQ</p>
          <p>Updates</p>
          <p>Help</p>
        </nav>

        <div className = "chat w-3/4 m-4 rounded-chat bg-chat">
          <p>Hi</p>
        </div>
      </div>
    </div>
  );
}

export default App;
