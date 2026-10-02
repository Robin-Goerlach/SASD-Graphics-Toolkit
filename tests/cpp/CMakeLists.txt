# This is a repository check, not a geometry/SVG implementation test.
add_test(NAME repository_contracts
    COMMAND "${Python3_EXECUTABLE}"
        "${PROJECT_SOURCE_DIR}/tools/check_repository.py"
        --root "${PROJECT_SOURCE_DIR}")
# Add actual C++ unit and conformance runners when their implementations exist.
add_test(NAME repository_guard_regressions
    COMMAND "${Python3_EXECUTABLE}"
        "${PROJECT_SOURCE_DIR}/tests/repository/test_repository_contracts.py")
