import React from 'react'
import PropTypes from 'prop-types'
import Button from './Button'
const Header = ({ title }) => {
    const onClick = () =>{
        console.log('click')
    }
    return (
        <header>
            <h1>{title}</h1>
            <Button color='green' text ='Hello' onClick={onClick}/>
        </header>
    )
}

Header.defaultProps = {
    title: 'Task Tracker',
}

Header.propTypes = {
    title : PropTypes.string.isRequired,
}

// const headingStyle ={
//     color: 'red', 
//     backgroundColor : 'black'
// }

export default Header
