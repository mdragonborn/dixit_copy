import React from 'react';
import Game from './Game.jsx'
import Players from './Players.jsx'
import ReactDOM from 'react-dom'

let current_user = null;
let game_participants = null;
var game_id = document.getElementById("game_component").dataset.game_id;

fetch('http://127.0.0.1:8000/current-user/?format=json').then(
  response => response.json()
).then(
  user => {
    current_user = user;
    render_component()
  }
);

fetch('http://127.0.0.1:8000/game/participants/2/?format=json').then(
  response => response.json()
).then(
  participants => {
    game_participants = participants;
    render_component()
  }
);


var game_sock = 'ws://' + window.location.host + "/game/";
// preset the current_user

// renders out the base component
function render_component() {
  console.log("jpg");
  ReactDOM.render(<Game current_user={current_user} socket={game_sock} game_id={game_id}/>, document.getElementById('game_component'))
  ReactDOM.render(<Players participants={game_participants} current_player={current_user}
                           socket={game_sock}/>, document.getElementById('players_component'))
}

render_component();
