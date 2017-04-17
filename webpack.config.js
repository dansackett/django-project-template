var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  context: __dirname,

  entry: {
    js_bundle: './static/js/app.js',
    tachyons: 'tachyons/css/tachyons.css',
    styles_bundle: './static/css/app.css'
  },

  output: {
    path: __dirname + '/static/bundles/',
    publicPath: '/static/bundles/',
    filename: '[name]-[hash].js'
  },

  plugins: [
    new ExtractTextPlugin({
      filename: '[name]-[hash].css',
      disable: false,
      allChunks: true
    }),
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        options: {
          presets: [
            [ 'es2015', { modules: false } ]
          ]
        }
      },
      {
        test: /\.css$/,
        loader: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: 'css-loader'
        })
      },
    ],
  },

  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.css']
  },
}
