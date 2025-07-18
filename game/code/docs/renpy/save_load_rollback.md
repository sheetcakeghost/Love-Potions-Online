# Saving, Loading, and Rollback

Ren'Py has support for saving game state, loading game state, and rolling back to a previous game state. Although implemented in a slightly different fashion, rollback can be thought of as saving the game at the start of each statement that interacts with the user, and loading saves when the user rolls back.

Note

While we usually attempt to keep save compatibility between releases, this compatibility is not guaranteed. We may decide to break save-compatibility if doing so provides a sufficiently large benefit.

## What is Saved

Ren'Py attempts to save the game state. This includes both internal state and Python state.

The internal state consists of all aspects of Ren'Py that are intented to change once the game has started, and includes:

*   The current statement, and all statements that can be returned to.
    
*   The images and displayables that are being shown.
    
*   The screens being shown, and the values of variables within those screens.
    
*   The music that Ren'Py is playing.
    
*   The list of nvl-mode text blocks.
    

The Python state consists of the variables in the store that have changed since the game began, and all objects reachable from those variables. Note that it's the change to the variables that matters – changes to fields in objects will not cause those objects to be saved.

Variables set using the  will always be saved.

In this example:

define a \= 1
define o \= object()
default c \= 17

label start:
    $ b \= 1
    $ o.value \= 42

only b and c will be saved. A will not be saved because it does not change once the game begins. O is not saved because it does not change – the object it refers to changes, but the variable itself does not.

## What isn't Saved

Python variables that are not changed after the game begins will not be saved. This can be a major problem if a variable that is not saved and one that is refer to the same object. (Alias the object.) In this example:

init python:
    a \= object()
    a.f \= 1

label start:
    $ b \= a
    $ b.f \= 2

    "a.f=\[a.f\] b.f=\[b.f\]"

a and b are aliased. Saving and loading may break this aliasing, causing a and b to refer to different objects. Since this can be very confusing, it's best to avoid aliasing saved and unsaved variables. (This is rare to encounter directly, but might come up when an unsaved variable and saved field alias.)

There are several other kinds of state that isn't saved:

control flow path

Ren'Py only saves the current statement, and the statement it needs to return to. It doesn't remember how it got there. Importantly, statements (including variable assignments) that are added to the game won't run.

mappings of image names to displayables

Since this mapping is not saved, the image may change to a new image when the game loads again. This allows an image to change to a new file as the game evolves.

configuration variables, styles, and style properties

Configuration variables and styles aren't saved as part of the game. Therefore, they should only be changed in `init` blocks, and left alone once the game has started.

## Where Ren'Py Saves

Saves occur at the start of a Ren'Py statement in the outermost interaction context.

What's important here is to note that saving occurs at the **start** of a statement. If a load or rollback occurs in the middle of a statement that interacts multiple times, the state will be the state that was active when the statement began.

This can be a problem in Python-defined statements. In:

python:

    i \= 0

    while i < 10:

        i += 1

        narrator("The count is now \[i\].")

if the user saves and loads in the middle, the loop will begin anew. Using Ren'Py script – rather than Python – to loop avoids this problem.:

$ i \= 0

while i < 10:

    $ i += 1

    "The count is now \[i\]."

## What Ren'Py Can Save

Ren'Py uses the Python pickle system to save game state. This module can save:

*   Basic types, such as True, False, None, int, str, float, complex, str, and Unicode objects.
    
*   Compound types, like lists, tuples, sets, and dicts.
    
*   Creator-defined objects, classes, functions, methods, and bound methods. For pickling these functions to succeed, they must remain available under their original names.
    
*   Character, Displayable, Transform, and Transition objects.
    

## What Ren'Py Can't Save

There are certain types that cannot be pickled:

*   Render objects.
    
*   Iterator objects.
    
*   Generator objects.
    
*   Coroutine tasks and futures, like those created with `async` and `await`.
    
*   File-like objects.
    
*   Network sockets, and objects that enclose them.
    
*   Inner functions and lambdas.
    

This may not be an exhaustive list.

Objects that can't be pickled can still be used, provided that their use is combined to namespaces that aren't saved by Ren'Py (like init variables, namespaces inside functions, or `python hide` blocks.)

For example, using a file object like:

$ monika\_file \= open(config.gamedir + "/monika.chr", "w")
$ monika\_file.write("Do not delete.")
$ monika\_file.close()

Won't work, as `f` could be saved between any of the three Python statements. Putting this in a `python hide` block will work:

python hide:

    monika\_file \= open(config.gamedir + "/monika.chr", "w")
    monika\_file.write("Do not delete.")
    monika\_file.close()

(Of course, using the python `with` statement would be cleaner.)

python hide:

    with open(config.gamedir + "/monika.chr", "w") as monika\_file:
        monika\_file.write("Do not delete.")

Coroutines, like those made with `async`, `await`, or the `asyncio` are similar. If you have:

init python:

    import asyncio

    async def sleep\_func():
        await asyncio.sleep(1)
        await asyncio.sleep(1)

then:

$ sleep\_task \= sleep\_func()
$ asyncio.run(sleep\_task)

will have problems, since sleep\_task can't be saved. But if it's not assigned to a variable:

$ asyncio.run(sleep\_func())

will run fine.

## Save Functions and Variables

There is one variable that is used by the high-level save system: .

This is a string that is stored with each save. It can be used to give a name to the save, to help users tell them apart.

More per-save data customization can be done with the Json supplementary data system, see .

There are a number of high-level save actions and functions defined in the . In addition, there are the following low-level save and load actions.

renpy.can\_load(_filename_, _test\=False_)

Returns true if filename exists as a save slot, and False otherwise.

renpy.copy\_save(_old_, _new_)

Copies the save at old to new. (Does nothing if old does not exist.)

renpy.list\_saved\_games(_regexp\='.'_, _fast\=False_)

Lists the save games. For each save game, returns a tuple containing:

*   The filename of the save.
    
*   The extra\_info that was passed in.
    
*   A displayable that, when displayed, shows the screenshot that was used when saving the game.
    
*   The time the game was stayed at, in seconds since the UNIX epoch.
    

regexp

A regular expression that is matched against the start of the filename to filter the list.

fast

If fast is true, the filename is returned instead of the tuple.

renpy.list\_slots(_regexp\=None_)

Returns a list of non-empty save slots. If regexp exists, only slots that begin with regexp are returned. The slots are sorted in string-order.

renpy.load(_filename_)

Loads the game state from the save slot filename. If the file is loaded successfully, this function never returns.

renpy.newest\_slot(_regexp\=None_)

Returns the name of the newest save slot (the save slot with the most recent modification time), or None if there are no (matching) saves.

If regexp exists, only slots that begin with regexp are returned.

renpy.rename\_save(_old_, _new_)

Renames a save from old to new. (Does nothing if old does not exist.)

renpy.save(_filename_, _extra\_info\=''_)

Saves the game state to a save slot.

filename

A string giving the name of a save slot. Despite the variable name, this corresponds only loosely to filenames.

extra\_info

An additional string that should be saved to the save file. Usually, this is the value of .

 should be called before this function.

renpy.slot\_json(_slotname_)

Returns the json information for slotname, or None if the slot is empty.

Much like the `d` argument to the  function, it will be returned as a dictionary. More precisely, the dictionary will contain the same data as it did when the game was saved.

renpy.slot\_mtime(_slotname_)

Returns the modification time for slot, or None if the slot is empty.

renpy.slot\_screenshot(_slotname_)

Returns a display that can be used as the screenshot for slotname, or None if the slot is empty.

renpy.take\_screenshot()

Causes a screenshot to be taken. This screenshot will be saved as part of a saved game.

renpy.unlink\_save(_filename_)

Deletes the save slot with the given name.

## Retaining Data After Load

When a game is loaded, the state of the game is reset (using the rollback system described below) to the state of the game when the current statement began executing.

In some cases, this may not be desirable. For example, when a screen allows editing of a value, we may want to retain that value when the game is loaded. When renpy.retain\_after\_load is called, data will not be reverted when a game is saved and loaded before the end of the next checkpointed interaction.

Note that while data is not changed, control is reset to the start of the current statement. That statement will execute again, with the new data in place at the start of the statement.

For example:

screen edit\_value:
    hbox:
        text "\[value\]"
        textbutton "+" action SetVariable("value", value + 1)
        textbutton "-" action SetVariable("value", value \- 1)
        textbutton "+" action Return(True)

label start:
    $ value \= 0
    $ renpy.retain\_after\_load()
    call screen edit\_value

renpy.retain\_after\_load()

Causes data modified between the current statement and the statement containing the next checkpoint to be retained when a load occurs.

## Rollback

Rollback allows the user to revert the game to an earlier state in much the same way as undo/redo systems that are available in most modern applications. While the system takes care of maintaining the visuals and game variables during rollback events, there are several things that should be considered while creating a game.

## What Data is Rolled Back?

Rollback affects variables that have been changed after the init phase, and objects of revertable types reachable from those variables. The short version is that lists, dicts, and sets created in Ren'Py script are revertable as are instances of classes defined in Ren'Py scripts. Data created inside Python or inside Ren'Py usually isn't revertable.

In more detail, inside the stores that Python embedded inside Ren'Py scripts run in, the object, list, dict, and set types have been replaced with equivalent types that are revertable. Objects that inherit from these types are also revertable. The  type inherits from the revertable object type.

To make the use of revertable objects more convenient, Ren'Py modifies Python found inside Ren'Py script files in the following way.

*   Literal lists, dicts, and sets are automatically converted to the revertable equivalent.
    
*   List, dict, and set comprehensions are also automatically converted to the revertable equivalent.
    
*   Other python syntax, such as extended unpacking, that can create lists, dicts, or sets converts the result to the revertable equivalent. However, for performance reasons, double-starred parameters to functions and methods (that create dictionaries of extra keyword arguments) are not converted to revertable objects.
    
*   Classes that do not inherit from any other types automatically inherit from the revertable object.
    

In addition:

*   The methods and operators of revertable types have been modified to return revertable objects when a list, dict, or set is produced.
    
*   Built in functions that return lists, dicts, and sets return a revertable equivalent.
    

Calling into Python code will not generally produce a revertable object. Some cases where you'll get an object that may not participate in rollback are:

*   Calling methods on built-in types, like the str.split method.
    
*   When the object is created in a Python module that's been imported, and then return to Ren'Py. (For example, an instance of collections.defaultdict won't participate in rollback.)
    
*   Objects returned from Ren'Py's API, unless documented otherwise.
    

If such data needs to participate in rollback, it may make sense to convert it to a type that does partipate. For example:

\# Calling list inside Python-in-Ren'Py converts a non-revertable list
\# into a revertable one.
$ attrs \= list(renpy.get\_attributes("eileen"))

## Supporting Rollback and Roll Forward

Most Ren'Py statements automatically support rollback and roll forward. If you call  directly, you'll need to add support for rollback and roll-forward yourself. This can be done using the following structure:

\# This is None if we're not rolling back, or else the value that was
\# passed to checkpoint last time if we're rolling forward.
roll\_forward \= renpy.roll\_forward\_info()

\# Set up the screen here...

\# Interact with the user.
rv \= ui.interact(roll\_forward\=roll\_forward)

\# Store the result of the interaction.
renpy.checkpoint(rv)

It's important that your game does not interact with the user after renpy.checkpoint has been called. (If you do, the user may not be able to rollback.)

renpy.can\_rollback()

Returns true if we can rollback.

renpy.checkpoint(_data\=None_, _\*_, _hard\=True_)

Makes the current statement a checkpoint that the user can rollback to. Once this function has been called, there should be no more interaction with the user in the current statement.

This will also clear the current screenshot used by saved games.

data

This data is returned by  when the game is being rolled back.

hard

If true, this is a hard checkpoint that rollback will stop at. If false, this is a soft checkpoint that will not stop rollback.

renpy.get\_identifier\_checkpoints(_identifier_)

Given a rollback\_identifier from a HistoryEntry object, returns the number of checkpoints that need to be passed to  to reach that identifier. Returns None of the identifier is not in the rollback history.

renpy.in\_rollback()

Returns true if the game has been rolled back.

renpy.roll\_forward\_info()

When in rollback, returns the data that was supplied to  the last time this statement executed. Outside of rollback, returns None.

renpy.rollback(_force\=False_, _checkpoints\=1_, _defer\=False_, _greedy\=True_, _label\=None_, _abnormal\=True_)

Rolls the state of the game back to the last checkpoint.

force

If true, the rollback will occur in all circumstances. Otherwise, the rollback will only occur if rollback is enabled in the store, context, and config.

checkpoints

Ren'Py will roll back through this many calls to renpy.checkpoint. It will roll back as far as it can, subject to this condition.

defer

If true, the call will be deferred until control returns to the main context.

greedy

If true, rollback will finish just after the previous checkpoint. If false, rollback finish just before the current checkpoint.

label

If not None, a label that is called when rollback completes.

abnormal

If true, the default, script executed after the transition is run in an abnormal mode that skips transitions that would have otherwise occured. Abnormal mode ends when an interaction begins.

renpy.suspend\_rollback(_flag_)

Rollback will skip sections of the game where rollback has been suspended.

flag:

When flag is true, rollback is suspended. When false, rollback is resumed.

## Blocking Rollback

Warning

Blocking rollback is a user-unfriendly thing to do. If a user mistakenly clicks on an unintended choice, he or she will be unable to correct their mistake. Since rollback is equivalent to saving and loading, your users will be forced to save more often, breaking game engagement.

It is possible to disable rollback in part or in full. If rollback is not wanted at all, it can simply be turned off through the  option.

More common is a partial block of rollback. This can be achieved by the  function. When called, it will instruct Ren'Py not to roll back before that point. For example:

label final\_answer:
    "Is that your final answer?"

menu:
    "Yes":
        jump no\_return
    "No":
        "We have ways of making you talk."
        "You should contemplate them."
        "I'll ask you one more time..."
        jump final\_answer

label no\_return:
    $ renpy.block\_rollback()

    "So be it. There's no turning back now."

When the label no\_return is reached, Ren'Py won't allow a rollback back to the menu.

## Fixing Rollback

Fixing rollback provides for an intermediate choice between unconstrained rollback and blocking rollback entirely. Rollback is allowed, but the user is not allowed to make changes to their decisions. Fixing rollback is done with the  function, as shown in the following example:

label final\_answer:
    "Is that your final answer?"
menu:
    "Yes":
        jump no\_return
    "No":
        "We have ways of making you talk."
        "You should contemplate them."
        "I'll ask you one more time..."
        jump final\_answer

label no\_return:
    $ renpy.fix\_rollback()

    "So be it. There's no turning back now."

Now, after the fix\_rollback function is called, it will still be possible for the user to roll back to the menu. However, it will not be possible to make a different choice.

There are some caveats to consider when designing a game for fix\_rollback. Ren'Py will automatically take care of locking any data that is given to `checkpoint()`. However, due to the generic nature of Ren'Py, it is possible to write scripts that bypass this and change things in ways that may have unpredictable results. Most notably, `call screen` doesn't work well with fixed rollback. It is up to the creator to block rollback at problematic locations.

The internal user interaction options for menus,  and `renpy.imagemap()` are designed to fully work with fix\_rollback.

## Styling Fixed Rollback

Because fix\_rollback changes the functionality of menus and imagemaps, it is advisable to reflect this in the appearance. To do this, it is important to understand how the widget states of the menu buttons are changed. There are two modes that can be selected through the  option.

The default option will set the chosen option to "selected", thereby activating the style properties with the "selected\_" prefix. All other buttons will be made insensitive and show using the properties with the "insensitive\_" prefix. Effectively this leaves the menu with a single selectable choice.

When the  option is set to False, all buttons are made insensitive. This means that the chosen option will use the "selected\_insensitive\_" prefix for the style properties while the other buttons use properties with the "insensitive\_" prefix.

## Fixed Rollback and Custom Screens

To simplify the creation of custom screens, two actions are provided to help with the most common uses. The  action returns the value when the button it is attached to is clicked. The  action can be used to jump to a script label. However, this action only works properly when the screen is called trough a `call screen` statement.

Examples:

screen demo\_imagemap():
    roll\_forward True

    imagemap:
        ground "imagemap\_ground.jpg"
        hover "imagemap\_hover.jpg"
        selected\_idle "imagemap\_selected\_idle.jpg"
        selected\_hover "imagemap\_hover.jpg"

        hotspot (8, 200, 78, 78) action ui.ChoiceJump("swimming", "go\_swimming", block\_all\=False)
        hotspot (204, 50, 78, 78) action ui.ChoiceJump("science", "go\_science\_club", block\_all\=False)
        hotspot (452, 79, 78, 78) action ui.ChoiceJump("art", "go\_art\_lessons", block\_all\=False)
        hotspot (602, 316, 78, 78) action ui.ChoiceJump("home", "go\_home", block\_all\=False)

screen rps():
    roll\_forward True

    hbox:
        imagebutton:
            idle "rock.png"
            hover "rock\_hover.png"
            selected\_insensitive "rock\_hover.png"
            action ui.ChoiceReturn("rock", "Rock", block\_all\=True)
        imagebutton:
            idle "paper.png"
            hover "paper\_hover.png"
            selected\_insensitive "paper\_hover.png"
            action ui.ChoiceReturn("paper", "Paper", block\_all\=True)
        imagebutton:
            idle "scissors.png"
            hover "scissors\_hover.png"
            selected\_insensitive "scissors\_hover.png"
            action ui.ChoiceReturn("scissors", "Scissors", block\_all\=True)

        if renpy.in\_fixed\_rollback():
            textbutton "Advance":
                action Return(renpy.roll\_forward\_info())
                \# required because of the block\_all=True in all the other buttons

label dough:
    call screen rps
    $ chosen \= \_return
    $ renpy.fix\_rollback()
    m "\[chosen\]!"

When writing custom Python routines that must play nice with the fix\_rollback system there are a few simple things to know. First of all the  function can be used to determine whether the game is currently in fixed rollback state. Second, when in fixed rollback state,  will always return the supplied roll\_forward data regardless of what action was performed. This effectively means that when the / functions are used, most of the work is done.

## Rollback-blocking and -fixing Functions

renpy.block\_rollback()

Prevents the game from rolling back to before the current statement.

renpy.fix\_rollback()

Prevents the user from changing decisions made before the current statement.

renpy.in\_fixed\_rollback()

Returns true if rollback is currently occurring and the current context is before an executed renpy.fix\_rollback() statement.

ui.ChoiceJump(_label_, _value_, _location\=None_, _block\_all\=None_, _sensitive\=True_, _args\=None_, _kwargs\=None_)

A menu choice action that returns value, while managing the button state in a manner consistent with fixed rollback. (See block\_all for a description of the behavior.)

label

The label text of the button. For imagebuttons and hotspots this can be anything. This label is used as a unique identifier of the options within the current screen. Together with location it is used to store whether this option has been chosen.

value

The location to jump to.

location

A unique location identifier for the current choices screen.

block\_all

If false, the button is given the selected role if it was the chosen choice, and insensitive if it was not selected.

If true, the button is always insensitive during fixed rollback.

If None, the value is taken from the  variable.

When true is given to all items in a screen, it will become unclickable (rolling forward will still work).

ui.ChoiceReturn(_label_, _value_, _location\=None_, _block\_all\=None_, _sensitive\=True_, _args\=None_, _kwargs\=None_)

A menu choice action that returns value, while managing the button state in a manner consistent with fixed rollback. (See block\_all for a description of the behavior.)

label

The label text of the button. For imagebuttons and hotspots this can be anything. This label is used as a unique identifier of the options within the current screen. Together with location it is used to store whether this option has been chosen.

value

The value this is returned when the choice is chosen.

location

A unique location identifier for the current choices screen.

block\_all

If false, the button is given the selected role if it was the chosen choice, and insensitive if it was not selected.

If true, the button is always insensitive during fixed rollback.

If None, the value is taken from the  variable.

When true is given to all items in a screen, it will become unclickable (rolling forward will still work).

## NoRollback

_class_ NoRollback

Instances of this class, and classes inheriting from this class, do not participate in rollback. Objects reachable through an instance of a NoRollback class only participate in rollback if they are reachable through other paths.

_class_ SlottedNoRollback

Instances of classes inheriting from this class do not participate in rollback. The difference between this and  is that this class does not have an associated dictionary, hence can be used with `__slots__` to reduce memory usage.

Objects reachable through an instance of a NoRollback class only participate in rollback if they are reachable through other paths.

For example:

init python:

    class MyClass(NoRollback):
        def \_\_init\_\_(self):
            self.value \= 0

label start:
    $ o \= MyClass()

    "Welcome!"

    $ o.value += 1

    "o.value is \[o.value\]. It will increase each time you rollback and then click ahead."

## Rollback-Supporting Classes

The following classes exist to help support the use of rollback in your game. They may be useful in some circumstances.

_class_ MultiRevertable

MultiRevertable is a mixin class that allows an object to inherit from more than one kind of revertable object. To use it, from MultiRevertable, then from the revertable classes you want to inherit from.

For example:

class MyDict(MultiRevertable, dict, object):
    pass

will create an class that will rollback both its dict contents and object fields.

_class_ defaultdict(_default\_factory_, _/_, _\*args_, _\*\*kwargs_)

This is a revertable version of collections.defaultdict. It takes a factory function. If a key is accessed that does not exist, the default\_factory function is called with the key as an argument, and the result is returned.

While the default\_factory attribute is present on this object, it does not participate in rollback, and so should not be changed.
