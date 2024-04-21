import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import SQLite from 'react-native-sqlite-storage';

const cadastrar = ({ atualizarListaFornecedores }) => {
    const [fornecedor, setFornecedor] = useState({
        nome: '',
        endereco: '',
        contato: '',
        categorias: ''
    });

    const apagar = () => {
        setFornecedor({
            nome: '',
            endereco: '',
            contato: '',
            categorias: ''
        });
    };

    const salvar = () => {
        if (!fornecedor.nome || !fornecedor.endereco || !fornecedor.contato || !fornecedor.categorias) {
            alert("O preenchimento de todos os campos são obrigatórios!")
            return false;
        }

        const db = SQLite.openDatabase({ name: 'database.db' });

        db.transaction(tx => {
            tx.executeSql(
                'CREATE TABLE IF NOT EXISTS fornecedores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, endereco TEXT, contato TEXT, categorias TEXT)'
            );
        });

        db.transaction(tx => {
            tx.executeSql(
                'INSERT INTO fornecedores (nome, endereco, contato, categorias) VALUES (?, ?, ?, ?)',
                [fornecedor.nome, fornecedor.endereco, fornecedor.contato, fornecedor.categorias],
                (_, resultSet) => {
                    console.log('Cadastrado com sucesso.');
                    atualizarListaFornecedores();
                    apagar(); 
                },
                (_, error) => {
                    console.error('Erro ao cadastrar:', error);
                }
            );
        });
    };

    return (
        <View style={{ padding: 20 }}>
            <Text style={{ fontFamily: 'Monospace', fontSize: 14, color: 'white', paddingBottom: 10 }}>
                Nome</Text>
            <TextInput
                value={fornecedor.nome}
                onChangeText={text => setFornecedor({ ...fornecedor, nome: text })}
                style={{ backgroundColor: 'white', borderRadius: 5, color: 'green', borderWidth: 1, borderColor: 'blue', marginBottom: 10, padding: 5,  textDecorationLine: 'none' }}
            />

            <Text style={{ fontFamily: 'Monospace', fontSize: 14, color: 'white', paddingBottom: 10 }}>
                Endereço</Text>
            <TextInput
                value={fornecedor.endereco}
                onChangeText={text => setFornecedor({ ...fornecedor, endereco: text })}
                style={{ backgroundColor: 'white', borderRadius: 5, color: 'green', borderWidth: 1, borderColor: 'blue', marginBottom: 10, padding: 10,  textDecorationLine: 'none' }}
            />

            <Text style={{ fontFamily: 'Monospace', fontSize: 14, color: 'white', paddingBottom: 10 }}>
                Contato</Text>
            <TextInput
                value={fornecedor.contato}
                onChangeText={text => setFornecedor({ ...fornecedor, contato: text })}
                style={{ backgroundColor: 'white', borderRadius: 5, color: 'blue', borderWidth: 1, borderColor: 'blue', marginBottom: 20, padding: 10,  textDecorationLine: 'none' }}
            />

            <Text style={{ fontFamily: 'Monospace', fontSize: 14, color: 'white', paddingBottom: 10 }}>
                Categorias</Text>
            <TextInput
                value={fornecedor.categorias}
                onChangeText={text => setFornecedor({ ...fornecedor, categorias: text })}
                style={{ backgroundColor: 'white', borderRadius: 5, color: 'green', borderWidth: 1, borderColor: 'blue', marginBottom: 10, padding: 10,  textDecorationLine: 'none' }}
            />

            <Button
                title="Cadastrar" onPress={salvar} />
        </View>
    );
};

export default cadastrar;
