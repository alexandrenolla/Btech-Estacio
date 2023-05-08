const mongoose = require('mongoose');
const banco = mongoose.connection;

const LivroSchema = new mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId,
  titulo: { type: String, required: true },
  codEditora: { type: Number, required: true },
  resumo: { type: String, required: true },
  autores: { type: [String], required: true }
});

module.exports = banco.model('Livro', LivroSchema);
