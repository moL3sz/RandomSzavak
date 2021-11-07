import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import commandList from "./commands"
import $ from "jquery"
import Terminal from "./terminal"
import TokenGeneration from "./token"

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('main-container')
);



$(".type-of-request-tool").each((i,e) =>{
  const className = $(e).attr("class")
  const type = className.split(" ")[1]
  ReactDOM.render(
    <React.StrictMode>
      <Terminal command={commandList[type]} type={type}/>
    </React.StrictMode>, 
    document.getElementById(`${type}-type`)
  )
})
ReactDOM.render(
  <TokenGeneration/>,
  document.getElementById("token-generation")

)


reportWebVitals();
