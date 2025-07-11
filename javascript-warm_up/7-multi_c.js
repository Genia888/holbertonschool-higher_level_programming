#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x) || x <= 0) {
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
