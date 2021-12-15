#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
let str = '';
str = str.concat(fs.readFileSync(args[0]), fs.readFileSync(args[1]));
fs.writeFile(args[2], str, (err) => {
  if (err) console.log(err);
});
