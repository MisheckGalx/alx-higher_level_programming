#!/usr/bin/node

/*
 * a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
}

const s1 = new Square(4);
console.log('Original Square:');
s1.print();

console.log('Double:');
s1.double();
