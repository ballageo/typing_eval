import axios from 'axios'
import {useState} from 'react'

export const Input = props => {
    const [userInput, setUserInput] = useState("")
    const changeHandler = (e) => {
        e.preventDefault()
        setUserInput(e.target.value)
        console.log("input: " + e.target.value)
        console.log("state: " + userInput)
    }
    const submitToBackend = (data) => {

    }
    
    return (
        <textarea onChange={(e) => changeHandler(e)} rows="10" cols="100"></textarea>
    )
}