#!/usr/bin/env python3
"""GUI Interface for the program"""

__author__="Tyler Westland"

import argparse
import os
import pygame
import sys

from maker.gui.measure import Measure


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
    args = parser.parse_args(args=args)
    return args


def main() -> None:
    """Main function.

    Parameters
    ----------
    Returns
    -------
    ???
        Something useful.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    """
    window = pygame.display.set_mode((820, 500))
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    # main application loop
    run = True
    # Test single note on a bar
    measure = Measure(2, 8, all_sprites)
    measure.move(10, 10)

    while run:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = pygame.mouse.get_pos()
                measure.check_mouse_click(mousex, mousey)

        # clear the display
        window.fill((255, 255, 255))

        # Draw everything
        all_sprites.draw(window)

        # update the display
        pygame.display.flip()

        # limit frames per second
        clock.tick(60)

    pygame.quit()

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
