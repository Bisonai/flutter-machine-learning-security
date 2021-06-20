import 'package:flutter/material.dart';
import 'dart:async';
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
  @override
  void initState() {
    super.initState();
    decryptFile('assets/bisonai_enc.txt');
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Bisonai Security App'),
        ),
        body: Center(
          // child: Text('${xorCipherShuffle(my_string_utf8).toDartString()}'),
        ),
      ),
    );
  }
}
