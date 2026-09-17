import imageio.v3 as imageio 
import sys

from datatypes import OrderedPair, Body, Universe
from functions import simulate
from drawing import animate_system
from animate import animate_surfaces
from custom_io import *

def main():
    print("Let's simulate gravity!")
    # Expect 5 user arguments (plus program name)
    if len(sys.argv) != 6:
        raise ValueError(
            "Error: incorrect number of command line arguments. Six desired."
        )
    scenario = sys.argv[1]
    # establish input file and output prefix
    input_file = f"{scenario}.txt"
    video_path = f"output/{scenario}.mp4"
    # Parse CLI arguments
    num_gens = int(sys.argv[2])
    time_step = float(sys.argv[3])
    canvas_width = int(sys.argv[4])
    drawing_frequency = int(sys.argv[5])
    print("Command line arguments read!")
    # Read initial universe
    initial_universe = read_universe(input_file)
    print("Simulating gravity now.")
    time_points = simulate(initial_universe, num_gens, time_step)
    #for t in time_points:
    #    print(t)
    print("Gravity simulation complete.")
    print("Rendering frames.")
    surfaces = animate_system(time_points, canvas_width, drawing_frequency)
    print("Frames drawn.")
    print("Encoding MP4 video.")
    animate_surfaces(surfaces, 'animation.mp4')
    print("Success! MP4 video produced.")
    print("Animation finished! Exiting normally.")

if __name__ == "__main__":
    main()
