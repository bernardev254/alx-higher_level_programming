#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = Number(w)) > 0) && ((h = Number(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let y = 0; y < this.width; y++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    const w = this.width;
    const h = this.height;
    this.width = h;
    this.height = w;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
