import {useEffect} from 'react'
import axios from 'axios'

export const Generator = props => {
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
        <div>
            <button onClick={ () => clickHandler() }>Generate!</button>
            <br/>
            <br/>
        </div>
    )
}
