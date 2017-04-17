var isProd = (process.env.NODE_ENV === 'production');

if (process.env.NODE_ENV === 'production') {
  module.exports = require('./webpack/webpack.prod.config.js');
} else if (process.env.NODE_ENV === 'development') {
  module.exports = require('./webpack/webpack.dev.config.js');
} else if (process.env.NODE_ENV === 'watch') {
  module.exports = require('./webpack/webpack.watch.config.js');
}
