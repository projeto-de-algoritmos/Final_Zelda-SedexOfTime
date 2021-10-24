import React from 'react';
import './styles.css'


function Input({inputTitle, inputPlaceholder, type, register, error, ...props}){
  return(
    <div className="inputComponent">
      <div className="inputTitle">{inputTitle}</div>
      <input 
        {...register}
        placeholder={inputPlaceholder ? inputPlaceholder: 'Insira...'} 
        className="inputArea"
        type={type}
        {...props}
        >
      </input>
      {error ? <p className="errorMessage">{error?.message}</p> :null}
      
    </div>
  );
}

export default Input;