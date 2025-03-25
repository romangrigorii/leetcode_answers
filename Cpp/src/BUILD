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
    srcs = [
        "1_twosum.cpp",
        "2_addtwonumbers.cpp",
        "3_longestsubstring.cpp",
        "4_medianoftwosortedarrays.cpp",
    ],
    hdrs = ["headers.hpp"],
    deps = [
        ":helpers"
    ]
)

cc_test(
    name = "test_suite",
    size = "medium",
    srcs = [
        "tests/test_1_twosum.cpp",
        "tests/test_2_addtwonumbers.cpp",
        "tests/test_3_longestsubstring.cpp",
        "tests/test_4_medianoftwosortedarrays.cpp",
    ],
    deps = [
        "@googletest//:gtest",
        "@googletest//:gtest_main",
        ":functions",
        ":helpers",
    ],
)