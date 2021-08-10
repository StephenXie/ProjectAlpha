import React from 'react'
import PropTypes from 'prop-types'

const Button = ({text,color,onClick}) => {
    return (
        <button onClick={onClick} className='py-2 px-4 bg-gradient-to-r from-red-400 to-blue-500 transform hover:scale-110 text-white w-full transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg' style={{ backgroundColor: color}}>{text}</button>
    )
}

Button.defaultProps = {
    color: 'steelblue',
}

Button.propTypes = {
    text: PropTypes.string,
    color: PropTypes.string,
}
export default Button
