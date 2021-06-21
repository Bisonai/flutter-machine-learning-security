import 'dart:ffi';
import 'dart:typed_data' show Uint8List;
import 'dart:io' show Platform;
import 'dart:async';

import 'package:ffi/ffi.dart';
import 'package:flutter/services.dart';
import 'package:bisonai_security/file_utils.dart' show FileUtils;


final DynamicLibrary bisonaiSecurityLib = Platform.isAndroid
? DynamicLibrary.open('libbisonai_security.so')
: DynamicLibrary.process();

typedef XorCipherShuffle = Pointer<Utf8> Function(Pointer<Uint8>, int, int, int, int, int, int, int);
typedef XorCipherShuffleNative = Pointer<Utf8> Function(Pointer<Uint8>, Int32, Int32, Int32, Int32, Int32, Int32, Int32);
final xorCipherShuffle = bisonaiSecurityLib.lookupFunction<XorCipherShuffleNative, XorCipherShuffle>('xor_cipher_shuffle');

typedef FreeString = void Function(Pointer<Utf8>);
typedef FreeStringNative = Void Function(Pointer<Utf8>);
final freeString = bisonaiSecurityLib.lookupFunction<FreeStringNative, FreeString>('free_string');

Future<String> decryptFile(
  String filePath,
  int a_key,
  int c_key,
  int m_key,
  int a_shuffle,
  int c_shuffle,
  int m_shuffle
) async {
  Uint8List binary_message_enc = await FileUtils.loadFileAsBytes(filePath);
  final message_length = binary_message_enc.length;
  final binary_message_enc_ptr = calloc<Uint8>(message_length);

  for (int i = 0; i < message_length; ++i) {
    binary_message_enc_ptr[i] = binary_message_enc[i];
  }

  final binary_message_dec_ptr = xorCipherShuffle(
    binary_message_enc_ptr,
    message_length,
    a_key,
    c_key,
    m_key,
    a_shuffle,
    c_shuffle,
    m_shuffle
  );

  final binary_message_dec = binary_message_dec_ptr.toDartString();

  calloc.free(binary_message_enc_ptr);
  freeString(binary_message_dec_ptr);

  return binary_message_dec;
}

class BisonaiSecurity {
  static const MethodChannel _channel = const MethodChannel('bisonai_security');
}
