import React from 'react'
import { useState } from 'react'
const AddTask = ({ onAdd }) => {
    const [text, setText] = useState('')
    const [reminder, setReminder] = useState(false)
    const onSubmit = (e) =>{
        e.preventDefault()
        if(!text){
            alert('Please add a task')
            return
        }
        onAdd({text,reminder})
        setText('')
        setReminder(false)
    }
    return (
        <div className=" modal-box fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2  z-50">
        <form className='add-form bg-white bg-opacity-100 relative w-full' onSubmit={onSubmit}>
            <div className='form-control'>
                <label> Task </label>
                <input type='text' placeholder='Add Task' value = {text} onChange={(e) => setText(e.target.value)}/>
            </div>
            {/* <div className='form-control'>
                <label>Day & Time</label>
                <input type='text' placeholder='Add Day & Time' value = {date} onChange={(e) => setDate(e.target.value)}/>
            </div> */}
            <div className='form-control-check'>
                <label> Set Reminder </label>
                <input type='checkbox' checked={reminder} value={reminder} onChange={(e) => setReminder(e.currentTarget.checked)}/>
            </div>
            <input type = 'submit' value='Save Task' className='btn btn-block'/>
        </form>
        </div>

    )
}

export default AddTask
