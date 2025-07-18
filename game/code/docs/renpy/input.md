# Text Input

With some limitations, Ren'Py can prompt the user to input a small amount of text. This prompting is done by the  function, which returns the entered text, allowing it to be saved in a variable or otherwise processed.

On Linux, text input is limited to languages that do not require input method (IME) support. Most Western languages should work, but Chinese, Japanese, and Korean probably won't.

The renpy.input function is defined as:

renpy.input(_default\=''_, _allow\=None_, _exclude\='{}'_, _length\=None_, _pixel\_width\=None_, _screen\='input'_, _mask\=None_, _copypaste\=True_, _multiline\=False_, _\*\*kwargs_)

Calling this function pops up a window asking the player to enter some text. It returns the entered text.

prompt

A string giving a prompt to display to the player.

default

A string giving the initial text that will be edited by the player.

allow

If not None, a string giving a list of characters that will be allowed in the text.

exclude

If not None, if a character is present in this string, it is not allowed in the text.

length

If not None, this must be an integer giving the maximum length of the input string.

pixel\_width

If not None, the input is limited to being this many pixels wide, in the font used by the input to display text.

screen

The name of the screen that takes input. If not given, the `input` screen is used.

mask

If not None, a single-character string that replaces the input text that is shown to the player, such as to conceal a password.

copypaste

When true, copying from and pasting to this input is allowed.

multiline

When true, move caret to next line is allowed.

If  is True, this function only returns default.

Keywords prefixed with `show_` have the prefix stripped and are passed to the screen.

Due to limitations in supporting libraries, on Android and the web platform this function is limited to alphabetic characters.

Games that use renpy.input will often want to process the result further, using standard Python string manipulation functions. For example, the following will ask the player for his or her name and remove leading or trailing whitespace. If the name is empty, it will be replaced by a default name. Finally, it is displayed to the user.

define pov \= Character("\[povname\]")

python:
    povname \= renpy.input("What is your name?", length\=32)
    povname \= povname.strip()

    if not povname:
         povname \= "Pat Smith"

pov "My name is \[povname\]!"

In this, the length of the input is limited to 32 characters. It's important to test your game with long names, to makes sure that those names do not break text layout. At the same time, too short fields may prevent people from entering their preferred name.
