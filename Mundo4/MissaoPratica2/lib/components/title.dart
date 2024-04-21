import 'package:flutter/material.dart';

class TitleSection extends StatelessWidget {
  final String title;
  final String location;
  final int likes;

  const TitleSection({
    super.key,
    required this.title,
    required this.location,
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
                    title,
                    style: const TextStyle(
                      fontWeight: FontWeight.light,
                    ),
                  ),
                ),
                Text(
                  location,
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
