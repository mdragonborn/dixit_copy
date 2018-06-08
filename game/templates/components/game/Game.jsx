import React from 'react';

import Websocket from 'react-websocket';

import MyHand from './MyHand';
import Table from './Table';
import StatusBar from './StatusBar';
import {MainLayout} from './styles';

export default class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      c: "starting",
      game: {
        tableCards: [
          {
            "id": 1,
            "image": "http://127.0.0.1:8000/media/cards/001.png",
            "codename": "leja"
          },
          {
            "id": 2,
            "image": "http://127.0.0.1:8000/media/cards/002.png",
            "codename": "leja"
          },
          {
            "id": 3,
            "image": "http://127.0.0.1:8000/media/cards/003.png",
            "codename": "leja"
          },
          {
            "id": 4,
            "image": "http://127.0.0.1:8000/media/cards/004.png",
            "codename": "leja"
          },
          {
            "id": 5,
            "image": "http://127.0.0.1:8000/media/cards/005.png",
            "codename": "leja"
          },
          {
            "id": 6,
            "image": "http://127.0.0.1:8000/media/cards/006.png",
            "codename": "leja"
          }
        ],
        state: "WAITING_FOR_START",
        myCards: [{id: 2, image: "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png"},],
        players: [],
        turn: 0
      },
      displayStatus: "Pick a card",
      gameStatus: "PICK_CARD",
      currentlyPicked: null,
      defaultCard: "http://127.0.0.1:8000/media/cards/pic879970.jpg"
    };

    this.onClickPickedCard = this.onClickPickedCard.bind(this);
    this.onClickPickMyCard = this.onClickPickMyCard.bind(this);
    this.handleData = this.handleData.bind(this);
  }

  componentDidMount() {
    this.getGame()
  }

  getGame() {
    const game_url = 'http://localhost:8000/game-from-id/'+this.props.game_id;

    fetch(game_url).then(
      response => this.setState({game:JSON.parse(response)})
    )
  }

  onClickPickedCard(props) {
    this.setState(((state) => {
      return {
        currentlyPickedTable: props,
        gameStatus: "WAITING_FOR_RESULTS",
        displayStatus: "Waiting for others..."
      }
    }));
  }

  onClickPickMyCard(props) {
    this.setState(((state) => {
      return {
        currentlyPicked: props,
        gameStatus: "PICK_FROM_TABLE",//"WAITING_FOR_OTHERS",
        displayStatus: "Waiting for others..."
      }
    }));
    console.log(this.state);
  }

  handleData(data) {
    let result = JSON.parse(data);
    switch(data.messageType){
      default:
        return;
    }
  }

  render() {
        console.log(this.state);
    return (
      <MainLayout>
        <Table gameStatus={this.state.gameStatus}
               cards={this.state.game.tableCards}
               onClickPickedCard={this.onClickPickedCard}
               defaultCard={this.state.defaultCard}
               submittedCount={this.state.submittedCount}
               currentlyPicked={this.state.currentlyPickedTable}
        />
        <StatusBar gameStatus={this.state.displayStatus}
        />
        <MyHand cards={this.state.game.myCards}
                defaultCard={this.state.defaultCard}
                onClickPickedCard={this.onClickPickMyCard}
                gameStatus={this.state.gameStatus}
                currentlyPicked = {this.state.currentlyPicked}
        />
        <Websocket ref="socket" url={this.props.socket}
                   onMessage={this.handleData} reconnect={true}/>
      </MainLayout>
    );
  }

}
