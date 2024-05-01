import 'package:flutter/material.dart';

class Titulo extends StatelessWidget {
  final String titulo;
  final String local;
  final int likes;

  const Titulo({
    super.key,
    required this.titulo,
    required this.local,
    required this.likes,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(32),
      child: Row(
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  padding: const EdgeInsets.only(bottom: 12),
                  child: Text(
                    titulo,
                    style: const TextStyle(
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Text(
                  local,
                  style: TextStyle(
                    color: Colors.blue,
                  ),
                ),
              ],
            ),
          ),
          const Icon(
            Icons.star,
            color: Colors.green,
          ),
          Text('$likes'),
        ],
      ),
    );
  }
}
