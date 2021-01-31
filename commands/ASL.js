// fs module for JSON parsing
const fs = require('fs');
const udp_sockets = require('../udp_sockets.js');
let rawDictionary = fs.readFileSync("./dictionary.json"); // process JSON before proceeding
let dictionary = JSON.parse(rawDictionary); // convert JSON to string 

// TODO:
function removeCase() {
    let newDictionary = [];
    return newDictionary;
}

function createImageList(sentence, dictionary) {
    let imageList = [];
    for (let i = 0; i < sentence.length; i++) {
        let word = sentence[i];
        if ( !(dictionary.hasOwnProperty(word)) ) { // word is unknown
            if (word.length > 1) {
                let letters = word.split("");
                for (let j = 0; j < letters.length; j++) {
                    let char = letters[j].toLowerCase(); // TODO: write function to access values case-insensitively
                    if (dictionary.hasOwnProperty(char)) {
                        imageList.push(dictionary[char]);
                    } else {
                        j++;
                    }
                }
            } else {
                i++; // unknown char
            }
        } else { // word is in dictionary
            let word = sentence[i];
            imageList.push(dictionary[word]);
        }
        if (dictionary.hasOwnProperty("spacebar")) {
            imageList.push(dictionary["spacebar"]); // separate words
        }
    }
    return imageList;
}

module.exports = function(message) {
    // load dictionary
    if (!loadDictionary){
        console.log("dictionary load failed.");
        //message.channel.send("ASL dictionary is unavailable at the moment.");
        return;
    }

    // send message to parser via UDP and listen for new messages
    // message.client.on("message", async (message) => {
    //     let parserOutput = await udp_sockets(message.content);
    // })

    let parserOutput = "hello";
    parserOutput.split(" ");

    let imageList = []; // clear
    imageList = createImageList(parserOutput, dictionary);
    console.log(imageList);

    //send messages
    let numImages = imageList.length;
    if (numImages > 0) {
        for (let i = 0; i < numImages; i++) {
            try {
                message.channel.send({ files: [`${imageList[i]}`] });
            } catch {
                console.error("images could not be found.")
            }    
        }
    }
};