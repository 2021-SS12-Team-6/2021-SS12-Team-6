// Module used to handle sending UDP data using Javascript
// export const name = 'udp_socks_js';

// export function 

var udp = require('dgram');
var buffer = require('buffer'); // Used to read and write to buffers for UDP
var client = udp.createSocket('udp4'); // Creates UDP socket

var DATA_TO_SEND = "Hello, World! Please change me";
var data = Buffer.from(DATA_TO_SEND)

// Getting message
client.on("message", (message, info) => {
    console.log("Data recieved from server : " + message.toString());
    console.log('Received %d bytes from %s:%d\n',message.length, info.address, info.port);
});

// Sending message
client.send(data, 200, 'localhost', (e) => {
    if(e) {
        console.log("Fatal error detected!");
        client.close();
    } else {
        console.log("Message Sent!");
    }
})