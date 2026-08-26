import random

from helper_functions import Average, InitializeSquareMatrix, Min2, SampleTotal, SumOfMinima


def BrayCurtisDistance(map1, map2):
    # Return the Bray-Curtis distance between two frequency maps.
    c = SumOfMinima(map1, map2)
    s1 = SampleTotal(map1)
    s2 = SampleTotal(map2)

    # don't allow the situation in which we have zero richness.
    if s1 == 0 or s2 == 0:
        raise ValueError("Error: sample given to BrayCurtisDistance() has no positive values.")

    av = Average(float(s1), float(s2))
    return 1 - (float(c) / av)


def JaccardDistance(map1, map2):
    # Return the Jaccard distance between two frequency maps.
    c = SumOfMinima(map1, map2)
    t = SumOfMaxima(map1, map2)
    return 1 - (float(c) / float(t))


def SumOfMaxima(map1, map2):
    # Return the sum of the maxima of values for keys present in either map ("union").
    c = 0

    for key in map2:
        if key in map1:
            c += Max2(map1[key], map2[key])
        else:
            c += map2[key]
    for key in map1:
        if key not in map2:
            c += map1[key]

    # raise an error if c is equal to zero since we don't want 0/0
    if c == 0:
        raise ValueError("Error: no species common to two maps given to SumOfMaxima")

    return c


def Max2(n1, n2):
    # Return the maximum of two numbers.
    if n1 < n2:
        return n2
    return n1


def SimpsonsIndex(sample):
    """Return Simpson's index: the sum of (n/N)^2 over all species in the sample,
    where n is a species' count and N is the total number of individuals."""
    total = SampleTotal(sample)
    simpson = 0.0

    if total == 0:
        raise ValueError("Error: Empty frequency map given to SimpsonsIndex()!")

    for val in sample.values():
        x = float(val) / float(total)
        simpson += x * x
    return simpson


def BetaDiversityMatrix(all_maps, dist_metric):
    """Return sorted sample names and the pairwise distance matrix between samples
    using the given distance metric ("Bray-Curtis" or "Jaccard")."""

    # first grab all sample names
    num_samples = len(all_maps)
    sample_names = list(all_maps.keys())

    # now sort sample names to make matrix ordered
    sample_names.sort()

    # now form the distance matrix

    mtx = InitializeSquareMatrix(num_samples)

    for i in range(num_samples):
        for j in range(i, num_samples):
            if dist_metric == "Bray-Curtis":
                d = BrayCurtisDistance(all_maps[sample_names[i]], all_maps[sample_names[j]])
                mtx[i][j] = d
                mtx[j][i] = d
            elif dist_metric == "Jaccard":
                d = JaccardDistance(all_maps[sample_names[i]], all_maps[sample_names[j]])
                mtx[i][j] = d
                mtx[j][i] = d
            else:
                raise ValueError("Error: Invalid distance metric name given to BetaDiversityMatrix().")
    return sample_names, mtx


def SimpsonsMap(all_maps):
    # Return a map from each sample name to its Simpson's index.
    s = {}
    for sample_name, freq_map in all_maps.items():
        s[sample_name] = SimpsonsIndex(freq_map)
    return s


def RichnessMap(all_maps):
    # Return a map from each sample name to its richness.
    r = {}
    for sample_name, freq_map in all_maps.items():
        r[sample_name] = Richness(freq_map)
    return r


def Richness(sample):
    # Return the richness of a frequency map (the number of keys with nonzero values).
    c = 0
    for val in sample.values():
        if val < 0:
            raise ValueError("Error: negative value in frequency map given to Richness()")
        elif val != 0:
            c += 1
    return c


def DownSampleMaps(all_maps, threshold):
    # Return a map of frequency maps, each randomly downsampled to the threshold.
    new_maps = {}
    for key, freq_map in all_maps.items():
        new_maps[key] = DownSample(freq_map, threshold)
    return new_maps


def DownSample(freq_map, threshold):
    # Return a new frequency map with the same keys, randomly downsampled to the threshold.
    total = SampleTotal(freq_map)
    if total < threshold:
        raise ValueError("DownSample() called on a frequency map with a total value less than the threshold!")

    # Create a list to store all the keys, repeated according to their frequency
    all_keys = []
    for key, count in freq_map.items():
        all_keys.extend([key] * count)

    # Take a random sample of size 'threshold' from the expanded list and count them
    chosen = random.sample(all_keys, threshold)

    new_map = {}
    for key in chosen:
        new_map[key] = new_map.get(key, 0) + 1

    return new_map
