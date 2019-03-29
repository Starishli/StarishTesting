import time
from functools import wraps


def time_test(n=10000):
    def time_test_decorator(foo):
        @wraps(foo)
        def decorated_foo():
            tic = time.time()

            for _ in range(n):
                foo()

            toc = time.time() - tic
            print("Total time used is %0.8f for %0f tests" % (toc, n))

        return decorated_foo
    return time_test_decorator


@time_test(n=20000)
def test_sample():
    x = [k ** 2 for k in range(100)]


if __name__ == "__main__":
    test_sample()
