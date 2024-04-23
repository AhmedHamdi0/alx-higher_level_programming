#!/usr/bin/node

const arg = process.argv[2];
const times = parseInt(arg, 10);

if (arg === undefined || isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
