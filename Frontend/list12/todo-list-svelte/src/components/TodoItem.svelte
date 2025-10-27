<script lang="ts">
  import type { Todo } from "../types";

  export let todo: Todo;

  export let onToggle: (id: number) => void;
  export let onRemove: (id: number) => void;
  export let onMoveUp: (id: number) => void;
  export let onMoveDown: (id: number) => void;
</script>

<li class="todo__container" class:todo__container--completed={todo.completed}>

  <div class="todo-element todo-name">{todo.name}</div>
  <button class="todo-element todo-button move-up" on:click={() => onMoveUp(todo.id)}>↑</button>
  <button class="todo-element todo-button move-down" on:click={() => onMoveDown(todo.id)}>↓</button>
  <button class="todo-element todo-button" on:click={() => onToggle(todo.id)}>
    {todo.completed ? "Revert" : "Done"}
  </button>
  <button class="todo-element todo-button" on:click={() => onRemove(todo.id)}>Remove</button>
</li>

<style>
  .todo__container--completed .todo-name {
    text-decoration: line-through;
    opacity: 0.5;
  }
</style>
