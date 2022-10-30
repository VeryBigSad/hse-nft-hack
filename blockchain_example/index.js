const {Block, Blockchain} = require('./blockchain.js');

const test = new Blockchain();
test.addBlock(new Block(Date.now().toString(), {from:"Stas", to:"Fedor", amount:'130000$'}));
test.addBlock(new Block(Date.now().toString(), {from:"Fedor", to:"Stas", amount:'1300$'}));

console.log(test.chain);