import React from 'react';
import ReactDOM from 'react-dom';

export default class Game extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            c: "starting",
            tableCards: [],
            status: "",
            myCards: [],
            defaultCard: ""
        };

        this.onClickPickedCard=this.onClickPickedCard.bind(this);
        this.onClickPickMyCard=this.onClickPickMyCard.bind(this);
    }

    onClickPickedCard(props){

    }

    onClickPickMyCard(props){

    }

    render() {
        return (
            <div>
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
            </div>
        );
    }

}