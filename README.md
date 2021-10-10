# What is this?
This is a small chip tune player inspired by the 
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
## Sleepy -- Too much silence
![Example of sleepy kitty](easter_egg_screenshots/sleepy.png?raw=true)

# Installing
## Pip
We suggest using a conda or virtual environment before installing.
After that one can install this package by running
```bash
pip install .
```
in the root directory of this repo.

## Dependencies
+ [synthesizer](https://github.com/yuma-m/synthesizer)
  + Only works on Linux and MacOS.
  + Go to linked Github to install required packages beyond Python.
+ [pygame](https://www.pygame.org/wiki/GettingStarted)
  + Shouldn't need anything beyond installing the package.
