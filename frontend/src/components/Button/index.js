import React from 'react';
import './styles.css'


function Button(props){

  return(
    <button className="addButton">{props.title}</button>
  );
}

export default Button;