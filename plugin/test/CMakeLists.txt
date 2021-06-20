cmake_minimum_required(VERSION 3.4.1)

project(BisonaiSecurityTest)

add_library(
  bisonai_security
  SHARED
  ../ios/Classes/utils.cc
  )

add_executable(BisonaiSecurityTest bisonai_security_test.cc)
target_include_directories(BisonaiSecurityTest PUBLIC
  ../ios/Classes/
  )
target_link_libraries(BisonaiSecurityTest PUBLIC bisonai_security)
