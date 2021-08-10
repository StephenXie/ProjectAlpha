import {FaTimes} from 'react-icons'

const Task = (task) => {
    return (
        <div className ='task'>
            <h3>{task.text} <FaTimes /></h3>
            <p>{task.date}</p>
        </div>
    )
}

export default Task
