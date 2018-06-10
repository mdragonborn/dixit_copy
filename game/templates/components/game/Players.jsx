import React from 'react'
import {PlayersLayout} from './styles'


//TODO get participants api
export default class Players extends React.Component {
  constructor(props) {
    super(props);
    this.state = { participants: []}
  }

  // componentWillMount(){
  //   fetch('http://127.0.0.1:8000/game/participants/2/?format=json').then(
  //     response => response.json()
  //   ).then(
  //     participants => {
  //       this.setState({participants})
  //     }
  //   )
  // }

  render() {
    let content = <PlayersLayout>
      {
        console.log(this.state.participants) ||
        this.props.participants ?
        this.props.participants.map(
          player =>
            <div className="user">
              <img src={player.profile_picture} alt="profile picture"/>
              <div className="name">{player.username}</div>
            </div>
        ):null
      }
    </PlayersLayout>;
    return content;
  }

}
