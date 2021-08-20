import { useState  } from "react";
import { withRouter } from "react-router-dom";
import Header from "./components/Header";
import Particle from "./components/Particle";
import Classes from "./components/Classes";
import Highlight from "./components/Highlight";
const GPAC = () => {
    const [classes, setClasses] = useState([]);
    return (
    <div className="my-container flex-1  bg-green-50">
      <Particle />
      <Header
      className=""
        imgLink="https://images.pexels.com/photos/1370296/pexels-photo-1370296.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=125&w=210"
        descriptions="Enter your grades, what types of classes you are taking, course credits(optional) and calculates your weighted and unweighted GPA."
      >
        <Highlight color="green" text="GPA" r={600}/> Calculator
      </Header>
      <Classes />
    </div>
    )
}

export default withRouter(GPAC)
