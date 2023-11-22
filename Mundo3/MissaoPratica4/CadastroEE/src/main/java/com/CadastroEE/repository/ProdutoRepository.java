package com.CadastroEE.repository;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.CadastroEE.model.Produto;

public interface ProdutoRepository extends CrudRepository<Produto, Long> {
    List<Produto> findByNome(String nome);
    // Nenhum método adicional necessário no momento
}
