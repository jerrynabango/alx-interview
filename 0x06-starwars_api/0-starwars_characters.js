#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');

const movie = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/';
const url = api + 'films/' + movie + '/';
request.get({ url: url }, function (error, response, body) {
  if (!error) {
    const all_characters = JSON.parse(body).all_characters;
    order(all_characters);
  }
});

function order (all_characters) {
  if (all_characters.length > 0) {
    request.get({ url: all_characters.shift() },
    function (error, res, body) {
      if (!error) {
        console.log(JSON.parse(body).name);
        order(all_characters);
      }
    });
  }
}
