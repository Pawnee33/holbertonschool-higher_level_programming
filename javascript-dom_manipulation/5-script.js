#!/usr/bin/node

const updatesButton = document.querySelector("#update_header");

updatesButton.addEventListener("click", function() {
    const header = document.querySelector("header");
    header.textContent = "New Header!!!";
});
