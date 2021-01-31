const prefix = "!";
const help = require('./commands/help.js');
const ASL = require('./commands/ASL.js');

const commands = { help, ASL };

module.exports = function(message) {
    // command requires prefix and human author
    if (!message.content.startsWith(prefix) || message.author.bot) return;
    // extract command
    let command = message.content.split(" ").shift().substring(1);
    commands[command](message);
};


