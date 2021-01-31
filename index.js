// require dotenv package
const dotenv = require('dotenv');
dotenv.config();

// require discord.js module
const Discord = require('discord.js');

// create a new Discord client
const client = new Discord.Client();

// import command handler
const commandHandler = require('./commandHandler.js');

// login to Discord with app's token
client.login(process.env.TOKEN);

// when client is ready, run this code once
client.once('ready', () => {
    console.log('Ready 👍');
});

// parse messages for commands
client.on('message', commandHandler);

