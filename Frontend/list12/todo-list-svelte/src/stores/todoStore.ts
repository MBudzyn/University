import { writable } from "svelte/store";
import type { Todo } from "../types";

function createTodoStore() {
  const { subscribe, update, set } = writable<Todo[]>([]);

  return {
    subscribe,
    add: (name: string) => {
      update((todos) => [
        ...todos,
        { id: Date.now(), name, completed: false },
      ]);
    },
    toggle: (id: number) => {
      update((todos) =>
        todos.map((todo) =>
          todo.id === id ? { ...todo, completed: !todo.completed } : todo
        )
      );
    },
    remove: (id: number) => {
      update((todos) => todos.filter((todo) => todo.id !== id));
    },
    moveUp: (id: number) => {
      update((todos) => {
        const idx = todos.findIndex((t) => t.id === id);
        if (idx <= 0) return todos;
        const newTodos = [...todos];
        [newTodos[idx - 1], newTodos[idx]] = [newTodos[idx], newTodos[idx - 1]];
        return newTodos;
      });
    },
    moveDown: (id: number) => {
      update((todos) => {
        const idx = todos.findIndex((t) => t.id === id);
        if (idx === -1 || idx === todos.length - 1) return todos;
        const newTodos = [...todos];
        [newTodos[idx + 1], newTodos[idx]] = [newTodos[idx], newTodos[idx + 1]];
        return newTodos;
      });
    },
    clear: () => set([]),
  };
}

export const todoStore = createTodoStore();
