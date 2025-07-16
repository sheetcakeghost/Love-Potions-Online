# Screen Actions, Values, and Functions

Ren'Py ships with a number of actions, values, and functions intended for use with screens and the screen language.

## Actions

Actions are invoked when a button (including imagebuttons, textbuttons, and hotspots) is activated, hovered, or unhovered. Actions may determine when a button is selected or insensitive.

Along with these actions, an action may be a function that does not take any arguments. The function is called when the action is invoked. If the action returns a value, then the value is returned from an interaction.

A list of actions can usually be provided in lieu of a single action, in which case the actions in the list are run in order. A list of actions is sensitive if all of the actions are sensitive, and selected if any of them are ; that unless  or , respectively, is part of the list.

### Control Actions

These are actions that manage screens, interaction results, and control flow.

Call(_label_, _\*args_, _\*\*kwargs_)

Ends the current statement, and calls label, given as a string. Arguments and keyword arguments are passed to .

Hide(_screen\=None_, _transition\=None_, _\_layer\=None_, _immediately\=False_)

This causes a screen to be hidden if it is shown.

screen

Either a string giving the name of the screen to be hidden, or None to hide the current screen.

transition

If not None, a transition that occurs when hiding the screen.

\_layer

This is passed as the layer argument to . Ignored if screen is None.

immediately

If True, the screen is hidden immediately, without the 'on hide' event.

Jump(_label_)

Causes control to transfer to label, given as a string.

NullAction()

Does nothing.

This can be used to make a button responsive to hover/unhover events, without actually doing anything.

Return(_value\=None_)

Causes the current interaction to return the supplied non-None value. This is often used with menus and imagemaps, to select what the return value of the interaction is. If the screen was called using the `call screen` statement, the return value is placed in the \_return variable.

When in a menu, this returns from the menu. (The value should be None in this case.)

Show(_screen_, _transition\=None_, _\*args_, _\*\*kwargs_)

This causes another screen to be shown. screen is a string giving the name of the screen. The arguments are passed to the screen being shown.

If not None, transition is used to show the new screen.

This action takes the \_layer, \_zorder and \_tag keyword arguments, which have the same meaning as in the  function.

ShowTransient(_screen_, _transition\=None_, _\*args_, _\*\*kwargs_)

Shows a transient screen. A transient screen will be hidden when the current interaction completes. The arguments are passed to the screen being shown.

If not None, transition is use to show the new screen.

This action takes the \_layer, \_zorder and \_tag keyword arguments, which have the same meaning as in the  function.

ToggleScreen(_screen_, _transition\=None_, _\*args_, _\*\*kwargs_)

This toggles the visibility of screen. If it is not currently shown, the screen is shown with the provided arguments. Otherwise, the screen is hidden.

If not None, transition is use to show and hide the screen.

This action takes the \_layer, \_zorder and \_tag keyword arguments, which have the same meaning as in the  function.

### Data Actions

A number of these actions, encompassing the most usual cases, follow a simple pattern shown in the following table:

| Managers | Accessors |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Variable | ScreenVariable | LocalVariable | Field | Dict |
| --- | --- | --- | --- | --- | --- |
| Set |  |  |  |  |  |
| Toggle |  |  |  |  |  |
| Cycle |  |  |  |  |  |
| Increment |  |  |  |  |  |

The accessors determine the target whose value will change, and the manager determines what the new value will be. Their behavior is relatively simple to grasp:

*   The \-Variable actions change the value of the global variable called name, found in the general store. The name argument must be a string, and can be a simple name like "strength", or one with dots separating the variable from fields, like "hero.strength" or "persistent.show\_cutscenes".
    
*   The \-ScreenVariable actions change the value of the variable called name, associated with the current top-level screen. In a used screen, this action sets the variable in the context of the screen containing all the used one(s).
    
*   The \-LocalVariable actions change the value of the variable called name, taken locally to the screen it's in. This action is only useful in a screen that has been used by another screen (for more information, see ). In all other cases, the -ScreenVariable actions should be preferred, as yielding better performance and allowing more of the screen to be cached. The -LocalVariable actions must be created in the context that the variable is set in - it can't be passed in from somewhere else.
    
*   The \-Field actions change the value of the field called field of the object object.
    
*   The \-Dict actions change the value of the key key in the dictionary dict : they change `dict[key]`. This also works with lists.
    

*   The Set- actions simply set the value of the target to the passed value. Note that this has nothing to do with `set`, which is a builtin type in Python. `target = value`
    
*   The Toggle- actions invert the boolean value of their target, between true\_value (if given and not None) and false\_value (same). When true\_value and false\_value are both None, `target = not target`
    
*   The Cycle- actions cycle through the provided values, which must be a non-empty sequence (a list, tuple or range). If the target's value is not in the sequence at the time the action runs, it is set to the first value in the sequence. The loop parameter (defaulting to True) determines what happens when the values run out : if True it's started from the beginning, if False it raises an exception. The reverse parameter (defaulting to False) reverses the passed values sequence.
    
*   The Increment- actions add amount to their target, which defaults to 1 but may be of any type compatible with the target. `target = target + amount`
    

CycleDict(_dict_, _key_, _values_, _\*_, _reverse\=False_, _loop\=True_)

See .

CycleField(_object_, _field_, _values_, _\*_, _reverse\=False_, _loop\=True_)

See .

CycleLocalVariable(_name_, _values_, _\*_, _reverse\=False_, _loop\=True_)

See .

CycleScreenVariable(_name_, _values_, _\*_, _reverse\=False_, _loop\=True_)

See .

CycleVariable(_name_, _values_, _\*_, _reverse\=False_, _loop\=True_)

See .

IncrementDict(_dict_, _key_, _amount\=1_)

See .

IncrementField(_object_, _field_, _amount\=1_)

See .

IncrementLocalVariable(_name_, _amount\=1_)

See .

IncrementScreenVariable(_name_, _amount\=1_)

See .

IncrementVariable(_name_, _amount\=1_)

See .

SetDict(_dict_, _key_, _value_)

See .

SetField(_object_, _field_, _value_)

See .

SetLocalVariable(_name_, _value_)

See .

SetScreenVariable(_name_, _value_)

See .

SetVariable(_name_, _value_)

See .

ToggleDict(_dict_, _key_, _true\_value\=None_, _false\_value\=None_)

See .

ToggleField(_object_, _field_, _true\_value\=None_, _false\_value\=None_)

See .

ToggleLocalVariable(_name_, _true\_value\=None_, _false\_value\=None_)

See .

ToggleScreenVariable(_name_, _true\_value\=None_, _false\_value\=None_)

See .

ToggleVariable(_name_, _true\_value\=None_, _false\_value\=None_)

See .

The following data actions do not follow the pattern above. Some of them are related to Python's `set` type, not to be confused with the Set- actions above.

AddToSet(_set_, _value_)

Adds value to set.

set

The set to add to. This may be a Python set or list, in which case the value is appended to the list.

value

The value to add or append.

RemoveFromSet(_set_, _value_)

Removes value from set.

set

The set to remove from. This may be a set or list.

value

The value to remove.

ToggleSetMembership(_set_, _value_)

Toggles the membership of value in set. If the value is not in the set, it's added. Otherwise, it is removed.

Buttons with this action are marked as selected if and only if the value is in the set.

set

The set to add to or remove from. This may be a set or list. In the case of a list, new items are appended.

value

The value to add or append.

### Menu Actions

These actions invoke menus, or are primarily useful while in the main or game menus.

Continue(_regexp\='\

Causes the last save to be loaded. The purpose of this is to load the player's last save from the main menu.

regexp

If present, will be used in renpy.newest\_slot. The default pattern will continue from any save, including quick saves and auto saves. If you want to continue from only saves created by the player, set this to `r"\d"`.

confirm

If true, causes Ren'Py to ask the user if they want to continue where they left off, if they are not at the main menu.

MainMenu(_confirm\=True_, _save\=True_)

Causes Ren'Py to return to the main menu.

confirm

If true, causes Ren'Py to ask the user if he wishes to return to the main menu, rather than returning directly.

save

If true, the game is saved in  before Ren'Py restarts and returns the user to the main menu. The game is not saved if  is None.

Quit(_confirm\=None_)

Quits the game.

confirm

If true, prompts the user if he wants to quit, rather than quitting directly. If None, asks if and only if the user is not at the main menu.

ShowMenu(_screen\=\_game\_menu\_screen_, _\*args_, _\_transition\=config.intra\_transition_, _\*\*kwargs_)

Causes us to enter the game menu, if we're not there already. If we are in the game menu, then this shows a screen or jumps to a label.

screen is usually the name of a screen, which is shown using the screen mechanism. If the screen doesn't exist, then "\_screen" is appended to it, and that label is jumped to. the screen mechanism with the `*args` and `**kwargs` passed to the screen. If the screen doesn't exist, then "\_screen" is appended to it, and that label is jumped to, ignoring args and kwargs.

If the optional keyword argument \_transition is given, the menu will change screens using the provided transition. If not manually specified, the default transition is config.intra\_transition.

*   ShowMenu("load")
    
*   ShowMenu("save")
    
*   ShowMenu("preferences")
    

This can also be used to show user-defined menu screens. For example, if one has a "stats" screen defined, one can show it as part of the game menu using:

*   ShowMenu("stats")
    

ShowMenu without an argument will enter the game menu at the default screen, taken from .

Extra arguments and keyword arguments are passed on to the screen

Start(_label\='start'_)

Causes Ren'Py to jump out of the menu context to the named label. The main use of this is to start a new game from the main menu. Common uses are:

*   Start() - Start at the start label.
    
*   Start("foo") - Start at the "foo" label.
    

### File Actions

These actions handle saving, loading, and deleting of files. Many of these take the name and page arguments.

name

The name of the file to save to. This can be a string or an integer. It's combined with the page to create the filename.

page

The page that this action acts on. This is one of "auto", "quick", or a positive integer. If None, the page is determined automatically, based on a persistent page number.

These are converted to a slot name using , if it's set.

FileAction(_name_, _page\=None_, _\*\*kwargs_)

"Does the right thing" with the file. This means loading it if the load screen is showing (current screen is named "load"), and saving otherwise.

name

The name of the slot to save to or load from. If None, an unused slot (a large number based on the current time) will be used.

page

The page that the file will be saved to or loaded from. If None, the current page is used.

Other keyword arguments are passed to FileLoad or FileSave.

FileDelete(_name_, _confirm\=True_, _page\=None_, _slot\=False_)

Deletes the file.

name

The name of the slot to delete.

confirm

If true and not at the main menu, prompt for confirmation before loading the file.

page

The page that the file will be loaded from. If None, the current page is used.

slot

If True, name is taken to be a slot name, and page is ignored.

FileLoad(_name_, _confirm\=True_, _page\=None_, _newest\=True_, _cycle\=False_, _slot\=False_)

Loads the file.

name

The name of the slot to load from. If None, an unused slot will be used, and hence the file will not be loadable.

confirm

If true and not at the main menu, prompt for confirmation before loading the file.

page

The page that the file will be loaded from. If None, the current page is used.

newest

If true, the button is selected if this is the newest file.

cycle

Ignored.

slot

If True, name is taken to be a slot name, and page is ignored.

FilePage(_page_)

Sets the file page to page, which should be one of "auto", "quick", or an integer.

FilePageNext(_max\=None_, _wrap\=False_, _auto\=True_, _quick\=True_)

Goes to the next file page.

max

If set, this should be an integer that gives the number of the maximum file page we can go to.

wrap

If true, we can go to the first page when on the last file page if max is set.

auto

If true and wrap is set, this can bring the player to the page of automatic saves.

quick

If true and wrap is set, this can bring the player to the page of automatic saves.

FilePagePrevious(_max\=None_, _wrap\=False_, _auto\=True_, _quick\=True_)

Goes to the previous file page, if possible.

max

If set, this should be an integer that gives the number of the maximum file page we can go to. This is required to enable wrap.

wrap

If true, we can go to the last page when on the first file page if max is set.

auto

If true, this can bring the player to the page of automatic saves.

quick

If true, this can bring the player to the page of automatic saves.

FileSave(_name_, _confirm\=True_, _newest\=True_, _page\=None_, _cycle\=False_, _slot\=False_, _action\=None_)

Saves the file.

The button with this slot is selected if it's marked as the newest save file.

name

The name of the slot to save to. If None, an unused slot (a large number based on the current time) will be used.

confirm

If true, then we will prompt before overwriting a file.

newest

Ignored.

page

The name of the page that the slot is on. If None, the current page is used.

cycle

If true, then saves on the supplied page will be cycled before being shown to the user.  slots are used in the cycle.

slot

If True, name is taken to be a slot name, and page is ignored.

action

An action that is run after the save is complete. This is only run if the save is successful.

FileTakeScreenshot()

Take a screenshot to be used when the game is saved. This can be used to ensure that the screenshot is accurate, by taking a picture of the screen before a file save screen is shown.

QuickLoad(_confirm\=True_)

Performs a quick load.

confirm

If true and not at the main menu, prompt for confirmation before loading the file.

QuickSave(_message\='Quick save complete.'_, _newest\=False_)

Performs a quick save.

message

A message to display to the user when the quick save finishes.

newest

Set to true to mark the quicksave as the newest save.

### Sync Actions

DownloadSync()

This action begins the process of downloading a Sync from the Ren'Py Sync server.

UploadSync()

This action begins the process of uploading the most recent saves to the Ren'Py Sync server.

### Audio Actions

The concept of channels and how they work, as well as most information about audio in Ren'Py, is explained at .

GetMixer(_mixer_, _db\=False_)

Returns the volume of mixer.

db

If true, returns the volume in decibels. If false, the default, returns the volume as a number between 0.0 and 1.0.

PauseAudio(_channel_, _value\=True_)

Sets the pause flag for channel.

If value is True, the channel is paused. If False, the channel is unpaused. If "toggle", the pause flag will be toggled.

Play(_channel_, _file_, _selected\=None_, _\*\*kwargs_)

Causes an audio file to be played on a given channel.

channel

The channel to play the sound on.

file

The file to play.

selected

If True, buttons using this action will be marked as selected if the file is playing on the channel. If False, this action will not cause the button to start playing. If None, the button is marked selected if the channel is a music channel, and not otherwise.

Any other keyword arguments are passed to .

Queue(_channel_, _file_, _\*\*kwargs_)

Causes an audio file to be queued on a given channel.

channel

The channel to play the sound on.

file

The file to play.

Any keyword arguments are passed to 

SetMixer(_mixer_, _volume_)

Sets the volume of mixer to value.

mixer

The mixer to set the volume of. A string, usually one of "main", "music", "sfx", or "voice". See  for more information about mixers.

value

The value to set the volume to. A number between 0.0 and 1.0, inclusive.

SetMute(_mixer_, _mute_)

Sets the mute status of one or more mixers. When a mixer is muted, audio channels associated with that mixer will stop playing audio.

mixer

Either a single string giving a mixer name, or a list of strings giving a list of mixers. The strings should be mixer names.

mute

True to mute the mixer, False to ummute it.

Stop(_channel_, _\*\*kwargs_)

Causes an audio channel to be stopped.

channel

The channel to stop the sound on.

Any keyword arguments are passed to 

ToggleMute(_mixer_)

Toggles the mute status of one or more mixers.

mixer

Either a single string giving a mixer name, or a list of strings giving a list of mixers. The strings should be mixer names.

### Focus Actions

CaptureFocus(_name\='default'_)

If a displayable is focused when this action is run, the rectangle containing that displayable is stored with the name name. This rectangle can then be retrieved with the  action, or the focus property of the  displayable.

If no displayable is focused, the previous capture with that name is removed.

name

The name of the focus rectangle to store. This should be a string. The name "tooltip" is special, as it is automatically captured when the tooltip is changed.

ClearFocus(_name\='default'_)

Clears a stored focus rectangle captured with . If name is None, all focus rectangles are cleared.

GetFocusRect(_name\='default'_)

If a focus rectangle with the given name has been stored (either with , or automatically by a tooltip, returns the a (x, y, h, w) rectangle. Otherwise, returns None.

name

The name of the focus rectangle to retrieve. The name "tooltip" is special, as it is automatically captured when the tooltip is changed.

ToggleFocus(_name\='default'_)

If the focus rectangle exists, clears it, otherwise captures it.

name

The name of the focus rectangle to store. This should be a string. The name "tooltip" is special, as it is automatically captured when the tooltip is changed.

### Other Actions

These are other actions, not found anywhere else.

Confirm(_prompt_, _yes_, _no\=None_, _confirm\_selected\=False_)

Prompts the user for confirmation of an action. If the user clicks yes, the yes action is performed. Otherwise, the no action is performed.

prompt

The prompt to display to the user.

confirm\_selected

If true, the prompt will be displayed even if the yes action is already selected. If false (the default), the prompt will not be displayed if the yes action is selected.

The sensitivity and selectedness of this action match those of the yes action.

See  for a function version of this action.

CopyToClipboard(_s_)

Copies the string s to the system clipboard, if possible. This should work on desktop and mobile platforms, but will not work on the web.

DisableAllInputValues()

Disables all active InputValue. This will re-focus the default InputValue, if there is one. Otherwise, no InputValue will be focused.

EditFile(_filename\=None_, _line\=1_)

Requests Ren'Py to open the given file in a text editor, if possible. This will work on some platforms but not others.

filename

If given, the filename to open. If None, the current filename and line number are used, with line being ignored.

line

The line number to open the file at.

ExecJS(_code_)

Executes the given JavaScript source code. This is only supported on the web, and will raise an exception on other platforms. The script is executed asynchronously in the window context, and the return value is not available.

code

The JavaScript code to execute.

Function(_callable_, _\*args_, _\_update\_screens\=True_, _\*\*kwargs_)

This Action calls `callable(*args, **kwargs)`.

callable

Callable object. This assumes that if two callables compare equal, calling either one will be equivalent.

args

positional arguments to be passed to callable.

kwargs

keyword arguments to be passed to callable.

\_update\_screens

When true, the interaction restarts and the screens are updated after the function returns.

If the function returns a non-None value, the interaction stops and returns that value. (When called using the call screen statement, the result is placed in the \_return variable.)

Instead of using a Function action, you can define your own subclass of the  class. This lets you name the action, and determine when it should be selected and sensitive.

Help(_help\=None_)

Displays help.

help

A string that is used to find help. This is used in the following way:

*   If a label with this name exists, the label is called in a new context.
    
*   Otherwise, this is interpreted as giving the name of a file that should be opened in a web browser.
    

If help is None,  is used as the default value. If it is also None, the  screen is shown in a new context, if it exists. Otherwise, does nothing.

HideInterface()

Causes the interface to be hidden until the user clicks. This is typically what happens when hitting the H key in a Ren'Py game.

If(_expression_, _true\=None_, _false\=None_)

This returns true if expression is true, and false otherwise. Use this to select an action based on an expression. Note that the default, None, can be used as an action that causes a button to be disabled.

InvertSelected(_action_)

This inverts the selection state of the provided action, while proxying over all of the other methods.

MouseMove(_x_, _y_, _duration\=0_)

Move the mouse pointer to x, y. If the device does not have a mouse pointer, if it is not possible for Ren'Py to move that pointer, or if the  is False, this does nothing.

duration

The time it will take to perform the move, in seconds. During this time, the mouse may be unresponsive.

Notify(_message_)

Displays message using .

OpenDirectory(_directory_)

Opens directory in a file browser. directory is relative to `config.basedir`.

OpenURL(_url_)

Causes url to be opened in a web browser.

QueueEvent(_event_, _up\=False_)

Queues the given event using .

RestartStatement()

This action causes Ren'Py to rollback to before the current statement, and then re-run the current statement. This may be used when changing a persistent variable that affects how the statement is displayed.

If run in a menu context, this waits until the player exits to a top-level context before performing the rollback.

RollForward()

This action causes a rollforward to occur, if a roll forward is possible. Otherwise, it is insensitive.

Rollback(_\*args_, _force\='menu'_, _\*\*kwargs_)

This action causes a rollback to occur, when a rollback is possible. Otherwise, nothing happens.

The arguments are given to . This includes the force argument which here defaults to "menu".

RollbackToIdentifier(_identifier_)

This causes a rollback to an identifier to occur. Rollback identifiers are returned as part of HistoryEntry objects.

Screenshot()

Takes a screenshot.

Scroll(_id_, _direction_, _amount\='step'_, _delay\=0.0_)

Causes a Bar, Viewport, or Vpgrid to scroll.

id

The id of a bar, viewport, or vpgrid in the current screen.

direction

For a vbar, one of "increase" or "decrease". For a viewport or vpgrid, one of "horizontal increase", "vertical increase", "horizontal decrease", or "vertical decrease".

amount

The amount to scroll by. This can be a number of pixels, or else "step" or "page".

delay

If non-zero, the scroll will be animated for this many seconds.

SelectedIf(_action_, _/_)

This indicates that one action in a list of actions should be used to determine if a button is selected. This only makes sense when the button has a list of actions. For example:

\# The button is selected only if mars\_flag is True
textbutton "Marsopolis":
    action \[ SelectedIf(SetVariable("mars\_flag", True)), SetVariable("on\_mars", True) \]

The action inside SelectedIf is run normally when the button is clicked.

SensitiveIf(_action_, _/_)

This indicates that one action in a list of actions should be used to determine if a button is sensitive. This only makes sense when the button has a list of actions. For example:

\# The button is sensitive only if mars\_flag is True
textbutton "Marsopolis":
    action \[ SensitiveIf(SetVariable("mars\_flag", True)), SetVariable("on\_mars", True) \]

The action inside SensitiveIf is run normally when the button is clicked.

Skip(_fast\=False_, _confirm\=False_)

Causes the game to begin skipping. If the game is in a menu context, then this returns to the game. Otherwise, it just enables skipping.

fast

If true, skips directly to the next menu choice.

confirm

If true, asks for confirmation before beginning skipping.

With(_transition_)

Causes transition to occur.

Additional actions are available in other pages of this documentation, such as ,  and ,  and , , and the .

Other actions can be created using the  class.

## Bar Values

Bar values are used with bars, to set the bar value, and to allow the bar to adjust an underlying property. To create a new bar value, subclass the  class. All classes that have the step keyword also accept the force\_step keyword whose behavior is described in .

AnimatedValue(_value\=0.0_, _range\=1.0_, _delay\=1.0_, _old\_value\=None_)

This animates a value, taking delay seconds to vary the value from old\_value to value.

value

The value itself, a number.

range

The range of the value, a number.

delay

The time it takes to animate the value, in seconds. Defaults to 1.0.

old\_value

The old value. If this is None, then the value is taken from the AnimatedValue we replaced, if any. Otherwise, it is initialized to value.

AudioPositionValue(_channel\='music'_, _update\_interval\=0.1_)

A value that shows the playback position of the audio file playing in channel.

update\_interval

How often the value updates, in seconds.

DictValue(_dict_, _key_, _range\=None_, _max\_is\_zero\=False_, _style\='bar'_, _offset\=0_, _step\=None_, _action\=None_, _force\_step\=False_, _min\=None_, _max\=None_)

A bar value that allows the user to adjust the value of a key in a dict, or of an element at a particular index in a list.

dict

The dict, or the list.

key

The key, or the index when using a list.

range

The range to adjust over. This must be specified if max and min are not given.

max\_is\_zero

If True, then when the key or index's value is zero, the value of the bar will be range, and all other values will be shifted down by 1. This works both ways - when the bar is set to the maximum, the value of the key or index is set to 0.

This is used internally, for some preferences.

style

The styles of the created bar.

offset

An offset to add to the value.

step

The amount to change the bar by. If None, defaults to 1/10th of the bar.

action

If not None, an action to call when the key or index's value is changed.

min

The minimum value of the bar. If both min and max are given, range and offset are calculated from them.

max

The maximum value of the bar. If both min and max are given, range and offset are calculated from them.

FieldValue(_object_, _field_, _range\=None_, _max\_is\_zero\=False_, _style\='bar'_, _offset\=0_, _step\=None_, _action\=None_, _force\_step\=False_, _min\=None_, _max\=None_)

A bar value that allows the user to adjust the value of a field on an object.

object

The object.

field

The field name, a string.

range

The range to adjust over. This must be specified if max and min are not given.

max\_is\_zero

If True, then when the field's value is zero, the value of the bar will be range, and all other values will be shifted down by 1. This works both ways - when the bar is set to the maximum, the value of the field is set to 0.

This is used internally, for some preferences.

style

The styles of the created bar.

offset

An offset to add to the value.

step

The amount to change the bar by. If None, defaults to 1/10th of the bar.

action

If not None, an action to call when the field's value is changed.

min

The minimum value of the bar. If both min and max are given, range and offset are calculated from them.

max

The maximum value of the bar. If both min and max are given, range and offset are calculated from them.

LocalVariableValue(_variable_, _range\=None_, _max\_is\_zero\=False_, _style\='bar'_, _offset\=0_, _step\=None_, _action\=None_, _force\_step\=False_, _min\=None_, _max\=None_)

A bar value that adjusts the value of a variable in a `use`d screen.

To target a variable in a top-level screen, prefer using .

For more information, see .

This must be created in the context that the variable is set in - it can't be passed in from somewhere else.

variable

A string giving the name of the variable to adjust.

range

The range to adjust over. This must be specified if max and min are not given.

max\_is\_zero

If True, then when the local variable's value is zero, the value of the bar will be range, and all other values will be shifted down by 1. This works both ways - when the bar is set to the maximum, the value of the local variable is set to 0.

This is used internally, for some preferences.

style

The styles of the created bar.

offset

An offset to add to the value.

step

The amount to change the bar by. If None, defaults to 1/10th of the bar.

action

If not None, an action to call when the local variable's value is changed.

min

The minimum value of the bar. If both min and max are given, range and offset are calculated from them.

max

The maximum value of the bar. If both min and max are given, range and offset are calculated from them.

MixerValue(_mixer_)

The value of an audio mixer.

mixer

The name of the mixer to adjust. This is usually one of "main", "music", "sfx", or "voice". See  for more information.

ScreenVariableValue(_variable_, _range\=None_, _max\_is\_zero\=False_, _style\='bar'_, _offset\=0_, _step\=None_, _action\=None_, _force\_step\=False_, _min\=None_, _max\=None_)

A bar value that adjusts the value of a variable in a screen.

In a `use`d screen, this targets a variable in the context of the screen containing the `use`d one(s). To target variables within a `use`d screen, and only in that case, use  instead.

variable

A string giving the name of the variable to adjust.

range

The range to adjust over. This must be specified if max and min are not given.

max\_is\_zero

If True, then when the screen variable's value is zero, the value of the bar will be range, and all other values will be shifted down by 1. This works both ways - when the bar is set to the maximum, the value of the screen variable is set to 0.

This is used internally, for some preferences.

style

The styles of the created bar.

offset

An offset to add to the value.

step

The amount to change the bar by. If None, defaults to 1/10th of the bar.

action

If not None, an action to call when the screen variable's value is changed.

min

The minimum value of the bar. If both min and max are given, range and offset are calculated from them.

max

The maximum value of the bar. If both min and max are given, range and offset are calculated from them.

StaticValue(_value\=0.0_, _range\=1.0_)

This allows a value to be specified statically.

value

The value itself, a number.

range

The range of the value.

VariableValue(_variable_, _range\=None_, _max\_is\_zero\=False_, _style\='bar'_, _offset\=0_, _step\=None_, _action\=None_, _force\_step\=False_, _min\=None_, _max\=None_)

A bar value that allows the user to adjust the value of a variable in the default store.

variable

The variable parameter must be a string, and can be a simple name like "strength", or one with dots separating the variable from fields, like "hero.strength" or "persistent.show\_cutscenes".

range

The range to adjust over. This must be specified if max and min are not given.

max\_is\_zero

If True, then when the variable's value is zero, the value of the bar will be range, and all other values will be shifted down by 1. This works both ways - when the bar is set to the maximum, the value of the variable is set to 0.

This is used internally, for some preferences.

style

The styles of the created bar.

offset

An offset to add to the value.

step

The amount to change the bar by. If None, defaults to 1/10th of the bar.

action

If not None, an action to call when the variable's value is changed.

min

The minimum value of the bar. If both min and max are given, range and offset are calculated from them.

max

The maximum value of the bar. If both min and max are given, range and offset are calculated from them.

XScrollValue(_viewport_)

The value of an adjustment that horizontally scrolls the viewport with the given id, on the current screen. The viewport must be defined before a bar with this value is.

YScrollValue(_viewport_)

The value of an adjustment that vertically scrolls the viewport with the given id, on the current screen. The viewport must be defined before a bar with this value is.

## Input Values

Input values are used with text inputs, to set the default text, to accept changed text, to respond to the enter key, and to determine if the text is editable by default. To create a new input value, subclass the  class.

Ren'Py-defined input values inherit from InputValue, which means that all values also include Enable(), Disable(), and Toggle() methods that return actions that enable, disable, and toggle editing, respectively. See also the  action.

DictInputValue(_dict_, _key_, _default\=True_, _returnable\=False_)

An input value that updates `dict[key]`.

dict

May be a dict object or a list.

default

If true, this input can be editable by default.

returnable

If true, the value of this input will be returned when the user presses enter.

FieldInputValue(_object_, _field_, _default\=True_, _returnable\=False_)

An input value that updates field on object.

field

A string giving the name of the field.

default

If true, this input can be editable by default.

returnable

If true, the value of this input will be returned when the user presses enter.

FilePageNameInputValue(_pattern\='Page {}'_, _auto\='Automatic saves'_, _quick\='Quick saves'_, _page\=None_, _default\=False_)

An input value that updates the name of a file page.

pattern

This is used for the default name of a page. Python-style substition is performed, such that {} is replaced with the number of the page.

auto

The name of the autosave page.

quick

The name of the quicksave page.

page

If given, the number of the page to display. This should usually be left as None, to give the current page.

default

If true, this input can be editable by default.

LocalVariableInputValue(_variable_, _default\=True_, _returnable\=False_)

An input value that updates a local variable in a `use`d screen.

To target a variable in a top-level screen, prefer using .

For more information, see .

This must be created in the context that the variable is set in - it can't be passed in from somewhere else.

variable

A string giving the name of the variable to update.

default

If true, this input can be editable by default.

returnable

If true, the value of this input will be returned when the user presses enter.

ScreenVariableInputValue(_variable_, _default\=True_, _returnable\=False_)

An input value that updates a variable in a screen.

In a `use`d screen, this targets a variable in the context of the screen containing the `use`d one(s). To target variables within a `use`d screen, and only in that case, use  instead.

variable

A string giving the name of the variable to update.

default

If true, this input can be editable by default.

returnable

If true, the value of this input will be returned when the user presses enter.

VariableInputValue(_variable_, _default\=True_, _returnable\=False_)

An input value that updates variable.

variable

A string giving the name of the variable to update.

The variable parameter must be a string, and can be a simple name like "strength", or one with dots separating the variable from fields, like "hero.strength" or "persistent.show\_cutscenes".

default

If true, this input can be editable by default.

returnable

If true, the value of this input will be returned when the user presses enter.

## Functions and Classes

These functions and classes are useful in association with screens.

### Preferences

While all preferences can be defined based on the Actions and Values given above, it requires some knowledge of Ren'Py to figure out the correct one to use. The preferences constructor makes this easy, by creation an action or value, as appropriate, based on the names used in the default preferences screen.

Preference(_name_, _value\=None_, _range\=None_)

This constructs the appropriate action or value from a preference. The preference name should be the name given in the standard menus, while the value should be either the name of a choice, "toggle" to cycle through choices, a specific value, or left off in the case of buttons.

Actions that can be used with buttons and hotspots are:

*   Preference("display", "fullscreen") - displays in fullscreen mode.
    
*   Preference("display", "window") - displays in windowed mode at 1x normal size.
    
*   Preference("display", 2.0) - displays in windowed mode at 2.0x normal size.
    
*   Preference("display", "any window") - displays in windowed mode at the previous size.
    
*   Preference("display", "toggle") - toggle display mode.
    
*   Preference("transitions", "all") - show all transitions.
    
*   Preference("transitions", "none") - do not show transitions.
    
*   Preference("transitions", "toggle") - toggle transitions.
    
*   Preference("video sprites", "show") - show all video sprites.
    
*   Preference("video sprites", "hide") - fall back to images where possible.
    
*   Preference("video sprites", "toggle") - toggle image fallback behavior.
    
*   Preference("show empty window", "show") - Allow the "window show" and "window auto" statement to show an empty window outside of the say statement.
    
*   Preference("show empty window", "hide") - Prevent the above.
    
*   Preference("show empty window", "toggle") - Toggle the above.
    
*   Preference("text speed", 0) - make text appear instantaneously.
    
*   Preference("text speed", 142) - set text speed to 142 characters per second.
    
*   Preference("joystick") - Show the joystick preferences.
    
*   Preference("skip", "seen") - Only skip seen messages.
    
*   Preference("skip", "all") - Skip unseen messages.
    
*   Preference("skip", "toggle") - Toggle between skip seen and skip all.
    
*   Preference("begin skipping") - Starts skipping.
    
*   Preference("after choices", "skip") - Skip after choices.
    
*   Preference("after choices", "stop") - Stop skipping after choices.
    
*   Preference("after choices", "toggle") - Toggle skipping after choices.
    
*   Preference("auto-forward time", 0) - Set the auto-forward time to infinite.
    
*   Preference("auto-forward time", 10) - Set the auto-forward time (unit is seconds per 250 characters).
    
*   Preference("auto-forward", "enable") - Enable auto-forward mode.
    
*   Preference("auto-forward", "disable") - Disable auto-forward mode.
    
*   Preference("auto-forward", "toggle") - Toggle auto-forward mode.
    
*   Preference("auto-forward after click", "enable") - Remain in auto-forward mode after a click.
    
*   Preference("auto-forward after click", "disable") - Disable auto-forward mode after a click.
    
*   Preference("auto-forward after click", "toggle") - Toggle auto-forward after click.
    
*   Preference("automatic move", "enable") - Allow Ren'Py to move the mouse automatically using the  action.
    
*   Preference("automatic move", "disable") - Disable the  action.
    
*   Preference("automatic move", "toggle") - Toggle automatic mouse mode.
    
*   Preference("wait for voice", "enable") - Wait for the currently playing voice to complete before auto-forwarding.
    
*   Preference("wait for voice", "disable") - Do not wait for the currently playing voice to complete before auto-forwarding.
    
*   Preference("wait for voice", "toggle") - Toggle wait voice.
    
*   Preference("voice sustain", "enable") - Sustain voice past the current interaction.
    
*   Preference("voice sustain", "disable") - Don't sustain voice past the current interaction.
    
*   Preference("voice sustain", "toggle") - Toggle voice sustain.
    
*   Preference("music mute", "enable") - Mute the music mixer.
    
*   Preference("music mute", "disable") - Un-mute the music mixer.
    
*   Preference("music mute", "toggle") - Toggle music mute.
    
*   Preference("sound mute", "enable") - Mute the sound mixer.
    
*   Preference("sound mute", "disable") - Un-mute the sound mixer.
    
*   Preference("sound mute", "toggle") - Toggle sound mute.
    
*   Preference("voice mute", "enable") - Mute the voice mixer.
    
*   Preference("voice mute", "disable") - Un-mute the voice mixer.
    
*   Preference("voice mute", "toggle") - Toggle voice mute.
    
*   Preference("mixer <mixer> mute", "enable") - Mute the specified mixer.
    
*   Preference("mixer <mixer> mute", "disable") - Unmute the specified mixer.
    
*   Preference("mixer <mixer> mute", "toggle") - Toggle mute of the specified mixer.
    
*   Preference("all mute", "enable") - Mute each individual mixer.
    
*   Preference("all mute", "disable") - Unmute each individual mixer.
    
*   Preference("all mute", "toggle") - Toggle mute of each individual mixer.
    
*   Preference("main volume", 0.5) - Set the adjustment applied to all channels.
    
*   Preference("music volume", 0.5) - Set the music volume.
    
*   Preference("sound volume", 0.5) - Set the sound volume.
    
*   Preference("voice volume", 0.5) - Set the voice volume.
    
*   Preference("mixer <mixer> volume", 0.5) - Set the specified mixer volume.
    
*   Preference("emphasize audio", "enable") - Emphasize the audio channels found in .
    
*   Preference("emphasize audio", "disable") - Do not emphasize audio channels.
    
*   Preference("emphasize audio", "toggle") - Toggle emphasize audio.
    
*   Preference("self voicing", "enable") - Enables self-voicing.
    
*   Preference("self voicing", "disable") - Disable self-voicing.
    
*   Preference("self voicing", "toggle") - Toggles self-voicing.
    
*   Preference("self voicing volume drop", 0.5) - Drops the volume of non-voice mixers when self voicing is active.
    
*   Preference("clipboard voicing", "enable") - Enables clipboard-voicing.
    
*   Preference("clipboard voicing", "disable") - Disable clipboard-voicing.
    
*   Preference("clipboard voicing", "toggle") - Toggles clipboard-voicing.
    
*   Preference("debug voicing", "enable") - Enables self-voicing debug
    
*   Preference("debug voicing", "disable") - Disable self-voicing debug.
    
*   Preference("debug voicing", "toggle") - Toggles self-voicing debug.
    
*   Preference("rollback side", "left") - Touching the left side of the screen causes rollback.
    
*   Preference("rollback side", "right") - Touching the right side of the screen causes rollback.
    
*   Preference("rollback side", "disable") - Touching the screen will not cause rollback.
    
*   Preference("gl powersave", True) - Drop framerate to allow for power savings.
    
*   Preference("gl powersave", False) - Do not drop framerate to allow for power savings.
    
*   Preference("gl framerate", None) - Runs at the display framerate.
    
*   Preference("gl framerate", 60) - Runs at the given framerate.
    
*   Preference("gl tearing", True) - Tears rather than skipping frames.
    
*   Preference("gl tearing", False) - Skips frames rather than tearing.
    
*   Preference("font transform", "opendyslexic") - Sets the accessibility font transform to opendyslexic.
    
*   Preference("font transform", "dejavusans") - Sets the accessibility font transform to deja vu sans.
    
*   Preference("font transform", None) - Disables the accessibility font transform.
    

See  for how to add font transforms.

*   Preference("font size", 1.0) - Sets the accessibility font size scaling factor.
    
*   Preference("font line spacing", 1.0) - Sets the accessibility font vertical spacing scaling factor.
    
*   Preference("system cursor", "disable") - Use the cursor defined in  or .
    
*   Preference("system cursor", "enable") - Use the system cursor, ignoring .
    
*   Preference("system cursor", "toggle") - Toggle system cursor.
    
*   Preference("high contrast text", "enable") - Enables white text on a black background.
    
*   Preference("high contrast text", "disable") - Disables high contrast text.
    
*   Preference("high contrast text", "toggle") - Toggles high contrast text.
    
*   Preference("audio when minimized", "enable") - Enable sounds playing when the window has been minimized.
    
*   Preference("audio when minimized", "disable") - Disable sounds playing when the window has been minimized.
    
*   Preference("audio when minimized", "toggle") - Toggle sounds playing when the window has been minimized.
    
*   Preference("audio when unfocused", "enable") - Enable sounds playing when the window is not in focus.
    
*   Preference("audio when unfocused", "disable") - Disable sounds playing when the window is not in focus.
    
*   Preference("audio when unfocused", "toggle") - Toggle sounds playing when the window is not in focus.
    
*   Preference("web cache preload", "enable") - Will cause the web cache to be preloaded.
    
*   Preference("web cache preload", "disable") - Will cause the web cache to not be preloaded, and preloaded data to be deleted.
    
*   Preference("web cache preload", "toggle") - Will toggle the web cache preload state.
    
*   Preference("voice after game menu", "enable") - Will cause the voice to continue being played when entering the game menu.
    
*   Preference("voice after game menu", "disable") - Will cause the voice to stop being played when entering the game menu.
    
*   Preference("voice after game menu", "toggle") - Will toggle the voice after game menu state.
    
*   Preference("restore window position", "enable") - Will cause the window position to be restored when the game is started.
    
*   Preference("restore window position", "disable") - Will cause the window position to not be restored when the game is started.
    
*   Preference("restore window position", "toggle") - Will toggle the restore window position state.
    

Values that can be used with bars are:

*   Preference("text speed")
    
*   Preference("auto-forward time")
    
*   Preference("main volume")
    
*   Preference("music volume")
    
*   Preference("sound volume")
    
*   Preference("voice volume")
    
*   Preference("mixer <mixer> volume")
    
*   Preference("self voicing volume drop")
    
*   Preference("font size")
    
*   Preference("font line spacing")
    

The range parameter can be given to give the range of certain bars. For "text speed", it defaults to 200 cps. For "auto-forward time", it defaults to 30.0 seconds per chunk of text. (These are maximums, not defaults.)

Actions that can be used with buttons are:

*   Preference("renderer menu") - Show the renderer menu.
    
*   Preference("accessibility menu") - Show the accessibility menu.
    
*   Preference("reset") - Reset preferences to defaults.
    

These screens are intended for internal use, and are not customizable.

GetCharacterVolume(_voice\_tag_)

This returns the volume associated with voice tag, a number between 0.0 and 1.0, which is interpreted as a fraction of the mixer volume for the voice channel.

### Gamepad

These functions and actions work with the gamepad.

GamepadCalibrate()

An action that invokes the gamepad calibration routine.

GamepadExists(_developer\=True_)

A function that returns true if a gamepad is present, and false otherwise.

developer

Forces this function to always return true while  is true.

### File Functions

These functions return useful information about files. They use the same default page as the file actions.

FileCurrentPage()

Returns the current file page as a string.

_class_ FileCurrentScreenshot(_empty\=None_, _\*\*properties_)

A displayable that shows the screenshot that will be saved with the current file, if a screenshot has been taken when entering a menu or with .

If there is no current screenshot, empty is shown in its place. (If empty is None, it defaults to .)

FileJson(_name_, _key\=None_, _empty\=None_, _missing\=None_, _page\=None_, _slot\=False_)

Accesses the Json information associated with name.

This always returns empty if the slot is empty.

If not, and if key is None, returns the entire dictionary containing the Json data.

Otherwise, this returns json\[key\] if key is defined on the json object of the save, and missing if there is a save with the given name, but it does not contain key.

Such Json data is added to a save slot by callbacks registered using .

By default, the following keys are defined:

\_save\_name

The value of  when the game was saved.

\_renpy\_version

The version of Ren'Py the save was created with.

\_version

The value of  when the save was created.

\_game\_runtime

The result of calling .

\_ctime

The time the save was created, in seconds since January 1, 1970, UTC.

FileLoadable(_name_, _page\=None_, _slot\=False_)

This is a function that returns true if the file is loadable, and false otherwise.

FileNewest(_name_, _page\=None_, _slot\=False_)

Returns True if this is the newest file slot, or False otherwise.

FilePageName(_auto\='a'_, _quick\='q'_)

Returns the name of the current file page, as a string. If a normal page, this returns the page number. Otherwise, it returns auto or quick.

FileSaveName(_name_, _empty\=''_, _page\=None_, _slot\=False_)

Return the save\_name that was in effect when the file was saved, or empty if the file does not exist.

FileScreenshot(_name_, _empty\=None_, _page\=None_, _slot\=False_)

Returns the screenshot associated with the given file. If the file is not loadable, then empty is returned, unless it's None, in which case, a Null displayable is created.

The return value is a displayable.

FileSlotName(_slot_, _slots\_per\_page_, _auto\='a'_, _quick\='q'_, _format\='%s%d'_)

Returns the name of the numbered slot. This assumes that slots on normal pages are numbered in a linear order starting with 1, and that page numbers start with 1. When slot is 2, and slots\_per\_page is 10, and the other variables are the defaults:

*   When the first page is showing, this returns "2".
    
*   When the second page is showing, this returns "12".
    
*   When the auto page is showing, this returns "a2".
    
*   When the quicksave page is showing, this returns "q2".
    

slot

The number of the slot to access.

slots\_per\_page

The number of slots per page.

auto

A prefix to use for the auto page.

quick

A prefix to use for the quick page.

format

The formatting code to use. This is given two arguments: A string giving the page prefix, and an integer giving the slot number.

FileTime(_name_, _format\='%b %d, %H:%M'_, _empty\=''_, _page\=None_, _slot\=False_)

Returns the time the file was saved, formatted according to the supplied format. If the file is not found, empty is returned.

The return value is a string.

FileUsedSlots(_page\=None_, _highest\_first\=True_)

Returns a list of used numeric file slots on the page.

page

The name of the page that will be scanned. If None, the current page is used.

highest\_first

If true, the highest-numbered file slot is listed first. Otherwise, the lowest-numbered slot is listed first.

### Side Image Functions

This function returns the side image to use.

SideImage()

Returns the side image associated with the currently speaking character, or a Null displayable if no such side image exists.

### Other Functions

CurrentScreenName()

Returns the name of the current screen, or None if there is no current screen. In the case of a screen including by the use screen, this returns the name of the screen that is doing the including, not the name of the screen being included.

### Tooltips

Tooltips can now be accessed by the  property available on all displayables, and the GetTooltip function. The GetTooltip function returns the value of the tooltip property when the displayable gains focus.

As a reminder, values passed to the  property must support equality.

Here's an example:

screen tooltip\_example():
    vbox:
        textbutton "North":
            action Return("n")
            tooltip "To meet a polar bear."

        textbutton "South":
            action Return("s")
            tooltip "All the way to the tropics."

        textbutton "East":
            action Return("e")
            tooltip "So we can embrace the dawn."

        textbutton "West":
            action Return("w")
            tooltip "Where to go to see the best sunsets."

        $ tooltip \= GetTooltip()

        if tooltip:
            text "\[tooltip\]"

The  displayable can be used to display "popup-style" tooltips, and has support for a special "tooltip" focus name, that is set to the location of the last focus that set a tooltip:

screen tooltip\_example2():
    frame:

        padding (20, 20)
        align (.5, .3)

        has vbox

        textbutton "North":
            action Return("n")
            tooltip "To meet a polar bear."

        textbutton "South":
            action Return("s")
            tooltip "All the way to the tropics."

        textbutton "East":
            action Return("e")
            tooltip "So we can embrace the dawn."

        textbutton "West":
            action Return("w")
            tooltip "Where to go to see the best sunsets."

    \# This has to be the last thing shown in the screen.

    $ tooltip \= GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer\_top True

            frame:
                xalign 0.5
                text tooltip

GetTooltip(_screen\=None_, _last\=False_)

Returns the tooltip of the currently focused displayable, or None if no displayable is focused.

screen

If not None, this should be the name or tag of a screen. If given, this function only returns the tooltip if the focused displayable is part of the screen.

last

If true, returns the last non-None value this function would have returned.

#### Legacy

Warning

This has been obsoleted by the above, but you might see it in older projects.

The tooltip class changes the screen when a button is hovered.

_class_ Tooltip(_default_)

A tooltip object can be used to define a portion of a screen that is updated when the mouse hovers an area.

A tooltip object has a `value` field, which is set to the default value passed to the constructor when the tooltip is created. When a button using an action created by the tooltip is hovered, the value field changes to the value associated with the action.

Action(_value_)

Returns an action that is generally used as the hovered property of a button. When the button is hovered, the value field of this tooltip is set to value. When the button loses focus, the value field of this tooltip reverts to the default.

When using a tooltip with a screen, the usual behavior is to create a tooltip object in a default statement. The value of the tooltip and the action method can then be used within the screen. The order of use within a screen doesn't matter – it's possible to use the value before an action is used.

Tooltips can take on any value. While in the example below we use the text statement to display a string on the screen, it's also possible to use the add statement to add a displayable. More complex behavior is also possible.

screen tooltip\_test:

    default tt \= Tooltip("No button selected.")

    frame:
        xfill True

        has vbox

        textbutton "One.":
            action Return(1)
            hovered tt.Action("The loneliest number.")

        textbutton "Two.":
            action Return(2)
            hovered tt.Action("Is what it takes.")

        textbutton "Three.":
            action Return(3)
            hovered tt.Action("A crowd.")

        text tt.value
