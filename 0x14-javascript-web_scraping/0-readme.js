#!/usr/bin/node
// reads the contents of a file storing it into a variable
// and log its contents onto the console

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (error, data) {
  if (!error) {
    console.log(data.toString());
  } else {
    console.log(error);
  }
});
