import type { Todo } from "../types";
import { TodoItem } from "./TodoItem";

type Props = {
  todos: Todo[];
  onToggle: (id: number) => void;
  onRemove: (id: number) => void;
  onMoveUp: (id: number) => void;
  onMoveDown: (id: number) => void;
};

export const TodoList: React.FC<Props> = ({
  todos,
  onToggle,
  onRemove,
  onMoveUp,
  onMoveDown,
}) => {
  return (
    <ul id="todo-list" className="todos__list">
      {todos.map((todo, idx) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          index={idx}
          total={todos.length}
          onToggle={onToggle}
          onRemove={onRemove}
          onMoveUp={onMoveUp}
          onMoveDown={onMoveDown}
        />
      ))}
    </ul>
  );
};
