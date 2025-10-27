<script lang="ts">
  export let remaining: number;
  export let onClear: () => void;
</script>

<header class="todos-header__container">
  <h2>
    Todo List (<span>{remaining}</span> remaining)
    <button class="todos-clear" on:click={onClear}>Clear all</button>
  </h2>
</header>
