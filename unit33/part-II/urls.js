const fs = require("fs");
const axios = require("axios");

async function getPage(URL) {
  try {
    const resp = await axios.get(URL);
    return resp.data;
  } catch (e) {
    return;
  }
}

function writeFile(path, data) {
  fs.writeFile(path, data, { encoding: "utf8", flag: "a+" }, (err) => {
    if (err) {
      console.log("Error", err);
    }
    console.log(`Wrote to ${path}`);
  });
}

async function readFile(path) {
  fs.readFile(path, "utf8", async (err, data) => {
    if (err) {
      console.log(err);
    }

    const URLarray = data.split("\n");
    let HTMLs = await Promise.all(Array.from(URLarray, (url) => getPage(url)));

    for (let i = 0; i < URLarray.length; i++) {
      try {
        const url = new URL(URLarray[i]);
        const outputFile = url.hostname;
        writeFile(outputFile, HTMLs[i]);
      } catch (e) {
        console.log(`Cannot download ${URLarray[i]}`);
      }
    }
  });
}

const fileName = process.argv[2];
readFile(fileName);
