#import "BisonaiSecurityPlugin.h"
#if __has_include(<bisonai_security/bisonai_security-Swift.h>)
#import <bisonai_security/bisonai_security-Swift.h>
#else
// Support project import fallback if the generated compatibility header
// is not copied when this plugin is created as a library.
// https://forums.swift.org/t/swift-static-libraries-dont-copy-generated-objective-c-header/19816
#import "bisonai_security-Swift.h"
#endif

@implementation BisonaiSecurityPlugin
+ (void)registerWithRegistrar:(NSObject<FlutterPluginRegistrar>*)registrar {
  [SwiftBisonaiSecurityPlugin registerWithRegistrar:registrar];
}
@end
