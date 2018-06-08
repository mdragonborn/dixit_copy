import React from 'react'
import {PlayersLayout} from './styles'

export default class Players extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      players: [
        {id: 1, name: "mdragonborn"},
        {id: 2, name: "micika"},
        {id: 3, name: "filasin"},
        {id: 4, name: "vomindoraan"}
      ],
      current_player: {
        id: 3,
        name: "filasin"
      }
    }
  }

  render() {
    let content = <PlayersLayout>
      {
        this.state.players.map(
          player => player.id === this.state.current_player.id ? null :
            <div className="user">
              <img src={player.picture} alt="profile picture"/>
              <div className="name">{player.name}</div>
            </div>
        )
      }
    </PlayersLayout>;
    return content;
  }

}