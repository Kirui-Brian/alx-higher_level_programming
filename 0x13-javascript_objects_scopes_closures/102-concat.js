#!/usr/bin/node
const fs = require('fs');

// Grab the file paths from the command line arguments
const [,, fileA, fileB, fileC] = process.argv;

const contentA = fs.readFileSync(fileA, { encoding: 'utf8', flag: 'r' });

// Concatenate the contents and write to the destination file
fs.writeFileSync(FileC, contentA + contentB);

console.log(`Contents of ${fileA} and ${fileB} have been concatenated into ${fileC}`);
