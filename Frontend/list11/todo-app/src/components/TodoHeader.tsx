type Props = {
  remaining: number;
  onClear: () => void;
};

export const TodoHeader: React.FC<Props> = ({ remaining, onClear }) => {
  return (
    <header className="todos-header__container">
      <h2>
        Todo List (<span id="count">{remaining}</span> remaining)
        <button id="todos-clear" className="todos-clear" onClick={onClear}>
          Clear all
        </button>
      </h2>
    </header>
  );
};
