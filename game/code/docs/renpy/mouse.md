# Custom Mouse Cursors

Ren'Py has two systems for creating custom mouse cursors. The first takes advantage of the hardware mouse cursor, while the second uses Ren'Py to draw a displayable as the mouse cursor.

The hardware mouse cursor has the advantages:

*   It is very fast.
    
*   It is very low overhead, leaving Ren'Py time to do other things.
    

And the limitation:

*   Cursors are limited to small sizes. 32x32 is guaranteed, while 64x64 seems to work widely.
    
*   Cursors are limited to sequences of image files.
    

Using Ren'Py to draw a displayable as a cursor inverts these restrictions. While the cursors can be anything Ren'Py can draw, Ren'Py needs to do the drawing. When triple buffering is enabled on a computer, a lag can be present that isn't for the harware cursor.

## Hardware Mouse Cursor

The hardware cursor is controlled by the  variable. This variable consists of a dictionary, that maps mouse names to a list of frames. Each frame is a 3-component tuple that contains an image file, and then X and Y offsets within that image.

For example:

define config.mouse \= { }
define config.mouse\['default'\] \= \[ ( "gui/arrow.png", 0, 0) \]
define config.mouse\['spin' \] \= \[
    ( "gui/spin0.png", 7, 7 ),
    ( "gui/spin1.png", 7, 7 ),
    ( "gui/spin2.png", 7, 7 ),
    ( "gui/spin3.png", 7, 7 ),
    ( "gui/spin4.png", 7, 7 ),
    ( "gui/spin5.png", 7, 7 ),
    ( "gui/spin6.png", 7, 7 ),
    ( "gui/spin7.png", 7, 7 ),
\]

When an animation consists of multiple frames, the frames are played back at 20fps. Ren'Py will only change the cursor when the image or offsets change.

The following table lists the various states that the cursor can be in and the corresponding usage:

| State | Usage |
| --- | --- |
| `default` | Used at all times unless another state is specified. It should always be present, as it is used when a more specific key is absent |
| `say` | Used when the player is on the "Say" screen. |
| `with` | Used during transitions. |
| `menu` | Used when the player is in a menu (for example, choice). |
| `prompt` | Used when the player is prompted for input. |
| `imagemap` | Used on an imagemap. |
| `button` | Used when the player is hovering over a button/imagebutton. |
| `pause` | Used during pause, renpy.pause() |
| `mainmenu` | Used in the main menu. |
| `gamemenu` | Used in the game menu. |

Every key can have an optional `pressed_` prefix, which indicates the cursor to use when the mouse is pressed. For instance, `pressed_button` is used when the user clicks on a button. To define a default pressed cursor style, use `pressed_default` key. It is used when no other pressed cursor is defined.

For example:

define config.mouse \= { }
define config.mouse\['default'\] \= \[ ( "gui/arrow.png", 0, 0) \]
define config.mouse\['pressed\_default'\] \= \[ ( "gui/arrow\_pressed.png", 0, 0) \]
define config.mouse\['button'\] \= \[ ( "gui/arrow\_button.png", 0, 0) \]
define config.mouse\['pressed\_button'\] \= \[ ( "gui/arrow\_button\_pressed.png", 0, 0) \]
define config.mouse\['menu'\] \= \[ ( "gui/arrow\_menu.png", 0, 0) \] \# This cursor will be used when the player is in a menu
\# Since there is no "pressed\_menu" cursor, "pressed\_default" cursor will be used instead

## Displayable Mouse Cursor

A displayable cursor uses the  variable, and the MouseDisplayable displayable. As an example:

image mouse spin:
    "gui/spin0.png"
    rotate 0.0
    linear 1.0 rotate 360.0

    \# Pause so image prediction can happen.
    pause 1.0

    repeat

define config.mouse\_displayable \= MouseDisplayable(
    "gui/arrow.png", 0, 0).add("spin", "mouse spin", 9.9, 9.9)

_class_ MouseDisplayable(_cursor_, _x_, _y_)

A displayable that wraps a mouse cursor displayable, and causes it to move across the screen when the player moves their mouse.

cursor

A displayable that is used to draw the mouse.

x, y

The coordinates of the hotspot, relative to the upper left corner of the mouse, in virtual pixels.

add(_name_, _cursor_, _x_, _y_)

This adds a second cursor, that is used when the name mouse is displayed. This returns the MouseDisplayable, so that calls to this method can be chained.

## Using Mouse Cursors

The usual way to use a mouse cursor is to provide the `mouse` property, giving the name of the cursor, to something that can be focused in a screen. (A button or bar.) For example:

screen test():
    textbutton "Mouse Test" action NullAction() mouse "spin"

It's also possible to use  to set the mouse cursor globally:

$ default\_mouse \= "spin"
