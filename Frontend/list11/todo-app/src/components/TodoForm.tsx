import { useState } from "react";

type Props = {
  onAdd: (text: string) => void;
};

export const TodoForm: React.FC<Props> = ({ onAdd }) => {
  const [value, setValue] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!value.trim()) return;
    onAdd(value.trim());
    setValue("");
  };

  return (
    <form className="add-item__container" onSubmit={handleSubmit}>
      <input
        type="text"
        name="todo-name"
        className="add-item__element add-item__input"
        placeholder="What's on your mind?"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        required
      />
      <button type="submit" className="add-item__element add-item__submit">
        Add
      </button>
    </form>
  );
};
