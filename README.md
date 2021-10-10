# What is this?
Created for the [2021 MakeUC Hackathon](https://makeuc.io/), this is a small chip tune player inspired by the 
[town tune in Animal Crossing](https://animalcrossing.fandom.com/wiki/Town_tune).

There are 16 notes:
+ G low - E high
+ ~: Rest
+ -: Hold (plays the previous note)
+ ?: Wild (plays a random note)
![Example tune](example_screenshot.png?raw=true)

# Easter Eggs
Putting specific sequences of notes will result in different things 
occurring.
Some are well known tunes, others are thematic sequences of notes.
## [Dies Irae](https://en.wikipedia.org/wiki/Dies_irae)
![Example of using Dies Irae](easter_egg_screenshots/dies_irae.png?raw=true)
## [Harry Potter](https://en.wikipedia.org/wiki/Music_of_the_Harry_Potter_films)
![Example of using Harry Potter](easter_egg_screenshots/harry_potter.png?raw=true)
## [Pokemon](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Theme)
![Example of using Pokemon](easter_egg_screenshots/pokemon.png?raw=true)
## [Naruto and Naruto Pikachu](https://en.wikipedia.org/wiki/Naruto)
![Example of using Naruto and Pokemon Together](easter_egg_screenshots/naruto_and_naruto_pokemon.png?raw=true)
## Sleepy -- Too much silence
![Example of sleepy kitty](easter_egg_screenshots/sleepy.png?raw=true)

# Demo
We posted a [demo video](https://youtu.be/MLxx63Jur7M) of this for 
[devpost](https://devpost.com/software/music-maker-2xf701) as part of the Hackathon

# Installing
## Pip
We suggest using a conda or virtual environment before installing.
After that one can install this package by running
```bash
pip install .
```
in the root directory of this repo.

One can then run the following command to start the program:
```bash
musicmaker-gui
```

## Dependencies
+ [synthesizer](https://github.com/yuma-m/synthesizer)
  + Only works on Linux and MacOS.
  + Go to linked Github to install required packages beyond Python.
+ [pygame](https://www.pygame.org/wiki/GettingStarted)
  + Shouldn't need anything beyond installing the package.
