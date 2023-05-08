const mongoose = require('mongoose');

const banco = mongoose.connect('mongodb://localhost:27017/Livraria', {
  useUnifiedTopology: true,
  useNewUrlParser: true
});

module.exports = banco;

