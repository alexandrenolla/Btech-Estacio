import React from 'react';
import { View, Text } from 'react-native';

const Header = () => {
  return (
    <View style={{  display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <Text style={{ textAlign: 'center', fontFamily: 'Monospace', fontSize: 14, lineHeight: 30, color: 'white', fontWeight: 'semibold' }}>Cadastro de Fornecedores</Text>
    </View>
  );
};

export default Header;
