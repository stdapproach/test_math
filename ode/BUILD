py_binary(
    name = "ode1",
    srcs = ["ode1.py"],
    imports = ["."],
)

py_binary(
    name = "examples",
    srcs = [
        "examples.py",
        "books_ref.py",
        "util_calc.py",
        "util_chart.py",
        "uget.py",
    ],
    imports = ["."],
)

py_binary(
    name = "show_examples",
    srcs = [
        "show_examples.py",
    ],
    deps = [":examples"],
    imports = ["."],
)

py_test(
   name = "test1",
   srcs = ["test/test1.py"],
   deps = [":examples"],
   imports = ["."],
)
