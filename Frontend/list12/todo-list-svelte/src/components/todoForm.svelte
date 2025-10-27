<script lang="ts">
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();
  let text = "";

  function handleSubmit(e: Event) {
    e.preventDefault();
    if (text.trim()) {
      dispatch("add", text.trim());
      text = "";
    }
  }
</script>

<form class="add-item__container" on:submit={handleSubmit}>
  <input
    type="text"
    placeholder="What's on your mind?"
    class="add-item__element add-item__input"
    bind:value={text}
    required
  />
  <button type="submit" class="add-item__element add-item__submit">Add</button>
</form>
