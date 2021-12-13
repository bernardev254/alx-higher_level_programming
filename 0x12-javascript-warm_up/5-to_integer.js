#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) || args[1] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', Number(args[1]));
}
