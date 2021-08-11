import { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import Header from './components/Header'
import Tasks from './components/Tasks'
import AddTask from './components/AddTask'
function Test() {
    const [showAddTask, setShowAddTask] = useState(false)
    const [tasks, setTasks] = useState([])
    useEffect(() => {
      const getTasks =async() =>{
        const tasksFromServer = await fetchTasks()
        setTasks(tasksFromServer)
      }
      getTasks()
    }, [])

    const fetchTasks = async () =>{
      const res = await fetch('http://127.0.0.1:8000/api/todos/')
      const data = await res.json()
      return data
    }
    const addTask =  async (task) =>{
      const res = await fetch('http://127.0.0.1:8000/api/todos/',{
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify(task),
      })

      const data = await res.json()

      setTasks([...tasks, data])
      // const id = Math.floor(Math.random() * 10000) + 1
      // const newTask = {id, ...task}
      // setTasks([...tasks, newTask])
    }
    const deleteTask = async (id) =>{
      await fetch(`http://127.0.0.1:8000/api/todos/${id}`,{
        method: 'DELETE'
      })
      console.log('delete',id)
      setTasks(tasks.filter((task) => task.id!== id))
    }

    const toggleReminder = (id) =>{
        setTasks(tasks.map((task) => task.id === id ? {...task, reminder: !task.reminder} : task))
    }
    return (
        <div className='container'>
            <Navbar/>
            <Header title='Todo List' onAdd={() => setShowAddTask(!showAddTask)} showAdd={showAddTask}/>
            {showAddTask && <AddTask onAdd={addTask}/>}
            {tasks.length > 0 ? (<Tasks tasks ={tasks} onDelete={deleteTask} onToggle={toggleReminder}/>) : ("No Tasks To Show")}
        </div>
        
    )
}

export default Test