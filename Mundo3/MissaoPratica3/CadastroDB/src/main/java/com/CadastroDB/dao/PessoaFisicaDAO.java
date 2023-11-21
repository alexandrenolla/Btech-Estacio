package com.CadastroDB.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import com.CadastroDB.model.PessoaFisica;
import com.CadastroDB.model.util.ConnectorBD;
import com.CadastroDB.model.util.SequenceManager;

@Repository
public class PessoaFisicaDAO {

    private ConnectorBD conectorBD;
    private SequenceManager sequenceManager;

    public PessoaFisicaDAO() {
        this.conectorBD = new ConnectorBD();
        this.sequenceManager = new SequenceManager();
    }

    public PessoaFisica getPessoa(Long id) {
        String sql = "SELECT * FROM PessoaFisica JOIN Pessoa ON PessoaFisica.id = Pessoa.id WHERE PessoaFisica.id = ?";
        try (Connection connection = conectorBD.getConnection();
             PreparedStatement statement = conectorBD.getPrepared(sql)) {
            statement.setLong(1, id);
            try (ResultSet resultSet = conectorBD.getSelect(statement)) {
                if (resultSet.next()) {
                    return extractPessoaFisicaFromResultSet(resultSet);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }    

    public List<PessoaFisica> getPessoas() {

        List<PessoaFisica> pessoas = new ArrayList<>();
        String sql = "SELECT * FROM PessoaFisica JOIN Pessoa ON PessoaFisica.id = Pessoa.id";
        try (Connection connection = conectorBD.getConnection();
                PreparedStatement statement = conectorBD.getPrepared(sql);
                ResultSet resultSet = conectorBD.getSelect(statement)) {
            while (resultSet.next()) {
                pessoas.add(extractPessoaFisicaFromResultSet(resultSet));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return pessoas;  
    }    

    public void incluir(PessoaFisica pessoa) {
        String sqlPessoa = "INSERT INTO Pessoa (nome, logradouro, cidade, estado, telefone, email) " +
            "VALUES (?, ?, ?, ?, ?, ?)";
        String sqlPessoaFisica = "INSERT INTO PessoaFisica (id, cpf) VALUES (?, ?)";
        try (Connection connection = conectorBD.getConnection();
            PreparedStatement stmtPessoa = conectorBD.getPrepared(sqlPessoa);
            PreparedStatement stmtPessoaFisica = conectorBD.getPrepared(sqlPessoaFisica)) {

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

            // Obtendo o ID gerado
            try (ResultSet generatedKeys = stmtPessoa.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    Long id = generatedKeys.getLong(1);
                    stmtPessoaFisica.setLong(1, id);
                    stmtPessoaFisica.setString(2, pessoa.getCpf());
                    stmtPessoaFisica.executeUpdate();
                } else {
                    throw new SQLException("Falha ao obter o ID da Pessoa, nenhum ID obtido.");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void alterar(PessoaFisica pessoa) {
        String sqlPessoa = "UPDATE Pessoa SET nome=?, logradouro=?, cidade=?, estado=?, telefone=?, email=? WHERE id=?";
        String sqlPessoaFisica = "UPDATE PessoaFisica SET cpf=? WHERE id=?";
        try (Connection connection = conectorBD.getConnection();
             PreparedStatement stmtPessoa = conectorBD.getPrepared(sqlPessoa);
             PreparedStatement stmtPessoaFisica = conectorBD.getPrepared(sqlPessoaFisica)) {

            stmtPessoa.setString(1, pessoa.getNome());
            stmtPessoa.setString(2, pessoa.getLogradouro());
            stmtPessoa.setString(3, pessoa.getCidade());
            stmtPessoa.setString(4, pessoa.getEstado());
            stmtPessoa.setString(5, pessoa.getTelefone());
            stmtPessoa.setString(6, pessoa.getEmail());
            stmtPessoa.setLong(7, pessoa.getId());

            stmtPessoaFisica.setString(1, pessoa.getCpf());
            stmtPessoaFisica.setLong(2, pessoa.getId());

            stmtPessoa.executeUpdate();
            stmtPessoaFisica.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void excluir(Long id) {
        String sqlPessoa = "DELETE FROM Pessoa WHERE id=?";
        String sqlPessoaFisica = "DELETE FROM PessoaFisica WHERE id=?";
        try (Connection connection = conectorBD.getConnection();
             PreparedStatement stmtPessoa = conectorBD.getPrepared(sqlPessoa);
             PreparedStatement stmtPessoaFisica = conectorBD.getPrepared(sqlPessoaFisica)) {

            stmtPessoa.setLong(1, id);
            stmtPessoaFisica.setLong(1, id);

            stmtPessoa.executeUpdate();
            stmtPessoaFisica.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private PessoaFisica extractPessoaFisicaFromResultSet(ResultSet resultSet) throws SQLException {
        PessoaFisica pessoa = new PessoaFisica();
        pessoa.setId(resultSet.getLong("id"));
        pessoa.setNome(resultSet.getString("nome"));
        pessoa.setLogradouro(resultSet.getString("logradouro"));
        pessoa.setCidade(resultSet.getString("cidade"));
        pessoa.setEstado(resultSet.getString("estado"));
        pessoa.setTelefone(resultSet.getString("telefone"));
        pessoa.setEmail(resultSet.getString("email"));
        pessoa.setCpf(resultSet.getString("cpf"));
        return pessoa;
    }
}
