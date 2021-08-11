import {FaTimes} from 'react-icons/fa'

const Task = ({task, onDelete, onToggle}) => {
    return (
        
        <div className ={`task ${task.reminder ? 'reminder' : ''}`} onDoubleClick={() => onToggle(task.id)}>
            <li class="border-gray-400 flex flex-row mb-2">
            <div
                class="shadow border select-none cursor-pointer bg-white dark:bg-gray-800 rounded-md flex flex-1 items-center p-4">
                <div class="flex-1 pl-1 mr-16">
                <div class="font-medium dark:text-white">
                    {task.text}
                </div>
                </div>
                <div class="text-gray-600 dark:text-gray-200 text-xs mr-8">
                {task.date}
                </div>
                <FaTimes style={{color : 'red', cursor: 'pointer'}} onClick={() => onDelete(task.id)}/>
            </div>
            </li>
        </div>
    )
}

export default Task
