import React from 'react'

const Highlight = ({color, text}) => {
    return (
        <span className={`inline text-transparent bg-clip-text bg-gradient-to-r from-${color}-500 to-${color}-700`}>{text}</span>
    )
}

export default Highlight
