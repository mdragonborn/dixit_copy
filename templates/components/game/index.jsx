import React from 'react';
// import LobbyBase from './LobbyBase.jsx'
import ReactDOM from 'react-dom'
import $ from 'jquery'

// lobby socket url
var lobby_sock = 'ws://' + window.location.host + "/game/";
// preset the current_user
var current_user = null;

// renders out the base component
function render_component(){
    console.log("jpg");
    ReactDOM.render(<h1>Henlo!</h1>, document.getElementById('game_component'))
}
        {/*<LobbyBase current_user={current_user} socket={lobby_sock}/>*/}


render_component();