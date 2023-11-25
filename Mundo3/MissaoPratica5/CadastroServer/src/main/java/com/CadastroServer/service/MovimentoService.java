package com.CadastroServer.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.CadastroServer.model.Movimento;
import com.CadastroServer.repository.MovimentoRepository;

import java.util.List;

@Service
public class MovimentoService {

    @Autowired
    private MovimentoRepository movimentoRepository;

    public List<Movimento> listarMovimentos() {
        return movimentoRepository.findAll();
    }

    public Movimento obterMovimento(Long id) {
        return movimentoRepository.findById(id).orElse(null);
    }

    public Movimento criarMovimento(Movimento movimento) {
        return movimentoRepository.save(movimento);
    }

    public Movimento atualizarMovimento(Long id, Movimento movimento) {
        if (movimentoRepository.existsById(id)) {
            movimento.setId(id);
            return movimentoRepository.save(movimento);
        }
        return null;
    }

    public void deletarMovimento(Long id) {
        movimentoRepository.deleteById(id);
    }
}
