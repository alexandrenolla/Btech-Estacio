import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, ScrollView } from 'react-native';
import SQLite from 'react-native-sqlite-storage';

const ListaFornecedores = () => {
    const [fornecedores, setFornecedores] = useState([]);

    useEffect(() => {
        const db = SQLite.openDatabase({ name: 'database.db' });

        db.transaction(tx => {
            tx.executeSql(
                'SELECT * FROM fornecedores',
                [],
                (_, { rows }) => {
                    const result = [];
                    for (let i = 0; i < rows.length; i++) {
                        result.push(rows.item(i));
                    }
                    setFornecedores(result);
                },
                (_, error) => {
                    console.error('Erro ao buscar fornecedores:', error);
                }
            );
        });
    }, []);

    return (
        <View style={{  flex: 1, padding: 40 }}>
            <Text style={{ fontFamily: 'Monospace', fontSize: 28, color: 'black', paddingBottom: 10, textAlign: 'center'}}>
                Fornecedores</Text>
            <FlatList
                data={fornecedores}
                renderItem={({ item }) => (
                    <View style={{ marginBottom: 10, backgroundColor: 'black', padding: 5 }}>
                        <Text style={{ fontFamily: 'Monospace', fontSize: 14, color: 'white' }}>Nome: {item.nome}</Text>
                        <Text style={{ fontFamily: 'Monospace', fontSize: 14, color: 'white' }}>Endereço: {item.endereco}</Text>
                        <Text style={{ fontFamily: 'Monospace', fontSize: 14, color: 'white' }}>Contato: {item.contato}</Text>
                        <Text style={{ fontFamily: 'RobMonospaceoto', fontSize: 14, color: 'white' }}>Categorias: {item.categorias}</Text>
                    </View>
                )}
                keyExtractor={item => item.id.toString()}
            />
        </View>
    );
};

export default ListaFornecedores;
