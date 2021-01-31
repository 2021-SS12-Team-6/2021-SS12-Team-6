/*
  User can upload their own recordings of .gif or .jpeg to Discord from local storage
*/
// Extract the required classes from the discord.js module
const { Client, MessageAttachment } = require('discord.js');

// Import the native fs module
const fs = require('fs');

// Create an instance of a Discord client
const client = new Client();

/*
  The ready event is vital, it means that only _after_ this will your bot start reacting to information
  received from Discord
*/
client.on('ready', () => {
  console.log('I am ready!');
});

client.on('message', message => {
  // If the message is '!myASL'
  if (message.content === '!myASL') {
    // Get the buffer from the 'myASL.gif', assuming that the file exists
    const buffer = fs.readFileSync('./myASL.gif');
    // Create the attachment using MessageAttachment
    const attachment = new MessageAttachment(buffer, 'myASL.gif');
    // Send the attachment in the message channel with a content
    message.channel.send(`myASL`, attachment);
  }
});

// Log our bot in using the token from https://discord.com/developers/applications
client.login('UserToken');

/*
  Once uploaded, the .gif can be added to the 'favorite' collection for repetitive use
*/
