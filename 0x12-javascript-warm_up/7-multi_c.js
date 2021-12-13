#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) || args[0] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; Number(args[0]) > i; i++) {
    console.log('C is fun');
  }
}
