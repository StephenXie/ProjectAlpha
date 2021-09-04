import React from "react";
import Class from "./Class";
const Classes = ({ classes, deleteClass, setData }) => {
  return (
    <div className="max-w-full mx-auto relative my-2">
      <div className="inline-block text-left space-y-3 ">
        <div id="myclasses" className="space-y-2">
        {classes.map((myclass) => (
      <Class key={myclass.id} myId={myclass.id} deleteClass={deleteClass} setData={setData}/>
    ))}
        </div>
      </div>
    </div>
  );
};

export default Classes;
