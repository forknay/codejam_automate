import 'package:car_rec_chatbot/services/auth/login_or_register.dart';
import 'package:car_rec_chatbot/pages/home_page.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:car_rec_chatbot/services/auth/auth_service.dart';
import 'package:car_rec_chatbot/pages/chat_page.dart';


class AuthGate extends StatelessWidget {
  final AuthService _authService = AuthService();
  AuthGate({super.key});
  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: StreamBuilder(
        stream: FirebaseAuth.instance.authStateChanges(),
        builder: (context, snapshot) {
          // user is logged in
          if (snapshot.hasData) {
            bool isCurrentUser =
                _authService.getCurrentUser()!.uid == 'NpjrXpa0xqhRYagxKQViysrC0Ee2';
            if (isCurrentUser) {
              return HomePage();
            }
            else {
              return ChatPage(receiverID: "cfhCvGguwDZMXYIzT2OrjnaKon32", receiverEmail: "chat@matadore.ai", );
            }
          }

          // user is NOT logged in
          else {
            return const LoginOrRegister();
          }
        },
      ),
    );
  }
}
