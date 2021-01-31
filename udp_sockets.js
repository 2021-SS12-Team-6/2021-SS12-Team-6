async function sendRetrieveUDP(msg) {
    const PORT_NUMBER = 200;
    const HOST = 'localhost';
    var udp = require('dgram');
    var buffer = require('buffer'); // Used to read and write to buffers for UDP
    var client = udp.createSocket('udp4'); // Creates UDP4 socket

    var data = buffer.from(msg); // Converts msg into byte buffer

    // When retrieving messages
    client.on("message", (message, info) => {
        console.log("Data recieved from server : " + message.toString());
        console.log('Received %d bytes from %s:%d\n',message.length, info.address, info.port);
        return message.toString();
    });

    // Sending message
    client.send(data, PORT_NUMBER, HOST, (e) => {
        if(e) {
            console.log("Fatal error detected!");
            client.close();
        } else {
            console.log("Message Sent!");
        }
    })
}