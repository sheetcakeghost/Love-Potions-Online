# Modes 

In Ren'Py, a mode is a concise way of describing the type of an interaction. When a mode is reported to Ren'Py, user-defined callbacks can be run. These calbacks can be used to react to a change in mode, perhaps by reconfiguring the user interface. For example, one can cause a transition to occur when switching from ADV-mode to NVL-mode, or when going to a menu, etc.

The goal of the mode systems is to provide a powerful and flexible way of detecting and responding to these changes.

## Default Modes 

The following are the modes corresponding to built-in interactions:

start

This is the mode that Ren'Py is in when a new context is created, such as at the start of a game. Ren'Py never automatically enters this mode, but instead, initializes the list of modes to include start.

say

The mode Ren'Py enters when an ADV-mode say executes.

menu

The mode Ren'Py enters when an ADV-mode menu executes.

nvl

The mode Ren'Py enters when an NVL-mode say executes.

nvl\_menu

The mode Ren'Py enters when an NVL-mode menu executes.

pause

The mode Ren'Py enters when  is run. This is also the mode Ren'Py is in when a `pause` statement of indefinite duration occurs.

with

The mode Ren'Py enters when a transition introduced by the `with` statement occurs. This is also used for `pause` statement with a duration specified.

Note that the with mode is entered at the start of the with statement, which is after any preceding scene, show, or hide statements have been run.

screen

The mode Ren'Py enters when a screen is invoked using the `call screen` statement.

imagemap

The mode Ren'Py enters when an old-style imagemap is invoked using `renpy.imagemap()`.

input

The mode Ren'Py enters when text input is requested using the  function.

Other modes can be entered by calling the renpy.mode function.

renpy.get\_mode() 

Returns the current mode, or None if it is not defined.

renpy.mode(_mode_) 

Causes Ren'Py to enter the named mode, or stay in that mode if it's already in it.

## Mode Callbacks 

The  variable contains a list of mode callbacks that are invoked whenever Ren'Py enters a mode. The mode callbacks are called with two parameters:

mode

A string giving the name of the mode that we are entering.

old\_modes

A list of strings, giving the modes that the system has previously entered, ordered from most recent to least recent.

Note that when entering a mode we're already in, the first item in old\_modes will be equal to mode.

### Example Mode Callbacks 

This mode callback causes transitions to occur when switching from ADV to NVL mode, and vice-versa. This ships as part of Ren'Py, so there's no need to actually use it.

init python:
    def \_nvl\_adv\_callback(mode, old\_modes):

        old \= old\_modes\[0\]

        if config.adv\_nvl\_transition:
            if mode \== "nvl" or mode \== "nvl\_menu":
                if old \== "say" or old \== "menu":
                    nvl\_show(config.adv\_nvl\_transition)

        if config.nvl\_adv\_transition:
            if mode \== "say" or mode \== "menu":
                if old \== "nvl" or old \== "nvl\_menu":
                    nvl\_hide(config.nvl\_adv\_transition)

    config.mode\_callbacks.append(\_nvl\_adv\_callback)
