import { useState, useEffect } from "react";
import Particles from "react-particles-js";
import {
  BrowserRouter as Router,
  Route,
  withRouter,
  Link,
} from "react-router-dom";
import Navbar from "./components/Navbar";
import Header from "./components/Header";
import { tw } from 'twind'
import Footer from "./components/Footer";
import Highlight from "./components/Highlight";
import Tasks from "./components/Tasks";
import AddTask from "./components/AddTask";
import './toggle.css'
import { Nav } from "reactstrap";

const Home = () => {
  const link = [
    "https://stephenxie.me/images/Pexels%20Videos%201720220.mp4",
    "https://stephenxie.me/images/background.mp4",
  ];
  const [techToggled, setTechToggled] = useState(false);
  const toggleTech = () =>{
    console.log("toggled")
    var video = document.getElementById("video-container");
    video.pause()
    setTechToggled(!techToggled);
    video.load();
    video.play();
  }
  
  return (
    <div>
      <header className="relative flex items-center justify-center h-screen mb-12 overflow-hidden">
        <div className="relative z-30 p-5 text-center text-2xl text-white rounded-xl">
          <h1 className="w3-margin w3-jumbo leading-tight text-6xl font-extrabold font-sans">
            {techToggled ? <Highlight color="green" text="Stephen"/> : "Stephen"} Xie
          </h1>
          <a
            id="about-me-button"
            href="https://stephenxie.me/"
            className={tw`py-4 px-6 m-4 ${
              techToggled ? "bg-green-300 hover:bg-green-500" : "bg-yellow-300 hover:bg-yellow-500"
            } focus:ring-blue-500 focus:ring-offset-blue-200 text-white w-2/5 transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2  rounded-full`}
            type="button"
          >
            About Me
          </a>
          <label htmlFor="toogleButton" className="flex cursor-pointer text-base font-medium justify-center">
          <div className="px-2 text-white">            
          {techToggled ? <span className="font-bold"><Highlight color="green" text="Tech" l={300} r={500}/></span> : "Tech"} mode</div>
          <div className="relative">
            <input
              id="toogleButton"
              type="checkbox"
              className="hidden"
              onClick={() => toggleTech()}
            />
            <div className="toggle-path bg-gray-200 w-9 h-5 rounded-full shadow-inner"></div>
            <div className="toggle-circle absolute w-3.5 h-3.5 bg-white rounded-full shadow inset-y-0 left-0"></div>
          </div>
        </label>
        </div>
        <div
          id="particles-js"
          className="absolute w-full"
          style={{ zIndex: 0 }}
        />
        <video
          autoPlay
          loop
          muted
          className="fixed h-auto w-full min-w-full min-h-full max-w-none"
          style={{ zIndex: -1, objectFit: "fill" }}
          id="video-container"
        >
          <source
            id="video"
            src={techToggled ? link[1] : link[0]}
            type="video/mp4"
          />
          Your browser does not support the video tag.
        </video>
        
      </header>
    </div>
  );
};

export default withRouter(Home);
