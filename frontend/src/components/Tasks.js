import Task from './Task'

const Tasks = ({ tasks,onDelete, onToggle}) => {
  return (
    <div class="container flex flex-col mx-2 md:mx-auto max-w-full md:w-3/5 w-11/12 items-center justify-center">
      <ul class="w-full flex flex-col">
      {tasks.map((task) => (
      <Task key = {task.id} task={task} onDelete={onDelete} onToggle={onToggle}/>
    ))}
      </ul>
    </div>
    
  )
}

export default Tasks
