import 'package:flutter/material.dart';

class PacotesPage extends StatelessWidget {
  const PacotesPage({super.key});

  @override
  Widget build(BuildContext context) {
  Color bgAppBar = Color.fromARGB(144, 0, 255, 68);
  Color bgBody = const Color(0xFFE0E0E0); 

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Pacotes de Viagem',
          style: TextStyle(color: Colors.black),
        ),
        backgroundColor: bgAppBar,
      ),
      body: Container(
        color: bgBody, 
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 10),
            _buildPacote(
              tipo: 'Pacote Capitão Gancho',
              descricao: 'Pântano dos Crocodilos para 10 noites.',
              preco: 'R\$ 10.000,00',
            ),
            _buildPacote(
              tipo: 'Pacote Sininho',
              descricao: 'Vale das Fadas com poeira de fada para 10 noites.',
              preco: 'R\$ 20.000,00',
            ),
            _buildPacote(
              tipo: 'Pacote Peter Pan',
              descricao: 'Toca dos Meninos Perdidos para 5 noites',
              preco: 'R\$ 30.000,00',
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildPacote({required String tipo, required String descricao, required String preco}) {
    return Container(
      width: 400,
      margin: const EdgeInsets.only(bottom: 20),
      padding: const EdgeInsets.all(40),
      decoration: BoxDecoration(
        color: Color.fromARGB(184, 88, 88, 90),
        borderRadius: BorderRadius.circular(3),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            tipo,
            style: const TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 5),
          Text(
            descricao,
            style: const TextStyle(
              fontSize: 12,
               color: Colors.white,
            ),
          ),
          const SizedBox(height: 5),
          Text(
            'Preço: $preco',
            style: const TextStyle(
              fontSize: 12,
              fontWeight: FontWeight.bold,
              color: Colors.black
            ),
          ),
        ],
      ),
    );
  }
}