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
      tableCards: [],
      status: "",
      myCards: [
        {
          "id": 2,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 2,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 2,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 2,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 2,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        },
        {
          "id": 2,
          "expansion": null,
          "image": "http://127.0.0.1:8000/media/cards/16586428_1363362600402292_1922198806_o.png",
          "codename": "leja"
        }
      ],
      defaultCard: ""
    };

    this.onClickPickedCard = this.onClickPickedCard.bind(this);
    this.onClickPickMyCard = this.onClickPickMyCard.bind(this);
  }

  onClickPickedCard(props) {

  }

  onClickPickMyCard(props) {

  }

  render() {
    return (
      <MainLayout>
        <Table gameStatus={this.state.gameStatus}
               cards={this.state.tableCards}
               onClickPickedCard={this.onClickPickedCard}/>
        <StatusBar gameStatus={this.state.gameStatus}
        />
        <MyHand cards={this.state.myCards}
                defaultCard={this.state.defaultCard}
                onClickPickedCard={this.onClickPickMyCard}
                gameStatus={this.state.gameStatus}
        />
      </MainLayout>
    );
  }

}