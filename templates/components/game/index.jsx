import React from 'react';
import Game from './Game.jsx'
import ReactDOM from 'react-dom'
import $ from 'jquery'

// lobby socket url
var lobby_sock = 'ws://' + window.location.host + "/game/";
// preset the current_user
var current_user = null;

// renders out the base component
function render_component(){
    console.log("jpg");
    ReactDOM.render(<Game/>, document.getElementById('game_component'))
}
        {/*<LobbyBase current_user={current_user} socket={lobby_sock}/>*/}


render_component();