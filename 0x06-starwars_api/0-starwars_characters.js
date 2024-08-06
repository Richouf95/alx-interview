#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';
const args = process.argv;

if (args.length > 2) {
  request(`${API_URL}/films/${args[2]}/`,
    (err, _, body) => {
      if (err) {
        console.log(err);
      }

      const characters = JSON.parse(body).characters;
      const charactersName = characters.map(
        url => new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        }));

      Promise.all(charactersName)
        .then(names => console.log(names.join('\n')))
        .catch(allErr => console.log(allErr));
    });
}
