import random
import time
from lru_cach import LRUCache


def range_sum_no_cache(array, L, R):
    return sum(array[L : R + 1])


def update_no_cache(array, index, value):
    array[index] = value
    return array


cache = LRUCache(1000)


def range_sum_with_cache(array, L, R):
    if cache.check((L, R)):
        return cache.get((L, R))

    result = sum(array[L : R + 1])

    cache.put((L, R), result)
    return result


def update_with_cache(array, index, value):
    array[index] = value  # Update the array at the given index

    # Remove all cache entries that include the updated index
    keys_to_remove = [key for key in cache.cache if key[0] <= index <= key[1]]
    for key in keys_to_remove:
        del cache.cache[key]
        # Optionally, remove from the doubly linked list (if the cache was moved to the front)
        node = cache.cache.get(key)

        if node:
            cache.list.remove(node)


def tests(n):
    req = ["Range", "Update"]
    queries = []
    for _ in range(n):
        q = random.choice(req)
        if q == "Range":
            L = random.randint(0, 4999)
            R = random.randint(L + 1, 9999)
            queries.append(("Range", L, R))
        elif q == "Update":
            index = random.randint(0, 9999)
            value = random.randint(0, 100_000)
            queries.append(("Update", index, value))
    return queries


if __name__ == "__main__":
    arr = [random.randrange(1, 100_001) for _ in range(10_000)]
    n = 50_000
    tests = tests(n)

    start_time = time.perf_counter()

    for query in tests:
        if query[0] == "Range":
            range_sum_no_cache(arr, query[1], query[2])
        else:
            update_no_cache(arr, query[1], query[2])
    print(
        f"Execution time without cache: {time.perf_counter() - start_time:.2f} seconds"
    )

    cache_hits = 0
    cache_misses = 0

    start_time = time.perf_counter()
    for query in tests:
        if query[0] == "Range":
            if cache.check((query[1], query[2])):
                cache_hits += 1
            else:
                cache_misses += 1
            range_sum_with_cache(arr, query[1], query[2])
        else:
            update_with_cache(arr, query[1], query[2])
    print(
        f"Execution time with LRU cache: {time.perf_counter() - start_time:.2f} seconds"
    )
    print(f"Cache hits: {cache_hits}, cahce misses: {cache_misses}")
