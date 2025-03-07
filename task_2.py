from functools import lru_cache
from pybst.splaytree import SplayTree
import time


@lru_cache(maxsize=1000)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_splay(n, tree):

    if tree.get_node(0) is None:
        tree.insert(0, 0)
    if tree.get_node(1) is None:
        tree.insert(1, 1)

    for i in range(2, n + 1):
        prev1 = tree.get_node(i - 1)
        prev2 = tree.get_node(i - 2)

        if tree.get_node(i) is None:
            tree.insert(i, prev1.value + prev2.value)

    return tree.get_node(n).value


if __name__ == "__main__":

    fib_arr = list(range(0, 951, 50))

    start_time = time.perf_counter()
    for test in fib_arr:
        result_lru = fibonacci_lru(test)
    print(
        f"Execution time with LRU cache: {time.perf_counter() - start_time:.5f} seconds"
    )
    # print(f"Fibonacci({n}) with LRU cache: {result_lru}")

    splay_tree = SplayTree()
    start_time = time.perf_counter()
    for test in fib_arr:
        result_splay = fibonacci_splay(test, splay_tree)
    print(
        f"Execution time with splay_tree: {time.perf_counter() - start_time:.5f} seconds"
    )
    # print(f"Fibonacci({n}) with Splay Tree: {result_splay}")
