from functools import lru_cache
from pybst.splaytree import SplayTree
import time
from matplotlib import pyplot as plt


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

    # Initialize the list to store results
    lru_times = []
    splay_times = []

    # Measure execution time for LRU cache
    for test in fib_arr:
        fibonacci_lru.cache_clear()
        test_start_time = time.perf_counter()
        result_lru = fibonacci_lru(test)
        lru_times.append(time.perf_counter() - test_start_time)

    # Measure execution time for Splay Tree
    for test in fib_arr:
        splay_tree = SplayTree()
        test_start_time = time.perf_counter()
        result_splay = fibonacci_splay(test, splay_tree)
        splay_times.append(time.perf_counter() - test_start_time)

    # Print Results
    print("\nResults Comparison:")
    print(f"{'-' * 85}")
    print(f"| {'n':<20} | {'LRU Cache Time (s)':<15} | {'Splay Tree Time (s)':<15} |")
    print(f"{'-' * 85}")

    # Output each value of n with corresponding times
    for n, lru_time, splay_time in zip(fib_arr, lru_times, splay_times):
        print(f"| {n:<20} | {lru_time:<15.8f} | {splay_time:<15.8f} |")

    plt.figure(figsize=(10, 6))
    plt.plot(fib_arr, lru_times, label="LRU Cache", color="blue", marker="o")
    plt.plot(fib_arr, splay_times, label="Splay Tree", color="red", marker="x")
    plt.xlabel("Fibonacci Number (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time Comparison: LRU Cache vs Splay Tree")

    plt.legend()

    # Show plot
    plt.grid(True)
    plt.show()
