const prefix = "!";
const help = require('./commands/help.js');
const asl = require('./commands/asl.js');

const commands = { help, asl };

module.exports = function(message) {
    // command requires prefix and human author
    if (!message.content.startsWith(prefix) || message.author.bot) return;
    // extract command
    let command = message.content.split(" ").shift().substring(1).toLowerCase();

    if (command in commands) {
        commands[command](message);
    } else {
        help(message);
    }
};


