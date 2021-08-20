import React from "react";
import Class from "./Class";
const Classes = ({ classes }) => {
  return (
    <div className="max-w-full m-auto relative">
      <div className="inline-block text-left space-y-3 ">
        <div id="classes" className="space-y-2">
          <Class />
        </div>
      </div>
    </div>
  );
};

export default Classes;
