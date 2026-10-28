#!/usr/bin/env python3
from math import prod
from multiprocessing import Pool
from time import monotonic

import numpy as np

shape = (1_000, 1_000)


def main():
    matrices = [np.random.randn(prod(shape)).reshape(shape) for _ in range(100)]
    start = monotonic()
    svds = [np.linalg.svd(m) for m in matrices]
    end = monotonic()
    print("Elapsed, serial execution:", end - start)

    start = monotonic()
    with Pool(8) as pool:
        svds = pool.map(np.linalg.svd, matrices)
    end = monotonic()
    print("Elapsed, parallel execution:", end - start)


if __name__ == "__main__":
    main()
