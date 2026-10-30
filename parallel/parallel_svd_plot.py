#!/usr/bin/env python3
from math import prod
from multiprocessing import Pool
from time import monotonic

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

shape = (1_000, 1_000)
count = 100


def main():
    matrices = [np.random.randn(prod(shape)).reshape(shape) for _ in range(count)]

    times = {}

    start = monotonic()
    svds = [np.linalg.svd(m) for m in matrices]
    end = monotonic()
    print("Elapsed, serial execution:", end - start)
    times[1] = end - start

    process_possibilities = range(2, 17)
    for p in process_possibilities:
        start = monotonic()
        with Pool(p) as pool:
            svds = pool.map(np.linalg.svd, matrices)
        end = monotonic()
        print("Elapsed, parallel execution with", p, "processes:", end - start)
        times[p] = end - start

    times_series = pd.Series(times)
    times_series.plot.line(xlabel="Processes", ylabel="Time (s)")
    plt.savefig("runtime_by_process_count.pdf", bbox_inches="tight")


if __name__ == "__main__":
    main()
