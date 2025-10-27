<script lang="ts">
  import "./app.css";
  import { todoStore } from "./stores/todoStore";
  import { derived } from "svelte/store";

  import TodoForm from "./components/TodoForm.svelte";
  import TodoHeader from "./components/TodoHeader.svelte";
  import TodoList from "./components/TodoList.svelte";

  const todos = todoStore;
  const remaining = derived(todos, ($todos) => $todos.filter((t) => !t.completed).length);
</script>

<div class="body__wrapper">
  <header class="header__wrapper">
    <h1>Hello, Mateusz!</h1>
  </header>
  <main class="main">
    <section>
      <TodoForm on:add={(e) => todoStore.add(e.detail)} />
    </section>
    <section class="todos__container">
      <TodoHeader remaining={$remaining} onClear={() => todoStore.clear()} />
      <TodoList
        todos={$todos}
        onToggle={todoStore.toggle}
        onRemove={todoStore.remove}
        onMoveUp={todoStore.moveUp}
        onMoveDown={todoStore.moveDown}
      />
    </section>
  </main>
</div>
