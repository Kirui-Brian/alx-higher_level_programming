#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};

// Exporting the function for external use.
module.exports = exports;
