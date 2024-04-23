#!/usr/bin/node

function addMeMaybe (number, callback) {
  callback(++number);
}

module.exports = { addMeMaybe };
