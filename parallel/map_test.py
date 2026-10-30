#!/usr/bin/env python3
from multiprocessing import Pool
from random import random
from time import monotonic, sleep


def f(x):
    sleep(random() * 2)
    sq = x * x
    print("Writing results to disk for", x)
    with open(f"{x}.txt", "w") as f:
        print(sq, file=f)
    return x, x * x


if __name__ == "__main__":
    start = monotonic()
    print(list(map(f, range(10))))
    end = monotonic()
    print("Serial execution:", end - start)

    with Pool(5) as pool:
        start = monotonic()
        results = pool.map(f, range(10))
        print(results)
        end = monotonic()
        print("Parallel with pool.map:", end - start)

    with Pool(5) as pool:
        start = monotonic()
        results = pool.imap(f, range(10))
        print(results)
        for result in results:
            print(result)
        end = monotonic()
        print("Parallel with pool.imap:", end - start)

    with Pool(5) as pool:
        start = monotonic()
        results = pool.imap_unordered(f, range(10))
        print(results)
        for result in results:
            print(result)
        end = monotonic()
        print("Parallel with pool.imap_unordered:", end - start)
