import type { Todo } from "../types";

export type Action =
  | { type: "ADD"; payload: string }
  | { type: "TOGGLE"; payload: number }
  | { type: "REMOVE"; payload: number }
  | { type: "MOVE_UP"; payload: number }
  | { type: "MOVE_DOWN"; payload: number }
  | { type: "CLEAR" };

export const todoReducer = (state: Todo[], action: Action): Todo[] => {
  switch (action.type) {
    case "ADD":
      const newTodo: Todo = {
        id: Date.now(),
        name: action.payload,
        completed: false,
      };
      return [...state, newTodo];
    case "TOGGLE":
      return state.map((todo) =>
        todo.id === action.payload
          ? { ...todo, completed: !todo.completed }
          : todo
      );
    case "REMOVE":
      return state.filter((todo) => todo.id !== action.payload);
    case "MOVE_UP": {
      const idx = state.findIndex((t) => t.id === action.payload);
      if (idx <= 0) return state;
      const newState = [...state];
      [newState[idx - 1], newState[idx]] = [newState[idx], newState[idx - 1]];
      return newState;
    }
    case "MOVE_DOWN": {
      const idx = state.findIndex((t) => t.id === action.payload);
      if (idx === -1 || idx >= state.length - 1) return state;
      const newState = [...state];
      [newState[idx], newState[idx + 1]] = [newState[idx + 1], newState[idx]];
      return newState;
    }
    case "CLEAR":
      return [];
    default:
      return state;
  }
};
