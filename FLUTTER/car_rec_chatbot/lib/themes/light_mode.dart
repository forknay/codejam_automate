import 'package:flutter/material.dart';

ThemeData lightMode = ThemeData(
  colorScheme: ColorScheme.light(
    surface: Colors.grey.shade300,
    primary: Colors.grey.shade500,
    secondary: Colors.grey.shade200,
    tertiary: Colors.white,
    inversePrimary: Colors.grey.shade900,
  ),
);

ThemeData darkMode = ThemeData(
  colorScheme: ColorScheme.dark(
    surface: const Color.fromARGB(255, 13, 4, 41),
  primary: const Color.fromRGBO(255, 238, 238, 1),
    secondary: const Color.fromARGB(255, 255, 255, 255).withOpacity(0.5),
    tertiary: Colors.black,
    inversePrimary: const Color.fromARGB(255, 96, 96, 127),
  ),
);