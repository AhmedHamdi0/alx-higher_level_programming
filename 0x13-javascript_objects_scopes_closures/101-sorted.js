#!/usr/bin/node

const data = require('./101-data').dict;

const result = {};
for (const userId in data) {
  const occurrences = data[userId];
  if (!result[occurrences]) {
    result[occurrences] = [];
  }
  result[occurrences].push(userId);
}

console.log(result);
