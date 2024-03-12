#!/usr/bin/node

/*
 * a class Rectangle that defines a rectangle
 */

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      //an empty object if w or h is not a positive integer//
      return {};
    }

    this.width = w;this.height = h;
  }

  print() {
    //the rectangle using the character X//
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
