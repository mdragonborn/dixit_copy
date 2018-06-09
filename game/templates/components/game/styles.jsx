import styled from 'styled-components';

export const MainLayout = styled.div`

`;

export const TableLayout = styled.div`
  padding: 5vh 0;
  text-align: center;
  align-content: center;
  justify-content: center;
  height: 35vh;
    
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
  
  img {
    max-width: 12vw;
    max-height: 30vh;
    padding: 10px;
    transition: all .2s ease-in-out;
    border-radius: 20px;
  }
  
  img:hover {
    transform: scale(1.3);
  }
  
  .grow {
    transform: scale(1.3);
  }
`;

export const PlayersLayout = styled.div`
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr;
  margin: 10px;
  background: lightblue;
  
  * {
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
    max-width: 12vw;
    max-height: 30vh;
    padding: 10px;
    transition: all .2s ease-in-out;
    border-radius: 20px;
  }
  
  img:hover {
    transform: scale(1.3);
  }
`;

export const StatusDiv = styled.div`
  text-align: center;
  border: 3px solid black;
  border-radius: 4px;
  font-size: 2rem;
`;
