#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).map(Number);
  const max = Math.max(...list);
  const index = list.indexOf(max);
  list.splice(index, 1);
  console.log(Math.max(...list));
}
