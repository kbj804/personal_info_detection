const config = require('../config');
const fs = require('fs');
const net = require('net');
const constants = require('./modules/constants');

const utils = require('../utils');

const SOCKET_PORT = config.SOCKET_PORT;

const socket = net.connect({ port: SOCKET_PORT, host: "183.111.96.29" });
socket.setEncoding('utf8');

let status = constants.STATUS.IDLE;
socket.on('connect', () => {
  console.log(`Connected to ${SOCKET_PORT}`);

  // COMMAND 1  
  const istream = fs.createReadStream("server/examples/test.txt");

  // let ostream = fs.createWriteStream("C:\\Users\\SHIN\\Desktop\\output.json");
  // ostream.write(utils.csvJSON(istream.toString()));

  let fileNameBuffer = Buffer.from(`{"command": 1, "param": {"fileType": 0, "addPath": "shin3372@inzent.com", "fileName": "20201202_test2.ua", "fileSize": 57}}\n`);
  socket.write(fileNameBuffer);

  socket.pipe(process.stdout);
  istream.on("readable", () => {
    let data;
    while (data = istream.read()) {
      console.log(data)
      if (status === constants.STATUS.ERROR) break;
      socket.write(data);
    }
  })

  istream.on("end", () => {
    socket.end();
  })

  // COMMAND 0
  // let fileNameBuffer = Buffer.from(`{"command": 0, "param": {}, "noData": true}\n`);
  // socket.write(fileNameBuffer);
});

const buf = []

socket.on('data', (chunk) => {
  const msg = JSON.stringify(JSON.parse(chunk));
  console.log(msg)

  status = msg.status;
  buf.push(chunk);
});

socket.on("end", () => {
  console.log("\nTransfer is done!");
})

socket.on("error", (err) => {
  console.log("Error", err);
});