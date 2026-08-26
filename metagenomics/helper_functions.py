def InitializeSquareMatrix(n):
    # Return an n x n list of lists of floats initialized to 0.0.
    return [[0.0 for _ in range(n)] for _ in range(n)]


def FrequencyMap(patterns):
    # Form the frequency map of a collection of input patterns.
    freq_map = {}
    for val in patterns:
        freq_map[val] = freq_map.get(val, 0) + 1
    return freq_map


def Average(x, y):
    # Return the average of two floats.
    return (x + y) / 2.0


def SampleTotal(freq_map):
    # Return the sum of the counts for each string in a sample.
    total = 0
    for val in freq_map.values():
        if val > 0:
            total += val
    return total


def SumOfMinima(map1, map2):
    # Return the sum of Min2(map1[key], map2[key]) over keys shared by both maps.
    c = 0
    for key in map1:
        if key in map2:
            c += Min2(map1[key], map2[key])
    return c


def Min2(n1, n2):
    # Return the minimum of two numbers.
    if n1 < n2:
        return n1
    return n2
