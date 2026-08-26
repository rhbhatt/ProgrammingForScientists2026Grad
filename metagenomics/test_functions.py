# Testing code for each function in functions.py, using the tests in the Tests directory.

import os
from dataclasses import dataclass

from functions import Richness, SimpsonsIndex
from helper_functions import SampleTotal


@dataclass
class RichnessTest:
    # Holds the information for a test that takes a sample and an integer.
    sample: dict
    result: int


@dataclass
class SimpsonsIndexTest:
    # Holds the information for a test that takes a sample and a float.
    sample: dict
    result: float


def ReadDirectory(directory):
    # Return a sorted list of file names in the given directory.
    return sorted(os.listdir(directory))


def ReadSample(file):
    # Read in a frequency map from a file.
    sample = {}
    with open(file, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split(" ")
            pattern = parts[0]
            value = int(parts[1])
            sample[pattern] = value
    return sample


def ReadIntegerFromFile(file):
    # Read in a single integer from a file.
    with open(file, "r") as f:
        line = f.readline().rstrip("\n")
    return int(line)


def ReadFloatFromFile(file):
    # Read in a single float from a file.
    with open(file, "r") as f:
        line = f.readline().rstrip("\n")
    return float(line)


def roundFloat(val, precision):
    # Round a float to a given number of decimals precision.
    return round(val, precision)


def ReadRichnessTests(directory):
    input_files = ReadDirectory(directory + "/input")
    output_files = ReadDirectory(directory + "/output")

    # ensure same number of input and output files
    if len(output_files) != len(input_files):
        raise ValueError("Error: number of input and output files do not match!")

    tests = []
    for input_file, output_file in zip(input_files, output_files):
        sample = ReadSample(directory + "input/" + input_file)
        result = ReadIntegerFromFile(directory + "output/" + output_file)
        tests.append(RichnessTest(sample=sample, result=result))
    return tests


def test_richness():
    tests = ReadRichnessTests("Tests/Richness/")
    for test in tests:
        our_answer = Richness(test.sample)
        assert our_answer == test.result, (
            f"Richness({test.sample}) = {our_answer}, want {test.result}"
        )


def ReadSimpsonsIndexTests(directory):
    input_files = ReadDirectory(directory + "/input")
    output_files = ReadDirectory(directory + "/output")

    if len(output_files) != len(input_files):
        raise ValueError("Error: number of input and output files do not match!")

    tests = []
    for input_file, output_file in zip(input_files, output_files):
        sample = ReadSample(directory + "input/" + input_file)
        result = ReadFloatFromFile(directory + "output/" + output_file)
        tests.append(SimpsonsIndexTest(sample=sample, result=result))
    return tests


def test_simpsons_index():
    tests = ReadSimpsonsIndexTests("Tests/SimpsonsIndex/")
    for test in tests:
        result = SimpsonsIndex(test.sample)
        assert roundFloat(result, 4) == roundFloat(test.result, 4), (
            f"SimpsonsIndex({test.sample}) = {result}, want {test.result}"
        )


def ReadSampleTotalTests(directory):
    input_files = ReadDirectory(directory + "/input")
    output_files = ReadDirectory(directory + "/output")

    if len(output_files) != len(input_files):
        raise ValueError("Error: number of input and output files do not match!")

    tests = []
    for input_file, output_file in zip(input_files, output_files):
        sample = ReadSample(directory + "input/" + input_file)
        result = ReadIntegerFromFile(directory + "output/" + output_file)
        tests.append(SampleTotalTest(sample=sample, result=result))
    return tests

