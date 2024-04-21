import React from 'react';
import { View, Text } from 'react-native';

const Header = () => {
  return (
    <View style={{  display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <Text style={{ textAlign: 'center', fontFamily: 'Monospace', fontSize: 28, lineHeight: 30, color: 'black', fontWeight: 'bold' }}>Cadastro de Fornecedores</Text>
    </View>
  );
};

export default Header;
