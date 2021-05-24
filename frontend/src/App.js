import './App.css';
import {Generator} from "./components/Generator.js"
import {Input} from "./components/Input.js"
import {useState} from 'react'

const App = () => {
  const [state, setState] = useState("")
  let input;
  if (state === "") {
    input = null
  } else {
    input = <Input />
  }
  return (
    <div className="App">
      <h2>Typing Evaluator!</h2>
      <h3>Click the button to randomly generate a paragraph to type!</h3>
      <Generator state={state} setState={setState} />
      {input}
      <p>The current state is: {state}</p>
    </div>
  );
}

export default App
