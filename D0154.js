process.stdin.resume();
process.stdin.setEncoding('utf8');

var lines = [];
var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
reader.on('line', (line) => {
  //
  lines.push(line);
  //
});
reader.on('close', () => {
  //
  console.log(parseInt(lines[0])**2 - parseInt(lines[1]));
  //
});
