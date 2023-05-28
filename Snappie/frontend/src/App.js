import logo from './static/logo.png'
import './App.css';
import React from 'react';

function App() {
  let response1 = "Octavate is a company that positions itself as an audio art dealer brand. Their main focus is on reactivating undervalued talent in the music industry through their unique artist management system. They combine expertise in music, data, and finance to identify and support promising artists who may have been overlooked or underappreciated.";

  return (
    <div className="App w-full min-h-screen">
      <div className = "topBar h-24 flex flex-row justify-start pt-8 pb-8 pl-32 pr-32">
        <img src={logo} className = "h-full object-contain object-center align-middle" alt="logo"/>
      </div>

      <div className = "flex flex-row">
        <nav className = "navBar h-menu w-1/4 flex flex-col items-center p-4 relative border">
          <button className = "navBut m-2 p-2 text-xl">My Dashboard</button>
          <button className = "navBut m-2 p-2 text-xl">Snappie Activity</button>
          <button className = "navBut m-2 p-2 text-xl">FAQ</button>
          <button className = "navBut m-2 p-2 text-xl">Updates</button>
          <button className = "navBut m-2 p-2 text-xl">Help</button>
          <div className = "account absolute bottom-8 w-3/4">
            <hr/>
            <p>Account: Yichen</p>
            <p>Sign out</p>
          </div>
        </nav>

        <div className = "chat relative max-h-menu w-3/4 m-4 rounded-chat bg-chat border border-black flex flex-col justify-between items-center">
          <div className = "chatBar flex flex-row justify-between w-full p-4 bg-white border rounded-t-chat">
            <button>Back</button>
            <p>Sexual Harrassment Training</p>
            <p>Progress: 40%</p>
          </div>

          <div className = "chatArea grow overflow-auto">
            <div className = "promptResponse">
              <p>Yichen</p>
              <p>{response1}</p>
            </div>
            <div className = "promptQuestion">
              <p>Yichen</p>
              <p>{response1}</p>
            </div>
            <div className = "promptResponse">
              <p>Yichen</p>
              <p>{response1}</p>
            </div>
            <div className = "promptQuestion">
              <p>Yichen</p>
              <p>{response1}</p>
            </div>
            <div className = "promptResponse">
              <p>Yichen</p>
              <p>{response1}</p>
            </div>
            <div className = "promptQuestion">
              <p>Yichen</p>
              <p>{response1}</p>
            </div>
          </div>

          <form className="prompt  w-full p-4 bg-chat rounded-b-chat">
            <textarea id="message" rows="1" 
            className="block resize-none overflow-hidden p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg 
            border border-black focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
            placeholder="Send a message...">
            </textarea>
            <button>Send</button>
            <p className="">Snappie may display inaccurate or offensive information that doesn’t represent Snap Instruct's views.</p>
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;
