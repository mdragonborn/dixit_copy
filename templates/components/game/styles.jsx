import styled from 'styled-components';

export const MainLayout = styled.div`

`;

export const TableLayout = styled.div`
    display: block;
    height: 30vh;
    text-align: center;
    align-content: center;
    justify-content: center;
    
    img {
    height: 150px;
    padding: 10px;
    transition: all .2s ease-in-out;
  }
  
  img:hover {
    transform: scale(1.1);
  }
  .grow {
    transform: scale(1.1);
  }
`;

export const PlayersLayout = styled.div`
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr;
  margin: 10px;
  background: lightblue;
  
  * {
    padding: 5px;
    margin: 5px;
  }
  
  img {
    width: 100px;
  }
  
  .user {
        border: 1px solid grey;
    border-radius: 2px;
  }
  
  .name {
    font-weight: bold;
  }
`;

export const HandGrid = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
  
  img {
    height: 150px;
    padding: 10px;
    transition: all .2s ease-in-out;
  }
  
  img:hover {
    transform: scale(1.1);
  }
`;

export const StatusDiv = styled.div`
  text-align: center;
  border: 3px solid black;
  border-radius: 4px;
  font-size: 2rem;
`;