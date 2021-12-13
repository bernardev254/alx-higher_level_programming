#!/usr/bin/node
const args = process.argv.slice(2);
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
add(Number(args[0]), Number(args[1]));
