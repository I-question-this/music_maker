#!/usr/bin/env python3
"""Play a saved tune file and optionally saves it."""

__author__="Tyler Westland"

import argparse
import json
import os
import sys
import tempfile
tempdir = tempfile.TemporaryDirectory()

from pygame import mixer

from maker.music.tune import Tune

def parse_arguments(args=None) -> None:
    """Returns the parsed arguments.
    Parameters
    ----------
    args: List of strings to be parsed by argparse.
        The default None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser(
            description="Play a saved tune file and optionally saves it.",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("tune_file", help="Path to the tune file.")
    parser.add_argument("-sw", "--save_wave", default=None,
            help="Path to save the wave file, default is to not save it.")
    save_wav: str=None
        
    args = parser.parse_args(args=args)
    return args


def main(tune_file:str, save_wave:str=None) -> None:
    """Main function.

    Parameters
    ----------
    tune_file: str
        Path to the tune file.
    save_wave: str=None
        Path to save the wav file, default is to not save it.
    Returns
    -------
    ???
        Something useful.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    with open(tune_file) as fin:
        tune = Tune.from_dict(json.load(fin))

    # Save wave form to temporary file
    if save_wave is None:
        save_wave = f"{tempdir.name}/temp.wav"
    tune.save_to_file(save_wave)

    # Starting the mixer
    mixer.init()
      
    # Loading the song
    mixer.music.load(save_wave)
      
    # Setting the volume
    mixer.music.set_volume(0.05)
      
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
