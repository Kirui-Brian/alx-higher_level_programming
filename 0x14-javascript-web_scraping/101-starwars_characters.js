#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;
    printCharacters(characterUrls, 0);
  }
});

function printCharacters(characterUrls, i) {
  if (i >= characterUrls.length) {
    return;
  }

  request(characterUrls[i], function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(characterUrls, i + 1);
    }
  });
}
