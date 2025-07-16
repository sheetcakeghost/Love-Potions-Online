# Character Callbacks

Ren'Py includes the ability to execute callbacks when various events occur during dialogue. This is done by giving the callback argument to , or setting the  or  variables.

The character callback is called with a single positional argument, the event that occured. Possible events are:

"begin"

Called at the start of a say statement.

"show"

Called before showing each segment of dialogue. Dialogue may be separated into multiple segments by the {w} or {p} text tags, but always consists of at least one segment.

"show\_done"

Called after showing each segment of dialogue.

"slow\_done"

Called after slow text finishes showing. Note that this event may occur after "end", in cases where dialogue does not cause an interaction to occur.

"end"

Called at the end of a say statement.

The callback is called with at the keyword arguments:

interact

This is true if the dialogue causes an interaction to occur.

type

The type of character (e.g. "nvl", "adv", "bubble").

what

The text that is going to be supplied to the what displayable.

multiple

The multiple argument to .

The "show" and "slow\_done" callbacks are also given additional keyword arguments:

start

The start of the current segment of dialogue, in the what string.

end

The end of the current segment of dialogue, in the what string.

delay

The amount of time Ren'Py will pause after the current segment of dialogue is shown, or None if Ren'Py will pause until the player clicks.

last\_segment

True if this is the last segment of dialogue in the say statement, False otherwise.

Other values of the positional argument and additional keyword arguments may be supplie to the callback. The callback should be written to ignore keyword arguments it does not understand.

## Example

This example plays beeps in place of a character voice, when slow text is enabled:

init python:
    def beepy\_voice(event, interact\=True, \*\*kwargs):
        if not interact:
            return

        if event \== "show\_done":
            renpy.sound.play("beeps.ogg")
        elif event \== "slow\_done":
            renpy.sound.stop()

define pike \= Character("Christopher Pike", callback\=beepy\_voice)

label start:

    pike "So, hanging out on Talos IV, minding my own business, when..."

To specialize a general callback with for specific characters, you can pass arguments to the callback function with the cb\_ prefix:

init python:
    def boopy\_voice(event, interact\=True, boopfile\="normal\_boop.ogg", \*\*kwargs):
        if not interact:
            return

        if event \== "show\_done":
            renpy.sound.play(boopfile)
        elif event \== "slow\_done":
            renpy.sound.stop()

define chrisjen \= Character("Chrisjen", callback\=boopy\_voice)
define nagata \= Character("Naomi", callback\=boopy\_voice, cb\_boopfile\="sfx-blipmale.ogg")
