import React from 'react';
import './styles.css'
import Card  from '../Card'

function List({answers, deleteCard}){

  return(
    <div className="cardList">
      {answers.map((item)=><Card key={item.nome} {...item} 
      deleteCard={()=>deleteCard(answers.filter((iten)=>iten.nome!==item.nome))}></Card>)}
    </div>
  );
}

export default List