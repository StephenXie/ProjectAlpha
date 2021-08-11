import React from 'react'
import NavbarItem from './NavbarItem'
const Navbar = () => {
    return (
<nav id="navbar" className=" bg-gray-700 md:bg-opacity-100  w-full dark:bg-gray-800 md:shadow-lg rounded-xl" style={{zIndex: 9999}}>
        <div className="max-w-full mx-auto px-8">
          <div className="flex items-center justify-between h-16">
            <div className=" flex items-center">
              <a className="flex-shrink-0" href="/">
                <img className="h-8 w-8" src="https://stephenxie.me/images/avatar_white%20-%20round.png" />
              </a>
              <div className="hidden md:block">
                <div className="ml-6 flex items-baseline space-x-4">
                    <NavbarItem title="Home" link=".."/>
                    <NavbarItem title="Todo" link=".."/>
                    <NavbarItem title="Formatter" link=".."/>
                    <NavbarItem title="Cryptic" link=".."/>
                    <NavbarItem title="GPAC" link=".."/>
                    <NavbarItem title="PasteX" link=".."/>
                    <NavbarItem title="Linky" link=".."/>                    
                </div>
              </div>
            </div>
            <div className="block">
              <div className="ml-4 flex items-center md:ml-6">
              </div>
            </div>
          </div>
        </div>
      </nav>
    )
}

export default Navbar
