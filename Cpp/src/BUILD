cc_library(
    name = "helpers",
    srcs = ["tests/helpers.cpp"],
    hdrs = ["tests/helpers.hpp"],
    deps = [
        "@googletest//:gtest",
        "@googletest//:gtest_main",
    ],
)

cc_library(
    name = "functions",
    srcs = ["1_twosum.cpp"],
    hdrs = ["headers.hpp"],
    deps = [
        ":helpers"
    ]
)

cc_test(
    name = "test_1_twosum",
    size = "medium",
    srcs = ["tests/test_1_twosum.cpp"],
    deps = [
        "@googletest//:gtest",
        "@googletest//:gtest_main",
        ":functions",
        ":helpers",
    ],
)