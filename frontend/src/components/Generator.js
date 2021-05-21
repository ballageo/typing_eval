// Button component that takes in props
import axios from 'axios'

export default Generator => {
    const clickHandler = () => {
        console.log("testing")
        axios.get('http://localhost:5000/api/test')
        .then(res => console.log(res))
        .catch(err => console.log(err))
    }
    return (
        <button onClick={ () => clickHandler() }>Generate!</button>
    )
}
