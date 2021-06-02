import axios from 'axios'
import {useState} from 'react'

export const Input = props => {
    const changeHandler = (e) => {
        e.preventDefault()
        props.setInput(e.target.value)
    }
    return (
        <textarea onChange={e => changeHandler(e)} rows="10" cols="100"></textarea>
    )
}