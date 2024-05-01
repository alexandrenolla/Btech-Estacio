import 'package:flutter/material.dart';
import 'destino.dart';
import 'destinos.dart';
import 'pacotes.dart';
import 'contatos.dart';
import 'sobre.dart';
import 'dart:async';

class Inicio extends StatefulWidget {
  const Inicio({Key? key}) : super(key: key);

  @override
  _InicioState createState() => _InicioState();
}

class _InicioState extends State<Inicio> {
  int _currentIndex = 0;
  final PageController _pageController = PageController();
  final List<Destino> _destinos = [
    Destino(
        jpeg: 'assets/images/pantano.jpeg',
        titulo: 'Pântano dos Crocodilos',
        local: 'Terra do nunca',
        texto:
            'O Pântano dos Crocodilos é um lugar surpreendentemente fascinante na Terra do Nunca. Este ambiente único é um oásis de biodiversidade e mistério, onde a vida floresce em abundância. As águas escuras e tranquilas do pântano abrigam uma variedade de criaturas fascinantes, desde pequenos anfíbios coloridos até grandes crocodilos majestosos, que deslizam graciosamente pela superfície. As margens do pântano estão adornadas com uma profusão de plantas exóticas e flores silvestres, criando uma paisagem exuberante e vibrante. Durante o amanhecer e o entardecer, o pântano se transforma em um cenário de beleza indescritível, quando os raios do sol se filtram através da névoa matinal ou pintam o céu de tons dourados ao se pôr..',
        likes: 333),
    Destino(
        jpeg: 'assets/images/fadas.jpeg',
        titulo: 'Vale das Fadas',
        local: 'Terra do nunca',
        texto:
            'O Vale das Fadas é um lugar encantado e mágico na Terra do Nunca, onde reside uma comunidade de seres mágicos e delicados conhecidos como fadas. Escondido em meio a uma vegetação exuberante e luminosa, o vale é um refúgio de beleza e tranquilidade. Aqui, as fadas vivem em harmonia com a natureza, entre flores coloridas e riachos cristalinos, criando um ambiente de pura magia e encantamento. O ar está impregnado com o brilho da poeira de fada, que dá vida às flores e concede poderes mágicos aos visitantes sortudos.',
        likes: 333),
    Destino(
        jpeg: 'assets/images/toca.jpeg',
        titulo: 'Toca dos Meninos Perdidos',
        local: 'Terra do nunca',
        texto:
            'A Toca dos Meninos Perdidos é um lugar especial na Terra do Nunca, central na história de Peter Pan. É o esconderijo secreto onde Peter Pan e os Meninos Perdidos vivem suas aventuras emocionantes. Escondida em meio à exuberante vegetação da ilha, a Toca dos Meninos Perdidos é um refúgio seguro e acolhedor para aqueles que se recusam a crescer. Construída com habilidade e imaginação, a toca é um labirinto de passagens secretas e salas escondidas, onde os meninos podem brincar, sonhar e ser livres. Aqui, sob a liderança de Peter Pan, os Meninos Perdidos formam uma família, compartilhando amizade e camaradagem enquanto exploram as maravilhas da Terra do Nunca. A Toca dos Meninos Perdidos é mais do que apenas um abrigo; é um símbolo de liberdade e aventura, onde o tempo parece parar e a juventude é eterna.',
        likes: 333),
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
    Color bgAppBar = Color.fromARGB(144, 0, 255, 68);
    Color bgBody = const Color(0xFFE0E0E0);

    return Scaffold(
      appBar: AppBar(
        backgroundColor: bgAppBar,
        actions: [
          IconButton(
            icon: const Icon(Icons.description_rounded),
            color: Colors.black,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const SobrePage()),
              );
            },
          ),
          IconButton(
            icon: const Icon(Icons.airplane_ticket_rounded),
            color: Colors.black,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const PacotesPage()),
              );
            },
          ),
          IconButton(
            icon: const Icon(Icons.airplanemode_on_rounded),
            color: Colors.black,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const DestinosPage()),
              );
            },
          ),
          IconButton(
            icon: const Icon(Icons.add_call),
            color: Colors.black,
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const ContatoPage()),
              );
            },
          )
        ],
      ),
      body: Container(
        color: bgBody,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            
            SizedBox(
              height: 200,
              child: GestureDetector(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => NextPage(
                            jpeg: _destinos[_currentIndex].jpeg,
                            titulo: _destinos[_currentIndex].titulo,
                            local: _destinos[_currentIndex].local,
                            texto: _destinos[_currentIndex].texto,
                            likes: _destinos[_currentIndex].likes)),
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
                      _destinos[index].jpeg,
                      fit: BoxFit.cover,
                    );
                  },
                ),
              ),
            ),
            const Padding(
              padding: EdgeInsets.all(60),
              child: Text(
                'Terra do Nunca Viagens',
                style: TextStyle(
                  fontSize: 25,
                  fontWeight: FontWeight.bold,
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
  final String jpeg;
  final String titulo;
  final String texto;
  final String local;
  final int likes;

  Destino(
      {required this.jpeg,
      required this.titulo,
      required this.texto,
      required this.local,
      required this.likes});
}
