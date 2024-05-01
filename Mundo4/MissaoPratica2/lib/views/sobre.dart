import 'package:flutter/material.dart';

class SobrePage extends StatelessWidget {
  const SobrePage({super.key});

  @override
  Widget build(BuildContext context) {
  Color bgAppBar = Color.fromARGB(144, 0, 255, 68);
    Color bgBody = const Color(0xFF33CE);

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Terra do Nunca Viagens',
          style: TextStyle(color: Colors.black),
        ),
        backgroundColor: bgAppBar,
      ),
      body: Container(
        color: bgBody,
        child: const Center(
          child: Padding(
            padding: EdgeInsets.all(20.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              children: <Widget>[
                Padding(
                  padding: EdgeInsets.symmetric(vertical: 10.0),
                  child: Text(
                    'Bem-vindo à Terra do Nunca Viagens',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.symmetric(vertical: 10.0),
                  child: Text(
                    'Em Terra do Nunca Viagens, acreditamos que a jornada é tão importante quanto o destino. Assim como Peter Pan, nós nos recusamos a crescer completamente, mantendo viva a chama da imaginação e da curiosidade. Nossos destinos são cuidadosamente selecionados para despertar o espírito de aventura em todos os viajantes, sejam eles jovens ou jovens de coração.',
                    textAlign: TextAlign.left,
                    
                  ),
                ),
                Padding(
                  padding: EdgeInsets.symmetric(vertical: 10.0),
                  child: Text(
                    'Nossa equipe é composta por entusiastas de viagens que compartilham uma paixão pela descoberta e pela exploração. Estamos aqui para transformar seus sonhos de viagem em realidade, criando itinerários personalizados que o transportarão para além dos limites da realidade cotidiana.',
                    textAlign: TextAlign.left,
                  ),
                ),
                Padding(
                  padding: EdgeInsets.symmetric(vertical: 10.0),
                  child: Text(
                    'Se você está pronto para embarcar em uma jornada mágica pelo mundo, junte-se a nós em Terra do Nunca Viagens. Deixe-nos ajudá-lo a descobrir novos horizontes, a criar memórias que durarão para sempre e a manter viva a chama da aventura em seu coração. Juntos, vamos voar para longe, rumo ao desconhecido, onde o impossível se torna possível e o tempo não tem poder sobre nós. Venha conosco e embarque na viagem de uma vida!',
                    textAlign: TextAlign.left
                  ),
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}