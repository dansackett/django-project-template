var webpack = require('webpack');
var config = require('./webpack.base.config.js');
var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var autoprefixer = require('autoprefixer');
var cssnano = require('cssnano');

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats-prod.json'}),

  new webpack.DefinePlugin({
    'process.env': {
      'NODE_ENV': JSON.stringify('production')
  }}),

  new webpack.optimize.UglifyJsPlugin({
    compressor: {
      warnings: false
    }
  })
]);

config.module.rules = config.module.rules.concat([
  {
    test: /\.css$/,
    loader: ExtractTextPlugin.extract({
      fallback: 'style-loader',
      loader: [
        { loader: 'css-loader' },
        {
          loader: 'postcss-loader',
          options: {
            plugins: [autoprefixer, cssnano]
          }
        }
      ]
    })
  }
]);

module.exports = config;
