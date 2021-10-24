import Button from './components/Button';
import Input from './components/Input';
import List from './components/List';
import axios from 'axios';
import Select from 'react-select'
import { useState} from 'react';
import { useForm } from "react-hook-form";
import './styles/global.css';
import logo from './assets/map_default.png';

function App() {

    const [answers, setAnswers] = useState([]);
    const [city, setCity] = useState([]);
    const { register, handleSubmit, reset, formState:{errors} } = useForm();
    const {
        register: register1,
        formState: { errors: errors1 },
        handleSubmit: handleSubmit1,
    } = useForm();
const cities = [
{ value: 'Castle Town', label: 'Castle Town' },
{ value: 'Hyrule Castle', label: 'Hyrule Castle' },
{ value: 'Kakarito Village', label: 'Kakarito Village' },
{ value: 'Zoras Domain', label: 'Zoras Domain' },
{ value: 'Zora River', label: 'Zora River' },
{ value: 'The Lost Woods', label: 'The Lost Woods' },
{ value: 'Deku Tree', label: 'Deku Tree' },
{ value: 'Kokiri Forest', label: 'Kokiri Forest' },
{ value: 'Lake Hylia', label: 'Lake Hylia' },
{ value: 'Gerudo Valley', label: 'Gerudo Valley' },
{ value: 'Gerudo Fortress', label: 'Gerudo Fortress' },
{ value: 'Desert Colossus', label: 'Desert Colossus' },
]

    function onSubmit (data){
        setAnswers([...answers,data]);
        reset();
    }

    function sendButton(pesoMax){
        const reqBody = {
            pesoMax,
            city,
            answers:answers
        }
        console.log(reqBody);
        const headers = {'content-type': 'application/json'}     
        axios.post('http://127.0.0.1:5000/charge/', reqBody, headers)     
            .then(function (response) {       
                setAnswers(response.data.data);
                console.log(response.data.data);     })
            .catch(error => {       
                console.log(error)   })
    }

    return (
    <>
    <div className='logo'>
        <img src={logo} alt="icon" />
    </div>
    <div className="form">
        <form key={0} onSubmit={handleSubmit(onSubmit)}>
            <div className="inputField">
                <Input 
                register={register("peso", {
                    validate: value => value > 0 || 'Peso inválido!', 
                    required: 'Campo obrigatório!'
                    })} 
                inputPlaceholder = "Peso do produto" 
                inputTitle="Peso do produto" 
                type="number"
                step="any"  
                error={errors.peso}>
            </Input>
            <Input 
            register={register("valor", {
                validate: value => value > 0 || 'Valor inválido!', 
                required: 'Campo obrigatório!'
                })} 
            inputPlaceholder = "Valor do produto" 
            inputTitle="Valor do produto" 
            type="number"
            step="any" 
            error={errors.valor}>
        </Input>
    </div>
    <Button title = 'Adicionar'/>
    </form>
          </div>
          <List answers={answers} deleteCard={setAnswers}/>

          <form className="sendForm" onSubmit={handleSubmit1(sendButton)}>
              <div className="sendFormContainer">
                  <Input 
                  register={register1("pesoMax", {
                  validate: value => value > 0 || 'Valor inválido!'
                  })} 
                  inputPlaceholder = "Peso max" 
                  inputTitle="Peso máximo suportado" 
                  type="number"
                  step="any" 
                  error={errors1.pesoMax}>
              </Input>
              <br/>
          <Select options={cities} onChange={setCity}/>
      </div>

      <Button title = 'Calcular'/> 
      </form>
        </>
        );
}

export default App;
