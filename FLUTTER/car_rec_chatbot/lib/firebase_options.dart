// File generated by FlutterFire CLI.
// ignore_for_file: type=lint
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        return macos;
      case TargetPlatform.windows:
        return windows;
      case TargetPlatform.linux:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for linux - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyBeJWGGnEsr6bgRPfuKlyYG5SMxGgcLwwA',
    appId: '1:65215121753:web:ae537d48e5e5112152a448',
    messagingSenderId: '65215121753',
    projectId: 'chatbot-cc091',
    authDomain: 'chatbot-cc091.firebaseapp.com',
    storageBucket: 'chatbot-cc091.firebasestorage.app',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyClWImdB49JS9riBwFwr5NWLuxQ4B_ORXc',
    appId: '1:65215121753:android:6d50fed603dfdb4152a448',
    messagingSenderId: '65215121753',
    projectId: 'chatbot-cc091',
    storageBucket: 'chatbot-cc091.firebasestorage.app',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyBKJGwJnwl7NOIQFXW9pl4tSDpfpHVhpcY',
    appId: '1:65215121753:ios:b3d85aa64e1ee87f52a448',
    messagingSenderId: '65215121753',
    projectId: 'chatbot-cc091',
    storageBucket: 'chatbot-cc091.firebasestorage.app',
    iosBundleId: 'com.example.carRecChatbot',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyBKJGwJnwl7NOIQFXW9pl4tSDpfpHVhpcY',
    appId: '1:65215121753:ios:b3d85aa64e1ee87f52a448',
    messagingSenderId: '65215121753',
    projectId: 'chatbot-cc091',
    storageBucket: 'chatbot-cc091.firebasestorage.app',
    iosBundleId: 'com.example.carRecChatbot',
  );

  static const FirebaseOptions windows = FirebaseOptions(
    apiKey: 'AIzaSyBeJWGGnEsr6bgRPfuKlyYG5SMxGgcLwwA',
    appId: '1:65215121753:web:39872e1f1413a50752a448',
    messagingSenderId: '65215121753',
    projectId: 'chatbot-cc091',
    authDomain: 'chatbot-cc091.firebaseapp.com',
    storageBucket: 'chatbot-cc091.firebasestorage.app',
  );
}
