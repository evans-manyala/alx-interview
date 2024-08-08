#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];

async function getMovieCharacters (movieId) {
  try {
    const movieResponse = await requestPromise(`${baseUrl}${movieId}`);
    const movieData = JSON.parse(movieResponse.body);

    const characterPromises = movieData.characters.map(characterUrl => requestPromise(characterUrl));
    const characterResponses = await Promise.all(characterPromises);

    characterResponses.forEach(characterResponse => {
      const characterData = JSON.parse(characterResponse.body);
      console.log(characterData.name);
    });
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

getMovieCharacters(movieId);
