package com.CadastroServer.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.CadastroServer.model.Movimento;
import com.CadastroServer.service.MovimentoService;

import java.util.List;

@RestController
@RequestMapping("/movimentos")
public class MovimentoController {

    @Autowired
    private MovimentoService movimentoService;

    @GetMapping
    public List<Movimento> listarMovimentos() {
        return movimentoService.listarMovimentos();
    }

    @GetMapping("/{id}")
    public Movimento obterMovimento(@PathVariable Long id) {
        return movimentoService.obterMovimento(id);
    }

    @PostMapping
    public Movimento criarMovimento(@RequestBody Movimento movimento) {
        return movimentoService.criarMovimento(movimento);
    }

    @PutMapping("/{id}")
    public Movimento atualizarMovimento(@PathVariable Long id, @RequestBody Movimento movimento) {
        return movimentoService.atualizarMovimento(id, movimento);
    }

    @DeleteMapping("/{id}")
    public void deletarMovimento(@PathVariable Long id) {
        movimentoService.deletarMovimento(id);
    }

    public void atualizarQuantidade(int produtoId, int quantidade) {
    }

    public void create(Movimento movimento) {
    }
    
}
