import { useState } from 'react'
import Header from './components/Header'
import Tasks from './components/Tasks'
function Test() {
    const [tasks, setTasks] = useState([
        {
          id: 1,
          text: "Nature walk in the park",
          description: "Visit the park with my friends",
          reminder: true,
        },
    
        {
          id: 2,
          text: "Visit",
          description: "Got to my aunt's place",
          reminder: true,
        },
    
        {
          id: 3,
          text: "Write",
          description: "Do an article about anthropology",
          reminder: false,
        },
    ])
    return (
        <div className='container'>
            <Header title='Todo List'/>
            <Tasks tasks ={tasks}/>
        </div>
        
    )
}

export default Test