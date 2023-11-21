package com.CadastroDB.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import com.CadastroDB.model.PessoaJuridica;
import com.CadastroDB.model.util.ConnectorBD;
import com.CadastroDB.model.util.SequenceManager;


@Repository
public class PessoaJuridicaDAO {

    private ConnectorBD conectorBD;
    private SequenceManager sequenceManager;

    public PessoaJuridicaDAO() {
        this.conectorBD = new ConnectorBD();
        this.sequenceManager = new SequenceManager();
    }

    public PessoaJuridica getPessoa(Long id) {
        String sql = "SELECT * FROM PessoaJuridica JOIN Pessoa ON PessoaJuridica.id = Pessoa.id WHERE PessoaJuridica.id = ?";
        try (Connection connection = conectorBD.getConnection();
             PreparedStatement statement = conectorBD.getPrepared(sql)) {
            statement.setLong(1, id);
            try (ResultSet resultSet = conectorBD.getSelect(statement)) {
                if (resultSet.next()) {
                    return extractPessoaJuridicaFromResultSet(resultSet);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public List<PessoaJuridica> getPessoas() {
        List<PessoaJuridica> pessoas = new ArrayList<>();
        String sql = "SELECT * FROM PessoaJuridica JOIN Pessoa ON PessoaJuridica.id = Pessoa.id";
        try (Connection connection = conectorBD.getConnection();
             PreparedStatement statement = conectorBD.getPrepared(sql);
             ResultSet resultSet = conectorBD.getSelect(statement)) {
            while (resultSet.next()) {
                pessoas.add(extractPessoaJuridicaFromResultSet(resultSet));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return pessoas;
    }

    public void incluir(PessoaJuridica pessoa) {
        String sqlPessoa = "INSERT INTO Pessoa (nome, logradouro, cidade, estado, telefone, email) " +
                "VALUES (?, ?, ?, ?, ?, ?)";
        String sqlPessoaJuridica = "INSERT INTO PessoaJuridica (idPessoa, cnpj) VALUES (last_insert_rowid(), ?)";
        try (Connection connection = conectorBD.getConnection();
             PreparedStatement stmtPessoa = conectorBD.getPrepared(sqlPessoa);
             PreparedStatement stmtPessoaJuridica = conectorBD.getPrepared(sqlPessoaJuridica)) {
    
            stmtPessoa.setString(1, pessoa.getNome());
            stmtPessoa.setString(2, pessoa.getLogradouro());
            stmtPessoa.setString(3, pessoa.getCidade());
            stmtPessoa.setString(4, pessoa.getEstado());
            stmtPessoa.setString(5, pessoa.getTelefone());
            stmtPessoa.setString(6, pessoa.getEmail());
    
            int affectedRows = stmtPessoa.executeUpdate();
    
            if (affectedRows == 0) {
                throw new SQLException("Falha ao inserir Pessoa, nenhuma linha afetada.");
            }
    
            // Obter o ID gerado para a Pessoa
            ResultSet generatedKeys = stmtPessoa.getGeneratedKeys();
            if (generatedKeys.next()) {
                long idPessoa = generatedKeys.getLong(1);
    
                // Inserir na tabela PessoaJuridica com o ID da Pessoa
                stmtPessoaJuridica.setLong(1, idPessoa);
                stmtPessoaJuridica.setString(1, pessoa.getCnpj());
                stmtPessoaJuridica.executeUpdate();
            } else {
                throw new SQLException("Falha ao obter o ID da Pessoa.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void alterar(PessoaJuridica pessoa) {
        String sqlPessoa = "UPDATE Pessoa SET nome=?, logradouro=?, cidade=?, estado=?, telefone=?, email=? WHERE id=?";
        String sqlPessoaJuridica = "UPDATE PessoaJuridica SET cnpj=? WHERE id=?";
        try (Connection connection = conectorBD.getConnection();
             PreparedStatement stmtPessoa = conectorBD.getPrepared(sqlPessoa);
             PreparedStatement stmtPessoaJuridica = conectorBD.getPrepared(sqlPessoaJuridica)) {
    
            stmtPessoa.setString(1, pessoa.getNome());
            stmtPessoa.setString(2, pessoa.getLogradouro());
            stmtPessoa.setString(3, pessoa.getCidade());
            stmtPessoa.setString(4, pessoa.getEstado());
            stmtPessoa.setString(5, pessoa.getTelefone());
            stmtPessoa.setString(6, pessoa.getEmail());
            stmtPessoa.setLong(7, pessoa.getId());
    
            stmtPessoaJuridica.setString(1, pessoa.getCnpj());
            stmtPessoaJuridica.setLong(2, pessoa.getId());
    
            stmtPessoa.executeUpdate();
            stmtPessoaJuridica.executeUpdate();
    
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }    

    public void excluir(Long id) {
        String sqlPessoa = "DELETE FROM Pessoa WHERE id=?";
        String sqlPessoaJuridica = "DELETE FROM PessoaJuridica WHERE id=?";
        try (Connection connection = conectorBD.getConnection();
             PreparedStatement stmtPessoa = conectorBD.getPrepared(sqlPessoa);
             PreparedStatement stmtPessoaJuridica = conectorBD.getPrepared(sqlPessoaJuridica)) {

            stmtPessoa.setLong(1, id);
            stmtPessoaJuridica.setLong(1, id);

            stmtPessoa.executeUpdate();
            stmtPessoaJuridica.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private PessoaJuridica extractPessoaJuridicaFromResultSet(ResultSet resultSet) throws SQLException {
        PessoaJuridica pessoa = new PessoaJuridica();
        pessoa.setId(resultSet.getLong("id"));
        pessoa.setNome(resultSet.getString("nome"));
        pessoa.setLogradouro(resultSet.getString("logradouro"));
        pessoa.setCidade(resultSet.getString("cidade"));
        pessoa.setEstado(resultSet.getString("estado"));
        pessoa.setTelefone(resultSet.getString("telefone"));
        pessoa.setEmail(resultSet.getString("email"));
        pessoa.setCnpj(resultSet.getString("cnpj"));
        return pessoa;
    }
}
