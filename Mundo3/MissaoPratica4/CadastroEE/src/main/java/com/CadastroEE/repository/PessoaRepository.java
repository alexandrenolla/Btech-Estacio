package com.CadastroEE.repository;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import com.CadastroEE.model.Pessoa;

public interface PessoaRepository extends CrudRepository<Pessoa, Long> {
    List<Pessoa> findByNome(String nome);
   
}
