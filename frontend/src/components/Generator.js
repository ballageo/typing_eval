import {useEffect} from 'react'
import axios from 'axios'

export const Generator = props => {
    
    return (
        <div>
            <button onClick={ () => props.clickHandler() }>Generate!</button>
            <br/>
            <br/>
        </div>
    )
}
