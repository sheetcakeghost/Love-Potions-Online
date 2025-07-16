# Store Variables

Ren'Py has a number of store variables that control its function. Store variables may be changed at any time. If a store variable is changed after the game has started, it will be be saved and loaded by the save system, and rolled-back when rollback occurs.

adv \= Character(...)

This is a template ADV-mode character, and the default character kind that is used when  is called.

\_autosave \= True

This variable can be set to False to disable autosave.

\_confirm\_quit \= True

This determines if quitting the game asks for confirmation. It is set to False during the splashscreen, and is ignored when in the main menu.

\_constant

If set to true in a store, indicates the store is constant. See .

default\_mouse

This is undefined by default. If defined, and if  is set at game startup, this is a key that is used to look up a mouse cursor when the current cursor does not exist, or is the default. This is used by  and .

See  for more information.

\_dismiss\_pause \= True

If True, the player can dismiss pauses and transitions.

\_game\_menu\_screen \= "save"

This is the screen that is displayed when entering the game menu with no more specific screen selected. (For example, when right-clicking, pressing escape, or when  is not given an argument.) If None, entry to the game menu is disallowed.

This is set to None at the start of the splashscreen, and restored to its original value when the splashscreen ends.

\_greedy\_rollback \= True

Determines if the game performs a greedy rollback after a load. A greedy rollback will rollback to just after the last statement that interacted, rather than to just before the statement that the game was in during the load.

\_history \= True

If true, Ren'Py will record dialogue history when a line is shown. (Note that  must be set as well.)

\_history\_list \= \

This is a list of history objects, corresponding to each line of history from oldest to newest. See the  section for more information.

\_ignore\_action \= None

When this is not None, it's an action that is run after clicking Ignore on the error handling screen. The action is usually , to jump the game to a place that can recover from an error. If None, control continues with the next Ren'Py statement.

main\_menu \= False

Ren'Py sets this variable to True while in the main menu. This can be used to have screens display differently while in the main menu.

\_menu \= False

Ren'Py sets this variable to True when entering a main menu or game menu context.

menu \= renpy.display\_menu

The function that's called to display the in-game menu. It should take the same arguments as , and pass unknown keyword arguments unchanged. Assigning  to this will display an nvl-mode menu.

mouse\_visible \= True

Controls if the mouse is visible. This is automatically set to true when entering the standard game menus.

name\_only \= Character(...)

This is a template character that is used when a string is given as the character name in a say statement. This:

"Eileen" "Hello, world."

is equivalent to:

$ temp\_char \= Character("Eileen", kind\=name\_only)
temp\_char "Hello, world."

except that the `temp_char` variable is not used.

narrator \= Character(...)

This is the character that speaks narration (say statements that do not give a character or character name). This:

"Hello, world."

is equivalent to:

narrator "Hello, world."

\_quit\_slot \= None

If not None, this should be a string giving the name of a file slot. When Ren'Py quits, the game will be saved in this slot.

\_rollback \= True

Controls if rollback is allowed.

say : Callable

A function that is called by Ren'Py to display dialogue, when a string is used in place of the speaking character:

define e \= Character("Eileen", who\_color\="#0f0")

label start:
    "Eileen" "My name is Eileen." \# will call the say function
    e "I like trains !" \# will not call the say function

This function should have the same signature as . It should not call  but rather use the other .

It's rare to call this function directly, as one can simply call a character with dialogue. This variable mostly exists to be redefined, as a way of hooking the say statement.

save\_name \= ""

A save name that is included with saves.

\_scene\_show\_hide\_transition \= None

If not None, this is a transition that will be performed using the with statement after a series of scene, show, and hide statements that are not followed by a with statement, or by a window transition.

See also

\_screenshot\_pattern \= None

If not None, this string is used in preference to  to determine the filename of a screenshot. Please see the documentation for that variable for the format of the string.

\_skipping \= True

Controls if skipping is allowed.

\_version \= ...

This is set to  when a new game is started. It can be used by the `after_load` label or  to determine which upgrades need to be done.

This is only set once, upon the initial start. After that, the game is responsible for updating \_version as necessary.

\_window \= False

This set by the `window show` and `window hide` statements, and indirectly by `window auto`. If true, the dialogue window is shown during non-dialogue statements.

\_window\_auto \= False

This is set to true by `window auto` and to false by `window show` and `window hide`. If true, the window auto behavior occurs.

\_window\_subtitle \= ''

This is appended to  to produce the caption for the game window. This is automatically set to  while in the game menu.
