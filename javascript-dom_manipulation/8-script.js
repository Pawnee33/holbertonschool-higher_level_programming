#!/usr/bin/node

document.addEventListener("DOMContentLoaded", function() {
  fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
    .then(function(response) {
      if (!response.ok) {
        throw new Error("Erreur : " + response.status);
      }
      return response.json();
    })
    .then(function(data) {
      const hello = document.querySelector("#hello");
      hello.textContent = data.hello;
    })
    .catch(function(erreur) {
      console.error("Problème :", erreur.message);
    });
});
