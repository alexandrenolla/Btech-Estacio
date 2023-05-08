const express = require('express');
const { json } = require('express');
const router = express.Router();
const LivroDAO = require('../modelo/livro-dao');

router.get('/', async (req, res) => {
    try {
        const livros = await LivroDAO.obter();
        res.json(livros);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Erro ao obter livros.' });
    }
});

router.post('/', json(), async (req, res) => {
    const livro = req.body;
    const resultado = await LivroDAO.incluir(livro);
    if (resultado.inseridos > 0) {
        res.status(201).json({ mensagem: 'Livro incluído com sucesso!' });
    } else {
        res.status(400).json({ mensagem: 'Não foi possível incluir o livro.' });
    }
});

router.delete('/:id', async (req, res) => {
    try {
        const { id } = req.params;
        await LivroDAO.excluir(id);
        res.json({ message: 'Livro excluído com sucesso!' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Erro ao excluir livro.' });
    }
});

module.exports = router;
