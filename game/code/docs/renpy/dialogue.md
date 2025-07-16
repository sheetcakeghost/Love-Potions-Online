# Dialogue and Narration

Text is fundamental to visual novels, and generally quite important to storytelling-based games. This text may consist of dialogue labeled with the character that is saying it, and narration, which does not have a speaker. (For convenience, we will lump both dialogue and narration together as dialogue, except where the differences are important.) It's also important that the user be able to customize the look of dialogue to suit their game.

In Ren'Py, most dialogue is written using say statements. The look of dialogue may be customized on a per-character basis by using Character objects.

## Say Statement

The `say` statement is used for dialogue and narration. Since it's almost always the most frequently used statement in Ren'Py scripts, the say statement has a syntax that minimizes the overhead in writing it. Some example say statements are:

    "This is narration."

    "Eileen" "This is dialogue, with an explicit character name."

    e "This is dialogue, using a character object instead."

    "Bam!!" with vpunch

The first form of the say statement consists of a string by itself. This form is used for narration, with the narration being the contents of the string.

The second form consists of two strings. The first string is the name of the character who is speaking, and the second is the dialogue being spoken.

The third form consists of a simple expression followed by a string. The simple expression should evaluate to either a string giving a character name, or a Character object. In the latter case, the character object is used to control how the dialogue is shown.

The final form consists of a string and a with clause which has a transition. In this case, the string is shown and a screen is shaken at the same time.

Although the precise details of what a say statement does is controlled by the character object used, the usual effect of a say statement is to display dialogue on the screen until the user clicks to dismiss it, then to remove that dialogue on the screen.

Certain characters have special meaning to Ren'Py, and so can't be used in dialogue strings. The `{` character begins a text tag, and the `[` character begins a substitution. To use them in dialogue, double them. It may also be necessary to precede a quote with a backslash to prevent it from closing the string. For example:

"I walked past a sign saying, Let's give it 100%%!"

It's also possible to use a proxy function instead of a character object. More details about this in .

## Defining Character Objects

By creating a Character object and using it in a say statement, you can customize the look (and to some extent, the behavior) of dialogue. Characters are created by using the `define` statement to assign a Character to a variable. For example:

define e \= Character("Eileen", who\_color\="#c8ffc8")

Once this is done, the character can be used in a say statement:

e "Hello, world."

Character is a Python function that takes a large number of keyword arguments. These keyword arguments control the behavior of the character.

Character(_name\=..._, _kind\=adv_, _\*\*args_)

Creates and returns a Character object, which controls the look and feel of dialogue and narration.

name

If a string, the name of the character for dialogue. When name is None, display of the name is omitted, as for narration. If no name is given, the name is taken from kind, and otherwise defaults to None.

kind

The Character to base this Character off of. When used, the default value of any argument not supplied to this Character is the value of that argument supplied to `kind`. This can be used to define a template character, and then copy that character with changes.

This can also be a namespace, in which case the 'character' variable in the namespace is used as the kind.

**Linked Image.** An image tag may be associated with a Character. This allows a say statement involving this character to display an image with the tag, and also allows Ren'Py to automatically select a side image to show when this character speaks.

image

A string giving the image tag that is linked with this character.

**Voice Tag.** If a voice tag is assign to a Character, the voice files that are associated with it, can be muted or played in the preference screen.

voice\_tag

A String that enables the voice file associated with the Character to be muted or played in the 'voice' channel.

**Prefixes and Suffixes.** These allow a prefix and suffix to be applied to the name of the character, and to the text being shown. This can be used, for example, to add quotes before and after each line of dialogue.

what\_prefix

A string that is prepended to the dialogue being spoken before it is shown.

what\_suffix

A string that is appended to the dialogue being spoken before it is shown.

who\_prefix

A string that is prepended to the name of the character before it is shown.

who\_suffix

A string that is appended to the name of the character before it is shown.

**Changing Name Display.** These options help to control the display of the name.

dynamic

If true, then name should either be a string containing a Python expression, a function, or a callable object. If it's a string, That string will be evaluated before each line of dialogue, and the result used as the name of the character. Otherwise, the function or callable object will be called with no arguments before each line of dialogue, and the return value of the call will be used as the name of the character.

**Controlling Interactions.** These options control if the dialogue is displayed, if an interaction occurs, and the mode that is entered upon display.

condition

If given, this should be a string containing a Python expression. If the expression is false, the dialogue does not occur, as if the say statement did not happen.

interact

If true, the default, an interaction occurs whenever the dialogue is shown. If false, an interaction will not occur, and additional elements can be added to the screen.

advance

If true, the default, the player can click to advance through the statement, and other means of advancing (such as skip and auto-forward mode) will also work. If false, the player will be unable to move past the say statement unless an alternate means (such as a jump hyperlink or screen) is provided.

callback

A function that is called when events occur while the character is speaking. See the section on  for more information.

**Click-to-continue.** A click-to-continue indicator is displayed once all the text has finished displaying, to prompt the user to advance.

ctc

A displayable to use as the click-to-continue indicator, unless a more specific indicator is used.

ctc\_pause

A displayable to use a the click-to-continue indicator when the display of text is paused by the {p} or {w} text tags.

ctc\_timedpause

A displayable to use a the click-to-continue indicator when the display of text is paused by the {p=} or {w=} text tags. When None, this takes its default from ctc\_pause, use `Null()` when you want a ctc\_pause but no ctc\_timedpause.

ctc\_position

Controls the location of the click-to-continue indicator. If `"nestled"`, the indicator is displayed as part of the text being shown, immediately after the last character. `"nestled-close"` is similar, except a break is not allowed between the text and the CTC indicator. If `"fixed"`, a new screen containing the CTC indicator is shown, and the position style properties of the CTC displayable are used to position the CTC indicator.

**Screens.** The display of dialogue uses a . These arguments allow you to select that screen, and to provide arguments to it.

screen

The name of the screen that is used to display the dialogue.

retain

If not true, an unused tag is generated for each line of dialogue, and the screens are shown non-transiently. Call  to remove all retaint screens. This is almost always used with .

Keyword arguments beginning with `show_` have the prefix stripped off, and are passed to the screen as arguments. For example, the value of `show_myflag` will become the value of the `myflag` variable in the screen. (The `myflag` variable isn't used by default, but can be used by a custom say screen.)

One show variable is, for historical reasons, handled by Ren'Py itself:

show\_layer

If given, this should be a string giving the name of the layer to show the say screen on.

**Styling Text and Windows.** Keyword arguments beginning with `who_`, `what_`, and `window_` have their prefix stripped, and are used to  the character name, the spoken text, and the window containing both, respectively.

For example, if a character is given the keyword argument `who_color="#c8ffc8"`, the color of the character's name is changed, in this case to green. `window_background="frame.png"` sets the background of the window containing this character's dialogue.

The style applied to the character name, spoken text, and window can also be set this way, using the `who_style`, `what_style`, and `window_style` arguments, respectively.

Setting  makes it possible to style other displayables as well. For example, when the default GUI is used, styles prefixed with `namebox_` are used to style the name of the speaking character.

## Say with Image Attributes

When a character is defined with an associated image tag, say statement involving that character may have image attributes placed between the character name and the second string.

In this form, if an image with the given tag is showing, Ren'Py will issue a show command involving the character tag and the attributes. If the image is not shown, Ren'Py will store the attributes for use by side images, but will not show an image.

For example:

define e \= Character("Eileen", image\="eileen")

label start:

    show eileen concerned
    e "I'm a little upset at you."

    e happy "But it's just a passing thing."

is equivalent to:

define e \= Character("Eileen")

label start:

    show eileen concerned
    e "I'm a little upset at you."

    show eileen happy
    e "But it's just a passing thing."

In the above example, the `concerned` and `happy` replace one another. But it is possible to revert to a `happy`\-less eileen without specifying the `concerned` attribute. An attribute name prepended with the minus sign ( - ) has that effect, just as it does with the .

For example:

define e \= Character("Eileen")

label start:

    show eileen
    e concerned "I'm a little upset at you."

    e happy "That's funny."

    e \-happy "I'm not sure what to think now."

When an @ is included in the list of attributes, any element placed after it has an only temporary effect, and is reverted at the end of the line of dialogue.

For example, the following code is equivalent to the previous example:

define e \= Character("Eileen", image\="eileen")

label start:

    show eileen concerned
    e "I'm a little upset at you."

    e @ happy "That's funny."

    e "I'm not sure what to think now."

A single line can combine permanent changes coming before the @, and temporary ones coming after.

e happy @ vhappy "Really! That changes everything."

The minus sign can also be used after the @ sign:

e @ right \-concerned "My anger is temporarily suspended..."
e "HOWEVER !"

To cause a transition to occur whenever the images are changed in this way, set  to a transition. For more control, use .

## Example Characters

Here are a few example characters:

\# A character that has its dialogue enclosed in parenthesis.
define e \= Character("Eileen", what\_prefix\='(', what\_suffix\=')')

\# A character that pulls its name from a variable.
define p \= Character("player\_name", dynamic\=True)

## Special Characters

A few character names are defined by default, and are used automatically in certain situations. Intentionally redefining these characters can change the behavior of Ren'Py, but accidentally using them can be a problem.

`adv`

The default kind of character used by Character. This sets up a character such that one line is displayed on the screen at a time.

`nvl`

A kind of Character that causes dialogue to be displayed in , with multiple lines of text on the screen at once.

`narrator`

The character that's used to display narration, by say statements without a character name.

`name_only`

A character that is used for dialogue in which the character name is given as a string. This character is copied to a new character with the given name, and then that new character is used to display the dialogue.

`centered`

A character that causes what it says to be displayed centered, in the middle of the screen, outside of any window.

`vcentered`

A character that causes what it says to be displayed centered in vertically oriented text, in the middle of the screen, outside of any window.

`extend`

A character that causes the last character to speak to say a line of dialogue consisting of the last line of dialogue spoken, "{fast}", and the dialogue given to extend. This can be used to have the screen change over the course of dialogue.

Extend is aware of NVL-mode and treats it correctly. Extend does not work properly if the language preference changes between the initial say and the extend.

For example:

\# Show the first line of dialogue, wait for a click, change expression, and show
\# the rest.

show eileen concerned
e "Sometimes, I feel sad."
show eileen happy
extend " But I usually quickly get over it!"

\# Similar, but automatically changes the expression when the first line is finished
\# showing. This only makes sense when the user doesn't have text speed set all the
\# way up.

show eileen concerned
e "Sometimes, I feel sad.{nw}"
show eileen happy
extend " But I usually quickly get over it!"

## Dialogue Window Management

Ren'Py includes several statements that allow for management of the dialogue window. As dialogue window is always shown during dialogue, these statements control the presence or absence of the window during non-dialogue interactions.

`window show`

The window show statement causes the window to be shown. It takes as an argument an optional transition, which is used to show the window. If the transition is omitted,  is used.

`window hide`

The window hide statement causes the window to be hidden. It takes as an argument an optional transition, which is used to hide the window. If the transition is omitted,  is used.

`window auto True`

This enables automatic management of the window. The window is shown before statements listed in  – by default, say statements. The window is hidden before statements listed in  – by default, `scene` and `call screen` statements, and `menu` statements without a caption.

Only statements are considered, not statement equivalent functions.

`window auto False`

This disables automatic management of the window. The window is not shown or hidden automatically.

The `window auto` statement uses  and  to show and hide the window, respectively. `window auto` is cancelled by `window show` and `window hide`.

For example:

window show \# shows the window with the default transition, if any.
pause       \# the window is shown during this pause.
window hide \# hides the window.
pause       \# the window is hidden during this pause.

window show dissolve \# shows the window with dissolve.
pause                \# the window is shown during this pause.
window hide dissolve \# hides the window with dissolve.
pause                \# the window is hidden during this pause.

window auto True

"The window is automatically shown before this line of dialogue."
pause                \# the window is shown during this pause.

scene bg washington  \# the window is hidden before the scene change.
with dissolve

window show     \# Shows the window before it normally would be shown.

show eileen
with dissolve

"Without window show, the window would have been shown here."

Dialogue window management is subject to the "show empty window" . If the preference is disabled, the statements above have no effect.

## Say with Arguments

Additional arguments can be passed to the say statement by including them in parenthesis after the say statement. For example, one can write:

e "Hello, world." (what\_color\="#8c8")

Arguments to the say statement are first processed by , if it is not None. If any remain, they are then passed to the character, which treats them as if they were present when the character was defined. So, the example above displays the dialogue in green. The keyword \_with\_none will override the with\_none attribute of the character.

The interact parameter is a special case : when it was passed as False when defining the Character, passing `interact=True` will not override that, meaning no interaction will happen in that case.

Note that  will be called every time a say statement executes, and not only when arguments are passed. It can be useful to implement conditional overrides over characters' customizations. For example:

init python:
    def say\_arguments\_callback(char, \*args, \*\*kwargs):
        if colorblind\_mode:
            kwargs\["what\_color"\] \= "#000"
        return args, kwargs

define config.say\_arguments\_callback \= say\_arguments\_callback

## Monologue Mode

Some visual novels have extended narration, or multiple blocks of dialogue from the same character. In these cases, typing the name of the character and the quotes multiple times is somewhat redundant.

To cover these cases, Ren'Py supports monologue mode. When dialogue is inside triple-quoted strings, Ren'Py will break the dialogue up into blocks at blank lines. Each block is then used to create its own say statement. Here's an example, with three blocks of narration followed by three lines of dialogue:

"""
This is the first line of narration. It's longer than the other two
lines, so it has to wrap.

This is the second line of narration.

This is the third line of narration.
"""

e """
This is the first line of dialogue. It's longer than the other two
lines, so it has to wrap.

This is the second line of dialogue.

This is the third line of dialogue.
"""

While additional clauses like arguments or attributes are allowed, they are passed to each line in the monologue, which may be less useful.

If you'd like to omit the spaces between the blocks, write `rpy monologue single` at the top level of the file, before the first monologue line.

If you'd like to disable this instead, and have all the lines you write between triple quotes be displayed as a single message, conserving line breaks, you can do it with `rpy monologue none`.

## The `character` Store

_Main article:_ 

The say statement will search the `character` named store before the default store. If you want to have a character with the same name as a variable in the default store, it can be defined using:

define character.e \= Character("Eileen")

This character can then be used alongside a variable in the default store:

default e \= 0

label start:

    \# This is still a terrible variable name.
    $ e \= 100

    e "Our current energy is \[e\] units."

This is especially useful in order to manage variable information about a character in a namespace without conflicting with the say statement:

define character.naomi \= Character("Naomi Nagata", who\_color\="#8c8")
default naomi \= PersonClass(engineering\=5, max\_g\_force\=.7) \# can be an object...
define character.fred \= Character("Fred Johnson", who\_color\="#72f")
default fred.money \= 1000 \# ...or a dedicated named store
default fred.rank \= "Colonel"

label traded:
    fred "Here you go."
    $ fred.money \-= 50
    $ naomi.money += 50
    naomi "Thanks ! I knew you would value my class-\[naomi.engineering\] engineering skills."

## Alternative Presentations

 : a mode that displays dialogue over the entire screen.

 : a mode that displays dialogue in speech bubbles that can be positioned interactively.

## See Also

 : how to use most of the features described here in a python context, although with some drawbacks and limitations.

 : provides information about the last say statement.
