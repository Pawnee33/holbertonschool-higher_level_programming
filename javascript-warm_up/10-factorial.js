#!/usr/bin/node

function factorial (number) {
  if (isNaN(number) || number <= 1) {
    return 1;
  }
  return factorial(number - 1) * number;
}
const number = parseInt(process.argv[2]);
console.log(factorial(number));
