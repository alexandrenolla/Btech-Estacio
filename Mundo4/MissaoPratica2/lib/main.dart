import 'package:flutter/material.dart';
import 'views/inicio.dart'; 

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Missao Prática 2',
      theme: ThemeData(
        primarySwatch: Colors.grey,
      ),
      home: const Inicio(), 
    );
  }
}
// Main

























