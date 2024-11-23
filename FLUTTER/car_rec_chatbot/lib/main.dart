import 'package:car_rec_chatbot/pages/register_page.dart';
import 'package:car_rec_chatbot/themes/light_mode.dart';
import 'package:flutter/material.dart';
import 'auth/login_or_register.dart';
import 'pages/login_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const LoginOrRegister(),
      theme: lightMode,
    );
  }
}

