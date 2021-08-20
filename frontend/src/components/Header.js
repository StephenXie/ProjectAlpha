import React from "react";
import PropTypes from "prop-types";
import Button from "./Button";
import Highlight from "./Highlight";
const Header = (props) => {
  return (
    <header className="relative shadow-xl bg-white rounded-3xl max-w-6xl w-auto mt-3 ">
      <div>
        <div className="card lg:card-side ">
          <figure>
            <img src={props.imgLink} />
          </figure>
          <div className="card-body ">
            <h2 className="card-title text-3xl font-extrabold">
            {props.children}
            </h2>
            <p className="break-normal">
              {props.descriptions}
            </p>
            <div className="card-actions">
            {props.button}
            </div>
          </div>
        </div>
      </div>
      
    </header>
  );
};

Header.defaultProps = {
  title: "",
};

Header.propTypes = {
  title: PropTypes.string.isRequired,
};

// const headingStyle ={
//     color: 'red',
//     backgroundColor : 'black'
// }

export default Header;
