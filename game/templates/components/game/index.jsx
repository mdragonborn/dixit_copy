import React from 'react';
import Game from './Game.jsx'
import Players from './Players.jsx'
import ReactDOM from 'react-dom'

var current_user = null;
var game = document.getElementById("game_component").dataset("game_id");

fetch('http://localhost:8000/currenct-user/?format=json').then(
  response => current_user=response
);



var game_sock = 'ws://' + window.location.host + "/game/";
// preset the current_user


// renders out the base component
function render_component(){
    console.log("jpg");
    ReactDOM.render(<Game current_user={current_user} game/>, document.getElementById('game_component'))
    ReactDOM.render(<Players/>, document.getElementById('players_component'))
}

render_component();
