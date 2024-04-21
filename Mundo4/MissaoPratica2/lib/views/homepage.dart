import 'package:flutter/material.dart';
import 'destino.dart';
import 'destinos.dart';
import 'pacotes.dart';
import 'contatos.dart';
import 'sobre.dart';
import 'dart:async';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _currentIndex = 0;
  final PageController _pageController = PageController();
  final List<Destino> _destinos = [
    Destino(
      imagePath: 'assets/images/pantano.jpeg',
      title: 'Pântano dos Crocodilos',
      location: 'Terra do nunca',
      bodyText: 'O Pântano dos Crocodilos é um lugar surpreendentemente fascinante na Terra do Nunca. Este ambiente único é um oásis de biodiversidade e mistério, onde a vida floresce em abundância. As águas escuras e tranquilas do pântano abrigam uma variedade de criaturas fascinantes, desde pequenos anfíbios coloridos até grandes crocodilos majestosos, que deslizam graciosamente pela superfície. As margens do pântano estão adornadas com uma profusão de plantas exóticas e flores silvestres, criando uma paisagem exuberante e vibrante. Durante o amanhecer e o entardecer, o pântano se transforma em um cenário de beleza indescritível, quando os raios do sol se filtram através da névoa matinal ou pintam o céu de tons dourados ao se pôr. Além de sua beleza natural, o Pântano dos Crocodilos também desempenha um papel importante na ecologia da Terra do Nunca, proporcionando um habitat vital para uma variedade de espécies e contribuindo para a riqueza ecológica da região. É um lugar que, embora possa inicialmente inspirar medo, revela-se como uma maravilha da natureza, cheia de vida e aventura.',
      likes: 333
    ),
    Destino(
      imagePath: 'assets/images/fadas.jpeg',
      title: 'Vale das Fadas',
      location: 'Terra do nunca',
      bodyText: 'O Vale das Fadas é um lugar encantado e mágico na Terra do Nunca, onde reside uma comunidade de seres mágicos e delicados conhecidos como fadas. Escondido em meio a uma vegetação exuberante e luminosa, o vale é um refúgio de beleza e tranquilidade. Aqui, as fadas vivem em harmonia com a natureza, entre flores coloridas e riachos cristalinos, criando um ambiente de pura magia e encantamento. O ar está impregnado com o brilho da poeira de fada, que dá vida às flores e concede poderes mágicos aos visitantes sortudos. No Vale das Fadas, os sons suaves das asas das fadas e o riso melodioso ecoam pelas copas das árvores, enquanto os raios de sol filtram-se através das folhas, criando um espetáculo de luz e cor. É um lugar onde a imaginação floresce livremente e os corações são preenchidos com alegria e admiração.',
      likes: 333
    ),
    Destino(
      imagePath: 'assets/images/toca.jpeg',
      title: 'Toca dos Meninos Perdidos',
      location: 'Terra do nunca',
      bodyText: 'A Toca dos Meninos Perdidos é um lugar especial na Terra do Nunca, central na história de Peter Pan. É o esconderijo secreto onde Peter Pan e os Meninos Perdidos vivem suas aventuras emocionantes. Escondida em meio à exuberante vegetação da ilha, a Toca dos Meninos Perdidos é um refúgio seguro e acolhedor para aqueles que se recusam a crescer. Construída com habilidade e imaginação, a toca é um labirinto de passagens secretas e salas escondidas, onde os meninos podem brincar, sonhar e ser livres. Aqui, sob a liderança de Peter Pan, os Meninos Perdidos formam uma família, compartilhando amizade e camaradagem enquanto exploram as maravilhas da Terra do Nunca. A Toca dos Meninos Perdidos é mais do que apenas um abrigo; é um símbolo de liberdade e aventura, onde o tempo parece parar e a juventude é eterna.',
      likes: 333
    ),
  ];

  @override
  void initState() {
    super.initState();
    Timer.periodic(const Duration(seconds: 5), (Timer timer) {
      if (_currentIndex < _destinos.length - 1) {
        _currentIndex++;
      } else {
        _currentIndex = 0;
      }
      _pageController.animateToPage(
        _currentIndex,
        duration: const Duration(milliseconds: 500),
        curve: Curves.easeIn,
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    Color bgAppBar = const Color(0xFF008584);
    Color bgBody = const Color(0xFFE0E0E0);

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Bem-vindo(a)',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: bgAppBar,
        actions: [
          IconButton(
            icon: const Icon(Icons.location_on),
            color: Colors.white,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const DestinosPage()),
              );
            },
          ),
          IconButton(
            icon: const Icon(Icons.card_travel),
            color: Colors.white,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const PacotesPage()),
              );
            },
          ),
          IconButton(
            icon: const Icon(Icons.contact_phone),
            color: Colors.white,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const ContatoPage()),
              );
            },
          ),
          IconButton(
            icon: const Icon(Icons.info),
            color: Colors.white,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const SobrePage()),
              );
            },
          ),
        ],
      ),
      body: Container(
        color: bgBody,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Padding(
              padding: EdgeInsets.all(45),
              child: Text(
                'Agência de Viagens dos Sonhos',
                style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            SizedBox(
              height: 300,
              child: GestureDetector(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => NextPage(
                      imagePath: _destinos[_currentIndex].imagePath,
                      title: _destinos[_currentIndex].title, 
                      location: _destinos[_currentIndex].location,
                      bodyText: _destinos[_currentIndex].bodyText, 
                      likes: _destinos[_currentIndex].likes
                    )),
                  );
                },
                child: PageView.builder(
                  controller: _pageController,
                  onPageChanged: (index) {
                    setState(() {
                      _currentIndex = index;
                    });
                  },
                  itemCount: _destinos.length,
                  itemBuilder: (context, index) {
                    return Image.asset(
                      _destinos[index].imagePath,
                      fit: BoxFit.cover,
                    );
                  },
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class Destino {
  final String imagePath;
  final String title;
  final String bodyText;
  final String location;
  final int likes;

  Destino({
    required this.imagePath,
    required this.title,
    required this.bodyText,
    required this.location,
    required this.likes
  });
}
