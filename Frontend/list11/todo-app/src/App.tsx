import { useReducer } from "react";
import { TodoForm } from "./components/TodoForm";
import { TodoList } from "./components/TodoList";
import { TodoHeader } from "./components/TodoHeader";
import { todoReducer } from "./reducers/TodoReducer";
import "./App.css";

export const App: React.FC = () => {
  const [todos, dispatch] = useReducer(todoReducer, []);

  const remaining = todos.filter((t) => !t.completed).length;

  return (
    <div className="body__wrapper">
      <header className="header__wrapper">
        <h1>Hello, Mateusz!</h1>
      </header>
      <main className="main">
        <section>
          <TodoForm onAdd={(text) => dispatch({ type: "ADD", payload: text })} />
        </section>
        <section className="todos__container">
          <TodoHeader remaining={remaining} onClear={() => dispatch({ type: "CLEAR" })} />
          <TodoList
            todos={todos}
            onToggle={(id) => dispatch({ type: "TOGGLE", payload: id })}
            onRemove={(id) => dispatch({ type: "REMOVE", payload: id })}
            onMoveUp={(id) => dispatch({ type: "MOVE_UP", payload: id })}
            onMoveDown={(id) => dispatch({ type: "MOVE_DOWN", payload: id })}
          />
        </section>
      </main>
    </div>
  );
};

export default App;
