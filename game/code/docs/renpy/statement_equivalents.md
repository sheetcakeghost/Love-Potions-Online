# Statement Equivalents

To allow Ren'Py to be scripted in Python, each Ren'Py statement has a Python equivalent. This usually consists of a Python function, but may also consist of a pattern of Python calls that perform an action equivalent to the statement.

Note that using statement equivalents in lieu of the original statements usually removes any possible  checks and prediction optimizations, making your game less easily checkable and possibly less fluid. It can also disable features in certain cases.

## Dialogue

Warning

Several features, such as skipping already-seen dialogues, are not available using the python version and only enabled when using the native say statement.

The Ren'Py  is equivalent to calling the character object (when any is present) as a function. Displaying narration (meaning when no character is supplied) can be done the same way, by using the `narrator` character.

e "Hello, world."
$ e("Hello, world.")

"And then the sun exploded."
$ narrator("And then the sun exploded.")

### Proxy functions

This equivalence of characters and function objects works in the other direction as well. It is possible to declare a Python function, and then use that function in the place of a character object in a native say statement. For example, the following function uses a variable to choose between two characters.

define lucy\_normal \= Character("Lucy")
define lucy\_evil \= Character("Evil Lucy")

init python:

    def l(what, \*\*kwargs):
        if lucy\_is\_evil:
            lucy\_evil(what, \*\*kwargs)
        else:
            lucy\_normal(what, \*\*kwargs)

label start:

    $ lucy\_is\_evil \= False

    l "Usually, I feel quite normal."

    $ lucy\_is\_evil \= True

    l "But sometimes, I get really mad!"

A function used in this way should either ignore unknown keyword arguments, or pass them to a character function. Doing this will allow the game to continue working if future versions of Ren'Py add additional keyword arguments to character calls.

Note that unlike other possible arguments, `interact=True` will always be passed to the function - unless manually passing `(interact=False)`. A  sees the arguments (including the supplementary interact) passed to the function. For example:

e "Hello, world." (what\_size\=32)

resolves to the following call:

e("Hello, world.", what\_size\=32, interact\=True)

Note that it's not required to pass `interact=True` when calling a Character object for it to work as intended. The following works just as well:

$ e("Hello, world.", what\_size\=32)

When e is a Character, this is further equivalent to:

$ Character(kind\=e, what\_size\=32)("Hello, world.")

But it's possible to use  or have `e` wrap a character to do things differently.

There is one additional way of replacing the say statement using Python:

renpy.say(_who_, _what_, _\*args_, _\*\*kwargs_)

The equivalent of the say statement.

who

Either the character that will say something, None for the narrator, or a string giving the character name. In the latter case, the  store function is called.

what

A string giving the line to say. Percent-substitutions are performed in this string.

interact

If true, Ren'Py waits for player input when displaying the dialogue. If false, Ren'Py shows the dialogue, but does not perform an interaction. (This is passed in as a keyword argument.)

This function is rarely necessary, as the following three lines are equivalent.

e "Hello, world."
$ renpy.say(e, "Hello, world.")
$ e("Hello, world.") \# when e is not a string
$ say(e, "Hello, world.") \# when e is a string

### Dialogue Window Management

 is performed by setting the  and  variables, and by using the following two functions:

\_window\_hide(_trans\=False_, _auto\=False_)

The Python equivalent of the `window hide` statement.

trans

If False, the default window hide transition is used. If None, no transition is used. Otherwise, the specified transition is used.

auto

If True, this becomes the equivalent of the `window auto hide` statment.

\_window\_show(_trans\=False_, _auto\=False_)

The Python equivalent of the `window show` statement.

trans

If False, the default window show transition is used. If None, no transition is used. Otherwise, the specified transition is used.

auto

If True, this becomes the equivalent of the `window auto show` statement.

## Choice Menus

The  has an equivalent Python function.

_class_ renpy.Choice(_value_, _/_, _\*args_, _\*\*kwargs_)

This encapsulates a menu choice with with arguments. The first positional argument is is the value that will be returned, and the other arguments are the arguments that will be passed to the choice screen.

This is intended for use in the items list of  to supply arguments to that screen.

value

The value that will be given to the choice screen.

Positional arguments and keyword arguments are stored in this object and used by renpy.display\_menu.

renpy.display\_menu(_items_, _\*_, _interact\=True_, _screen\='choice'_, _type\='menu'_, _\_layer\=None_, _args\=None_, _kwargs\=None_)

This displays a menu to the user. items should be a list of 2-item tuples. In each tuple, the first item is a textual label, and the second item is the value to be returned if that item is selected. If the value is None, the first item is used as a menu caption.

This function takes many optional arguments, of which only a few are documented. Except for items, all arguments should be given as keyword arguments.

interact

If false, the menu is displayed, but no interaction is performed.

screen

The name of the screen used to display the menu.

type

May be "menu" or "nvl". If "nvl", the menu is displayed in NVL mode. Otherwise, it is displayed in ADV mode.

\_layer

The layer to display the menu on. If not given, defaults to  for normal choice menus, and `config.nvl_choice_layer` for NVL choice menus.

\_args

If not None, this should be a tuple containing the positional  supplied to this menu.

\_kwargs

If not None, this should be a dict containing the keyword  supplied to this menu.

Note that most Ren'Py games do not use menu captions, but use narration instead. To display a menu using narration, write:

$ narrator("Which direction would you like to go?", interact\=False)
$ result \= renpy.display\_menu(\[ ("East", "east"), ("West", "west") \])

If you need to supply per-item arguments, use  objects as the values. For example:

renpy.display\_menu(\[
    ("East", renpy.Choice("east", icon\="right\_arrow"),
    ("West", renpy.Choice("west", icon\="left\_arrow"),
    \])

## Displaying Images

The image, scene, show, and hide statements each have an equivalent Python function (see  for the original statements).

renpy.get\_at\_list(_name_, _layer\=None_)

Returns the list of transforms being applied to the image with tag name on layer. Returns an empty list if no transforms are being applied, or None if the image is not shown.

If layer is None, uses the default layer for the given tag.

renpy.hide(_name_, _layer\=None_)

Hides an image from a layer. The Python equivalent of the hide statement.

name

The name of the image to hide. Only the image tag is used, and any image with the tag is hidden (the precise name does not matter).

layer

The layer on which this function operates. If None, uses the default layer associated with the tag.

renpy.image(_name_, _d_)

Defines an image. This function is the Python equivalent of the image statement.

name

The name of the image to display, a string.

d

The displayable to associate with that image name.

This function may only be run from inside an init block. It is an error to run this function once the game has started.

renpy.scene(_layer\='master'_)

Removes all displayables from layer. This is equivalent to the scene statement, when the scene statement is not given an image to show.

A full scene statement is equivalent to a call to renpy.scene followed by a call to . For example:

scene bg beach

is equivalent to:

$ renpy.scene()
$ renpy.show("bg beach")

renpy.show(_name_, _at\_list\=\

Shows an image on a layer. This is the programmatic equivalent of the show statement.

name

The name of the image to show, a string.

at\_list

A list of transforms that are applied to the image. The equivalent of the `at` property.

layer

A string, giving the name of the layer on which the image will be shown. The equivalent of the `onlayer` property. If None, uses the default layer associated with the tag.

what

If not None, this is a displayable that will be shown in lieu of looking on the image. (This is the equivalent of the show expression statement.) When a what parameter is given, name can be used to associate a tag with the image.

zorder

An integer, the equivalent of the `zorder` property. If None, the zorder is preserved if it exists, and is otherwise set to 0.

tag

A string, used to specify the image tag of the shown image. The equivalent of the `as` property.

behind

A list of strings, giving image tags that this image is shown behind. The equivalent of the `behind` property.

atl

If not None, an ATL Transform that will be applied. This takes only the ATL itself, it does not apply prior state.

show a
$ renpy.show("a")

show expression w
\# anonymous show expression : no equivalent

show expression w as a
$ renpy.show("a", what\=w)
$ renpy.show("y", what\=w, tag\="a") \# in this case, name is ignored

show a at T, T2
$ renpy.show("a", at\_list\=(T, T2))

show a onlayer b behind c zorder d as e
$ renpy.show("a", layer\="b", behind\=\["c"\], zorder\="d", tag\="e")

renpy.show\_layer\_at(_at\_list_, _layer\='master'_, _reset\=True_, _camera\=False_)

The Python equivalent of the `show layer` layer `at` at\_list statement. If camera is True, the equivalent of the `camera` statement.

reset

If true, the transform state is reset to the start when it is shown. If false, the transform state is persisted, allowing the new transform to update that state.

## Transitions

The equivalent of the  is the  function.

renpy.with\_statement(_trans_, _always\=False_)

Causes a transition to occur. This is the Python equivalent of the with statement.

trans

The transition.

always

If True, the transition will always occur, even if the user has disabled transitions.

This function returns true if the user chose to interrupt the transition, and false otherwise.

## Jump

The equivalent of the  is the  function.

renpy.jump(_label_)

Causes the current statement to end, and control to jump to the given label.

## Call

The equivalent of the  is the  function.

renpy.call(_label_, _\*args_, _from\_current\=False_, _\*\*kwargs_)

Causes the current Ren'Py statement to terminate, and a jump to a label to occur. When the jump returns, control will be passed to the statement following the current statement.

The label must be either of the form "global\_name" or "global\_name.local\_name". The form ".local\_name" is not allowed.

from\_current

If true, control will return to the current statement, rather than the statement following the current statement. (This will lead to the current statement being run twice. This must be passed as a keyword argument.)

renpy.return\_statement(_value\=None_)

Causes Ren'Py to return from the current Ren'Py-level call.

## Pause

The equivalent of the  is the  function.

renpy.pause(_delay\=None_, _\*_, _predict\=False_, _modal\=True_, _hard\=False_)

Causes Ren'Py to pause. Returns true if the user clicked to end the pause, or false if the pause timed out or was skipped.

delay

If given, the number of seconds Ren'Py should pause for.

The following should be given as keyword arguments:

predict

If True, when all prediction - including prediction scheduled with  and  - has been finished, the pause will be ended.

This also causes Ren'Py to prioritize prediction over display smoothness for the duration of the pause. Because of that, it's recommended to not display animations during prediction.

The pause will still end by other means - when the user clicks or skips, or when the delay expires (if any).

modal

If True, a timed pause will not end (it will hold) when a modal screen is being displayed. If False, the pause will end while a modal screen is being displayed.

hard

When True, Ren'Py may prevent the user from clicking to interrupt the pause. If the player enables skipping, the hard pause will be skipped. There may be other circumstances where the hard pause ends early or prevents Ren'Py from operating properly, these will not be treated as bugs.

In general, using hard pauses is rude. When the user clicks to advance the game, it's an explicit request - the user wishes the game to advance. To override that request is to assume you understand what the player wants more than the player does.

tl;dr - Don't use renpy.pause with hard=True.

Calling renpy.pause guarantees that whatever is on the screen will be displayed for at least one frame, and hence has been shown to the player.

## Layeredimage

The  statement has Python equivalents. The group statement does not: the name of the group is supplied to , and the `auto` feature can be implemented using .

_class_ Attribute(_group_, _attribute_, _image\=None_, _default\=False_, _group\_args\={}_, _\*\*kwargs_)

This is used to represent a layer of an LayeredImage that is controlled by an attribute. A single attribute can control multiple layers, in which case all layers corresponding to that attribute will be displayed.

group

A string giving the group the attribute is part of. This may be None, in which case a group with the same name as the attribute is created.

attribute

A string giving the name of the attribute.

image

If not None, this should be a displayable that is displayed when this attribute is shown.

default

If True, and no other attribute for the group is selected, this attribute is.

The following keyword arguments are also known:

at

A transform or list of transforms that are applied to the image.

if\_all

An attribute or list of attributes. The displayable is only shown if all of these are showing.

if\_any

An attribute or list of attributes. if not empty, the displayable is only shown if any of these are showing.

if\_not

An attribute or list of attributes. The displayable is only shown if none of these are showing.

Other keyword arguments are interpreted as transform properties. If any are present, a transform is created that wraps the image. (For example, pos=(100, 200) can be used to offset the image by 100 pixels horizontally and 200 vertically.)

If the image parameter is omitted or None, and the LayeredImage has been given the image\_format parameter, the image\_format is used to generate an image filename.

_class_ Condition(_condition_, _image_, _\*\*kwargs_)

When the condition is true, the layer is displayed. Otherwise, nothing is displayed.

This is used to implement a single `if`, `elif` **or** `else` layeredimage statement (for `else`, condition should be "True"). Several Conditions can then be passed to a  to emulate a full if/elif/else statement.

condition

This should be a string giving a Python condition that determines if the layer is displayed.

image

If not None, this should be a displayable that is displayed when the condition is true.

if\_all

An attribute or list of attributes. The condition is only evaluated if all of these are showing.

if\_any

An attribute or list of attributes. If not empty, the condition is only evaluated if any of these are showing.

if\_not

An attribute or list of attributes. The condition is only evaluated if none of these are showing.

at

A transform or list of transforms that are applied to the image.

Other keyword arguments are interpreted as transform properties. If any is present, a transform is created that wraps the image. (For example, pos=(100, 200) can be used to offset the image by 100 pixels horizontally and 200 vertically.)

_class_ ConditionGroup(_conditions_)

Takes a list of  to combine them into a single .

Implements the if/elif/else statement.

_class_ LayeredImage(_attributes_, _at\=\

This is an image-like object that, when shown with the proper set of attributes, shows a displayable created by compositing together the displayables associated with those attribute.

attributes

This must be a list of Attribute, Condition, ConditionGroup or  objects. Each one reflects a displayable that may or may not be displayed as part of the image. The items in this list are in back-to-front order, with the first item further from the viewer and the last closest. Passing a displayable directly is the equivalent of the always layeredimage statement.

at

A transform or list of transforms that are applied to the displayable after it is parameterized.

name

The name of the layeredimage. This is used as part of the names of image components.

image\_format

When a given image is a string, and this is supplied, the image name is interpolated into image\_format to make an image file. For example, "sprites/eileen/{image}.png" will look for the image in a subdirectory of sprites. (This is not used by auto groups, which look for images and not image files.)

format\_function

A function that is used instead of layeredimage.format\_function to format the image information into a displayable.

attribute\_function

If not None, a function that's called with a set of attributes supplied to the image, and returns the set of attributes used to select layers. This is called when determining the layers to display, after the attribute themselves have been chosen. It can be used to express complex dependencies between attributes or select attributes at random.

offer\_screen

Sets whether or not the available area is taken into account as for how children are placed and how they are sized (when they have variable size). If False, the available area is considered, and if True it is not. If None, defaults to .

Additional keyword arguments may contain transform properties. If any are present, a transform is created that wraps the result image. Remaining keyword arguments are passed to a Fixed that is created to hold the layer. Unless explicitly overridden, xfit and yfit are set to true on the Fixed, which means it will shrink to the smallest size that fits all of the layer images it is showing.

A LayeredImage is not a displayable, and can't be used in all the places a displayable can be used. This is because it requires an image name (generally including image attributes) to be provided. As such, it should either be displayed through a scene or show statement, or by an image name string used as a displayable.

add(_a_)

a

An Attribute, Condition, ConditionGroup or  object.

This method adds the provided layer to the list of layers of the layeredimage, as if it had been passed in the attributes argument to the constructor.
