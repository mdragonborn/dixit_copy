import React from 'react';


export default class MyHand extends React.Component {
  render() {
    return (
      <HandGrid>
        { this.gameStatus === "PICK_CARD" ?
            this.props.cards.map(
            src => <img src={src}
                        onClick={this.props.onClickPickedCard(src)}
                   />
          ):
          this.props.cards.size === 0 ?
            Array(6).map(
              i => <img src = {this.props.defaultCard} />
            ):
            this.props.cards.map(
              src => <img src={src}/>
            )
        }
      </HandGrid>)
  }
}