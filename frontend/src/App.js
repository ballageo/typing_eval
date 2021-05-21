import logo from './logo.svg';
import './App.css';
import Generator from "./components/Generator.js"
import {useState} from 'react'

export default App => {
  const [state, setState] = useState("")
  return (
    <div className="App">
      <h2>Typing Evaluator!</h2>
      <h3>Click the button to randomly generate a paragraph to type!</h3>
      <Generator state={state} setState={setState} />
      <p>The current state is: {state}</p>
    </div>
  );
}
