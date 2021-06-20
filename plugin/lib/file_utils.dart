import 'dart:typed_data';
import 'package:flutter/services.dart' show rootBundle;


class FileUtils {
  /// Loads a file from project assets as [Uint8List] bytes.
  ///
  /// [fileAssetLocation] specifies the path of asset at project level.
  /// For example: If file is located at <root-dir>/assets/filename.txt then fileAssetLocation is
  /// assets/filename.txt.
  static Future<Uint8List> loadFileAsBytes(String fileAssetLocation) async {
    final rawAssetFile = await rootBundle.load(fileAssetLocation);
    final rawBytes = rawAssetFile.buffer.asUint8List();
    return rawBytes;
  }
}
