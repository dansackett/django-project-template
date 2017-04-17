var config = require('./webpack.base.config.js');
var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin');

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats.json'}),
])

config.module.rules = config.module.rules.concat([
  {
    test: /\.css$/,
    loader: ExtractTextPlugin.extract({
      fallback: 'style-loader',
      use: 'css-loader'
    })
  }
]);

module.exports = config;
