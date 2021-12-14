#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = Number(w)) > 0) && ((h = Number(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
