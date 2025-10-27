document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("add-todo-form");
    const input = form.querySelector('input[name="todo-name"]');
    const todoList = document.getElementById("todo-list");
    const countSpan = document.getElementById("count");
    const clearBtn = document.getElementById("todos-clear");


    function updateCount() {
        const allTodos = todoList.querySelectorAll("li:not(.todo__container--completed)");
        countSpan.textContent = allTodos.length;
    }

    function createTodoItem(text) {
        const li = document.createElement("li");
        li.className = "todo__container";

        const nameDiv = document.createElement("div");
        nameDiv.className = "todo-element todo-name";
        nameDiv.textContent = text;

        const upBtn = document.createElement("button");
        upBtn.className = "todo-element todo-button move-up";
        upBtn.textContent = "↑";
        upBtn.addEventListener("click", () => {
            const prevLi = li.previousElementSibling;
            if (prevLi) {
                todoList.insertBefore(li, prevLi);
            }
        });

        const downBtn = document.createElement("button");
        downBtn.className = "todo-element todo-button move-down";
        downBtn.textContent = "↓";
        downBtn.addEventListener("click", () => {
            const nextLi = li.nextElementSibling;
            if (nextLi) {
                todoList.insertBefore(nextLi, li);
                li.parentNode.insertBefore(li, nextLi.nextSibling);
            }
        });


        const doneBtn = document.createElement("button");
        doneBtn.className = "todo-element todo-button";
        doneBtn.textContent = "Done";
        doneBtn.addEventListener("click", () => {
            if (li.classList.contains("todo__container--completed")) {
                li.classList.remove("todo__container--completed");
                doneBtn.textContent = "Done";
            } else {
                li.classList.add("todo__container--completed");
                doneBtn.textContent = "Revert";
            }
            updateCount();
        });

        const removeBtn = document.createElement("button");
        removeBtn.className = "todo-element todo-button";
        removeBtn.textContent = "Remove";
        removeBtn.addEventListener("click", () => {
            li.remove();
            updateCount();
        });

        li.appendChild(nameDiv);
        li.appendChild(upBtn);
        li.appendChild(downBtn);
        li.appendChild(doneBtn);
        li.appendChild(removeBtn);

        return li;
    }

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const todoText = input.value.trim();
        if (todoText !== "") {
            const newTodo = createTodoItem(todoText);
            todoList.appendChild(newTodo);
            input.value = "";
            updateCount();
        }
    });

    form.addEventListener("Clear all", (event) => {
        event.preventDefault();
        const todoText = input.value.trim();
        if (todoText !== "") {
            const newTodo = createTodoItem(todoText);
            todoList.appendChild(newTodo);
            input.value = "";
            updateCount();
        }
    });

    clearBtn.addEventListener("click", () => {
        todoList.innerHTML = "";
        updateCount();
    });

    updateCount();
});