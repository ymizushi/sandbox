import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'バイク維持費比較・見積もり',
      home: Scaffold(
        appBar: AppBar(
          title: Text('バイク維持費比較・見積もり'),
        ),
        body: Center(
          child: Text('Hello World'),
        ),
      ),
    );
  }
}
