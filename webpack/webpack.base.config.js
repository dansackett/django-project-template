var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var CleanWebpackPlugin = require('clean-webpack-plugin');

PATHS = {
  root: path.resolve(__dirname, '../'),
  static: path.resolve(__dirname, '../static'),
  build: path.resolve(__dirname, '../static/bundles'),
};

module.exports = {
  context: __dirname,

  entry: {
    app: path.resolve(PATHS.static, 'js/app.js')
  },

  output: {
    path: PATHS.build,
    publicPath: '/static/bundles/',
    filename: '[name]-[hash].js'
  },

  plugins: [
    new ExtractTextPlugin({
      filename: '[name]-[hash].css',
      disable: false,
      allChunks: true
    }),

    new CleanWebpackPlugin(PATHS.build, {
      root: PATHS.root
    })
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
      }
    ],
  },

  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.css']
  },
}
