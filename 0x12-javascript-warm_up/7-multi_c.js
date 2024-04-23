#!/usr/bin/node

const arg = process.argv[2];
const times = parseInt(arg, 10);

if (!isNaN(times) && times > 0) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
