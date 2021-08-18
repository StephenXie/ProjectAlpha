import React from "react";
import PropTypes from "prop-types";
import Button from "./Button";
const Header = ({ title, imgLink, onAdd, showAdd }) => {
  return (
    <header className="relative shadow-lg bg-white rounded-3xl mt-3">
      <div>
        <div className="card lg:card-side bordered">
          <figure>
            <img src={imgLink} />
          </figure>
          <div className="card-body">
            <h2 className="card-title">{title}</h2>
            <p>
              Drop down some notes or reminders for yourself by clicking on the button.
            </p>
            <div className="card-actions">
            <Button
                color={showAdd ? "red" : "green"}
                text={showAdd ? "Hide Add Task" : "Show Add Task"}
                onClick={onAdd}
            />
            </div>
          </div>
        </div>
      </div>
      
    </header>
  );
};

Header.defaultProps = {
  title: "Task Tracker",
};

Header.propTypes = {
  title: PropTypes.string.isRequired,
};

// const headingStyle ={
//     color: 'red',
//     backgroundColor : 'black'
// }

export default Header;
