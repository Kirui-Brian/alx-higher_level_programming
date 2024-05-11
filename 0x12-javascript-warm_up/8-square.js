#!/usr/bin/node
const x = Number(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let s = '';
  for (let i = 0; i < x; i++) {
    s += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(s);
  }
}
