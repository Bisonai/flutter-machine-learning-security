import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:bisonai_security/bisonai_security.dart';

void main() {
  const MethodChannel channel = MethodChannel('bisonai_security');

  TestWidgetsFlutterBinding.ensureInitialized();

  setUp(() {
    channel.setMockMethodCallHandler((MethodCall methodCall) async {
      return '42';
    });
  });

  tearDown(() {
    channel.setMockMethodCallHandler(null);
  });

  test('getPlatformVersion', () async {
    expect(await BisonaiSecurity.platformVersion, '42');
  });
}
