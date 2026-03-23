#!/usr/bin/node

const addButton = document.querySelector("#add_item");

addButton.addEventListener("click", function() {
    const item = document.createElement("li");
    item.textContent = "Item";
    const myList = document.querySelector(".my_list");
    myList.appendChild(item);
});
