import React from 'react';
import { TableLayout } from './styles'

export default class Table extends React.Component {
  render() {
    let content;
    switch (this.props.gameStatus) {
      case "WAITING_FOR_OTHERS":
        content = <TableLayout>
          {Array(this.props.submittedCount).fill(1).map(
            i => <img src={this.props.defaultCard}
              alt="default"
            />
          )}
        </TableLayout>;
        break;
      case "PICK_FROM_TABLE":
        content = <TableLayout>
          {
            this.props.cards.map(
              i => <img src={i.image}
                onClick={() => this.props.onClickPickedCard(i.id)}
                alt={i.codename}
              />
            )
          }</TableLayout>;
        break;
      case "WAITING_FOR_RESULTS":
          content =  <TableLayout>
          {
            this.props.cards.map(
              i => <img src={i.image}
                alt={i.codename}
                className={i.id===this.props.currentlyPicked?"grow":""}
              />
            )
          }</TableLayout>;
        break;
      default:
        content = <TableLayout />
    }
    return content;
  }
}