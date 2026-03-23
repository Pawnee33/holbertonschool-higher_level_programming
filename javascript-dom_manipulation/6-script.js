#!/usr/bin/node

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")

.then(function(response) {
    console.log(response.status);
    if (!response.ok) {
        throw new Error("Erreur : " + response.status);
    }
    return response.json();
})
.then(function(data) {
    document.querySelector('#character').textContent = data.name;
})
.catch(function(erreur) {
    console.error("Probléme :", erreur.message);
});
