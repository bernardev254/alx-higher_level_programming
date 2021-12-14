#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) || args[0] === undefined) {
  console.log('Missing size');
} else {
  const a = Number(args[0]);
  for (let i = 0; i < a; i++) {
    let str = '';
    for (let y = 0; y < a; y++) {
      str += 'X';
    }
    console.log(str);
  }
}
