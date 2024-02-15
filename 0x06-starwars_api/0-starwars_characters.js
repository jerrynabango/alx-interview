#!/usr/bin/node
const req = require('request');
const movieId = process.argv[2];
const options = {
  url: `https://swapi-api.hbtn.io/api/films/${movieId}`,
  method: 'GET'
};

req(options, function (err, res, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    all(chars, 0);
  }
});

function all(chars, index) {
  req(chars[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        all(chars, index + 1);
      }
    }
  });
}
