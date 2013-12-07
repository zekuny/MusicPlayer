Re-use guidance
===============

###Existing functional files for music player:
* font: The folder font includes hy.ttf, which is used to change the default font you want to show in the music player.
* image: The folder image includes images for the music player, basically the images for background and buttons.
* music: The folder music includes sub-folders and music files. The sub-folders can contain it's own music files for classification purpose. If you do not choose a certain sub-folder, the default playing order is from the music files in parent folder to sub-folders.
* main.py: This includes logical structure for the program.
* MButton.py: This includes python codes for button functions.
* MStack.py: This includes python codes to store music file's path and name.

###Re-use: 
#### You may add music to music folder or change images for background and buttons.
#### There are many functions for you to realize:
* Add lyrics display.
* Change music background according to the singer of the Music.
* Add different play modes: random play, single cycle, etc.
* Add the function to search music.
* Add different style for playing music, say, heavy metal, country music, hip-pop, etc.
* Other functions you think that can make a better music player.

##### Notice: When you make any functional changes, you may add a separate .py file for the realization of functions and also modify the main.py to call these functions.
