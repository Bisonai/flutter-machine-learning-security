# Bisonai Security Flutter Plugin


## Example

```dart
import 'package:bisonai_security/bisonai_security.dart';

String assetDecoded = '';

final int a_key = 3007;
final int c_key = 0;
final int m_key = pow(2, 14) - 3;

final int a_shuffle = 3007;
final int c_shuffle = 0;
final int m_shuffle = pow(2, 14) - 3;

Future<String> assetDecodedFuture = decryptFile(
  'assets/bisonai_enc.txt',
  a_key,
  c_key,
  m_key,
  a_shuffle,
  c_shuffle,
  m_shuffle,
);

assetDecodedFuture.then((value) => setState(() { assetDecoded = value; }))
.catchError((error) => print(error));
```
