import {useEffect} from 'react'
import axios from 'axios'

function Generator (props) {
    const clickHandler = () => {
        console.log("testing")
        axios.get('http://localhost:5000/api/generate')
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