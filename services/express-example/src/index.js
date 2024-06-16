import express from 'express';

const app = express();

app.get('/', (req, res) => {
  res.json({
    service: 'express-example',
    version: '0.1.0',
  });
});

// Start the server
app.listen(8000, () => {
  console.log('Server started on port 8000');
});
