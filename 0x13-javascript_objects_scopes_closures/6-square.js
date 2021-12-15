#!/usr/bin/node
const mySquare = require('./5-square');
module.exports = class Square extends mySquare {
  charPrint (C) {
    if (!C) {
      super.print();
    } else {
      for (let x = 0; x < this.width; x++) {
        let str = '';
        for (let y = 0; y < this.width; y++) {
          str += C;
        }
        console.log(str);
      }
    }
  }
};
