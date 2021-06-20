import 'dart:ffi';
import 'package:ffi/ffi.dart';
import 'dart:io' show Platform;
import 'dart:async';
import 'package:flutter/services.dart';
import 'dart:typed_data' show Uint8List;
import 'package:bisonai_security/file_utils.dart' show FileUtils;


final DynamicLibrary bisonaiSecurityLib = Platform.isAndroid
    ? DynamicLibrary.open("libbisonai_security.so")
    : DynamicLibrary.process();

final Pointer<Utf8> Function(Pointer <Uint8>, int) xorCipherShuffle =
  bisonaiSecurityLib
    .lookup<NativeFunction<Pointer<Utf8> Function(Pointer<Uint8>, Int32)>>("xor_cipher_shuffle")
    .asFunction();

typedef FreeString = void Function(Pointer<Utf8> str);
typedef FreeStringNative = Void Function(Pointer<Utf8> str);
final freeString =
      bisonaiSecurityLib.lookupFunction<FreeStringNative, FreeString>('free_string');

void decryptFile(String filePath) async {
  Uint8List binary_message_enc = await FileUtils.loadFileAsBytes(filePath);
  final message_length = binary_message_enc.length;
  final binary_message_enc_ptr = calloc<Uint8>(message_length);

  for (int i = 0; i < message_length; ++i) {
    binary_message_enc_ptr[i] = binary_message_enc[i];
  }

  final binary_message_dec_ptr = xorCipherShuffle(binary_message_enc_ptr, message_length);
  final binary_message_dec = binary_message_dec_ptr.toDartString();

  calloc.free(binary_message_enc_ptr);
  freeString(binary_message_dec_ptr);

  print(binary_message_dec);
}


class BisonaiSecurity {
  static const MethodChannel _channel =
      const MethodChannel('bisonai_security');

  static Future<String> get platformVersion async {
    final String version = await _channel.invokeMethod('getPlatformVersion');
    return version;
  }
}
