import React, { useState, useEffect } from "react";

const Class = ({myId, deleteClass, setData}) => {
  const [name, setName] = useState(myId);
  const [grade, setGrade] = useState("");
  const [weight, setWeight] = useState("");
  const onChange = () => {
    setData(myId, name, grade, weight);
    console.log("change")
  };
  useEffect(()=>{
    onChange()
  },[name,grade,weight])
  return (
    <div id={`class-${myId}`} className="m-auto">
      <input
        id="class_name"
        name="class_name"
        type="text"
        placeholder="Class name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ width: "30%" }}
        className="inline-block max-w-md rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
      />
      <select
        id="grade"
        name="grade"
        value={grade}
        onChange={(e) => setGrade(e.target.value)}
        style={{ width: "13%" }}
        className="inline-block m-auto w-24 text-gray-700 py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
        required
      >
        <option value="A+">A+</option>
        <option value="A" selected="selected">
          A
        </option>
        <option value="A-">A-</option>
        <option value="B+">B+</option>
        <option value="B">B</option>
        <option value="B-">B-</option>
        <option value="C+">C+</option>
        <option value="C">C</option>
        <option value="C-">C-</option>
        <option value="D+">D+</option>
        <option value="D">D</option>
        <option value="D-">D-</option>
        <option value="F">F</option>
      </select>
      <select
        id="class_type"
        name="class_type"
        value={weight}
        onChange={(e) => setWeight(e.target.value)}
        style={{ width: "20%" }}
        className="inline-block m-auto w-36 text-gray-700 py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
        required
      >
        <option value="R" selected="selected">
          Regular
        </option>
        <option value="AP/IB">AP/IB</option>
        <option value="H+">Honors(5)</option>
        <option value="H-">Honors(4.5)</option>
        <option value="C">College</option>
      </select>
      <select
        id="credit"
        name="credit"
        style={{ width: "20%" }}
        className="inline-block m-auto w-36 text-gray-700 py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
        required
      >
        <option selected value={1}>
          Default
        </option>
        <option value={1}>1</option>
        <option value="1.5">1.5</option>
        <option value={2}>2</option>
        <option value="2.5">2.5</option>
        <option value={3}>3</option>
        <option value="3.5">3.5</option>
        <option value={4}>4</option>
        <option value="4.5">4.5</option>
        <option value={5}>5</option>
        <option value="5.5">5.5</option>
      </select>
      <button
        type="button"
        className="inline-block m-auto transform hover:scale-110 duration-200"
        onClick={() => deleteClass(myId)}
        id="delete_class"
      >
        <img
          className="pb-1 inline-block m-auto"
          src="https://stephenxie.github.io/images/delete.svg"
          height={40}
          width={40}
        />
      </button>
    </div>
  );
};

export default Class;
