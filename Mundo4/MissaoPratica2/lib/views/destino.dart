import 'package:flutter/material.dart';
import '../components/containerBotoes.dart';
import '../components/titulo.dart';

class NextPage extends StatelessWidget {
  final String jpeg;
  final String titulo;
  final String local;
  final String texto;
  final int likes;

  const NextPage({
    required this.jpeg,
    required this.titulo,
    required this.local,
    required this.likes,
    required this.texto,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
  Color bgAppBar = Color.fromARGB(144, 0, 255, 68);
    Color bgBody = const Color(0xFFF5F5F5); 

    return Scaffold(
      appBar: AppBar(
        backgroundColor: bgAppBar,
        title: const Text(
          'Viagem escolhida',
          style: TextStyle(color: Colors.black),
        ),
      ),
      body: Container(
        color: bgBody,
        child: Column(
          children: [
            Image.asset(jpeg),
            Titulo(titulo: titulo, local: local, likes: likes),
            ContainerBotoes(),
            const SizedBox(height: 20),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 30),
              child: Text(
                texto,
                textAlign: TextAlign.justify,
                style: const TextStyle(fontSize: 14),
              ),
            ),
          ],
        ),
      ),
    );
  }
}