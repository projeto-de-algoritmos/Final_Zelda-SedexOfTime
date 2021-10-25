import React from 'react';
import './styles.css'

function Card({nome, peso, valor, deleteCard, porcentagem}){

  return(
    <div className="card" > 
    {/* {`${nome} ${peso} ${valor}`} */}
    <span><strong>Nome:</strong> {nome}</span>
    <span><strong>Peso:</strong> {peso} kg</span>
    <span><strong>Valor:</strong> {valor} rupes</span>
    { porcentagem ? 
    <span><strong>Porcentagem:</strong> {(porcentagem * 100).toFixed(2)}</span>:
        <button className="deleteBtn" onClick={deleteCard}>x</button>
    }
    </div>
  );
}

export default Card;
