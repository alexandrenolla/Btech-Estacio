import 'package:flutter/material.dart';
import '../components/button.dart';
import '../components/title.dart';

class NextPage extends StatelessWidget {
  final String imagePath;
  final String title;
  final String location;
  final String bodyText;
  final int likes;

  const NextPage({
    required this.imagePath,
    required this.title,
    required this.location,
    required this.bodyText,
    required this.likes,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Color bgAppBar = const Color(0xFF008584); 
    Color bgBody = const Color(0xFFF5F5F5); 

    return Scaffold(
      appBar: AppBar(
        backgroundColor: bgAppBar,
        title: const Text(
          'Viagem escolhida',
          style: TextStyle(color: Colors.white),
        ),
      ),
      body: Container(
        color: bgBody,
        child: Column(
          children: [
            Image.asset(imagePath),
            TitleSection(title: title, location: location, likes: likes),
            ButtonSection(),
            const SizedBox(height: 20),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 30),
              child: Text(
                bodyText,
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