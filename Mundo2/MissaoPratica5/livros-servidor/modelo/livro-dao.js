const Livro = require('./livro-schema');

class LivroDAO {
  async obter() {
    return await Livro.find();
  }

  async incluir(livro) {
    return await Livro.create(livro);
  }

  async excluir(codigo) {
    return await Livro.deleteOne({ _id: codigo });
  }
}

const livroDAO = new LivroDAO();

module.exports = livroDAO;
  