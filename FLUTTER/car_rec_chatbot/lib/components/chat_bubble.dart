import 'package:flutter/material.dart';

class ChatBubble extends StatelessWidget {
  final String message;
  final bool isCurrentUser;

  const ChatBubble({
    super.key, 
    required this.message, 
    required this.isCurrentUser,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: isCurrentUser ? Theme.of(context).colorScheme.primary : Theme.of(context).colorScheme.inversePrimary,
        borderRadius: BorderRadius.circular(8),
      ),
      padding: const EdgeInsets.all(9),
      margin: const EdgeInsets.symmetric(vertical: 5, horizontal: 25),
      child: Text(message, style: TextStyle(color: isCurrentUser ? 
                                  Theme.of(context).colorScheme.tertiary: 
                                  Theme.of(context).colorScheme.primary),),
    );
  }
}
