import React from 'react';
import {HandGrid} from './styles';

export default class MyHand extends React.Component {
  render() {
    let content;
    switch(this.props.gameStatus){
      case "PICK_CARD":
        content =  this.props.cards.map(
            i => <img src={i.image}
                        onClick={() => this.props.onClickPickedCard(i.id)}
                        alt={i.codename}
                   />
          );
        break;
      case "WAITING_FOR_OTHERS":
      case "PICK_FROM_TABLE":
      case "WAITING_FOR_RESULTS":
        content = this.props.cards.map(
              i => <img src={ i.id===this.props.currentlyPicked?this.props.defaultCard:i.image }
                        alt={'default'}
                   />
            );
        break;
      default:
        content = this.props.cards.map(
              i => <img src={i.image}
                        alt={i.codename}
                   />
            );
    }
    return (
      <HandGrid>
        {content}
      </HandGrid>)
  }
}