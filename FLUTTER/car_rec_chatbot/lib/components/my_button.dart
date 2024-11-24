import 'package:flutter/material.dart';

class MyButton extends StatefulWidget {
  final void Function()? onTap;
  final String text;

  const MyButton({
    super.key,
    required this.text,
    required this.onTap,
  });

  @override
  _MyButtonState createState() => _MyButtonState();
}

class _MyButtonState extends State<MyButton> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return MouseRegion(
      onEnter: (_) => setState(() => _isHovered = true),
      onExit: (_) => setState(() => _isHovered = false),
      child: GestureDetector(
        onTap: widget.onTap,
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 200),
          width: _isHovered ? 220 : 200,
          height: _isHovered ? 70 : 60,
          decoration: BoxDecoration(
            gradient: LinearGradient(
              colors: _isHovered
                  ? [Theme.of(context).colorScheme.inversePrimary, Theme.of(context).colorScheme.primary]
                  : [Theme.of(context).colorScheme.primary, Theme.of(context).colorScheme.inversePrimary],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            boxShadow: _isHovered
                ? [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.2),
                      spreadRadius: 2,
                      blurRadius: 5,
                      offset: Offset(0, 3),
                    ),
                  ]
                : [],
            borderRadius: BorderRadius.circular(12),
          ),
          padding: const EdgeInsets.all(8),
          margin: const EdgeInsets.symmetric(horizontal: 25),
          child: Center(
            child: Text(
              widget.text,
              style: TextStyle(
                color: theme.colorScheme.onPrimary,
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ),
      ),
    );
  }
}
