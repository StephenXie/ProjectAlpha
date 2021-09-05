import { useState  } from "react";
import { withRouter } from "react-router-dom";
import Header from "./components/Header";
import Particle from "./components/Particle";
import Button from "./components/Button"
import GPA from "./components/GPA";
import Classes from "./components/Classes";
import Class from "./components/Class";
import Highlight from "./components/Highlight";
const GPAC = () => {
    const [classes, setClasses] = useState([{id:0, name: "", grade: "A", weight:"R", credit: "1"}]); 
    const [numClass, setNumClass] = useState(1);
    const addClass = () => {
      setClasses([...classes, {id: numClass, name: "", grade: "A", weight:"R", credit: "1"}])
      setNumClass(numClass+1);
    }
    const deleteClass = (id) =>{
      console.log(classes)
      setClasses(classes.filter((myclass) => myclass.id!==id))
      
    }
    const setData = (id, name, grade, weight, credit) =>{
      setClasses(classes.map((myclass) => ( myclass.id==id ? {...myclass, name: name, grade: grade, weight: weight, credit: credit} : myclass)))
    }
    return(
    <div className="my-container flex-1  bg-green-50">
      <Particle />
      <Header
      className=""
        imgLink="https://images.pexels.com/photos/1370296/pexels-photo-1370296.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=125&w=210"
        descriptions="Enter your grades, what types of classes you are taking, course credits(optional) and calculates your weighted and unweighted GPA."
      button={<Button text={<div className="flex flex-row space-x-2"><svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path d="M12 14l9-5-9-5-9 5 9 5z" />
      <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />
    </svg><span>Add Class</span></div>} color="green" onClick={addClass} className="relative"/>}
      >
        <div className="animate__animated animate__flip animate__faster"><Highlight color="green" text="GPA" r={600}/> Calculator</div> 
      </Header>
      <GPA key={classes} classes={classes}/>
      <Classes classes={classes} deleteClass={deleteClass} setData={setData}/>
    </div>
    )
}

export default withRouter(GPAC)
