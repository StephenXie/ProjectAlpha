import { React, useState, useEffect } from "react";
import Button from "./Button";
const GPA = ({ classes }) => {
  const [GPA, setGPA] = useState({});
  useEffect(() => {
    getGPA();
  }, [classes]);
  const toJson = (data) => {
    var obj = new Object();
    obj.class_name = data.map((myclass) => myclass.name);
    obj.grade = data.map((myclass) => myclass.grade);
    obj.class_type = data.map((myclass) => myclass.weight);
    obj.credit = data.map((myclass) => myclass.credit);
    var myJSON = JSON.stringify(obj);
    return myJSON;
  };
  const getGPA = async () => {
    var myJSON = toJson(classes);
    console.log(myJSON);
    const res = await fetch("https://www.stephenxie.com/apiGPAcal/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: myJSON,
    });

    const data = await res.json();

    setGPA(data);
  };

  return (
    <div className="shadow stats w-3/5 mx-auto relative">
      <div className="stat">
        <div className="stat-figure text-blue-500">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            className="inline-block w-8 h-8 stroke-current"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </div>
        <div className="stat-title">Weighted GPA</div>
        <div className="stat-value">{GPA.GPA_w}</div>
        <div className="stat-desc"><progress value={GPA.pct_w} max="100" class="progress progress-info"></progress></div>
      </div>
      <div className="stat">
        <div className="stat-figure text-secondary">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            className="inline-block w-8 h-8 stroke-current"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </div>
        <div className="stat-title">Unweighted GPA</div>
        <div className="stat-value">{GPA.GPA_u}</div>
        <div className="stat-desc"><progress value={GPA.pct_u} max="100" class="progress progress-secondary"></progress></div>
      </div>
    </div>
  );
};

export default GPA;
