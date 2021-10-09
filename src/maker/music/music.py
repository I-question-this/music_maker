#!/usr/bin/env python3
"""Default template for my python files"""

__author__="Tyler Westland"

import argparse
import os
import sys

from pygame import mixer


def parse_arguments(args=None) -> None:
    """Returns the parsed arguments.
    Parameters
    ----------
    args: List of strings to be parsed by argparse.
        The default None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser(
            description="A default template for python",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("-o", "--output_file", help="Path to the output file.",
            default="output")
    parser.add_argument("-q", "--quiet", help="Don't print out non-errors",
                        default=False, action="store_true")
    args = parser.parse_args(args=args)
    return args


def main(input_file:str, quiet:bool=False, output_file:str="output") -> None:
    """Main function.

    Parameters
    ----------
    input_file: str
        Path the input file.
    output_file: str
        Path to the output file. Default is 'output'
    quiet: bool
        Rather non-errors should be printed. Default is False
    Returns
    -------
    ???
        Something useful.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    # Error check if the file even exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError("File not found: {}".format(input_file))

    # Starting the mixer
    mixer.init()
      
    # Loading the song
    mixer.music.load(input_file)
      
    # Setting the volume
    mixer.music.set_volume(0.7)
      
    # Start playing the song
    mixer.music.play()
      
    # infinite loop
    while True:
        print("Press 'p' to pause, 'r' to resume")
        print("Press 'e' to exit the program")
        query = input("  ")
          
        if query == 'p':
            # Pausing the music
            mixer.music.pause()     
        elif query == 'r':
            # Resuming the music
            mixer.music.unpause()
        elif query == 'e':
            # Stop the mixer
            mixer.music.stop()
            break

    return None


def cli_interface() -> None:
    """Get program arguments from command line and run main"""
    args = parse_arguments()
    try:
        main(**vars(args))
        sys.exit(0)
    except FileNotFoundError as exp:
        print(exp, file=sys.stderr)
        sys.exit(-1)


# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    cli_interface()
