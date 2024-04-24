#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destination = process.argv[4];

const contentA = fs.readFileSync(fileA).toString();
const contentB = fs.readFileSync(fileB).toString();
const concatenatedContent = contentA + contentB;

fs.writeFileSync(destination, concatenatedContent);
