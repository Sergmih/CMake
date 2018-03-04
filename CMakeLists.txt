cmake_minimum_required(VERSION 2.8)
project(bot)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")
set(SOURCES_LIST C/main.cpp C/main.h A/index.h B/lib.h B/lib1.h B/lib2.h)
include_directories(A C)
add_subdirectory(B)
add_executable(bot ${SOURCES_LIST})

