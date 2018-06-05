import React from 'react';
import {HandGrid} from './styles';

export default class MyHand extends React.Component {
  render() {
    console.log(this.props.cards);
    return (
      <HandGrid>
        { this.props.gameStatus === "PICK_CARD" ?
            this.props.cards.map(
            i => <img src={i.image}
                        onClick={() => this.props.onClickPickedCard(i.id)}
                        alt={i.codename}
                   />
          ):
          this.props.gameStatus === "WAITING_FOR_OTHERS"?
            this.props.cards.map(
              i => <img src={ i.id===this.props.currentlyPicked?this.props.defaultCard:i.image }
                        alt={'default'}
                   />
            )
            :
          this.props.cards.length === 0 ?
            Array(6).fill(1).map(
              i => <img src = {this.props.defaultCard}
                        alt="default"
              />
            ):
            this.props.cards.map(
              i => <img src={i.image}
                        alt={i.codename}
                   />
            )
        }
      </HandGrid>)
  }
}