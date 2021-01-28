const fs = require('fs');
const path = require('path')

module.exports = {
  getFilesizeInBytes(filename) {
    const stats = fs.statSync(filename);
    const fileSizeInBytes = stats.size;
    return fileSizeInBytes;
  },
  remove_linebreaks(str) {
    return str.replace(/[\r\n]+/gm, "");
  },
  makeid(length) {
    let result = '';
    let characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    let charactersLength = characters.length;

    for (let i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  },
  createDirectories(pathname, callback) {
    const __dirname = path.resolve();
    fs.mkdir(path.resolve(__dirname, pathname), { recursive: true }, e => {
      if (e) {
        console.error("ERROR", e);
      } else {
        callback();
      }
    });
  },
  writeDefaultPolicy(defaultPolicy, callback) {
    this.createDirectories(path.join(appRoot, config.POLICY_FILE_PATH), () => {
      let ostream = fs.createWriteStream(path.join(appRoot, config.POLICY_FILE_PATH, config.POLICY_FILE_NAME));
      ostream.write(defaultPolicy, callback);
    });
  },
  mapFilterEmpty(data, key) {
    return data.map(item => item[key]).filter(x => !(!x));
  },
  csvJSON(csv) {
    const lines = csv.split("\n");

    const result = [];

    const headers = lines[0].split(",");

    for (let i = 1; i < lines.length; i++) {

      const obj = {};
      const currentline = lines[i].split(",");

      for (let j = 0; j < headers.length; j++) {
        obj[headers[j]] = currentline[j];
      }

      result.push(obj);

    }

    return JSON.stringify(result);
  }
}