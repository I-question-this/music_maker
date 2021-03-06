#!/usr/bin/env python3
"""GUI Interface for the program"""

__author__="Tyler Westland"

import argparse
import os
import pygame
from pygame import mixer
import sys
import tempfile

from maker.gui.assets import BACKGROUND_CAT_ASSET,\
                             BACKGROUND_DEAD_CAT_ASSET,\
                             BACKGROUND_SLEEPY_CAT_ASSET,\
                             BOKEMON_ASSET,\
                             LIGHTNING_BOLT_ASSET,\
                             NARUTO_ASSET,\
                             PIKACHU_ASSET,\
                             PLAY_BUTTON_ASSET
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
    window = pygame.display.set_mode((1000, 830))
    clock = pygame.time.Clock()

    # Prepare the backgrounds
    background_normal_image = pygame.transform.scale(
            pygame.image.load(BACKGROUND_CAT_ASSET), 
            (window.get_width(), window.get_height()))
    background_dead_image = pygame.transform.scale(
            pygame.image.load(BACKGROUND_DEAD_CAT_ASSET), 
            (window.get_width(), window.get_height()))
    background_sleepy_image = pygame.transform.scale(
            pygame.image.load(BACKGROUND_SLEEPY_CAT_ASSET), 
            (window.get_width(), window.get_height()))
    bokemon_image = pygame.transform.scale(
            pygame.image.load(BOKEMON_ASSET), 
            (70, 100))
    lightning_bolt_image = pygame.transform.scale(
            pygame.image.load(LIGHTNING_BOLT_ASSET),
            (50, 100))
    pikachu_image = pygame.transform.scale(
            pygame.image.load(PIKACHU_ASSET), 
            (70, 100))
    naruto_image = pygame.transform.scale(
            pygame.image.load(NARUTO_ASSET), 
            (50, 100))

    # Set the normal background
    background_image = background_normal_image

    play_button_image = pygame.image.load(PLAY_BUTTON_ASSET)
    play_button_rect = pygame.Rect(
            (325,675),
            (int(window.get_width()/3), 
             int(window.get_height()/5.5)))
    play_button_image = pygame.transform.scale(
            play_button_image, 
            (play_button_rect.width, play_button_rect.height))

    # Set up temporary save file location
    tempdir = tempfile.TemporaryDirectory()
    temp_wave = f"{tempdir.name}/temp.wav"
    # Set up mixer
    mixer.init()
    mixer.music.set_volume(0.05)

    # Create the notes
    all_sprites = pygame.sprite.Group()
    measure = Measure(2, 8, all_sprites)
    measure.move(145, 300)

    # main application loop
    run = True
    # Game states
    draw_lightning_bolt = False
    draw_bokemon = False
    draw_pikachu = False
    draw_naruto = False
    while run:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = pygame.mouse.get_pos()
                measure.check_mouse_click(mousex, mousey)

                mouse_rect = pygame.Rect((mousex, mousey), (0,0))
                if play_button_rect.contains(mouse_rect):
                    # Create the tune
                    tune = measure.to_tune()
                    # Crate the wave file
                    tune.save_to_file(temp_wave)
                    # Load the wave file
                    mixer.music.load(temp_wave)
                    # Play the wave file
                    mixer.music.play()
                    # Check for easer eggs
                    if "Dies Irae" in tune.easter_eggs:
                        background_image = background_dead_image
                    elif "Boring" in tune.easter_eggs:
                        background_image = background_sleepy_image
                    else:
                        background_image = background_normal_image

                    draw_lightning_bolt = "Parry Hotter" in tune.easter_eggs
                    draw_bokemon = "Bokemon" in tune.easter_eggs and\
                            "Boruto" in tune.easter_eggs
                    draw_pikachu = "Bokemon" in tune.easter_eggs and\
                            "Boruto" not in tune.easter_eggs
                    draw_naruto = "Boruto" in tune.easter_eggs

                    if draw_bokemon:
                        tune.key_signature = "F"
                    else:
                        tune.key_signature = "C#"

        # clear the display
        window.fill((255, 255, 255))
        
        # Draw background
        window.blit(background_image, (0,0))

        # Draw lighting bolt
        if draw_lightning_bolt:
            window.blit(lightning_bolt_image, (470,100)) 

        if draw_bokemon:
            window.blit(bokemon_image, (20,700)) 

        if draw_pikachu:
            window.blit(pikachu_image, (20,700)) 

        if draw_naruto:
            window.blit(naruto_image, (890,730)) 

        # Draw play button
        window.blit(play_button_image, play_button_rect)

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
