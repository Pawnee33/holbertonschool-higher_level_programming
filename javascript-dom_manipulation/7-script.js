#!/usr/bin/node

fetch("https://swapi-api.hbtn.io/api/films/?format=json")

  .then(function(response) {
    if (!response.ok) {
      throw new Error("Erreur : " + response.status);
    }
    return response.json();
  })
  .then(function(data) {
    data.results.forEach(function(film) {
      const li = document.createElement("li");
      li.textContent = film.title;
      document.querySelector("#list_movies").appendChild(li);
    });
  })
  .catch(function(erreur) {
    console.error("Problème :", erreur.message);
  });
