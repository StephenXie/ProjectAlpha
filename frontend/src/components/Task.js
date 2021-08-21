import { FaTimes } from "react-icons/fa";
import "../collapse.css"
const Task = ({ task, onDelete, onToggle }) => {
  return (
    <div
      className={`task ${task.reminder ? "reminder" : ""}`}
      onDoubleClick={() => onToggle(task.id)}
    >
      <li class="border-gray-400 flex flex-row mb-2">
        <div className="shadow border select-none cursor-pointer bg-white dark:bg-gray-800 rounded-md flex flex-1 flex-row justify-between items-center p-3">
          <div tabindex="0" className={`my-collapse w-3/5 rounded-box absolute p-1 ${task.description ? "my-collapse-arrow" : ""}`}>
            {task.description && <input type="checkbox" /> }
            <div className="my-collapse-title font-medium dark:text-white">{task.text}</div>
            <div className="my-collapse-content"><p>{task.description}</p></div>
          </div>
          <div className="flex flex-row">
          <div className="text-gray-600  :text-gray-200 text-xs mr-8 ">
            {task.date}
          </div>
          <FaTimes
            style={{ color: "red", cursor: "pointer" }}
            onClick={() => onDelete(task.id)}
          />
          </div>
        </div>
      </li>
    </div>
  );
};

export default Task;
