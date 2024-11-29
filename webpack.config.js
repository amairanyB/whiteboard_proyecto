const path = require('path');

module.exports = {
  entry: './whiteboardmanager/frontend/src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'whiteboardmanager/frontend/static/frontend')
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  }
};

