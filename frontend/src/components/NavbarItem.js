import React from 'react'

const NavbarItem = ({ title, link}) => {
    return (
        <a className="text-white hover:text-gray-300 dark:hover:text-white px-3 py-2 rounded-md text-lg  font-bold" href={link}>
            {title}
        </a>
    )
}

export default NavbarItem
