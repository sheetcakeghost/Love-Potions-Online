# Custom Text Tags

Ren'Py has support for defining your own text tags. These text tags can manipulate the text and text tags defined within, including adding and removing text and other text tags.

Custom text tags are created by assigning a text tag function to an entry in one of the following dictionaries.

define config.custom\_text\_tags \= { }

Maps text tag names to text tag functions, when the text tag can wrap other text.

define config.self\_closing\_custom\_text\_tags \= { }

Maps text tag names to a self-closing text tag functions, when the text tag does not wrap other text.

Warning

The functions may be called at any moment as part of the prediction process. For that reason, their behavior should not depend on the state of the game (global variables, typically) and they should not induce side-effects (calling  for example, or changing global variables).

A text tag function takes three arguments: The tag itself, the argument for the tag, and a list of content tuples. For example, for the text:

"{big=2}Hello, {b}World{/b}{/big}"

The tag will be "big", the argument will be the string "2", and the list of content tuples will be:

\[
    (renpy.TEXT\_TEXT, "Hello, "),
    (renpy.TEXT\_TAG, "b"),
    (renpy.TEXT\_TEXT, "World"),
    (renpy.TEXT\_TAG, "/b"),
\]

The text tag function should return a new list of content tuples, which is used to replace the text tag and its contents.

Content tuples consist of two components. The first component is one of the the constants in the following list. The second component varies based on the first component, as described below.

renpy.TEXT\_TEXT

The second component is text that is intended for display to the user.

renpy.TEXT\_TAG

The second component is the contents of a text tag, without the enclosing braces.

renpy.TEXT\_DISPLAYABLE

The second component is a displayable to be embedded into the text.

renpy.TEXT\_PARAGRAPH

This represents a break between paragraphs, and the second component is undefined (but must be present).

A self-closing text tag function is similar, except that it does not take the third argument.

Lists of tokens can be passed to  when its tokenized argument is True.

Warning

The dialogue text tags {p}, {w}, {nw}, and {fast} are processed before custom text tags, and should either be not included inside a custom text tag, or passed through unchanged.

## Examples

The example `big` text tag works like the {size} text tag, but applies a multiplier to its argument.

init python:

    def big\_tag(tag, argument, contents):

        size \= int(argument) \* 20

        return \[
                (renpy.TEXT\_TAG, u"size={}".format(size)),
            \] + contents + \[
                (renpy.TEXT\_TAG, u"/size"),
            \]

    config.custom\_text\_tags\["big"\] \= big\_tag

"This is {big=3}BIG!{/big}"

The example `rot13` text tag applies the ROT13 transform to text. Note that ROT26 – ROT13 applied twice – is just normal text.

init python:

    def rot13\_transform(s):

        ROT13 \= { }

        for i, j in zip("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"):
             ROT13\[i\] \= j
             ROT13\[j\] \= i

             i \= i.lower()
             j \= j.lower()

             ROT13\[i\] \= j
             ROT13\[j\] \= i

        return "".join(ROT13.get(i, i) for i in s)

    def rot13\_tag(tag, argument, contents):
        rv \= \[ \]

        for kind, text in contents:

            if kind \== renpy.TEXT\_TEXT:
                text \= rot13\_transform(text)

            rv.append((kind, text))

        return rv

    config.custom\_text\_tags\["rot13"\] \= rot13\_tag

"Rot0. {rot13}Rot13. {rot13}Rot26. {/rot13}Rot13. {/rot13}Rot0."

The `bang` text tag inserts a specific image into the text, and doesn't require a closing tag.

init python:
    def bang\_tag(tag, argument):
        return \[ ( renpy.TEXT\_TAG, "size=40"), (renpy.TEXT\_TEXT, "!"), (renpy.TEXT\_TAG, "/size") \]

    config.self\_closing\_custom\_text\_tags\["bang"\] \= bang\_tag

"This is awesome{bang}"
