import 'package:flutter/material.dart';

class DestinosPage extends StatelessWidget {
  const DestinosPage({super.key});

  @override
  Widget build(BuildContext context) {
    Color bgAppBar = const Color(0xFF008584);
    Color bgBody = const Color(0xFFF5F5F5);

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Destinos',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: bgAppBar,
      ),
      body: Container(
        color: bgBody,
        child: ListView(
          padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 16),
          children: [
            _buildDestino(
              nome: 'Pântano dos Crocodilos',
              pais: 'Terra do nunca',
              descricao:
                  'Durante o amanhecer e o entardecer, o pântano se transforma em um cenário de beleza indescritível, quando os raios do sol se filtram através da névoa matinal ou pintam o céu de tons dourados ao se pôr.',
            ),
            _buildDestino(
              nome: 'Vale das Fadas',
              pais: 'Terra do nunca',
              descricao:
                  'O Vale das Fadas é um lugar encantado e mágico na Terra do Nunca, onde reside uma comunidade de seres mágicos e delicados conhecidos como fadas. Escondido em meio a uma vegetação exuberante e luminosa, o vale é um refúgio de beleza e tranquilidade.',
            ),
            _buildDestino(
              nome: 'Toca dos Meninos Perdidos',
              pais: 'Terra do nunca',
              descricao:
                  'Escondida em meio à exuberante vegetação da ilha, a Toca dos Meninos Perdidos é um refúgio seguro e acolhedor para aqueles que se recusam a crescer..',
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDestino(
      {required String nome, required String pais, required String descricao}) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            nome,
            style: const TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            'País: $pais',
            style: const TextStyle(
              fontStyle: FontStyle.italic,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            descricao,
            textAlign: TextAlign.justify,
          ),
        ],
      ),
    );
  }
}
