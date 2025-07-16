# Python Statements

Ren'Py is written in the Python programming language, and includes support for including Python inside Ren'Py scripts. Python support can be used for many things, from setting a flag to creating new displayables. This chapter covers ways in which Ren'Py scripts can directly invoke Python, through the various Python statements.

Ren'Py 7 supports Python 2.7. Ren'Py 8 supports Python 3.9.

Note

If you know Python, you'll be able to take advantage of that. However, not everything you know about Python will apply directly. For example. Python packages that don't ship with Ren'Py may not work inside Ren'Py.

There are also some Python constructs that work, but may lead to problems in saving. Please read the  page for more details, especially the section on . (You need to be careful with files, sockets, iterators, task, futures, and generators.)

Finally, while many statements have Python equivalents, those equivalents can be inferior. For example, Ren'Py can predict the `show` statement, and load images early, but it can't predict the  function.

## Python

The `python` statement takes a block of Python, and runs the block when control reaches the statement. A basic Python statement can be very simple:

python:
    flag \= True

Python statements can get more complex, when necessary:

python:
    player\_health \= max(player\_health \- damage, 0)
    if enemy\_vampire:
        enemy\_health \= min(enemy\_health + damage, enemy\_max\_health)

There are two modifiers to the Python statement that change its behavior:

`hide`

If given the hide modifier, the Python statement will run the block of Python in an anonymous scope. The scope will be lost when the Python block terminates.

This allows Python to use temporary variables that can't be saved – but it means that the store needs to be accessed as fields on the store object, rather than directly.

`in`

The `in` modifier takes a name. Instead of executing in the default store, the Python will execute in the store with that name.

## One-line Python Statement

A common case is to have a single line of Python that runs in the default store. For example, a Python one-liner can be used to initialize or update a flag. To make writing Python one-liners more convenient, there is the one-line Python statement.

The one-line Python statement begins with the dollar-sign `$` character, and contains everything else on that line. Here are some example of Python one-liners:

\# Set a flag.
$ flag \= True

\# Initialize a variable.
$ romance\_points \= 0

\# Increment a variable.
$ romance\_points += 1

\# Call a function that exposes Ren'Py functionality.
$ renpy.movie\_cutscene("opening.ogv")

Python one-liners always run in the default store.

## Init Python Statement

The `init python` statement runs Python at initialization time, before the game loads. Among other things, this can be used to define classes and functions, or to initialize styles, config variables, or persistent data.

init python:

    def auto\_voice\_function(ident):
        return "voice/" + ident + ".ogg"

    config.auto\_voice \= auto\_voice\_function

    if persistent.endings is None:
        persistent.endings \= set()

init 1 python:

    \# The bad ending is always unlocked.
    persistent.endings.add("bad\_ending")

A priority number can be placed between `init` and `python`. When a priority is not given, 0 is used. Init statements are run in priority order, from lowest to highest. Init statements of the same priority are run in Unicode order by filepath, and then from top to bottom within a file.

To avoid conflict with Ren'Py, creators should use priorities in the range -999 to 999. Priorities of less than 0 are generally used for libraries and to set up themes. Normal init statements should have a priority of 0 or higher.

Init python statements also take the `hide` or `in` clauses.

Variables that have their value set in an init python block are not saved, loaded, and do not participate in rollback. Therefore, these variables should not be changed after init is over.

Warning

Classes created within Ren'py and inheriting nothing or explicitly inheriting `object`, and subclasses of these classes, do not support `__slots__`. Trying to do so will misbehave with rollback in older versions of renpy, and will raise errors in newer versions.

In order to have slotted classes, creators should explicitly subclass `python_object`, which doesn't support rollback.

## Define Statement

The `define` statement sets a single variable to a value at init time. The variable is treated as constant, and should not be changed after being set. For example:

define e \= Character("Eileen")

is equivalent (except for some advantages, see below) to:

init python:
    e \= Character("Eileen")

The define statement can take an optional named store (see below), by prepending it to the variable name with a dot. The store is created if it doesn't already exist. For example:

define character.e \= Character("Eileen")

The define statement can take an optional index, making it possible to add entries to a dictionary:

define config.tag\_layer\["eileen"\] \= "master"

In addition to `=`, define can take two more operators. The `+=` operator adds, and is generally used for list concatenaton. The `|=` or operator is generally used to concatenate sets. For example:

define config.keymap\["dismiss"\] += \[ "K\_KP\_PLUS" \]
define endings |= { "best\_ending" }

One advantage of using the define statement is that it records the filename and line number at which the assignment occurred, and makes that available to the navigation feature of the launcher. Another advantage is that  will be able to check defined values, for example by detecting whether the same variable is defined twice, potentially with different values.

Variables that are defined using the define statement are treated as constant, are not saved or loaded, and should not be changed. This constant-nature extends to objects reachable through these variables through field access and subscripting. (Ren'Py does not enforce this, but will produce undefined behavior when this is not the case.)

## Default Statement

The `default` statement sets a single variable to a value if that variable is not defined when the game starts, or after a new game is loaded. For example:

default points \= 0

When the variable `points` is not defined at game start, this statement is equivalent to:

label start:
    $ points \= 0

When the variable `points` is not defined at game load, it's equivalent to:

label after\_load:
    $ points \= 0

The default statement can take an optional named store (see below), by prepending it to the variable name with a dot. The store is created if it doesn't already exist. For example:

default schedule.day \= 0

As for the `define` statement,  offers checks and optimizations related to the `default` statement.

Note

It is highly recommended to `default` every variable in your game that is susceptible to change. If you use `init python` or `define` to declare a variable, when a player play a game and changes that variable, then goes back to the main menu and starts a new game, the variable will not have the value set in `init python` and so the former game will "leak" in the newly started one. If you create these variables in the start label instead, they will be missing when you load a save file that existed before.

## Names in the Store

The default place that Ren'Py stores Python variables is called the store. It's important to make sure that the names you use in the store do not conflict.

The define statement assigns a value to a variable, even when it's used to define a character. This means that it's not possible to use the same name for a character and a flag.

The following faulty script:

define e \= Character("Eileen")

label start:

    $ e \= 0

    e "Hello, world."

    $ e += 1
    e "You scored a point!"

will not work, because the variable `e` is being used as both a character and a flag. Other things that are usually placed into the store are transitions and transforms.

Names beginning with underscore `_` are reserved for Ren'Py's internal use. In addition, there is an .

## Other Named Stores

Named stores provide a way of organizing Python functions and variables into modules. By placing Python in named stores, you can minimize the chance of name conflicts. Each store corresponds to a Python module. The default store is `store`, while a named store is accessed as `store.named`.

Named stores can be created using `python in` blocks (or their `init python` or `python early` variants), or using `default`, `define` or  statements. Variables in can be imported individually using `from store.named import variable`, and a named store itself can be imported using `from store import named`.

Named stores can be accessed by supplying the `in` clause to `python` or `init python` (or `python early`), all of which run the Python they contain in the given named store.

For example:

init python in mystore:

    serial\_number \= 0

    def serial():

        global serial\_number
        serial\_number += 1
        return serial\_number

default character\_stats.chloe\_substore.friends \= {"Eileen",}

label start:
    $ serial \= mystore.serial()

    if "Lucy" in character\_stats.chloe\_substore.friends:
        chloe "Lucy is my friend !"
    elif character\_stats.chloe\_substore.friends:
        chloe "I have friends, but Lucy is not one of them."

    python in character\_stats.chloe\_substore:
        friends.add("Jeremy")

From a `python in` block, the default "outer" store can be accessed using either `renpy.store`, or `import store`.

Named stores participate in save, load, and rollback in the same way that the default store does. Special namespaces such as `persistent`, `config`, `renpy`... do not and never have supported substore creation within them.

## Constant Stores

A named store can be declared to be constant by setting a variable named `_constant` to a true value, using, for example:

init python in mystore:
    \_constant \= True

When a store is constant, variables in that store are not saved, and objects reachable solely from those variables do not participate in rollback.

Variables in a constant store can be changed during the init phase. It's only after init (including statements like `define`, `transform`, etc.) completes that the store must be treated as constant.

As Ren'Py has no way of enforcing this, it is the responsibility of the creator to ensure that variables in a constant store do not change after the init phase.

The reason for declaring a store constant is that each store and variable incurs a small amount of overhead to support saving, loading, and rollback. A constant store avoids this overhead.

The following stores are declared constant by default:

\_errorhandling
\_gamepad
\_renpysteam
\_warper
audio
achievement
build
director
iap
layeredimage
updater

## JSONDB

_class_ JSONDB(_filename_, _default\=None_)

A JSONDB is a two-level database that uses JSON to store its data It's intended to be used by game developers to store data in a database that can be version-controlled as part of the game script. For example, this can store information associated with each say statement, that can change how a say statement is displayed.

JSONDBs are not intended for data that is changed through or because of the player's actions.  or normal save files are better choices for that data.

The database should only contain data that Python can serialize to JSON. This includes lists, dictionaries (with strings as keys), strings, numbers, True, False, and None. See  about interoperability, how data converts between the two formats, and the various associated pitfalls.

The two levels of the database are dictionaries both keyed by strings. The first level is read only - when a key on the first level dictionary is accessed, a second level dictionary is created, optionally with default contents. The second level dictionary is read-write, and when one of the keys in a second level dictionary is changed, that change is saved to the database whe the game exits.

Like other persistent data, JSONDBs do not participate in rollback.

A JSONDB should be created during init (in an init python block or define statement), and will automatically be saved to the disk provided at least one key in the dictionary is set. For example:

define balloonData \= JSONDB("balloon.json", default\={ "enabled" : False })

This creates a JSONDB that is stored in the file balloon.json, and has a default values. The second leval values can be used as normal dictionaries:

screen say(who, what):

    default bd \= balloonData\[renpy.get\_translation\_identifier()\]

    if bd\["enabled"\]:
        use balloon\_say(who, what)
    else:
        use adv\_say(who, what)

    if config.developer:
        textbutton "Dialogue Balloon Mode":
            action ToggleDict(bd, "enabled")

The JSONDB constructor takes the following arguments:

filename

The filename the database is stored in. This is relative to the game directory. It's recommended that the filename end in ".json".

default

If this is not None, it should be a dictionary. When a new second level dictionary is created, this object is shallow copied and used to initialized the new dictionary. The new dictionary will only be saved as part of the database if at least one key in it is saved.

## First and Third-Party Python Modules and Packages

Ren'Py can import pure-Python modules and packages. First-party modules and packages – ones written for the game – can be placed directly into the game directory. Third party packages can be placed into the game/python-packages directory.

For example, to install the python-dateutil package, one can change into the game's base directory, and run the command:

pip install \--target game/python\-packages python\-dateutil

In either case, the module or package can be imported from an init python block:

init python:
    import dateutil.parser

Warning

Python defined in .rpy files is transformed to allow rollback to work. Python imported from .py files is not. As a result, objects created in Python will not work with rollback, and probably should not be changed after creation.

Not all Python packages are compatible with Ren'Py. It's up to you to audit the packages you install and make sure the packages will work.

## Injecting Python

Python can be injected into a game at runtime by creating a file named `exec.py` in the base directory. It's suggested that this file is created under a different name, edited, and then atomically moved into place.

When Ren'Py sees a file named `exec.py`, it will load the contents of the file, delete the file, and execute the contents in the game store using Python's `exec`. This is always done during an interaction.

This is intended to support debugging tools. By default it is enabled when developer mode is true, but can also be enabled by setting the RENPY\_EXEC\_PY environment variable.
