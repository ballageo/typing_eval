import axios from 'axios'
import {useState} from 'react'

export const Input = props => {
    const changeHandler = (e) => {
        if (e.key == "Backspace") {
            props.setDelCount((s, p) => s += 1)
        }
        props.setInput(e.target.value)
    }
    return (
        <textarea onKeyUp={e => changeHandler(e)} rows="10" cols="100"></textarea>
    )
}