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
    surface: const Color.fromARGB(255, 0, 3, 27),
    primary: Colors.white,
    inversePrimary: const Color.fromARGB(255, 91, 102, 233),
    secondary: Colors.white.withOpacity(0.1),
    tertiary: Colors.black,
  ),
);

ThemeData bluetheme = ThemeData(
  colorScheme: ColorScheme.dark(
    surface: const Color.fromARGB(255, 169, 188, 208),
    primary: Color.fromARGB(255, 216, 219, 226),
    inversePrimary: Color.fromARGB(255,55,63,81),
    secondary: Colors.white.withOpacity(0.1),
    tertiary: Color.fromARGB(255, 31, 42, 69),
),
);
