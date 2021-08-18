import { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, withRouter, Link } from "react-router-dom";
import Navbar from "./components/Navbar";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Tasks from "./components/Tasks";
import AddTask from "./components/AddTask";
import Particle from "./components/Particle";
function Todo() {
  const [showAddTask, setShowAddTask] = useState(false);
  const [tasks, setTasks] = useState([]);
  useEffect(() => {
    const getTasks = async () => {
      const tasksFromServer = await fetchTasks();
      setTasks(tasksFromServer);
    };
    getTasks();
  }, []);

  const fetchTasks = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/todos/");
    const data = await res.json();
    return data;
  };
  const addTask = async (task) => {
    const res = await fetch("http://127.0.0.1:8000/api/todos/", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(task),
    });

    const data = await res.json();

    setTasks([...tasks, data]);
    // const id = Math.floor(Math.random() * 10000) + 1
    // const newTask = {id, ...task}
    // setTasks([...tasks, newTask])
  };
  const deleteTask = async (id) => {
    await fetch(`http://127.0.0.1:8000/api/todos/${id}`, {
      method: "DELETE",
    });
    console.log("delete", id);
    setTasks(tasks.filter((task) => task.id !== id));
  };

  const toggleReminder = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, reminder: !task.reminder } : task
      )
    );
  };
  return (
    <div className="my-container flex-1">
      <Navbar current="Todo"/>
      <Particle />
      <Header
        title="Todo List"
        imgLink="https://images.pexels.com/photos/7103/writing-notes-idea-conference.jpg?auto=compress&cs=tinysrgb&dpr=2&h=125&w=210"
        onAdd={() => setShowAddTask(!showAddTask)}
        showAdd={showAddTask}
      />
      
      {showAddTask && <AddTask onAdd={addTask} />}
      {tasks.length > 0 ? (
        <Tasks tasks={tasks} onDelete={deleteTask} onToggle={toggleReminder} />
      ) : (
        "No Tasks To Show"
      )}
    </div>
  );
}

export default withRouter(Todo);
