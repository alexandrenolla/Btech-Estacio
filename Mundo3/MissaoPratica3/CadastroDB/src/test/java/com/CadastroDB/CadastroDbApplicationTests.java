package com.CadastroDB;

import com.CadastroDB.dao.PessoaFisicaDAO;
import com.CadastroDB.dao.PessoaJuridicaDAO;
import com.CadastroDB.model.PessoaFisica;
import com.CadastroDB.model.PessoaJuridica;

public class CadastroDbApplicationTests {

    public static void main(String[] args) {
        // Operações com Pessoa Física
        testPessoaFisicaOperations();

        // // Operações com Pessoa Jurídica
        testPessoaJuridicaOperations();

    }

    private static void testPessoaFisicaOperations() {
        PessoaFisicaDAO pessoaFisicaDAO = new PessoaFisicaDAO();
    
        // a. Instanciar uma pessoa física e persistir no banco de dados.
        PessoaFisica pessoaFisica = new PessoaFisica();
        pessoaFisica.setNome("Joao");
        pessoaFisica.setLogradouro("Rua 11, Centro");
        pessoaFisica.setCidade("Riacho do Sul");
        pessoaFisica.setEstado("PA");
        pessoaFisica.setTelefone("1111-111");
        pessoaFisica.setEmail("joao@riacho.com");
        pessoaFisica.setCpf("11111111111");
        pessoaFisicaDAO.incluir(pessoaFisica);
    
        // Verifica se a pessoa foi corretamente persistida antes de tentar alterar/excluir
        if (pessoaFisica.getId() != null) {
            // b. Alterar os dados da pessoa física no banco.
            pessoaFisica.setNome("Novo Nome");
            pessoaFisicaDAO.alterar(pessoaFisica);
    
            // c. Consultar todas as pessoas físicas do banco de dados e listar no console.
            System.out.println("Pessoas Físicas no Banco:");
            pessoaFisicaDAO.getPessoas().forEach(System.out::println);
    
            // d. Excluir a pessoa física criada anteriormente no banco.
            pessoaFisicaDAO.excluir(pessoaFisica.getId());
        } else {
            System.out.println("Falha ao persistir Pessoa Física no banco.");
        }
    }
    
    private static void testPessoaJuridicaOperations() {
        PessoaJuridicaDAO pessoaJuridicaDAO = new PessoaJuridicaDAO();
    
        // e. Instanciar uma pessoa jurídica e persistir no banco de dados.
        PessoaJuridica pessoaJuridica = new PessoaJuridica();
        pessoaJuridica.setNome("JJC");
        pessoaJuridica.setLogradouro("Rua 11, Centro");
        pessoaJuridica.setCidade("Riacho do Sul");
        pessoaJuridica.setEstado("PA");
        pessoaJuridica.setTelefone("1212-1212");
        pessoaJuridica.setEmail("jjc@riacho.com");
        pessoaJuridica.setCnpj("11111111111111");
        pessoaJuridicaDAO.incluir(pessoaJuridica);
    
        // Verifica se a pessoa foi corretamente persistida antes de tentar alterar/excluir
        if (pessoaJuridica.getId() != null) {
            // f. Alterar os dados da pessoa jurídica no banco.
            pessoaJuridica.setNome("Novo Nome Jurídico");
            pessoaJuridicaDAO.alterar(pessoaJuridica);
    
            // g. Consultar todas as pessoas jurídicas do banco e listar no console.
            System.out.println("Pessoas Jurídicas no Banco:");
            pessoaJuridicaDAO.getPessoas().forEach(System.out::println);
    
            // h. Excluir a pessoa jurídica criada anteriormente no banco.
            pessoaJuridicaDAO.excluir(pessoaJuridica.getId());
        } else {
            System.out.println("Falha ao persistir Pessoa Jurídica no banco.");
        }
    }
    
}
