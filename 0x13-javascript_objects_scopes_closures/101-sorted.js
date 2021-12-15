#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const [k, v] of Object.entries(dict)) {
  if (!(v in newDict)) {
    newDict[v] = [k];
  } else {
    newDict[v].push(k);
  }
}
console.log(newDict);
