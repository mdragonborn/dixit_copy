import React from 'react';
import ReactDOM from 'react-dom';
import MyHand from './MyHand';
import Table from './Table';
import StatusBar from './StatusBar';
import {MainLayout} from './styles';

export default class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      c: "starting",
      tableCards: [
        {
          "id": 2,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 3,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 4,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 5,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 6,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 7,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        }
      ],
      submittedCount: 3,
      gameStatus: "PICK_CARD",
      displayStatus: "Pick a card",
      myCards: [
        {
          "id": 2,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 3,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 4,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 5,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 6,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 7,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        }
      ],
      currentlyPicked: null,
      defaultCard: "http://127.0.0.1:8000/media/cards/pic879970.jpg"
    };

    this.onClickPickedCard = this.onClickPickedCard.bind(this);
    this.onClickPickMyCard = this.onClickPickMyCard.bind(this);
    this.handleData = this.handleData.bind(this);
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
               cards={this.state.tableCards}
               onClickPickedCard={this.onClickPickedCard}
               defaultCard={this.state.defaultCard}
               submittedCount={this.state.submittedCount}
               currentlyPicked={this.state.currentlyPickedTable}
        />
        <StatusBar gameStatus={this.state.displayStatus}
        />
        <MyHand cards={this.state.myCards}
                defaultCard={this.state.defaultCard}
                onClickPickedCard={this.onClickPickMyCard}
                gameStatus={this.state.gameStatus}
                currentlyPicked = {this.state.currentlyPicked}
        />
      </MainLayout>
    );
  }

}