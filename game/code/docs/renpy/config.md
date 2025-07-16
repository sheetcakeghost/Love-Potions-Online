# Configuration Variables

Configuration variables control the behavior of Ren'Py's implementation, allowing Ren'Py itself to be customized in a myriad of ways. These range from the common (such as changing the screen size) to the obscure (adding new kinds of archive files).

Ren'Py's implementation makes the assumption that, once the GUI system has initialized, configuration variables will not change. Changing configuration variables outside of `init` blocks can lead to undefined behavior. Configuration variables are not part of the save data.

Most configuration variables are easily set using a `define` statement:

define config.rollback\_enabled \= False

Dict and list variables can be populated using `define` or in an `init python` block:

define config.preload\_fonts += \["OrthodoxHerbertarian.ttf"\]
define config.adjust\_attributes\["eileen"\] \= eileen\_adjust\_function

init python hide:
    def inter\_cbk():
        \# this is a terrible callback
        renpy.notify("Interacting !")

    config.interact\_callbacks.append(inter\_cbk)

## Project Info

define config.name \= ""

This should be a string giving the name of the game. This is included as part of tracebacks and other log files, helping to identify the version of the game being used.

define config.version \= ""

This should be a string giving the version of the game. This is included as part of tracebacks and other log files, helping to identify the version of the game being used.

define config.window\_icon \= None

If not None, this is expected to be the filename of an image giving an icon that is used for the game's main window. This does not set the icon used by windows executables and mac apps, as those are controlled by .

define config.window\_title \= None

The static portion of the title of the window containing the Ren'Py game.  is appended to this to get the full title of the window.

If None, the default, this defaults to the value of .

## Auto-Forward Mode

define config.afm\_bonus \= 25

The number of bonus characters added to every string when auto-forward mode is in effect.

define config.afm\_callback \= None

If not None, a Python function that is called to determine if it is safe to auto-forward. The intent is that this can be used by a voice system to disable auto-forwarding when a voice is playing.

define config.afm\_characters \= 250

The number of characters in a string it takes to cause the amount of time specified in the auto forward mode preference to be delayed before auto-forward mode takes effect.

define config.afm\_voice\_delay \= .5

The number of seconds after a voice file finishes playing before AFM can advance text.

## Callbacks

These take functions that are called when certain events occur. These are not the only callbacks - ones corresponding to more specific features are listed in the section on that feature.

define config.after\_default\_callbacks \= \

A list of functions that are called (with no arguments) whenever default statements are processed. The default statements are run after the init phase, but before the game starts; when the a save is loaded; after rollback; before lint; and potentially at other times.

Similar to the default statement, these callbacks are a good place to add data to the game that does not exist, but needs to.

define config.context\_callback \= None

This is a callback that is called with no arguments when Ren'Py enters a new context, such as a menu context.

define config.interact\_callbacks \= \

A list of functions that are called (without any arguments) when an interaction is started or restarted.

define config.label\_callbacks \= \

This is a list of callbacks that are called whenever a labels is reached. The callbacks are called with two arguments. The first is the name of the label. The second is True if the label was reached through jumping, calling, or creating a new context, and False otherwise.

define config.periodic\_callbacks \= \

This is a list of functions that are called, with no arguments, at around 20Hz.

define config.python\_callbacks \= \

A list of functions. The functions in this list are called, without any arguments, whenever a Python block is run outside of the init phase.

One possible use of this would be to have a function limit a variable to within a range each time it is adjusted.

The functions may be called while Ren'Py is starting up, before the start of the game proper, and potentially before the variables the function depends on are initialized. The functions are required to deal with this, perhaps by using `hasattr(store, 'varname')` to check if a variable is defined.

define config.python\_exit\_callbacks \= \

A list of functions that are called when Ren'Py is about to exit to the operating system. This is intended to be used to deinitalize python modules.

Much of Ren'Py is deinitalized before these functions are called, so it's not safe to use Ren'Py functions in these callbacks.

define config.scene\_callbacks \= \

A list of functions that are called when the scene statement runs, or  is called. The functions are called with a single argument, the layer that the scene statement is called on. These functions are called after the layer is cleared, but before the optional image is added, if present.

Ren'Py may call renpy.scene for its own purposes, so it's recommended to check the layer name before acting on these callbacks.

define config.start\_callbacks \= \

A list of callbacks functions that are called with no arguments after the init phase, but before the game (including the splashscreen) starts. This is intended to be used by frameworks to initialize variables that will be saved.

The default value of this variable includes callbacks that Ren'Py uses internally to implement features such as nvl-mode. New callbacks can be appended to this list, but the existing callbacks should not be removed.

define config.start\_interact\_callbacks \= \

A list of functions that are called (without any arguments) when an interaction is started. These callbacks are not called when an interaction is restarted.

define config.statement\_callbacks \= \

A list of functions that are called when a statement is executed. These functions are generally called with the name of the statement in question. However, there are some special statement names.

"say"

Normal say statements.

"say-bubble"

Say statements in bubble mode.

"say-nvl"

Say statements in NVL mode.

"say-bubble"

Say statements in bubble mode.

"say-centered"

Say statments using the `centered` character.

"menu":

Normal menu statements.

"menu-nvl"

Menu statements in NVL mode.

"menu-with-caption"

Menu statements with a caption.

"menu-nvl-with-caption"

Menu statements with a caption in NVL mode.

There is a default callback in this list that is used to implement `window auto`.

define config.with\_callback \= None

If not None, this should be a function that is called when a  occurs. This function can be responsible for putting up transient things on the screen during the transition. The function is called with two arguments: the transition that is occurring, and the transition it is paired with. The latter is None except in the case of the implicit None transition produced by an inline with statement, in which case it is the inline transition that produced the with None. It is expected to return a transition, which may or may not be the transition supplied as its argument.

## Characters and Dialogue

define config.all\_character\_callbacks \= \

A list of callbacks that are called by all characters. This list is prepended to the list of character-specific callbacks. Ren'Py includes its own callbacks at the start of this list.

define config.character\_callback \= None

The default value of the callback parameter of .

define config.character\_id\_prefixes \= \

This specifies a list of style property prefixes that can be given to a . When a style prefixed with one of the given prefix is given, it is applied to the displayable with that prefix as its ID.

For example, the default GUI adds "namebox" to this. When a Character is given the namebox\_background property, it sets  on the displayable in the say screen with the id "namebox".

define config.say\_allow\_dismiss \= None

If not None, this should be a function. The function is called with no arguments when the user attempts to dismiss a . If this function returns True, the dismissal is allowed, otherwise it is ignored.

define config.say\_arguments\_callback \= None

If not None, this should be a function that takes the speaking character, followed by positional and keyword arguments. It's called whenever a say statement occurs, even when the statement doesn't explicitly pass arguments. The arguments passed to the callback always include an interact argument, and include the others provided in the say statement (if any).

This should return a pair, containing a tuple of positional arguments (almost always empty), and a dictionary of keyword arguments (almost always with at least interact in it). Those will replace the arguments passed to the callback.

For example:

def say\_arguments\_callback(who, interact\=True, color\="#fff"):
    return (), { "interact" : interact, "what\_color" : color }

config.say\_arguments\_callback \= say\_arguments\_callback

define config.say\_sustain\_callbacks \= \

A list of functions that are called, without arguments, before the second and later interactions caused by a line of dialogue with pauses in it. Used to sustain voice through pauses.

## Choice Menus

define config.auto\_choice\_delay \= None

If not None, this variable gives a number of seconds that Ren'Py will pause at an in-game menu before picking a random choice from that menu. We'd expect this variable to always be set to None in released games, but setting it to a number will allow for automated demonstrations of games without much human interaction.

define config.menu\_arguments\_callback \= None

If not None, this should be a function that takes positional and/or keyword arguments. It's called whenever a menu statement runs, with the arguments to that menu statement.

This should return a pair, containing a tuple of positional arguments (almost always empty), and a dictionary of keyword arguments.

define config.menu\_include\_disabled \= False

When this variable is set, choices disables with the if statement are included as disabled buttons.

define config.menu\_window\_subtitle \= ""

The  variable is set to this value when entering the main or game menus.

define config.narrator\_menu \= True

If true, narration inside a menu is displayed using the narrator character. Otherwise, narration is displayed as captions within the menu itself.

## Display

define config.adjust\_view\_size \= None

If not None, this should be a function taking two arguments, the width and height of the physical window. It is expected to return a tuple giving the width and height of the OpenGL viewport, the portion of the screen that Ren'Py will draw pictures to.

This can be used to configure Ren'Py to only allow certain sizes of screen. For example, the following allows only integer multiples of the original screen size:

init python:

    def force\_integer\_multiplier(width, height):
        multiplier \= min(width / config.screen\_width, height / config.screen\_height)
        multiplier \= max(int(multiplier), 1)
        return (multiplier \* config.screen\_width, multiplier \* config.screen\_height)

    config.adjust\_view\_size \= force\_integer\_multiplier

define config.display\_start\_callbacks \= \

This contains a list of functions that are called after Ren'Py displays a window, but before the first frame is rendered. The main use of this is to allow libraries to gain access to resources that need an initializd gui, like OpenGL functions.

define config.gl\_clear\_color \= "#000"

The color that the window is cleared to before images are drawn. This is mainly seen as the color of the letterbox or pillarbox edges drawn when aspect ratio of the window (or monitor in fullscreen mode) does not match the aspect ratio of the game.

define config.gl\_lod\_bias \= \-0.5

The default value of the  uniform, which controls the mipmap level Ren'Py uses.

define config.gl\_resize \= True

Determines if the user is allowed to resize an OpenGL-drawn window.

define config.gl\_test\_image \= "black"

The name of the image that is used when running the OpenGL performance test. This image will be shown for 5 frames or .25 seconds, on startup. It will then be automatically hidden.

define config.minimum\_presplash\_time \= 0.0

The minimum amount of time, in seconds, a presplash, Android presplash, or iOS LaunchImage is displayed for. If Ren'Py initializes before this amount of time has been reached, it will sleep to ensure the image is shown for at least this amount of time. The image may be shown longer if Ren'Py takes longer to start up.

define config.nearest\_neighbor \= False

Uses nearest-neighbor filtering by default, to support pixel art or melting players' eyes.

define config.physical\_height \= None

If set, this is the default height of the window containing the Ren'Py game, in pixels. If not set, the height of the window defaults to .

define config.physical\_width \= None

If set, this is the default height of the window containing the Ren'Py game, in pixels. If not set, the height of the window defaults to .

define config.screen\_height \= 600

The virtual height of the game, in pixels. If  is not set, this is also the default size of the window containing the game. Usually set by  to a much larger size.

define config.screen\_width \= 800

The virtual width of the game, in pixels. If  is not set, this is also the default size of the window containing the game. Usually set by  to a much larger size.

define config.shader\_part\_filter \= None

If not None, this is a function that is called with a tuple of shader part names. It should return a new tuple of shader parts that will be used.

## File I/O

define config.file\_open\_callback \= None

If not None, this is a function that is called with the file name when a file needs to be opened. It should return a file-like object, or None to load the file using the usual Ren'Py mechanisms. Your file-like object must implement at least the read, seek, tell, and close methods.

One may want to also define a  that matches this.

define config.open\_file\_encoding \= False

If not False, this is the encoding that  uses when its encoding parameter is none. This is mostly used when porting Python 2 games that used  extensively to Python 3, to have those files open as text by default.

This gets its default value from the RENPY\_OPEN\_FILE\_ENCODING environment variable.

## History

define config.history\_callbacks \= \

This contains a list of callbacks that are called before Ren'Py adds a new object to \_history\_list. The callbacks are called with the new HistoryEntry object as the first argument, and can add new fields to that object.

Ren'Py uses history callbacks internally, so creators should append their own callbacks to this list, rather than replacing it entirely.

define config.history\_current\_dialogue \= True

If true, the current dialogue will appear in the history screen.

define config.history\_length \= None

The number of entries of dialogue history Ren'Py keeps. This is set to 250 by the default gui.

## Input, Focus, and Events

define config.allow\_screensaver \= True

If True, the screensaver may activite while the game is running. If False, the screensaver is disabled.

define config.controller\_blocklist \= \

A list of strings, where each string is matched against the GUID of a game controller. These strings are mached as a prefix to the controller GUID (which cand be found in `log.txt`), and if matched, prevent the controller from being initialized.

define config.focus\_crossrange\_penalty \= 1024

This is the amount of penalty to apply to moves perpendicular to the selected direction of motion, when moving focus with the keyboard.

define config.input\_caret\_blink \= 1.0

If not False, sets the blinking period of the default caret, in seconds.

define config.keymap \= { ... }

This variable contains a keymap giving the keys and mouse buttons assigned to each possible operation. Please see the section on  for more information.

define config.longpress\_duration \= 0.5

The amount of time the player must press the screen for a longpress to be recognized on a touch device.

define config.longpress\_radius \= 15

The number of pixels the touch must remain within for a press to be recognized as a longpress.

define config.longpress\_vibrate \= .1

The amount of time the device will vibrate for after a longpress.

define config.pad\_bindings \= { ... }

An equivalent of  for gamepads. Please see 's section about pad bindings for more information.

define config.pass\_controller\_events \= False

If true, pygame-like CONTROLLER events are passed to Displayables event handlers. If not, those are consumed by Ren'Py.

define config.pass\_joystick\_events \= False

If true, pygame-like JOYSTICK events are passed to Displayables event handlers. If not, those are consumed by Ren'Py.

define config.web\_input \= True

If True, the web platform will use the browser's input system to handle . If False, Ren'Py's own input system will be used. The browser's input system supports more languages, virtual keyboards, and other conveniences, but is not as customizable.

This may be changed at init time, and also in translate python blocks.

To only use the browser's input system on touchscreen devices, use:

define config.web\_input \= renpy.variant("touch")

## Layered Images

define config.layeredimage\_offer\_screen \= True

This variable sets the default value for the `offer_screen` property of layeredimages. See  for more information.

## Layers

define config.bottom\_layers \= \

This is a list of names of layers that are displayed above all other layers, and do not participate in a transition that is applied to all layers. If a layer name is listed here, it should not be listed in `` config.layers` `` or .

define config.choice\_layer \= "screens"

The layer the choice screen (used by the menu statement) is shown on.

define config.clear\_layers \= \

A list of names of layers to clear when entering the main and game menus.

define config.context\_clear\_layers \= \

A list of layers that are cleared when entering a new context.

define config.default\_tag\_layer \= "master"

The layer an image is shown on if its tag is not found in .

define config.detached\_layers \= \

These are layers which do not get automatically added to scenes. They are always treated as  and intended for use with the  displayable for embedding.

define config.interface\_layer \= "screens"

The layer that built-in screens are shown on.

define config.layer\_clipping \= { ... }

Controls layer clipping. This is a map from layer names to (x, y, height, width) tuples, where x and y are the coordinates of the upper-left corner of the layer, with height and width giving the layer size.

If a layer is not mentioned in config.layer\_clipping, then it will take up the full size of its container. Typically this will be the screen, unless being shown inside a  displayable.

define config.layer\_transforms \= { }

A dictionary mapping layer names to lists of transforms. These transforms are applied last, after `show layer` and `camera` transforms have already been applied.

If the layer name is None, then the transforms are applied to to the combination of all layers in , after any transition has been applied.

define config.layers \= \

This variable gives a list of all of the layers that Ren'Py knows about, in the order that they will be displayed to the screen. (The lowest layer is the first entry in the list.) Ren'Py uses the layers "master", "transient", "screens", and "overlay" internally (and possibly others in future versions), so they should always be in this list.

The  can add layers to this variable without needing to know the original contents.

define config.overlay\_layers \= \

This is a list of all of the overlay layers. Overlay layers are cleared before the overlay functions are called. "overlay" should always be in this list.

define config.say\_layer \= "screens"

The layer the say screen is shown on. This layer should be in .

define config.sticky\_layers \= \

A list of layer names that will, when a tag is shown on them, take precedence over that tag's entry in  for the duration of it being shown.

define config.tag\_layer \= { }

A dictionary mapping image tag strings to layer name strings. When an image is shown without a specific layer name, the image's tag is looked up in this dictionary to get the layer to show it on. If the tag is not found here,  is used.

define config.top\_layers \= \

This is a list of names of layers that are displayed above all other layers, and do not participate in a transition that is applied to all layers. If a layer name is listed here, it should not be listed in `` config.layers` `` or .

define config.transient\_layers \= \

This variable gives a list of all of the transient layers. Transient layers are layers that are cleared after each interaction. "transient" should always be in this list.

## Media (Music, Sound, and Video)

define config.audio\_filename\_callback \= None

If not None, this is a function that is called with an audio filename, and is expected to return a second audio filename, the latter of which will be played.

This is intended for use when an a games has audio file formats changed, but it's not destired to update the game script.

define config.auto\_channels \= { "audio" : ( "sfx", "", ""  ), ... }

This is used to define automatic audio channels. It's a map the channel name to a tuple containing 3 components:

*   The mixer the channel uses.
    
*   A prefix that is given to files played on the channel.
    
*   A suffix that is given to files played on the channel.
    

define config.auto\_movie\_channel \= True

If True, and the play argument is given to , an audio channel name is automatically generated for each movie.

 takes precendece over this variable.

define config.context\_fadein\_music \= 0

The amount of time in seconds Ren'Py spends fading in music when the music is played due to a context change. (Usually, when the game is loaded.)

define config.context\_fadeout\_music \= 0

The amount of time in seconds Ren'Py spends fading out music when the music is played due to a context change. (Usually, when the game is loaded.)

define config.enter\_sound \= None

If not None, this is a sound file that is played when entering the game menu.

define config.exit\_sound \= None

If not None, this is a sound file that is played when exiting the game menu.

define config.fadeout\_audio \= 0.016

The default audio fadeout time that's used to fade out audio, when audio is stopped with the `stop` statement or , or when a new audio track is started with the `play` statement or . This is not used when queued audio beings.

A short fadeout is the default to prevent clicks and pops when audio is stopped or changed.

define config.game\_menu\_music \= None

If not None, a music file to play when at the game menu.

define config.has\_music \= True

If true, the "music" mixer is enabled. The default GUI will hide the music mixer if this is false. When this, config.has\_sound, and config.has\_voice are all false, the default GUI will hide the main mixer as well.

define config.has\_sound \= True

If true, the "sfx" mixer is enabled. The default GUI will hide the sound mixer if this is false.

define config.has\_voice \= True

If true, the "voice" mixer is enabled. The default GUI will hide the voice mixer if this is false. Ren'Py will disable the voice system if this is false.

define config.main\_menu\_music \= None

If not None, a music file to play when at the main menu.

define config.main\_menu\_music\_fadein \= 0.0

The number of seconds to take to fade in .

define config.main\_menu\_stop\_channels \= \

A list of channels that are stopped when entering or returning to the main menu.

define config.mipmap\_movies \= False

The default value of the mipmap argument to .

define config.movie\_mixer \= "music"

The mixer that is used when a  automatically defines a channel for video playback.

define config.play\_channel \= "audio"

The name of the audio channel used by , , and .

define config.preserve\_volume\_when\_muted \= False

If False, the default, the volume of channels are shown as 0 and changing it disables mute when the channel is mute. Otherwise, It is shown and adjustable while keeping mute.

define config.single\_movie\_channel \= None

If not None, and the play argument is give to , this is the name used for the channel the movie is played on. This should not be "movie", as that name is reserved for Ren'Py's internal use.

define config.skip\_sounds \= False

If True, non-looping audio will not be played when Ren'Py is skipping.

define config.sound \= True

If True, sound works. If False, the sound/mixer subsystem is completely disabled.

define config.sound\_sample\_rate \= 48000

The sample rate that the sound card will be run at. If all of your wav files are of a lower rate, changing this to that rate may make things more efficient.

define config.web\_video\_base \= "./game"

When playing a movie in the web browser, this is a URL that is appended to to the movie filename to get the full URL to play the movie from. It can include directories in it, so "" would also be fine.

This allows large movie files to be hosted on a different server than the rest of the game.

define config.web\_video\_prompt \= \_("Touch to play the video.")

On Mobile Safari on iOS, by default, the player will need to click to play a movie with sound. This variable gives the message that's used to prompt players to click.

define config.webaudio\_required\_types \= \

When running on the web platform, Ren'Py will check the browser to see if it can play audio files of these mime types. If the browser can, it is used to play the files. If not, a slower and potentially skip prone wasm decoder is used.

By default, the browser's web audio system is used on Chrome and Firefox, and wasm is used on safari. If your game only uses mp3 audio, this can be changed using

define config.webaudio\_required\_types \= \[ "audio/mpeg" \]

To used the faster web audio system on Safari as well.

## Mouse

define config.mouse \= None

This variable controls the use of user-defined mouse cursors. If None, the system mouse is used, which is usually a black-and-white mouse cursor.

Otherwise, this should be a dictionary giving the mouse animations for various mouse types. Keys used by the default library include `default`, `say`, `with`, `menu`, `prompt`, `imagemap`, `button`, `pause`, `mainmenu`, and `gamemenu`. The `default` key should always be present, as it is used when a more specific key is absent. Keys can have an optional prefix `pressed_` to indicate that the cursor will be used when the mouse is pressed.

Each value in the dictionary should be a list of (image, xoffset, yoffset) tuples, representing frames.

image

The mouse cursor image. The maximum size for this image varies based on the player's hardware. 32x32 is guaranteed to work everywhere, while 64x64 works on most hardware. Larger images may not work.

xoffset

The offset of the hotspot pixel from the left side of the cursor.

yoffset

The offset of the hotspot pixel from the top of the cursor.

The frames are played back at 20Hz, and the animation loops after all frames have been shown.

See  for more information and examples.

define config.mouse\_displayable \= None

If not None, this should either be a displayable, or a callable that returns a displayable. The callable may return None, in which case Ren'Py proceeds if the displayable is None.

If a displayable is given, the mouse cursor is hidden, and the displayable is shown above anything else. This displayable is responsible for positioning and drawing a sythetic mouse cursor, and so should probably be a  or something very similar.

See  for more information.

define config.mouse\_focus\_clickthrough \= False

If true, clicks that cause a window to be focused will be processed normally. If false, such clicks will be ignored.

define config.mouse\_hide\_time \= 30

The mouse is hidden after this number of seconds has elapsed without any mouse input. This should be set to longer than the expected time it will take to read a single screen, so mouse users will not experience the mouse appearing then disappearing between clicks.

If None, the mouse will never be hidden.

## Paths

define config.archives \= \

A list of archive files that will be searched for images and other data. The entries in this should consist of strings giving the base names of archive files, without the .rpa extension.

The archives are searched in the order they are found in this list. A file is taken from the first archive it is found in.

At startup, Ren'Py will automatically populate this variable with the names of all archives found in the game directory, sorted in reverse ascii order. For example, if Ren'Py finds the files `data.rpa`, `patch01.rpa`, and `patch02.rpa`, this variable will be populated with `['patch02', 'patch01', 'data']`.

define config.gamedir \= ...

The full path leading to the game's `game/` directory. This is a read-only variable. There is no guarantee that any file will be there, typically on platforms such as android.

define config.savedir \= ...

The complete path to the directory in which the game is saved. This should only be set in a `python early` block. See also , which generates the default value for this if it is not set during a `python early` block.

define config.search\_prefixes \= \

A list of prefixes that are prepended to filenames that are searched for.

define config.searchpath \= \

A list of directories that are searched for images, music, archives, and other media, but not scripts. This is initialized to a list containing "common" and the name of the game directory.

## Quit

define config.quit\_action : Action

The action that is called when the user clicks the quit button on a window. The default action prompts the user to see if they want to quit the game.

define config.quit\_callbacks \= \

A list of functions that are called without any arguments when Ren'Py is either terminating or reloading the script. This is intended to free resources, such as opened files or started threads, that arte created inside init code, if such things aren't freed automatically.

define config.quit\_on\_mobile\_background \= False

If True, the mobile app will quit when it loses focus, rather than saving and restoring its state. (See also , which controls this behavior.)

## Replay

define config.after\_replay\_callback \= None

If not None, a function that is called with no arguments after a replay completes.

define config.replay\_scope \= { "\_game\_menu\_screen" : "preferences", ... }

A dictionary mapping variables in the default store to the values the variables will be given when entering a replay.

## Rollback

define config.call\_screen\_roll\_forward \= False

The value is used when the roll\_forward property of a screen is None.

define config.ex\_rollback\_classes \= \

A list of class objects that should not generate a warning that the object supported rollback in the past, but do not now. If you have intentionally removed rollack support from a class, place the class object in this list and the warning will be suppressed.

Chances are, you don't want to use this - you want to add `object` to the list of base types for your class.

define config.fix\_rollback\_without\_choice \= False

This option determines how the built-in menus or imagemaps behave during fixed rollback. The default value is False, which means that only the previously selected menu option remains clickable. If set to True, the selected option is marked but no options are clickable. The user can progress forward through the rollback buffer by clicking.

define config.hard\_rollback\_limit \= 100

This is the number of steps that Ren'Py will let the user interactively rollback. Set this to 0 to disable rollback entirely, although we don't recommend that, as rollback is useful to let the user see text he skipped by mistake.

define config.pause\_after\_rollback \= False

If False, the default, rolling back will skip any pauses (timed or not) and stop only at other interactions such as dialogues, menus... If True, renpy will include timeless pauses to the valid places a rollback can take the user.

define config.rollback\_enabled \= True

Should the user be allowed to rollback the game? If set to False, the user cannot interactively rollback.

define config.rollback\_length \= 128

When there are more than this many statements in the rollback log, Ren'Py will consider trimming the log. This also covers how many steps Ren'Py will rollback when trying to load a save when the script has changed.

Decreasing this below the default value may cause Ren'Py to become unstable.

define config.rollback\_side\_size \= .2

If the rollback side is enabled, the fraction of the screen on the rollback side that, when clicked or touched, causes a rollback to occur.

## Saving and Loading

define config.after\_load\_callbacks \= \

A list of functions that are called (with no arguments) when a load occurs.

If these callbacks change data (for example, migrating data from an old version of the game),  should be called to prevent the player from rolling back and reverting the changes.

define config.auto\_load \= None

If not None, the name of a save file to automatically load when Ren'Py starts up. This is intended for developer use, rather than for end users. Setting this to "1" will automatically load the game in save slot 1.

define config.autosave\_callback \= None

A callback or list of callbacks or Actions that will be called after each time a background autosave happens. Although actions may be used, the Return action will not function.

If a non-Action callback shows a displayable or screen,  should be called.

::

define config.autosave\_callback = Notify("Autosaved.")

define config.autosave\_frequency \= 200

Roughly, the number of interactions that will occur before an autosave occurs. To disable autosaving, set  to False, don't change this variable.

define config.autosave\_on\_choice \= True

If True, Ren'Py will autosave upon encountering an in-game choice. (When  is called.)

define config.autosave\_on\_input \= True

If True, Ren'Py will autosave when the user inputs text. (When  is called.)

define config.autosave\_on\_quit \= True

If True, Ren'Py will attempt to autosave when the user attempts to quit, return to the main menu, or load a game over the existing game. (To save time, the autosave occurs while the user is being prompted to confirm his or her decision.)

define config.autosave\_prefix\_callback \= None

If not None, this is a function that is called with no arguments, and return the prefix of autosave files. The default prefix used is "auto-", which means the autosave slots will be "auto-1", "auto-2", etc.

define config.autosave\_slots \= 10

The number of slots used by autosaves.

define config.file\_slotname\_callback \= None

If not None, this is a function that is used by the  to convert a page and name into a slot name that can be passed to the .

page

This is a string containing the name of the page that is being accessed. This is a string, usually containing a number, but it also may contain special values like "quick" or "auto".

name

The is a string that contains the name of the slot on the page. It may also contain a regular expression pattern (like r'd+'), in which case the same pattern should be included in the result.

The default behavior is equivalent to:

def file\_slotname\_callback(page, name):
    return page + "-" + name

config.file\_slotname\_callback \= file\_slotname\_callback

One use of this is to allow the game to apply a prefix to save files.

See also .

define config.has\_autosave \= True

If true, the game will autosave. If false, no autosaving will occur.

define config.load\_failed\_label \= None

If a string, this is a label that is jumped to when a load fails because the script has changed so much that Ren'Py can't recover. Before performing the load, Ren'Py will revert to the start of the last statement, then it will clear the call stack.

This may also be a function. If it is, the function is called with no arguments, and is expected to return a string giving the label.

define config.loadable\_callback \= None

When not None, a function that's called with a filename. It should return True if the file is loadable, and False if not. This can be used with  or .

define config.quicksave\_slots \= 10

The number of slots used by quicksaves.

define config.save \= True

If True, Ren'Py will allow the user to save the game. If False, Ren'Py will not allow the user to save the game, and will not show existing saves.

define config.save\_directory \= "..."

This is used to generate the directory in which games and persistent information are saved. The name generated depends on the platform:

Windows

%APPDATA%/RenPy/save\_directory

Mac OS X

~/Library/RenPy/save\_directory

Linux/Other

~/.renpy/save\_directory

Setting this to None creates a "saves" directory underneath the game directory. This is not recommended, as it prevents the game from being shared between multiple users on a system. It can also lead to problems when a game is installed as Administrator, but run as a user.

This must be set with either the define statement, or in a `python early` block. In either case, this will be run before any other statement, and so it should be set to a string, not an expression.

To locate the save directory, read  instead of this variable.

define config.save\_dump \= False

If set to True, Ren'Py will create the file save\_dump.txt whenever it saves a game. This file contains information about the objects contained in the save file. Each line consists of a relative size estimate, the path to the object, information about if the object is an alias, and a representation of the object.

define config.save\_json\_callbacks \= \

A list of callback functions that are used to create the json object that is stored with each save and marked accessible through  and .

Each callback is called with a Python dictionary that will eventually be saved. Callbacks should modify that dictionary by adding JSON-compatible Python types, such as numbers, strings, lists, and dicts. The dictionary at the end of the last callback is then saved as part of the save slot.

The dictionary passed to the callbacks may have already have keys beginning with an underscore `_`. These keys are used by Ren'Py, and should not be changed.

For example:

init python:
    def jsoncallback(d):
        d\["playername"\] \= player\_name

    config.save\_json\_callbacks.append(jsoncallback)

`FileJson(slot)` and `renpy.slot_json(slot)` will recover the state of the `d` dict-like object as it was at the moment the game was saved. The value of the `player_name` variable at the moment the game was saved is also accessible by `FileJson(slot, "playername")`.

define config.save\_on\_mobile\_background \= True

If True, the mobile app will save its state when it loses focus. The state is saved in a way that allows it to be automatically loaded (and the game to resume its place) when the app starts again.

define config.save\_persistent \= True

If True, Ren'Py will save persistent data. If False, persistent data will not be saved, and changes to persistent will be lost when the game ends.

define config.save\_physical\_size \= True

If True, the physical size of the window will be saved in the preferences, and restored when the game resumes.

define config.save\_token\_keys \= \

A list of keys that the game will trust when loading a save file. This can be used to allow the game's creator to distribute save files that will be loaded without displaying a warning.

To allow the save token for the current computer to be trusted in this way, open the  and run:

print(renpy.get\_save\_token\_keys())

This will print the keys out in log.txt. The value can then be used to define this config.save\_token\_keys. This variable must be set with a define statement, or in a python early block.

define config.thumbnail\_height \= 75

The height of the thumbnails that are taken when the game is saved. These thumbnails are shown when the game is loaded. Please note that the thumbnail is shown at the size it was taken at, rather than the value of this setting when the thumbnail is shown to the user.

This is changed by the default GUI.

define config.thumbnail\_width \= 100

The width of the thumbnails that are taken when the game is saved. These thumbnails are shown when the game is loaded. Please note that the thumbnail is shown at the size it was taken at, rather than the value of this setting when the thumbnail is shown to the user.

This is changed by the default GUI.

## Screen Language

define config.always\_shown\_screens \= \

A list of names of screens that Ren'Py will always show, even in menus, and when the interface is hidden. If a screen in this list is ever not shown, that screen will be re-shown. This is used by Ren'Py, which may modify the list.

Setting  is usually more appropriate.

define config.context\_copy\_remove\_screens \= \

Contains a list of screens that are removed when a context is copied for rollback or saving.

define config.help \= None

The default value for the  action.

define config.help\_screen \= "help"

The name of the screen shown by pressing f1 on the keyboard, or by the  action under certain circumstances.

define config.imagemap\_auto\_function : Callable

A function that expands the auto property of a screen language  or  statement into a displayable. It takes the value of the auto property, and the desired image, one of: "insensitive", "idle", "hover", "selected\_idle", "selected\_hover", or "ground". It should return a displayable or None.

The default implementation formats the auto property with the desired image, and then checks if the computed filename exists.

define config.keep\_side\_render\_order \= True

If True, the order of substrings in the Side positions will be determine the order of children render.

define config.menu\_clear\_layers \= \

A list of layer names (as strings) that are cleared when entering the game menu.

define config.notify : Callable

This is called by  or  with a single message argument, to display the notification. The default implementation is . This is intended to allow creators to intercept notifications.

define config.overlay\_screens \= \

A list of screens that are displayed when the overlay is enabled, and hidden when the overlay is suppressed. (The screens are shown on the screens layer, not the overlay layer.)

define config.per\_frame\_screens \= \

This is a list of strings giving the name of screens that are updated once per frame, rather than once per interaction. Ren'Py uses this internally, so if you add a screen, append the name rather than replacing the list in its entirety.

define config.transition\_screens \= True

If True, screens will participate in transitions, dissolving from the old state of the screen to the new state of the screen. If False, only the latest state of the screen will be shown.

define config.variants \= \

A list of screen variants that are searched when choosing a screen to display to the user. This should always end with None, to ensure that the default screens are chosen. See .

## Screenshots

define config.pre\_screenshot\_actions \= \

A list of actions that are run before a screenshot is taken. This is intended to hide transient elements that should not be shown in the screenshot.

define config.screenshot\_callback : Callable

A function that is called when a screenshot is taken. The function is called with a single parameter, the full filename the screenshot was saved as.

define config.screenshot\_crop \= None

If not None, this should be a (x, y, height, width) tuple. Screenshots are cropped to this rectangle before being saved.

define config.screenshot\_pattern \= "screenshot%04d.png"

The pattern used to create screenshot files. This pattern is applied (using Python's %-formatting rules) to the natural numbers to generate a sequence of filenames. The filenames may be absolute, or relative to config.renpy\_base. The first filename that does not exist is used as the name of the screenshot.

Directories are created if they do not exist.

See also , which is used in preference to this variable if not None.

## Self-Voicing / Text to Speech

define config.tts\_substitutions \= \

This is a list of (pattern, replacement) pairs that are used to perform substitutions on text before it is passed to the text-to-speech engine, so that the text-to-speech engine can pronounce it correctly.

Patterns may be either strings or regular expressions, and replacements must be strings.

If the pattern is a string, it is escaped, then prefixed and suffixed with r'' (to indicate it must begin and end at a word boundary), and then compiled into a regular expression. When the pattern is a string, the replacement is also escaped.

If the pattern is a regular expression, it is used as-is, and the replacement is not escaped.

The substitutions are performed in the order they are given. If a substitution matches the string, the match is checked to see if it is in title case, upper case, or lower case ; and if so the corresponding casing is performed on the replacement. Once this is done, the replacement is applied.

For example:

define config.tts\_substitutions \= \[
    ("Ren'Py", "Ren Pie"),
\]

Will cause the string "Ren'Py is pronounced ren'py." to be voiced as if it were "Ren Pie is pronounced ren pie."

define config.tts\_voice \= None

If not None, a string giving a non-default voice that is used to play back text-to-speech for self voicing. The possible choices are platform specific, and so this should be set in a platform-specific manner. (It may make sense to change this in translations, as well.)

## Showing Images

define config.adjust\_attributes \= { }

If not None, this is a dictionary. When a statement or function that contains image attributes executes or is predicted, the tag is looked up in this dictionary. If it is not found, the None key is looked up in this dictionary.

If either is found, they're expected to be a function. The function is given an image name, a tuple consisting of the tag and any attributes. It should return an adjusted tuple, which contains and a potential new set of attributes.

As this function may be called during prediction, it must not rely on any state.

define config.cache\_surfaces \= False

If True, the underlying data of an image is stored in RAM, allowing image manipulators to be applied to that image without reloading it from disk. If False, the data is dropped from the cache, but kept as a texture in video memory, reducing RAM usage.

define config.conditionswitch\_predict\_all \= False

The default value of the predict\_all argument for  and , which determines if all possible displayables are shown.

define config.default\_attribute\_callbacks \= { }

When a statement or function that contains image attributes executes or is predicted, and the tag is not currently being shown, it's looked up in this dictionary. If it is not found, the None key is looked up instead.

If either is found, they're expected to be a function. The function is given an image name, a tuple consisting of the tag and any attributes. It should return an iterable which contains any additional attributes to be applied when an image is first shown.

The results of the function are treated as additive-only, and any explicit conflicting or negative attributes will still take precedence.

As this function may be called during prediction, it must not rely on any state.

define config.default\_transform \= ...

When a displayable is shown using the show or scene statements, the transform properties are taken from this transform and used to initialize the values of the displayable's transform.

The default transform is .

define config.displayable\_prefix \= { }

See .

define config.hide \= renpy.hide

A function that is called when the  is executed. This should take the same arguments as renpy.hide.

define config.image\_cache\_size \= None

If not None, this is used to set the size of the , as a multiple of the screen size. This number is multiplied by the size of the screen, in pixels, to get the size of the image cache in pixels.

If set too large, this can waste memory. If set too small, images can be repeatedly loaded, hurting performance.

define config.image\_cache\_size\_mb \= 300

This is used to set the size of the , in megabytes. If  is False, an image takes 4 bytes per pixel, otherwise it takes 8 bytes per pixel.

If set too large, this can waste memory. If set too small, images can be repeatedly loaded, hurting performance. If not none,  is used instead of this variable.

define config.keep\_running\_transform \= True

If True, showing an image without supplying a transform or ATL block will cause the image to continue the previous transform an image with that tag was using, if any. If False, the transform is stopped.

define config.max\_texture\_size \= (4096, 4096)

The maximum size of an image that Ren'Py will load as a single texture. This is important for 3d models, while 2d images will be split into multiple textures if necessary.

Live2d will adjust this to fit the largest live2d texture.

define config.optimize\_texture\_bounds \= True

When True, Ren'Py will scan images to find the bounding box of the non-transparent pixels, and only load those pixels into a texture.

define config.predict\_statements \= 32

This is the number of statements, including the current one, to consider when doing predictive image loading. A breadth-first search from the current statement is performed until this number of statements is considered, and any image referenced in those statements is potentially predictively loaded. Setting this to 0 will disable predictive loading of images.

define config.scene \= renpy.scene

A function that's used in place of  by the . Note that this is used to clear the screen, and  is used to show a new image. This should have the same signature as .

define config.show \= renpy.show

A function that is used in place of  by the  and  statements. This should have the same signature as , and pass unknown keyword arguments unchanged.

define config.speaking\_attribute \= None

If not None, this should be a string giving an image attribute, which is added to the character's image tag when the character is speaking, and removed when the character stops.

This is applied to the image on the default layer for the tag, which can be set using .

This is very similar to temporary attributes shown using @ in dialogue lines. The attribute is not removed when the text apparition animation ends, but when the dialogue window gets dismissed.

define config.tag\_transform \= { ... }

A dictionary mapping image tag strings to transforms or lists of transforms. When an image is newly-shown without an at clause, the image's tag is looked up in this dictionary to find a transform or list of transforms to use.

define config.tag\_zorder \= { }

A dictionary mapping image tag strings to zorders. When an image is newly-shown without a zorder clause, the image's tag is looked up in this dictionary to find a zorder to use. If no zorder is found, 0 is used.

define config.transform\_uses\_child\_position \= True

If True, transforms will inherit  from their child. If not, they won't.

## Skipping

define config.allow\_skipping \= True

If set to False, the user is not able to skip over the text of the game. See .

define config.fast\_skipping \= False

Set this to True to allow fast skipping outside of developer mode.

define config.skip\_delay \= 75

The amount of time that dialogue will be shown for, when skipping statements using ctrl, in milliseconds. (Although it's nowhere near that precise in practice.)

define config.skip\_indicator \= True

If True, the library will display a skip indicator when skipping through the script.

## Text and Fonts

define config.font\_hinting \= { None : "auto" }

This is a dictionary from a string containing the font filename to a string giving one of the font hinting modes in . When  is True, the value is looked up in this dictionary, and the resulting mode is used.

If no key is found, None is looked up, and the resulting mode is used.

define config.font\_name\_map \= { }

This is a map from (font name) to (font filepath/fontgroup). Font names simplify and shorten `{font}` tags, and gives them access to the  feature.

define config.font\_transforms \= { ... }

This is used to create new font transforms for accessibility purposes. The font transforms can be activated by `Preferences()` using "font transform" as the first argument.

The dictionary maps strings giving the nam use to a function. The function is called with a font or  as the only argument, and is expected to return a font or font group. For example, the dejavusans transform is defined as:

init python:
    def dejavusans(f):
        return "DejaVuSans.ttf"

    config.font\_transforms\["dejavusans"\] \= dejavusans

define config.font\_replacement\_map \= { }

This is a map from (font, bold, italics) to (font, bold, italics), used to replace a font with one that's specialized as having bold and/or italics. For example, if you wanted to have everything using an italic version of `Vera.ttf` use `VeraIt.ttf` instead, you could write:

init python:
    config.font\_replacement\_map\["Vera.ttf", False, True\] \= ("VeraIt.ttf", False, False)

Please note that these mappings only apply to specific variants of a font. In this case, requests for a bold italic version of vera will get a bold italic version of vera, rather than a bold version of the italic vera.

define config.hyperlink\_handlers \= { ... }

A dictionary mapping a hyperlink protocol to the handler for that protocol. A handler is a function that takes the value (everything after the :) and performs some action. If a value is returned, the interaction ends. Otherwise, the click is ignored and the interaction continues.

define config.hyperlink\_protocol \= "call\_in\_new\_context"

The protocol that is used for hyperlinks that do not have a protocol assigned to them. See the  text tag for a description as to what the possible protocols mean.

define config.mipmap\_text \= False

The default value of the mipmap argument to , including text used in screen statements.

define config.new\_substitutions \= True

If True, Ren'Py will apply new-style (square-bracket) substitutions to all text displayed.

define config.old\_substitutions \= True

If True, Ren'Py will apply old-style (percent) substitutions to text displayed by the  and  statements.

define config.preload\_fonts \= \

A list of the names of TrueType and OpenType fonts that Ren'Py should load when starting up. Including the name of a font here can prevent Ren'Py from pausing when introducing a new typeface.

define config.replace\_text \= None

If not None, a function that is called with a single argument, a text to be displayed to the user. The function can return the same text it was passed, or a replacement text that will be displayed instead.

The function is called after substitutions have been performed and after the text has been split on tags, so its argument contains nothing but actual text. All displayed text passes through the function: not only dialogue text, but also user interface text.

This can be used to replace specific ASCII sequences with corresponding Unicode characters, as demonstrated by the following:

def replace\_text(s):
    s \= s.replace("'", u'2019') \# apostrophe
    s \= s.replace('--', u'2014') \# em dash
    s \= s.replace('...', u'2026') \# ellipsis
    return s
config.replace\_text \= replace\_text

See also

define config.say\_menu\_text\_filter \= None

If not None, then this is a function that is given the text found in strings in the  and  statements. It is expected to return new (or the same) strings to replace them.

This runs very early in the say and menu statement processing, before translation and substitutions are applied. For a filter that runs later, see .

define config.textshader\_callbacks \= { }

This is dictionary that maps strings to callables. When  with the string are used, the function is called to return a string giving another textshader. This can be used to make a textshader that changes based on a persistent variable, for example.

## Transitions

define config.adv\_nvl\_transition \= None

A transition that is used to show the NVL-mode window when showing ADV-mode text directly after NVL-mode text.

define config.after\_load\_transition \= None

A transition that is used after loading, when entering the loaded game.

define config.end\_game\_transition \= None

The transition that is used to display the main menu after the game ends normally, either by invoking return with no place to return to, or by calling .

define config.end\_splash\_transition \= None

The transition that is used to display the main menu after the end of the splashscreen.

define config.enter\_replay\_transition \= None

If not None, a transition that is used when entering a replay.

define config.enter\_transition \= None

If not None, this variable should give a transition that will be used when entering the game menu.

define config.enter\_yesno\_transition \= None

If not None, a transition that is used when entering the yes/no prompt screen.

define config.exit\_replay\_transition \= None

If not None, a transition that is used when exiting a replay.

define config.exit\_transition \= None

If not None, this variable should give a transition that will be performed when exiting the game menu.

define config.exit\_yesno\_transition \= None

If not None, a transition that is used when exiting the yes/no prompt screen.

define config.game\_main\_transition \= None

If not None, a transition that is used when returning to the main menu from the game menu, using the  action.

define config.intra\_transition \= None

The transition that is used between screens of the game and main menu. (That is, when the screen is changed with .)

define config.nvl\_adv\_transition \= None

A transition that is used to hide the NVL-mode window when showing ADV-mode text directly after NVL-mode text.

define config.pause\_with\_transition \= False

If false,  is always used by the `pause` statement. If true, when given a delay, `pause 5` is equivalent to `with Pause(5)`.

define config.say\_attribute\_transition \= None

If not None, a transition to use when the image is changed by a say statement with image attributes.

define config.say\_attribute\_transition\_callback : Callable

This is a function that return a transition to apply and a layer to apply it on

This should be a function that takes four arguments, the image tag being shown, a mode parameter, a set containing pre-transition tags and a set containing post-transition tags. Where the value of the mode parameter is one of:

*   "permanent", for permanent attribute change (one that lasts longer than the current say statement).
    
*   "temporary", for a temporary attribute change (one that is restored at the end of the current say statement).
    
*   "both", for a simultaneous permanent and temporary attribute change (one that in part lasts longer than the current say statement, and in part is restored at the end of the current say statement).
    
*   "restore", for when a temporary (or both) change is being restored.
    

This should return a 2-component tuple, consisting of:

*   The transition to use, or None if no transition should occur.
    
*   The layer the transition should be on, either a string or None. This is almost always None.
    

The default implementation of this returns (config.say\_attribute\_transition, config.say\_attribute\_transition\_layer).

define config.say\_attribute\_transition\_layer \= None

If not None, this must be a string giving the name of a layer. (Almost always "master".) The say attribute is applied to the named layer, and Ren'Py will not pause to wait for the transition to occur. This will have the effect of transitioning in the attribute as dialogue is shown.

define config.window\_hide\_transition \= None

The transition used by the window hide statement when no transition has been explicitly specified.

define config.window\_show\_transition \= None

The transition used by the window show statement when no transition has been explicitly specified.

## Transition Control

define config.implicit\_with\_none \= True

If True, then by default the equivalent of a  statement will be performed after interactions caused by dialogue, menus input, and imagemaps. This ensures that old screens will not show up in transitions.

define config.load\_before\_transition \= True

If True, the start of an interaction will be delayed until all images used by that interaction have loaded. (Yeah, it's a lousy name.)

define config.mipmap\_dissolves \= False

The default value of the mipmap argument to , , , and .

define config.overlay\_during\_with \= True

True if we want overlays to be shown during , or False if we'd prefer that they be hidden during the with statements.

## Translation

define config.default\_language \= None

If not None, this should be a string giving the default language that the game is translated into by the translation framework.

See  for more details.

define config.defer\_styles \= False

When true, the execution of style statements is deferred until after all `translate python` blocks have executed. This lets a `translate python` block update variables that are then used in style (not translate style) statements.

While this defaults to False, it's set to True when  is called.

define config.defer\_tl\_scripts \= Fasle

When True, avoids loading scripts in the tl directory until the language is selected. See .

define config.enable\_language\_autodetect \= False

If true, Ren'Py will attempt to determine the name of the language to use based on the locale of the player's system. If successful, this language will be used as the default language.

define config.locale\_to\_language\_function : Callable

A function that determines the language the game should use, based on the user's locale. It takes 2 string arguments that give the ISO code of the locale and the ISO code of the region.

It should return a string giving the name of a translation to use, or None to use the default translation.

define config.new\_translate\_order \= True

Enables the new order of style and translate statements introduced in .

define config.translate\_clean\_stores \= \

A list of named stores that are cleaned to their state at the end of the init phase when the translation language changes.

define config.translate\_ignore\_who \= \

A list of strings giving characters that will not have tanslations generated. This is useful for characters that are used for debugging or note purposes. This compares against string value of the expression in the statement. (So "e" will match `e` but not `l`, even if e and l are the same object.)

## Voice

See also

define config.auto\_voice \= None

This may be a string, a function, or None. If None, auto-voice is disabled.

If a string, this is formatted with the `id` variable bound to the identifier of the current line of dialogue. If this gives an existing file, that file is played as voice audio.

If a function, the function is called with a single argument, the identifier of the current line of dialogue. The function is expected to return a string. If this gives an existing file, that file is played as voice audio.

See  for more details.

define config.emphasize\_audio\_channels \= \

A list of strings giving audio channel names.

If the "emphasize audio" preference is enabled, when one of the audio channels listed starts playing a sound, all channels that are not listed in this variable have their secondary audio volume reduced to  over  seconds.

When no channels listed in this variable are playing audio, all channels that are not listed have their secondary audio volume raised to 1.0 over  seconds.

For example, setting this to `[ 'voice' ]` will lower the volume of all non-voice channels when a voice is played.

define config.emphasize\_audio\_time \= 0.5

See above.

define config.emphasize\_audio\_volume \= 0.5

See above.

define config.voice\_filename\_format \= "{filename}"

A string that is formatted with the string argument to the voice statement to produce the filename that is played to the user. For example, if this is "{filename}.ogg", the `voice "test"` statement will play `test.ogg`.

## Window Management

define config.choice\_empty\_window \= None

If not None, and a choice menu (usually invoked with the `menu` statement) does not have a caption, this function is called with the arguments ("", interact=False).

The expected use of this is:

define config.choice\_empty\_window \= extend

Doing this displays repeats the last line of dialogue as the caption of the menu, if no other caption is given.

Other implementations are possible, but it's assumed that this will always display a dialogue window.

define config.empty\_window : Callable

This is called with no arguments when \_window is True, and no window has been shown on the screen. (That is, no call to  has occurred.) It's expected to show an empty window on the screen, and return without causing an interaction.

The default implementation of this uses the narrator character to display a blank line without interacting.

define config.window \= None

This controls the default method of dialogue window management. If not None, this should be one of "show", "hide", or "auto".

When set to "show", the dialogue window is shown at all times. When set to "hide", the dialogue window is hidden when not in a say statement or other statement that displays dialogue. When set to "auto", the dialogue window is hidden before scene statements, and shown again when dialogue is shown.

This sets the default. Once set, the default can be changed using the `window show`, `window hide` and `window auto` statements. See  for more information.

define config.window\_auto\_hide \= \

A list of statements that cause `window auto` to hide the empty dialogue window.

define config.window\_auto\_show \= \

A list of statements that cause `window auto` to show the empty dialogue window.

## Developer

### Compatibility

define config.label\_overrides \= { }

This variable gives a way of causing jumps and calls of labels in Ren'Py script to be redirected to other labels. For example, if you add a mapping from "start" to "mystart", all jumps and calls to "start" will go to "mystart" instead.

define config.script\_version \= None

If not None, this is interpreted as a script version. Ren'Py uses the script version to enable some compatibility features, if necessary. If None, we assume this is a latest-version script.

This is normally set in a file added by the Ren'Py launcher when distributions are built, and so generally shouldn't be set.

### Development

define config.console \= False

This enables the console in the case  is not true.

define config.developer \= "auto"

If set to True, developer mode is enabled. Developer mode gives access to the shift+D developer menu, shift+R reloading, and various other features that are not intended for end users.

This can be True, False, or "auto". If "auto", Ren'Py will detect if the game has been packaged into a distribution, and set config.developer as appropriate.

### Debugging

define config.clear\_log \= False

If true, the log created by  is cleared each time Ren'Py starts.

define config.debug\_image\_cache \= False

If True, Ren'Py will write information about the  to image\_cache.txt.

define config.debug\_prediction \= False

If True, Ren'Py will will write information about and errors that occur during prediction (of execution flow, images, and screens) to log.txt and the console.

define config.debug\_sound \= False

Enables debugging of sound functionality. This disables the suppression of errors when generating sound. However, if a sound card is missing or flawed, then such errors are normal, and enabling this may prevent Ren'Py from functioning normally. This should always be False in a released game.

define config.debug\_text\_overflow \= False

When true, Ren'Py will log text overflows to text\_overflow.txt. A text overflow occurs when a  displayable renders to a size larger than that allocated to it. By setting this to True and setting the  and  style properties of the dialogue window to the window size, this can be used to report cases where the dialogue is too large for its window.

define config.disable\_input \= False

When true,  terminates immediately and returns its default argument.

define config.exception\_handler \= None

If not None, this should be a function that takes three arguments:

*   A string giving the text of a traceback, abbreviated so that it only includes creator-written files.
    
*   The full text of the traceback, including both creator-written and Ren'Py files.
    
*   The path to a file containing a traceback method.
    

This function can present the error to a user in any way fit. If it returns True, the exception is ignored and control is transferred to the next statement. If it returns False, the built-in exception handler is use. This function may also call  to transfer control to some other label.

define config.lint\_character\_statistics \= True

If true, and  is true, the lint report will include statistics about the number of dialogue blocks spoken for each character. The chanracter statistics are disabled when the game is packaged, to prevent spoilers.

define config.lint\_hooks \= \

This is a list of functions that are called, with no arguments, when lint is run. The functions are expected to check the script data for errors, and print any they find to standard output (using the Python `print` statement is fine in this case).

define config.log \= None

If not None, this is expected to be a filename. Much of the text shown to the user by  or  statements will be logged to this file.

define config.log\_events \= False

If true, Ren'Py will log pygame-style events to the log.txt file. This will hurt performance, but might be useful for debugging certain problems.

define config.log\_width \= 78

The width of lines logged when  is used.

define config.missing\_image\_callback \= None

If not None, this function is called when an attempt to load an image fails. The callback is passed the filename of the missing image. It may return None, or it may return an . If an image manipulator is returned, that image manipulator is loaded in the place of the missing image.

One may want to also define a , especially if this is used with a .

define config.missing\_label\_callback \= None

If not None, this function is called when Ren'Py attempts to access a label that does not exist in the game. The callback should take a single parameter, the name of the missing label. It should return the name of a label to use as a replacement for the missing label, or None to cause Ren'Py to raise an exception.

define config.profile \= False

If set to True, some profiling information will be output to stdout.

define config.profile\_init \= 0.25

`init` and `init python` blocks taking longer than this amount of time to run are reported to log file.

define config.raise\_image\_exceptions \= None

If True, Ren'Py will raise an exception when an image name is not found. If False, Ren'Py will display a textual error message in place of the image.

If None, this takes on the value of config.developer.

This is set to False when Ren'Py ignores an exception.

define config.raise\_image\_load\_exceptions \= None

If True, Ren'Py will raise an exception when an exception happens during image loading. If False, Ren'Py will display a textual error message in place of the image.

If None, this takes on the value of config.developer.

This is set to False when Ren'Py ignore an exception.

define config.return\_not\_found\_label \= None

If not None, a label that is jumped to when a return site is not found. The call stack is cleared before this jump occurs.

### Garbage Collection

define config.gc\_print\_unreachable \= False

If True, Ren'Py will print to its console and logs information about the objects that are triggering collections.

define config.gc\_thresholds \= (25000, 10, 10)

The GC thresholds that Ren'Py uses when not idle. These are set to try to ensure that garbage collection doesn't happen. The three numbers are:

*   The net number of objects that need to be allocated before a level-0 collection.
    
*   The number of level-0 collections that trigger a level-1 collection.
    
*   The number of level-1 collections that trigger a level-2 collection.
    

(Level-0 collections should be fast enough to not cause a frame drop, level-1 collections might, level-2 will.)

define config.idle\_gc\_count \= 2500

The net number of objects that triggers a collection when Ren'Py has reached a steady state. (The fourth frame or later after the screen has been updated.)

define config.manage\_gc \= True

If True, Ren'Py will manage the GC itself. This means that it will apply the settings below.

### Reload

define config.autoreload \= True

If True, Shift+R will toggle automatic reloading. When automatic reloading is enabled, Ren'Py will reload the game whenever a used file is modified.

If False, Ren'Py will reload the game once per press of Shift+R.

define config.reload\_modules \= \

A list of strings giving the names of python modules that should be reloaded along with the game. Any submodules of these modules will also be reloaded.
