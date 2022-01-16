import 'package:flutter/material.dart';
import 'extensions.dart';

void main() {
  runApp(const NewSortApp());
}

class NewSortApp extends StatelessWidget {
  const NewSortApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'New sort algorithm demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const NewSortPage(title: 'New sort algorithm demo'),
    );
  }
}

class NewSortPage extends StatefulWidget {
  const NewSortPage({Key? key, required this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<NewSortPage> createState() => _NewSortPageState();
}

class _NewSortPageState extends State<NewSortPage> {
  List<int> _numbers = [2, 12, 3, 12, 345, 10, 30];

  void _sort() async {
    for (var l in _numbers.nsort()) {
      await Future.delayed(const Duration(seconds: 1));
      setState(() {
        _numbers = l;
      });
    }
  }

  void _submitText(String va) async {
    List<int> v = va
        .replaceAll("[", "")
        .replaceAll("]", "")
        .split(",")
        .map((v) => int.parse(v))
        .toList();
    setState(() {
      _numbers = v;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              '$_numbers',
              style: Theme.of(context).textTheme.headline4,
            ),
            TextField(
              onSubmitted: _submitText,
              decoration: InputDecoration(
                  border: const OutlineInputBorder(),
                  hintText: _numbers.toString(),
                  labelText: "カンマ区切りの数字を入力してね"),
            )
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _sort,
        tooltip: 'Sort!!',
        child: const Text("Sort"),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
