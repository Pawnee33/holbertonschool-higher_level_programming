#!/usr/bin/node

let Times = parseInt(process.argv[2]);
if (isNaN(Times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Times; i++) {
    console.log('C is fun')
  }
}
