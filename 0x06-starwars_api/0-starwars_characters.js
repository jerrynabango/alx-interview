#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const req = require('request');

const movie = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/';
const url = `${api}films/${movie}/`;

req.get({ url: url }, function (error, res, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    listCharacters(chars);
  }
});

function listCharacters(chars) {
  if (chars.length > 0) {
    req.get({ url: chars.shift() }, function (error, res, body) {
      if (!error) {
        console.log(JSON.parse(body).name);
        listCharacters(chars);
      }
    });
  }
}
