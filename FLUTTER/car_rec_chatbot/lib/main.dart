import 'package:car_rec_chatbot/flask_connect.dart';
import 'package:car_rec_chatbot/services/auth/auth_gate.dart';
import 'package:car_rec_chatbot/firebase_options.dart';
import 'package:car_rec_chatbot/pages/register_page.dart';
import 'package:car_rec_chatbot/themes/light_mode.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'services/auth/login_or_register.dart';
import 'pages/login_page.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const AuthGate(),
      theme: lightMode,
    );
  }
}

class AuthGate extends StatefulWidget {
  const AuthGate({Key? key}) : super(key: key);

  @override
  _AuthGateState createState() => _AuthGateState();
}

class _AuthGateState extends State<AuthGate> {
  @override
  void initState() {
    super.initState();
    fetchData();
  }

  Future<void> fetchData() async {
    final String url = 'http://10.121.158.137:5000/';
    try {
      final response = await http.get(Uri.parse(url));
      if (response.statusCode == 200) {
        // If the server returns a 200 OK response, parse the JSON.
        var data = json.decode(response.body);
        print('Data received: $data');
      } else {
        // If the server did not return a 200 OK response, throw an exception.
        print('Failed to load data');
      }
    } catch (e) {
      print('Error: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Auth Gate')),
      body: Center(child: const Text('Welcome to the Auth Gate')),
    );
  }
}
