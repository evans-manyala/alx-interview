#!/usr/bin/env node

const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2]; // First positional argument

if (!movieId || isNaN(movieId) || movieId < 1 || movieId > 6) {
    console.log("Please provide a valid movie ID (1-6).");
    process.exit(1);
}

const filmUrl = `${baseUrl}${movieId}/`;

request(filmUrl, (error, response, body) => {
    if (error) {
        console.error(`An error occurred: ${error}`);
        return;
    }
    
    if (response.statusCode !== 200) {
        console.error(`Failed to retrieve film data. Status code: ${response.statusCode}`);
        return;
    }
    
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;
    
    characterUrls.forEach(url => {
        request(url, (error, response, body) => {
            if (error) {
                console.error(`An error occurred while fetching character data: ${error}`);
                return;
            }
            
            if (response.statusCode !== 200) {
                console.error(`Failed to retrieve character data. Status code: ${response.statusCode}`);
                return;
            }
            
            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
});