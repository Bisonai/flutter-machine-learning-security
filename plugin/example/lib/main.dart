import 'package:flutter/material.dart';
import 'dart:async';
import 'dart:math' show pow;
import 'package:flutter/services.dart';
import 'package:bisonai_security/bisonai_security.dart';


void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String assetDecoded = '';

  final int a_key = 3007;
  final int c_key = 0;
  final int m_key = pow(2, 14) - 3;

  final int a_shuffle = 3007;
  final int c_shuffle = 0;
  final int m_shuffle = pow(2, 14) - 3;

  @override
  void initState() {
    super.initState();

    Future<String> assetDecodedFuture = decryptFile(
      'assets/bisonai_enc.txt',
      a_key,
      c_key,
      m_key,
      a_shuffle,
      c_shuffle,
      m_shuffle,
    );

    assetDecodedFuture.then((value) => setState(() { assetDecoded = value; }))
    .catchError((error) => print(error));
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Bisonai Security App'),
        ),
        body: Center(
          child: Text(assetDecoded),
        ),
      ),
    );
  }
}
