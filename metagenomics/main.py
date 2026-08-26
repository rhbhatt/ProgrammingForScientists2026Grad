from functions import (
    BetaDiversityMatrix,
    DownSampleMaps,
    SimpsonsIndex,
    SimpsonsMap,
)
from helper_functions import SampleTotal
from io_functions import (
    ReadFrequencyMapFromFile,
    ReadSamplesFromDirectory,
    WriteBetaDiversityMatrixToFile,
    WriteSimpsonsMapToFile,
)


def main():
    print("Metagenomics!")

    # step 1: reading input from a single file.

    filename = "Data/Fall_Allegheny_1.txt"
    freq_map = ReadFrequencyMapFromFile(filename)
    print("File read successfully! We have", len(freq_map), "total patterns.")

    # we may as well do something with our file. For example, let's print its Simpson's Index.
    print("Simpson's Index:", SimpsonsIndex(freq_map))

    # step 2: reading input from a directory

    path = "Data/"
    all_maps = ReadSamplesFromDirectory(path)

    print("Samples read successfully! We have", len(all_maps), "total samples.")

    print("Let's determine the depth of each sample.")

    depth_map = {}
    for key, freq_map in all_maps.items():
        depth_map[key] = SampleTotal(freq_map)

    print("Printing the depth of each sample to the console.")

    for key, val in depth_map.items():
        print(key, "depth:", val)

    # let's take a sequencing depth of 400
    sequencing_depth = 400

    print("Downsampling all samples to a threshold of", sequencing_depth)

    downsampled_maps = DownSampleMaps(all_maps, sequencing_depth)

    # step 3: processing the data that we have received.

    # now all of our maps have been processed and we can start working with them.

    # for example, let's compute the evenness of each sample.

    simpson = SimpsonsMap(downsampled_maps)

    # now let's look at beta diversity.

    dist_metric = "Bray-Curtis"
    sample_names, mtx = BetaDiversityMatrix(downsampled_maps, dist_metric)

    # we cannot really analyze anything from this printing.

    # It would be better to print to a file.  Hence, we will need to learn writing to a file.

    simpson_file = "Matrices/SimpsonMatrix.csv"
    WriteSimpsonsMapToFile(simpson, simpson_file)

    out_filename = "Matrices/BetaDiversityMatrix.csv"
    WriteBetaDiversityMatrixToFile(mtx, sample_names, out_filename)

    print("Success! Now we are ready to do something cool with our data.")


if __name__ == "__main__":
    main()
