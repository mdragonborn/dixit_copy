import styled from 'styled-components';

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