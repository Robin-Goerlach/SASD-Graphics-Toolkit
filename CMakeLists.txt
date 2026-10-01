cmake_minimum_required(VERSION 3.22)

project(
    SASDGraphicsToolkit
    VERSION 0.1.0
    DESCRIPTION "Modern C++ 2D graphics and visualization toolkit for SASD projects"
    LANGUAGES CXX
)

option(SASD_GRAPHICS_BUILD_TESTS "Build SASD Graphics Toolkit tests" ON)
option(SASD_GRAPHICS_BUILD_DEMOS "Build SASD Graphics Toolkit demos" ON)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

message(STATUS "SASD Graphics Toolkit ${PROJECT_VERSION}")
message(STATUS "Build tests: ${SASD_GRAPHICS_BUILD_TESTS}")
message(STATUS "Build demos: ${SASD_GRAPHICS_BUILD_DEMOS}")

# Implementation targets will be added in later milestones.
# Planned first targets:
# - sasd_graphics_core
# - sasd_graphics_rendering_svg
# - sasd_graphics_boards
# - sasd_graphics_charts

if(SASD_GRAPHICS_BUILD_TESTS)
    enable_testing()
endif()
