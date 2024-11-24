import 'package:http/http.dart' as http;
import 'dart:convert';

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