import { useState, useEffect } from "react";
import Particles from "react-particles-js";
import Navbar from "./components/Navbar";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Tasks from "./components/Tasks";
import AddTask from "./components/AddTask";
import { Nav } from "reactstrap";

const Home = () => {
    return (
        <div>
            <Navbar current="Home" />
        </div>
    )
}

export default Home
