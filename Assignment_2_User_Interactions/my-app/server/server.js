const express = require('express');
const { spawn } = require('child_process');

const app = express();
const PORT = 3001;

app.get('/get-metrics', (req, res) => {
  const pythonProcess = spawn('python', ['metrics.py']);

  let metricsData = '';

  pythonProcess.stdout.on('data', (data) => {
    metricsData += data.toString();
  });

  pythonProcess.on('close', () => {
    res.send(metricsData);
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});