import './App.css';
import {Generator} from "./components/Generator.js"
import {Input} from "./components/Input.js"
import React, {useState, useEffect} from 'react'
import axios from 'axios'


export const App = () => {
  // Setting variables
  const [state, setState] = useState("")
  const [render, setRender] = useState(false)
  const [delCount, setDelCount] = useState(0)
  const [userInput, setUserInput] = useState("")
  const input = render === false ? null : <Input inputString={userInput} setInput={setUserInput} delCount={delCount} setDelCount={setDelCount} /> // Determines whether to render the input box for a user
  
  // Declaring functions
  useEffect(() => { // callback function runs after dependency in array is changed
    if (render === false) { // only if box is not shown, function will happen
      axios.post('http://localhost:5000/api/stat/create',{text: userInput, delCount: delCount}, {withCredentials: true}) // post user input data to server
        .then(res => console.log(res))
        .catch(err => console.log(err))
    }
  }, [render]); // dependency array 'looking' at render state
  
  const clickHandler = () => {
    axios.get('http://localhost:5000/api/generate', {withCredentials: true})
      .then(res => {
        console.log(res)
        setRender(true) // Sets render to 'true', showing input box
        setState(res.data)}) // Saves generated text from API call, showing to user
      .catch(err => console.log(err))
    setTimeout(() => {
      setRender(false) // Sets render to 'false', hiding input box
      setState("") // Clears text from screen after timeout
      setDelCount(0) // resets del counter
    }, 60000)
  }
  // Return of App
  return (
    <div className="App">
      <h2>Typing Evaluator!</h2>
      <h3>Click the button to randomly generate a paragraph to type!</h3>
      <Generator clickHandler={clickHandler} />
      <p>{input}</p>
      <h4>{state}</h4>
    </div>
  );
}
