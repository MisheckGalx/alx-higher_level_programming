#!/usr/bin/node

/*
 * a class Square that defines a square and inherits from Square of 5-square.js
 */

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  constructor(size) {
    super(size);
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

const s1 = new SquareWithCharPrint(4);
console.log('Print with default character:');
s1.charPrint();

console.log('Print with custom character:');
s1.charPrint('C');
