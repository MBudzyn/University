<script lang="ts">
  import TodoItem from "./TodoItem.svelte";
  import type { Todo } from "../types";

  export let todos: Todo[];
  export let onToggle: (id: number) => void;
  export let onRemove: (id: number) => void;
  export let onMoveUp: (id: number) => void;
  export let onMoveDown: (id: number) => void;
</script>

<ul class="todos__list">
  {#each todos as todo, idx}
    <TodoItem
      {todo}
      index={idx}
      total={todos.length}
      onToggle={onToggle}
      onRemove={onRemove}
      onMoveUp={onMoveUp}
      onMoveDown={onMoveDown}
    />
  {/each}
</ul>
