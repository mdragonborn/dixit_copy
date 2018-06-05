import React from 'react';
import {StatusDiv} from './styles'

export default class StatusBar extends React.Component {
  render() {
    return (
      <StatusDiv>
        {this.props.gameStatus || " "}
      </StatusDiv>
    );
  }
}