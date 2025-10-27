import type { Todo } from "../types";

type Props = {
  todo: Todo;
  index: number;
  total: number;
  onToggle: (id: number) => void;
  onRemove: (id: number) => void;
  onMoveUp: (id: number) => void;
  onMoveDown: (id: number) => void;
};

export const TodoItem: React.FC<Props> = ({
  todo,
  onToggle,
  onRemove,
  onMoveUp,
  onMoveDown,
}) => {
  return (
    <li
      className={`todo__container${todo.completed ? " todo__container--completed" : ""}`}
    >
      <div className="todo-element todo-name">{todo.name}</div>
      <button className="todo-element todo-button move-up" onClick={() => onMoveUp(todo.id)}>
        ↑
      </button>
      <button className="todo-element todo-button move-down" onClick={() => onMoveDown(todo.id)}>
        ↓
      </button>
      <button className="todo-element todo-button" onClick={() => onToggle(todo.id)}>
        {todo.completed ? "Revert" : "Done"}
      </button>
      <button className="todo-element todo-button" onClick={() => onRemove(todo.id)}>
        Remove
      </button>
    </li>
  );
};
