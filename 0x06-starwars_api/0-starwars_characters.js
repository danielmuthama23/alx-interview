#!/usr/bin/node
// script that prints all characters of a Star Wars movie.

const request = require('request');
const util = require('util');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Convert the callback-based request method to a Promise-based method
const requestPromise = util.promisify(request);

(async function () {
  try {
    const { statusCode, body } = await requestPromise(url);

    if (statusCode === 200) {
      const data = JSON.parse(body);
      const characterUrls = data.characters;
      const ids = characterUrls.map(url => parseInt(url.split('/').slice(-2, -1)[0]));
      const sortedIds = ids.sort((a, b) => a - b);

      for (const id of sortedIds) {
        const { statusCode, body } = await requestPromise(`https://swapi-api.alx-tools.com/api/people/${id}/`);

        if (statusCode === 200) {
          const data = JSON.parse(body);
          const charactername = data.name;
          console.log(charactername);
        } else {
          console.log(`Error: Received status code ${statusCode}`);
        }
      }
    } else {
      console.log(`Error: Received status code ${statusCode}`);
    }
  } catch (error) {
    console.log(`Error: ${error}`);
  }
})();
