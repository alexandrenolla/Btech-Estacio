import 'package:flutter/material.dart';

class DestinosPage extends StatelessWidget {
  const DestinosPage({super.key});

  @override
  Widget build(BuildContext context) {
    Color bgAppBar = Color.fromARGB(144, 0, 255, 68);
    Color bgBody = const Color(0xFFE0E0E0);

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Destinos',
          style: TextStyle(color: Colors.black),
        ),
        backgroundColor: bgAppBar,
      ),
      body: Container(
        color: bgBody,
        padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 16),
        child: ListView(
          children: [
            _buildContainer(
              child: _buildDestino(
                nome: 'Pântano dos Crocodilos',
                pais: 'País: Terra do nunca',
                descricao:
                    'Durante o amanhecer e o entardecer, o pântano se transforma em um cenário de beleza indescritível, quando os raios do sol se filtram através da névoa matinal ou pintam o céu de tons dourados ao se pôr.',
              ),
            ),
            _buildContainer(
              child: _buildDestino(
                nome: 'Vale das Fadas',
                pais: 'País: Terra do nunca',
                descricao:
                    'O Vale das Fadas é um lugar encantado e mágico na Terra do Nunca, onde reside uma comunidade de seres mágicos e delicados conhecidos como fadas. Escondido em meio a uma vegetação exuberante e luminosa, o vale é um refúgio de beleza e tranquilidade.',
              ),
            ),
            _buildContainer(
              child: _buildDestino(
                nome: 'Toca dos Meninos Perdidos',
                pais: 'País: Terra do nunca',
                descricao:
                    'Escondida em meio à exuberante vegetação da ilha, a Toca dos Meninos Perdidos é um refúgio seguro e acolhedor para aqueles que se recusam a crescer..',
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildContainer({required Widget child}) {
    return Container(
      width: 400,
      margin: const EdgeInsets.only(bottom: 20),
      padding: const EdgeInsets.all(40),
      decoration: BoxDecoration(
        color: Color.fromARGB(184, 88, 88, 90),
        borderRadius: BorderRadius.circular(3),
      ),
      child: child,
    );
  }

  Widget _buildDestino({
    required String nome,
    required String pais,
    required String descricao,
  }) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          nome,
          style: const TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: Colors.white,
          ),
        ),
        const SizedBox(height: 5),
        Text(
          pais,
          style: const TextStyle(
            fontSize: 16,
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
      ],
    );
  }
}