import 'package:flutter/material.dart';

void main() {
  runApp(MuseScoreDiagnosticApp());
}

class MuseScoreDiagnosticApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Diagnostic MuseScore Web',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Diagnostic MuseScore Web')),
      body: Center(
        child: Padding(
          padding: EdgeInsets.all(16),
          child: Text(
            'Bienvenue dans l\'application web de diagnostic MuseScore.\n'
            'La version Web est une démo simple. Pour une expérience complète, utilisez la version mobile.',
            style: TextStyle(fontSize: 18),
            textAlign: TextAlign.center,
          ),
        ),
      ),
    );
  }
}