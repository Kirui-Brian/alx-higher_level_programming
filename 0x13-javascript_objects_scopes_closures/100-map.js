#!/usr/bin/node
const { list } = require('./100-data.js');

const newwList = list.map((element, index) => element * index);

console.log(list);
console.log(newList);
