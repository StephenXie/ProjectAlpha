import { useState  } from "react";
import { withRouter } from "react-router-dom";
import Header from "./components/Header";
import Particle from "./components/Particle";
import Button from "./components/Button"
import Classes from "./components/Classes";
import Class from "./components/Class";
import Highlight from "./components/Highlight";
const GPAC = () => {
    const [classes, setClasses] = useState([{id:0, name: "", grade: ""}]); 
    const [numClass, setNumClass] = useState(1);
    const addClass = () => {
      setClasses([...classes, {id: numClass, name: "", grade: "A-"}])
      setNumClass(numClass+1);
    }
    const deleteClass = (id) =>{
      console.log(classes)
      setClasses(classes.filter((myclass) => myclass.id!==id))
      console.log(`delete class ${id}`)
      
    }
    const setData = (id, name, grade, weight) =>{
      setClasses(classes.map((myclass) => ( myclass.id==id ? {...myclass, name: name, grade: grade, weight: weight} : myclass)))
    }
    return(
    <div className="my-container flex-1  bg-green-50">
      <Particle />
      <Header
      className=""
        imgLink="https://images.pexels.com/photos/1370296/pexels-photo-1370296.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=125&w=210"
        descriptions="Enter your grades, what types of classes you are taking, course credits(optional) and calculates your weighted and unweighted GPA."
      button={<Button text="Add class" color="green" onClick={addClass} className="relative"/>}
      >
        <div className="animate__animated animate__flip"><Highlight color="green" text="GPA" r={600}/> Calculator</div> 
      </Header>
      <Classes classes={classes} deleteClass={deleteClass} setData={setData}/>
    </div>
    )
}

export default withRouter(GPAC)
