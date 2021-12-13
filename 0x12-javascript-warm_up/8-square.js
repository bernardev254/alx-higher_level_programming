#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) || args[0] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; Number(args[0]) > i; i++) {
    for (let y = 0; y < Number(args[0]); y++) {
      console.log('X');
    }
  }
}
