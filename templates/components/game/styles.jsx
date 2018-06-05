import styled from 'styled-components';

export const MainLayout = styled.div`

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