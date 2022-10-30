
const crypto = require('crypto'), SHA256 = message => crypto.createHash('sha256').update(message).digest('hex');

class NFTWorker{
    getMeta(filename){
        let fs = require('fs');
        let fileContent = fs.readFileSync(filename, 'hex');
        return fileContent;
    }

    getNFT(hash){
        const { StringDecoder } = require('string_decoder');
        const decoder = new StringDecoder('hex');

        let fs = require('fs');
        let file = fs.writeFileSync('NFT.png',decoder.write(hash),'hex');

        return true;
    }

    hashMeta(hash){
        return SHA256(hash + this.timestamp);
    }


}

worker = new NFTWorker();
hash = worker.getMeta('image.png');
if (worker.getNFT(hash)){
    console.log('Success!');
}

