// Button component that takes in props
import axios from 'axios'

const Generator = props => {
    const clickHandler = () => {
        console.log("testing")
        axios.get('http://localhost:5000/api/test')
        .then(res => {
            console.log(res)
            props.setState(res.data)
        })
        .catch(err => console.log(err))
    }
    return (
        <button onClick={ () => clickHandler() }>Generate!</button>
    )
}

export default Generator