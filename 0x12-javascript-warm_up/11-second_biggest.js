#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log('0');
} else {
  const myArray = args.map(Number);
  const second = myArray.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
