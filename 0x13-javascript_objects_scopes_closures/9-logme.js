#!/usr/bin/node

let count = 0; // This variable will keep track of the number of arguments printed.

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++; // Increment the count after printing.
};

// Exporting the function for external use.
module.exports = exports;
