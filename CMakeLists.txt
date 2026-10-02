cmake_minimum_required(VERSION 3.22)
project(SASDGraphicsToolkit VERSION 0.1.0
    DESCRIPTION "Multi-language 2D graphics and visualization toolkit"
    LANGUAGES CXX)

option(SASD_GRAPHICS_BUILD_TESTS "Run repository checks and future C++ tests" ON)
option(SASD_GRAPHICS_BUILD_DEMOS "Configure future C++ samples" ON)

add_subdirectory(src/cpp)
if(SASD_GRAPHICS_BUILD_TESTS)
    enable_testing()
    find_package(Python3 3.10 REQUIRED COMPONENTS Interpreter)
    add_subdirectory(tests/cpp)
endif()
if(SASD_GRAPHICS_BUILD_DEMOS)
    add_subdirectory(samples/cpp)
endif()
message(STATUS "Graphics: C++ scaffold only; no library or renderer targets yet")
