# Future C++ targets belong here. Requiring C++20 on each real target with
# target_compile_features(... PUBLIC cxx_std_20) will also inform consumers.
# No dummy library is created: the repository currently contains no C++ API.
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
