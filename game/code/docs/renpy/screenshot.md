# Screenshots

Ren'Py includes built-in functionality for taking screenshots of the game, as well as of displayables in the game. The latter is suitable for creating "paper dolls" made of multiple displayables and saving them to disk for the player's later use, such as an avatar creator.

When Ren'Py takes a screenshot, of the entire screen or a displayable, the screenshot will be taken at the drawable size, after window scaling and High DPI adjustments are applied. This generally captures what the user is seeing or would be seeing, rather than the native size of the assets.

By default, capturing a screenshot is bound to the 's' key.

There are a few screenshot-related actions and screen functions.

*   
    
*   
    
*   
    

## Functions

There are also functions that can be used to take screenshots:

renpy.render\_to\_file(_d_, _filename_, _width\=None_, _height\=None_, _st\=0.0_, _at\=None_, _resize\=False_)

Renders a displayable or Render, and saves the result of that render to a file. The render is performed by Ren'Py's display system, such that if the window is upscaled the render will be upscaled as well.

d

The displayable or Render to render. If a Render, width, height, st, and at are ignored.

filename

A string, giving the name of the file to save the render to. This is interpreted as relative to the base directory. This must end with .png.

width

The width to offer d, in virtual pixesl. If None, .

height

The height to offer d, in virtual pixels. If None, .

st

The time of the render, in the shown timebase.

at

The time of the rendem in the animation timebase. If None, st is used.

resize

If True, the image will be resized to the virtual size of the displayable or render. This may lower the quality of the result.

This function may only be called after the Ren'Py display system has started, so it can't be called during the init phase or before the first interaction.

Ren'Py not rescan files while the game is running, so this shouldn't be used to sythesize assets that are used as part of the game.

renpy.render\_to\_surface(_d_, _width\=None_, _height\=None_, _st\=0.0_, _at\=None_, _resize\=False_)

This takes a displayable or Render, and returns a pygame\_sdl2 surface. The render is performed by Ren'Py's display system, such that if the window is upscaled the render will be upscaled as well.

d

The displayable or Render to render. If a Render, width, height, st, and at are ignored.

width

The width to offer d, in virtual pixesl. If None, .

height

The height to offer d, in virtual pixels. If None, .

st

The time of the render, in the shown timebase.

at

The time of the rendem in the animation timebase. If None, st is used.

resize

If True, the surface will be resized to the virtual size of the displayable or render. This may lower the quality of the result.

This function may only be called after the Ren'Py display system has started, so it can't be called during the init phase or before the first interaction.

renpy.screenshot(_filename_)

Saves a screenshot in filename.

Returns True if the screenshot was saved successfully, False if saving failed for some reason.

The  and  variables control the file the screenshot is saved in.

renpy.screenshot\_to\_bytes(_size_)

Returns a screenshot as a bytes object, that can be passed to im.Data(). The bytes will be a png-format image, such that:

$ data \= renpy.screenshot\_to\_bytes((640, 360))
show expression im.Data(data, "screenshot.png"):
    align (0, 0)

Will show the image. The bytes objects returned can be stored in save files and persistent data. However, these may be large, and care should be taken to not include too many.

size

The size the screenshot will be resized to. If None, the screenshot will be resized, and hence will be the size of the player's window, without any letterbars.

This function may be slow, and so it's intended for save-like screenshots, and not realtime effects.
