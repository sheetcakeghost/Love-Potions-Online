# Advanced GUI

This section has some odds and ends about advanced usage of the GUI.

## Python Functions

There are some Python functions that support the GUI.

gui.button\_properties(_kind_)

Given a kind of button, returns a dictionary giving standard style properties for that button. This sets:

As described below.

To gui.kind\_borders.padding (if it exists).

To gui.kind\_width (if it exists).

To gui.kind\_height (if it exists).

(Note that if kind is the string "nvl\_button", this will look for the gui.nvl\_button\_background variable.)

The background is a frame that takes its background picture from the first existing one of:

*   gui/button/kind\_\[prefix\_\].background.png
    
*   gui/button/\[prefix\_\].background.png
    

If a gui variables named gui.kind\_borders exists, it's used. Otherwise,  is used. If gui.kind\_tile exists, it determines if the borders are tiled, else  controls tiling.

For what \ documentation.

gui.init(_width_, _height_, _fov\=75_)

Initializes the gui.

width

The width of the default window.

height

The height of the default window.

fov

The field of view of the 3d stage.

gui.rebuild()

Rebuilds the GUI.

Note: This is a very slow function.

gui.text\_properties(_kind\=None_, _accent\=False_)

Given a kind of button, returns a dictionary giving standard style properties for that button. This sets: Given a kind of textbutton, returns a dictionary giving standard style properties for the text inside that button. This sets:

To gui.kind\_text\_font, if it exists.

To gui.kind\_text\_size, if it exists.

To gui.kind\_text\_xalign, if it exists.

To gui.kind\_text\_xalign, if it exists.

To "subtitle" if gui.kind\_text\_xalign is greater than zero and less than one.

There are also a number of variables that set the text  style property:

color

To gui.kind\_text\_color, if it exists. If the variable is not set, and accent is True, sets the text color to the default accent color.

insensitive\_color

To gui.kind\_text\_insensitive\_color, if it exists.

idle\_color

To gui.kind\_text\_idle\_color, if it exists.

hover\_color

To gui.kind\_text\_hover\_color, if it exists.

selected\_color

To gui.kind\_text\_selected\_color, if it exists.

All other  are available. When kind is not None,  are also available. For example, gui.kind\_text\_outlines sets the outlines style property, gui.kind\_text\_kerning sets kerning, and so on.

gui.variant(_f_, _variant\=None_)

A decorator that causes a function to be called when the gui is first initialized, and again each time the gui is rebuilt. This is intended to be used as a function decorator, of the form:

@gui.variant
def small():
    gui.text\_size \= 30
    \# ...

It can also be called with f (a function) and variant (a string), giving the variant name.

gui.button\_text\_properties(kind=None, accent=False):

An obsolete alias for .

### More on gui.rebuild

The gui.rebuild function is a rather slow function that updates the GUI to reflect the current state of Ren'Py. What it does is:

*   Re-runs all of the `define` statements that define variables in the gui namespace.
    
*   Re-runs all of the `translate python` blocks for the current language.
    
*   Re-runs all of the `style` statements.
    
*   Rebuilds all of the styles in the system.
    

Note that `init python` blocks are not re-run on `gui.rebuild`. In this way,

define gui.text\_size \= persistent.text\_size

and:

init python:
    gui.text\_size \= persistent.text\_size

are different.

### The default statement, the gui namespace, and gui.rebuild

The `default` statement has changed semantics when applied to the `gui` namespace. When applied to a variable in the `gui` namespace, the default statement runs interleaved with the define statement, and the default statements are not re-run when  is called.

What this means is that if we have:

default gui.accent\_color \= "#c04040"
define gui.hover\_color \= gui.accent\_color

The first time the game is run, the accent color will be set, and then the hover color will be set to the accent color. (Both are then used to set various style colors.)

However, if as part of the game script, we have:

$ gui.accent\_color \= "#4040c0"
$ gui.rebuild()

Ren'Py will only re-run the define, so it will set the hover color to the accent color, and then update the styles. This makes it possible to have parts of the GUI that change as the game progresses.

## GUI Preferences

Ren'Py also supports a GUI preference system, consisting of a single function and a pair of actions.

gui.SetPreference(_name_, _value_, _rebuild\=True_)

This Action sets the gui preference with name to value.

rebuild

If true, the default,  is called to make the changes take effect. This should generally be true, except in the case of multiple gui.SetPreference actions, in which case it should be False in all but the last one.

This is a very slow action, and probably not suitable for use when a button is hovered.

gui.TogglePreference(_name_, _a_, _b_, _rebuild\=True_)

This Action toggles the gui preference with name between value a and value b. It is selected if the value is equal to a.

rebuild

If true, the default,  is called to make the changes take effect. This should generally be true, except in the case of multiple gui.SetPreference actions, in which case it should be False in all but the last one.

This is a very slow action, and probably not suitable for use when a button is hovered.

gui.preference(_name_, _default\=..._)

This function returns the value of the gui preference with name.

default

If given, this value becomes the default value of the gui preference. The default value must be given the first time the preference is used.

### Example

The GUI preference system is used by calling  when defining variables, with the name of the preference and the default value. For example, one can use GUI preferences to define the text font and size.

define gui.text\_font \= gui.preference("font", "DejaVuSans.ttf")
define gui.text\_size \= gui.preference("size", 22)

It's then possible to use the  and  actions to add change the values of the preferences. Here's some examples that can be added to the preferences screen.

vbox:
    style\_prefix "check"
    label \_("Options")
    textbutton \_("OpenDyslexic") action gui.TogglePreference("font", "OpenDyslexic-Regular.otf", "DejaVuSans.ttf")

vbox:
    style\_prefix "radio"
    label \_("Text Size")
    textbutton \_("Small") action gui.SetPreference("size", 20)
    textbutton \_("Medium") action gui.SetPreference("size", 22)
    textbutton \_("Big") action gui.SetPreference("size", 24)
