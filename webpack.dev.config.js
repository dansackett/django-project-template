var config = require('./webpack.config.js');
var BundleTracker = require('webpack-bundle-tracker')
var BrowserSyncPlugin = require('browser-sync-webpack-plugin');

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats.json'}),

  new BrowserSyncPlugin({
      host: 'localhost',
      port: 3000,
      proxy: 'http://localhost:8000/',
      notify: false
    },
    {
      // prevent BrowserSync from reloading the page
      // and let Webpack Dev Server take care of this
      reload: false
    }
  )
])

config.output.publicPath = 'http://0.0.0.0:45537/static/bundles/';

module.exports = config;
