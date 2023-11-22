package com.CadastroEE.repository;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import com.CadastroEE.model.Usuario;

public interface UsuarioRepository extends CrudRepository<Usuario, Long> {
    Usuario findByNome(String nome);
    // Nenhum método adicional necessário no momento
}
