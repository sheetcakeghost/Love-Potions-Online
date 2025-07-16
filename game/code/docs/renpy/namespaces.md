# Namespaces

Ren'Py uses namespaces to organize variables and methods. This file contains descriptions of some of the namespaces Ren'Py uses, primarily to help editors provide autocompletion and documentation.

achievement

A namespace that contains functions that grant and manage . This also contains much of the Steamworks integration.

bubble:

A namespace that contains variables that control the display of .

build:

A namespace that contains variables that control the .

config:

A namespace that contains variables that control the  of Ren'Py. These variables should be set at init time (in `init python` blocks or with the `define`) and should not be changed once the game has started.

define:

The define namespace contains functions that define new variables, such as families of transitions.

director:

The director namespace contains functions that control the , which lets you insert images and music into the game interactively.

define gui

The gui namespace contains functions that control the . These variables only matter if you are using the default GUI system, and may not be used if you've replaced it. Define statements that affect the gui namespace are re-run when the translaton changes.

iap

The iap namespace contains functions that control the .

im

**Note: Most functions in the im namespace are deprecated.**

The im namespace contains image manipulators, which load or manipulate images on the CPU. Most functions here can be accomplished on the GPU using .

layeredimage

 are a way to combine multiple images into a single image, using attributes and conditions to control which images are shown. The layeredimage namespace contains classes that allow you to create and manipulate layered images from Python, the equivalent of the `layeredimage` statement.

persistent

The persistent namespace contains  data. Fields on this object start as None, and retain their values between runs of the game, even when not loading a save slot.

The values of fields on the persistent object should be of Python-supplied types, like booleans, numbers, strings, lists, tuples, dicts, and sets. Classes you define should not be assigned to the persistent object.

preferences

The  namespace contains variables that contain preferences. While these can be read and set, the most common use is with the `default` statement, using syntax like:

default preferences.fullscreen \= True

preferences.volume

The  namespace contains variables that set the default volumes for each mixer. These should be set using the `default` statement, like:

default preferences.volume.music \= 0.5

renpy

The renpy namespace contains function and classes that are part of the Ren'Py engine itself. These can be the equivalent of Ren'Py language statements, or can introduce functionality that does not merit a dedicated statement.

renpy.audio.filter

The renpy.audio.filter namespace contains classes and functions that create .

renpy.music

The renpy.audio.music namespace contains functions that control the . These functions work with the music channel by default.

renpy.sound

The renpy.audio.sound namespace contains functions that control the . These functions work with the sound channel by default. Most functions are documented under their renpy.music equivalents.

style

The style namespace contains styles and functions that manipulate styles. Styles are used to control the appearance of text, images, and other elements in Ren'Py. Using the `style` statement is preferred to using the style namespace directly.

ui

**Note: Most functions in the ui namespace are deprecated.**

The ui namespace contains older functions and classes used to display user interface elements. With the exception of ui.adjustment, ui.interact, ui.callsinnewcontext, and ui.invokesinnewcontext, these functions are obsolete.

updater

The updater namespace contains functions, classes, and variables that control the .

- - -

Built with  using a  provided by .

jQuery(function () { SphinxRtdTheme.Navigation.enable(false); });