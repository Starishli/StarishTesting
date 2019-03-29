from source import time_test


@time_test(n=100000)
def foo_list():
    x = 4
    y = 6
    _ = x in [1, 2, 3, 4, 5]
    _ = y in [1, 2, 3, 4, 5]


@time_test(n=100000)
def foo_tuple():
    x = 4
    y = 6
    _ = x in (1, 2, 3, 4, 5)
    _ = y in (1, 2, 3, 4, 5)


if __name__ == "__main__":
    foo_list()
    foo_tuple()

