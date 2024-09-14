const yargs = require('yargs');
const {add,calculator, substract} = require('./calculator')

const options = yargs(process.argv);

console.log("Hello world");
console.log(add(5,10));
console.log(substract(10,5))