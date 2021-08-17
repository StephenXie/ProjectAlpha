import React from 'react'
import PropTypes from 'prop-types'
import Button from './Button'
const Header = ({ title, onAdd, showAdd }) => {
    return (
        <header className="relative pb-36">
            <h1>{title}</h1>
            <Button color={showAdd ? "red" : "green"} text ={showAdd ? "Hide Add Task" : "Show Add Task"} onClick={onAdd}/>
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
