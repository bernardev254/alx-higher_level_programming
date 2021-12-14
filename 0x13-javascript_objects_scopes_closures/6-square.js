#!/usr/bin/node
const mySquare = require('./5-square');
class Square extends mySquare {
  charPrint (C) {
    if (C === undefined) {
      for (let i = 0; i < this.size; i++) {
        let str = '';
        for (let y = 0; y < this.size; y++) {
          str += 'X';
        }
        console.log(str);
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        let str = '';
        for (let y = 0; y < this.size; y++) {
          str += C;
        }
        console.log(str);
      }
    }
  }
}
module.exports = Square;
