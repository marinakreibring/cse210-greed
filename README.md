# cse210-greed
cse210 week 4 developer
Greed is a game in which the player seeks to gather as many falling gems (*)as possible. Each gem adds 1 point to the score. If the player catches a rock (@), he looses 1 point. The game continues as long as the player wants more!
The game will consist of 8 classes. 
The entire game is controlled by the Director class. 
Class Color defines the colors.
Class Point defines the position of the pointer.
Classes KeyboardService and VideoService provide corresponding services.
Class Cast is a collection of actors in the game.
The Actor class is a superclass with Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
All these attributes are inherited by its derived class - class Artifact(Actor). Artifact also has his private attribute: points. 
This way the principle of inharitance is applied in this game.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- greed        (source code for game)
  +-- data              (data files for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Author
---
* Marina Kreibring (timarina1997@yahoo.com)