#!/usr/bin/node

const arg = process.argv[2];
const parsed = parseInt(arg, 10);

if (!isNaN(parsed)) {
  console.log(`My number: ${parsed}`);
} else {
  console.log('Not a number');
}
