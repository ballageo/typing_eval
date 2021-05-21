import logo from './logo.svg';
import './App.css';
import Generator from "./components/Generator.js"

export default App => {
  return (
    <div className="App">
    <h2>Typing Evaluator!</h2>
    <h3>Click the button to randomly generate a paragraph to type!</h3>
        <Generator className="btn"/>
    </div>
  );
}
