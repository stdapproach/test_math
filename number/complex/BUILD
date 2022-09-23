py_binary(
    name = "py1",
    srcs = [
        "py1.py",
        "utils/complex_utils.py"
    ],
)

py_test(
   name = "add_test",
   srcs = ["test/add_test.py"],
   deps = [
        ":py1",
    ],
)

py_test(
   name = "conjugate_test",
   srcs = ["test/conjugate_test.py"],
   deps = [
        ":py1",
    ],
)

py_test(
   name = "py1_test",
   srcs = ["py1_test.py"],
   deps = [
        ":py1",
    ],
)

py_test(
   name = "complex_utils_test",
   srcs = ["test/complex_utils_test.py"],
   main = "test/complex_utils_test.py",
   deps = [
        ":py1",
    ],
)

py_test(
   name = "py2_test",
   srcs = ["test/py2_test.py"],
   deps = [
        ":py1",
    ],
)