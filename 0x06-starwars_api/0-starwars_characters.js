#!/usr/bin/node

const axios = require('axios');

const baseUrl = 'https://swapi.dev/api/films/';
const movieId = process.argv[2];

if (!movieId || isNaN(movieId) || movieId < 1 || movieId > 6) {
  console.log('Please provide a valid movie ID (1-6).');
  process.exit(1);
}

const filmUrl = `${baseUrl}${movieId}/`;

axios.get(filmUrl)
  .then(response => {
    const filmData = response.data;
    const characterUrls = filmData.characters;

    // Fetch each character
    const characterPromises = characterUrls.map(url =>
      axios.get(url)
        .then(response => {
          const characterData = response.data;
          console.log(characterData.name);
        })
        .catch(error => {
          console.error(`An error occurred while fetching character data: ${error.message}`);
        })
    );

    // Wait for all character data to be fetched
    return Promise.all(characterPromises);
  })
  .catch(error => {
    console.error(`An error occurred: ${error.message}`);
  });
