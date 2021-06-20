cmake_minimum_required(VERSION 3.4.1)

add_library( bisonai_security
  SHARED
  ../ios/Classes/xor_cipher_shuffle.cc
  ../ios/Classes/utils.cc
  )
