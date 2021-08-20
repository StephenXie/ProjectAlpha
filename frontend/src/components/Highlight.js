const Highlight = ({color, text, l, r}) => {
    return (
        <span className={`inline text-transparent bg-clip-text bg-gradient-to-r from-${color}-${l ? l : 500} to-${color}-${r ? r : 700}`}>{text}</span>
    )
}

export default Highlight
