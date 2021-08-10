import React, { Component } from "react";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      activeItem: {
        content: "",
        date: "",
      },
      todoList: [],
    };
  }

  async componentDidMount() {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/todos/");
      const todoList = await res.json();
      this.setState({
        todoList,
      });
    } catch (e) {
      console.log(e);
    }
  }
  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.todoList;
    return newItems.map((item) => (
      <li key={item.id} className="">
        <span
          className={` ${this.state.viewCompleted ? "completed-todo" : ""}`}
          title={item.content}
        >
          {item.content}
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="content">
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;