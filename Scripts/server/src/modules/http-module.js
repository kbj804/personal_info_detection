const http = require("http");
const url = require('url');
const path = require("path");
const fs = require('fs');
const dayjs = require('dayjs')
const router = require('./router');

router.register(["POST"], '/writePolicyFile', (request, response) => {
  let requestBody = '';
  request.on('data', (data) => {
    requestBody += data;
  });

  request.on('end', () => {
    try {
      let ostream = fs.createWriteStream(path.join(appRoot, config.POLICY_FILE_PATH, 'policy.json'));
      ostream.write(requestBody);
      response.writeHead(200, { "Content-Type": "text/html" });
      response.end();
    } catch (err) {
      console.error(err)
      response.writeHead(400, { "Content-Type": "text/html" });
      response.end();
    }
  });
});

router.register(["GET"], '/getPolicyFile', (request, response) => {
  const defaultPolicy = JSON.stringify(config.DEFAULT_POLICY);

  function writeDefaultPolicy() {
    utils.writeDefaultPolicy(defaultPolicy, () => {
      response.writeHead(200, { "Content-Type": "application/json" });
      response.end(defaultPolicy);
    });
  }

  try {
    let data = fs.readFileSync(path.join(appRoot, config.POLICY_FILE_PATH, 'policy.json'));

    if (data.length > 0) {
      response.writeHead(200, { "Content-Type": "application/json" });
      response.end(data);
    } else {
      writeDefaultPolicy();
    }
  } catch {
    writeDefaultPolicy();
  }
});

router.register(["GET"], '/getStatistics', (request, response) => {
  const queryData = url.parse(request.url, true).query;

  let outputData = JSON.parse(fs.readFileSync(path.join(appRoot, config.POLICY_FILE_PATH, 'output.json')).toString());
  let logsData = JSON.parse(fs.readFileSync(path.join(appRoot, config.POLICY_FILE_PATH, 'logs.json')).toString());

  const result = {
    userList: [],
    chartData: {}
  }

  let userListResult = [...new Set([...utils.mapFilterEmpty(logsData, "user"), ...utils.mapFilterEmpty(outputData, "user")])]
  result.userList = userListResult

  result.userList.forEach(item => {
    result.chartData[item] = { abnormalDetectData: { leak: [], leakNormal: [], normal: [], normalLeak: [] }, actData: {}, dateActData: {} }
  });

  outputData.forEach(item => {
    if (!item.user || !item.error_min_max) return false;

    const policyData = JSON.parse(fs.readFileSync(path.join(appRoot, config.POLICY_FILE_PATH, 'policy.json')));
    const threshold = policyData.detection.threshold;

    let itemKey = "leak"
    let itemVal = +item.error_min_max;

    if (itemVal >= threshold.normalLeak) {
      itemKey = "normalLeak"
    }
    else if (itemVal >= threshold.normal) {
      itemKey = "normal"
    }
    else if (itemVal >= threshold.leakNormal) {
      itemKey = "leakNormal"
    }

    result.chartData[item.user].abnormalDetectData[itemKey].push({ x: dayjs(item.date, "YYYY-MM-DD HH:mm:ss").unix() * 1000, y: itemVal })
  });

  logsData.forEach(item => {
    if (!item.user || !item.activity || !item.time) return false;

    result.chartData[item.user].actData[item.activity] = result.chartData[item.user].actData[item.activity] ? result.chartData[item.user].actData[item.activity] + 1 : 1;


    if (!result.chartData[item.user].dateActData[item.activity]) result.chartData[item.user].dateActData[item.activity] = [];
    console.log(dayjs(item.time, "DD/MM/YYYY HH:mm:ss").format("YYYY MM DD HH mm ss"))
    result.chartData[item.user].dateActData[item.activity].push({ x: dayjs(item.time, "DD/MM/YYYY HH:mm:ss").unix() * 1000, y: 1 });
  });

  if (logsData.length > 0) {
    response.writeHead(200, { "Content-Type": "application/json" });
    response.end(JSON.stringify(result));
  }
});

module.exports = (config) => {
  http.createServer((request, response) => {
    const handler = router.route(request);
    handler.process(request, response);
  })
    .listen(config.WEB_PORT, () => {
      console.log(`HTTP server listening ${config.WEB_PORT}`)
    });
}