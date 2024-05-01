import 'package:flutter/material.dart';

class ContatoPage extends StatelessWidget {
  const ContatoPage({super.key});

  @override
  Widget build(BuildContext context) {
    Color bgAppBar = Color.fromARGB(144, 0, 255, 68);
    Color bgBody = const Color(0xFFF5F5F5);
    Color textColor = const Color.fromRGBO(0, 0, 0, 1);

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Contato do Peter Pan',
          style: TextStyle(color: Colors.black),
        ),
        backgroundColor: bgAppBar,
      ),
      body: Container(
        color: bgBody,
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Icon(Icons.telegram),
                    SizedBox(width: 10),
                    Text(
                      '+55 (21) 99333-9222',
                      style: TextStyle(
                        color: textColor,
                        fontSize: 16,
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Icon(Icons.email),
                    SizedBox(width: 10),
                    Text(
                      'terradonuncaviagens@email.com',
                      style: TextStyle(
                        color: textColor,
                        fontSize: 16,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
