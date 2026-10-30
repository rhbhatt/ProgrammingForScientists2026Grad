#!/usr/bin/env python3
from math import prod
from multiprocessing import Pool
from time import monotonic

import numpy as np

shape = (1_000, 1_000)
count = 100


def main():
    matrices = [np.random.randn(prod(shape)).reshape(shape) for _ in range(count)]

    start = monotonic()
    svds = [np.linalg.svd(m) for m in matrices]
    end = monotonic()
    print("Elapsed, serial execution:", end - start)

    process_possibilities = range(2, 17)
    for p in process_possibilities:
        start = monotonic()
        with Pool(p) as pool:
            svds = pool.map(np.linalg.svd, matrices)
        end = monotonic()
        print("Elapsed, parallel execution with", p, "processes:", end - start)


if __name__ == "__main__":
    main()
