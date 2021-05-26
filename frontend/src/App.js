import './App.css';
import {Generator} from "./components/Generator.js"
import {Input} from "./components/Input.js"
import React, {useState, useEffect} from 'react'
import axios from 'axios'


const App = () => {
  const [state, setState] = useState("")
  const [render, setRender] = useState(false)
  let input
  render == false ? input = null : input = <Input /> // Determines whether to render the input box for a user
  const clickHandler = () => {
    axios.get('http://localhost:5000/api/generate')
    .then(res => {
      setRender(true) // Sets render to 'true', showing input box
      console.log(res)
      setState(res.data) // Saves generated text from API call, showing to user
      setTimeout(() => {
        setRender(false) // Sets render to 'false', hiding input box
        setState("") // Clears text from screen after timeout
      }, 1500)}) 
    .catch(err => console.log(err))
  }
  return (
    <div className="App">
      <h2>Typing Evaluator!</h2>
      <h3>Click the button to randomly generate a paragraph to type!</h3>
      <Generator clickHandler={clickHandler} state={state} setState={setState} submitted={render} setSubmitted={setRender} />
      {input}
      <h4>{state}</h4>
    </div>
  );
}

export default App
