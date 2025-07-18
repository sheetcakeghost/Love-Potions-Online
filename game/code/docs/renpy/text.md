# Text

Ren'Py contains several ways of displaying text. The  and  statements are primarily concerned with the display of text to the user. The user interface often contains text, displayed using the , , and  screen language statements. These functions, along with others, create  displayables, and show them on the screen.

The Text displayable is responsible for managing the process of showing the text to the user. The text displayable performs actions in the following order:

1.  Translating text.
    
2.  Interpolating data into the text.
    
3.  Styling the text using styles and text tags.
    
4.  Laying out the styled text.
    
5.  Drawing the text to the screen.
    

This chapter discusses the process of text display in Ren'Py.

## Escape Characters

There are three special characters that can control the way Ren'Py displays text. A creator needs to be aware of these characters to ensure that their writing is not accidentally misinterpreted by the engine.

(backslash)

The backslash character is used to introduce when writing a Ren'Py or Python string. Some common escape codes are:

 (backslash-doublequote)

Includes a doublequote in a double-quoted string.

 (backslash-quote)

Includes a single quote in a single-quoted string.

(backslash-space)

Includes an additional space in a Ren'Py string. By default, Ren'Py script text collapses adjacent whitespace into a single space character.

 (backslash-n)

Includes a newline character in the text.

\ (backslash-backslash)

Includes a backslash character in the text.

 (backslash-percent)

Includes a protected percent character in the text. It's also possible to write it as %% : both protections will result in a single % character being written in the end.

\[ (left bracket)

The left bracket is used to introduce interpolation of a value into the text. To include a single left bracket in your text, double it – write `[[`.

{ (left brace)

The left brace is used to introduce a text tag. To include a left brace in your text, double it – write `{{`.

【 (left lenticular bracket)

The left lenticular bracket is used to to introduce ruby/furigana text. To include a left lenticular bracket in your text, double it – write `【【`.

## Interpolating Data

Ren'Py supports interpolating data into the text string before it is displayed. For example, if the player's name is stored in the `playername` variable, one could write a line of dialogue like:

g "Welcome to the Nekomimi Institute, \[playername\]!"

Ren'Py will search for variables in the following order:

*   When used in a screen, screen-local variables.
    
*   Variables found in the `interpolate` namespace.
    
*   Variables found in the global namespace.
    

Ren'Py isn't limited to interpolating simple variables. It can also interpolate any valid Python expression. So it's possible to have:

g "My first name is \[player.names\[0\]\]."

It's possible to apply formatting when displaying numbers. This will display a floating point number to two decimal places:

g "I like you \[100.0 \* points / max\_points:.2\] percent!"

Ren'Py's string formatting is taken from the  string formatting syntax. Ren'Py uses \[ to introduce string interpolation because { was taken by text tags.

Along with the `!s` and `!r` conversion flags supported by Python, Ren'Py supports several more flags. The `!q` conversion flag ensures that text tags are properly quoted, so that displaying a string will not introduce unwanted formatting constructs. For example:

g "Don't pull a fast one on me, \[playername!q\]."

The `!t` flag will translate the interpolated string:

if points \> 5:
    $ mood \= \_("happy")
else:
    $ mood \= \_("annoyed")

g "I'm \[mood!t\] to see you."

The `!i` flag will make additional interpolate for the interpolated string:

define earned\_points\_info \= \_("\[points\]{image=points.png} earned points")
g "I'm happy to see you you have \[earned\_points\_info!ti\]."

This should be used to substitute the text that has a substitution inside. It's often useful in screen language, see .

The `!u` flag forces the text to uppercase and the `!l` flag forces the text to lowercase. The `!c` flag acts only on the first character, capitalizing it. These flags may be combined, for example using `!cl` would capitalize the first character, and force the remaining text to lowercase.

It should be noted that:

*   the order in which the flags are given does not change the result : `!cl` will do just the same as `!lc`.
    
*   Supplementary exclamation marks will be ignored, and will not circumvent the previous rule : `!l!c` will do the same as `!c!l` or `!cl`.
    

The transformations are done in the following order:

1.  `r`/`s` (repr or str)
    
2.  `t` (translate)
    
3.  `i` (recursive interpolation)
    
4.  `q` (quoting)
    
5.  `u` (uppercase)
    
6.  `l` (lowercase)
    
7.  `c` (capitalize)
    

## Styling and Text Tags

In Ren'Py, text gains style information in two ways. The first is from the style that is applied to the entire block of text. Please see the section about the  for more details, especially the section on .

The second way is through text tags. Text tags are suitable for styling a portion of text block, or a small fraction of the text blocks in the program. If you find yourself applying the same text tags to every line of text, consider using a style instead.

There are two types of text tags. Some text tags are self-closing, while others allow a closing tag. The close tag starts with a slash (/), and tags are closed in last-in, first-out order. Each closing tag should match the corresponding opening tag. If not, Ren'Py will produce a lint warning.

For example:

\# This line is correct.
"Plain {b}Bold {i}Bold-Italic{/i} Bold{/b} Plain"

\# This line is incorrect, and will cause incorrect behavior.
"Plain {b}Bold {i}Bold-Italic{/b} Italic{/i} Plain"

It is not necessary to close all text tags. Ren'Py will close all tags that are open at the end of the text block. For example:

"{size=+20}This is big!"

Some text tags take an argument. In that case, the tag name is followed by an equals sign (=), and the argument. The argument may not contain the right-brace (}) character. The meaning of the argument varies based on the text tag.

### General Text Tags

Tags that apply to all text are:

a

The anchor tag creates a hyperlink between itself and its closing tag. While the behavior of the hyperlink is controlled by the  style property, the default handler has the following behavior.

*   When the argument begins with `jump:`, the rest of the argument is a label to jump to.
    
*   When the argument begins with `call:`, the rest of the argument is a label to call. As usual, a call ends the current Ren'Py statement.
    
*   When the argument begins with `call_in_new_context:`, the rest of the argument is a label to call in a new context (using ).
    
*   When the argument begins with `show:`, the rest of the argument is a screen to show.
    
*   When the argument begins with `showmenu:`, the rest of the argument is a game menu screen to show.
    
*   Otherwise, the argument is a URL that is opened by the system web browser.
    

If there is no protocol section in the argument,  is prepended to it. If config.hyperlink\_protocol has been set to "jump", {a=label} and {a=jump:label} become equivalent. Creators can define new protocols using .

label test:

    e "Why don't you visit {a=https://renpy.org}Ren'Py's home page{/a}?"

    e "Or {a=jump:more\_text}here for more info{/a}."

    return

label more\_text:

    e "In Hot Springs, Arkansas, there's a statue of Al Capone you can take a picture with."

    e "That's more info, but not the kind you wanted, is it?"

    return

alpha

The alpha text tag renders the text between itself and its closing tag in the specified opacity. The opacity should be a value between 0.0 and 1.0, corresponding to fully invisible and fully opaque, respectively. If the value is prefixed by + or -, the opacity will be changed by that amount instead of completely replaced. If the value is prefixed by \*, the opacity will be multiplied by that amount.

"{alpha=0.1}This text is barely readable!{/alpha}"
"{alpha=-0.1}This text is 10 percent more transparent than the default.{/alpha}"
"{alpha=\*0.5}This text is half as opaque as the default.{/alpha}"

alt

The alt tag prevents text from being rendered, while still making the text available for the text-to-speech system.

g "Good to see you! {image=heart.png}{alt}heart{/alt}"

See also the  character.

art

The alternate ruby top tag marks text between itself and its closing tag as alternate ruby top text. See the section on  for more information.

b

The bold tag renders the text between itself and its closing tag in a bold font.

"An example of {b}bold test{/b}."

color

The color text tag renders the text between itself and its closing tag in the specified color. The color should be in #rgb, #rgba, #rrggbb, or #rrggbbaa format.

"{color=#f00}Red{/color}, {color=#00ff00}Green{/color}, {color=#0000ffff}Blue{/color}"

cps

The characters per second tag sets the speed of text display, for text between the tag and its closing tag. If the argument begins with an asterisk, it's taken as a multiplier to the current text speed. Otherwise, the argument gives the speed to show the text at, in characters per second.

"{cps=20}Fixed Speed{/cps} {cps=\*2}Double Speed{/cps}

font

The font tag renders the text between itself and its closing tag in the specified font. The argument is the filename of the font to use.

"Try out the {font=mikachan.ttf}mikachan font{/font}."

i

The italics tag renders the text between itself and its closing tag in italics.

"Visit the {i}leaning tower of Pisa{/i}."

image

The image tag is a self-closing tag that inserts an image into the text. The image should be the height of a single line of text. The argument should be either the image filename, or the name of an image defined with the image statement.

g "Good to see you! {image=heart.png}{alt}heart{/alt}"

k

The kerning tag is a tag that adjust the kerning of characters between itself and its closing tag. It takes as an argument a floating point number giving the number of pixels of kerning to add to each kerning pair. (The number may be negative to decrease kerning.)

"{k=-.5}Negative{/k} Normal {k=.5}Positive{/k}"

noalt

The noalt tag prevents text from being spoken by the text-to-speech system. This is often used in conjunction with the alt tag, to provide accessible and visual options

g "Good to see you! {noalt}<3{/noalt}{alt}heart{/alt}"

outlinecolor

The outline text tag changes all the outlines (including drop shadows) to the given color. The color should be in #rgb, #rgba, #rrggbb, or #rrggbbaa format.

"Let's have a {outlinecolor=#00ff00}Green{/outlinecolor} outline."

plain

The plain tag ensures the text does not have bold, italics, underline, or strikethrough applied.

"{b}This is bold. {plain}This is not.{/plain} This is bold.{/b}"

rb

The ruby bottom tag marks text between itself and its closing tag as ruby bottom text. See the section on  for more information.

rt

The ruby top tag marks text between itself and its closing tag as ruby top text. See the section on  for more information.

s

The strikethrough tag draws a line through text between itself and its closing tag.

g "It's good {s}to see you{/s}."

shader

The shader tag applies a text shader to a section of text. The argument is the name of the shader to apply.

"This text is {shader=jitter:u\_\_jitter=1.0, 3.0}jittery{/shader}."

See  for more information.

size

The size tag changes the size of text between itself and its closing tag. The argument should be an integer, optionally preceded by + or -. If the argument is just an integer, the size is set to that many pixels high. Otherwise, the size is increased or decreased by that amount.

"{size=+10}Bigger{/size} {size=-10}Smaller{/size} {size=24}24 px{/size}."

You can also provide a floating point number preceded by a \*, in which case the size will be multiplied by that number and then rounded down.

"{size=\*2}Twice as big{/size} {size=\*0.5}half as big.{/size}"

space

The space tag is a self-closing tag that inserts horizontal space into a line of text. As an argument, it takes an integer giving the number of pixels of space to add.

"Before the space.{space=30}After the space."

u

The underline tag underlines the text between itself and its closing tag.

g "It's good to {u}see{/u} you."

vspace

The vspace tag is a self-closing tag that inserts vertical space between lines of text. As an argument, it takes an integer giving the number of pixels of space to add.

"Line 1{vspace=30}Line 2"

#

Text tags beginning with # are ignored, but can be included to distinguish strings for the purpose of translation.

"New{#playlist}"

### Dialogue Text Tags

Text tags that only apply to dialogue are:

w

The wait tag is a self-closing tag that waits for the user to click to continue. If it is given an argument, the argument is interpreted as a number, and the wait automatically ends after that many seconds have passed.

"Line 1{w} Line 1{w=1.0} Line 1"

p

The paragraph pause tag is a self-closing tag that terminates the current paragraph, and waits for the user to click to continue. If it is given an argument, the argument is interpreted as a number, and the wait automatically ends after that many seconds have passed.

"Line 1{p}Line 2{p=1.0}Line 3"

nw

The no-wait tag is a self-closing tag that causes the current line of dialogue to automatically dismiss itself once the end of line has been displayed.

g "Looks like they're{nw}"
show trebuchet
g "Looks like they're{fast} playing with their trebuchet again."

If it is given an argument, the argument is interpreted as a number, and the wait automatically ends after that many seconds have passed.

g "I'm gonna fall in a few seconds!{nw=2}"
show g\_gone

The no-wait tag will wait for self-voicing to complete before advancing.

fast

If the fast tag is displayed in a line of text, then all text before it is displayed instantly, even in slow text mode. The fast tag is a self-closing tag.

g "Looks like they're{nw}"
show trebuchet
g "Looks like they're{fast} playing with their trebuchet again."

If present, the {fast} tag will cause voice to be sustained from the previous line.

done

Text after the done tag is not displayed. Why would you want this? It's to allow text to avoid jumping around when  is True.

When the done tag is present, the line of dialogue is not added to the history buffer. If the nw tag is present, it should be before the done tag.:

g "Looks like they're{nw}{done} playing with their trebuchet again."
show trebuchet
g "Looks like they're{fast} playing with their trebuchet again."

clear

The clear text tag only makes sense on a line by itself in the . It does the same thing at the `nvl clear` statement without ending the block of text.

"""
Block 1 on page 1.

Block 2 on page 1.

{clear}

Block 1 on page 2.

etc.
"""

It's also possible to define  using Python.

### Style Text Tags

Ren'Py supports text tags that access styles. These are text tags where the tag name is empty. In this case, the argument is taken to be the name of a style. For example, the {=mystyle} tag will access the `mystyle` style.

The text between the tag and the corresponding closing tag has the following properties set to those defined in the style:

*   antialias
    
*   font
    
*   size
    
*   bold
    
*   italic
    
*   underline
    
*   strikethrough
    
*   color
    
*   black\_color
    
*   kerning
    

## Non-English Languages

The default font for Ren'Py contains characters for English and many other languages. For size reasons, it doesn't contain the characters required to render other languages, including Chinese, Japanese, and Korean. In order to support these languages, a project must first change the fonts it uses.

Ren'Py should then support most world languages without further configuration. However, Korean can be written with or without spacing between words. Ren'Py has a special mode to support Korean with spaces, which can be enabled by setting:

define gui.language \= "korean-with-spaces"

This can be changed from the default of "unicode" in gui.rpy.

Japanese has multiple rules for line breaking. We recommend starting with "japanese-normal", and moving to "japanese-loose" or "japanese-strict" for more or less break opportunities, respectively.

define gui.language \= "japanese-loose"

Ideographic languages provide a large number of opportunities for line breaking. To enable a faster but less-accurate line-breaking algorithm, use:

define gui.language \= "greedy"

The faster line-breaking algorithm is not be necessary unless the game is displaying huge amounts of text, such as in NVL-mode.

The line breaking algorithms can be further configured using the  function.

### Vertical Text

When the  style property is set, Ren'Py will produce vertically oriented text. The text is written top-to-bottom, right-to-left.

There are two text tags that interact with vertical text.

horiz

Includes horizontally-oriented text inside vertical text.

vert

Includes vertically-oriented text inside horizontal text. (This will not rotate the text to the vertical orientation.)

Note

If the font does not contain vertical text spacing information, Ren'Py will attempt to synthesize this information from horizontal text information. The spacing may not remain constant between Ren'Py releases.

## Ruby Text

Ruby text (also known as furigana or interlinear annotations) is a way of placing small text above a character or word. There are several steps required for your game to support ruby text.

First, you must set up styles for the ruby text. The following style changes are required:

1.  One of the  or  properties must be used to leave enough vertical space for the ruby text.
    
2.  A new named style must be created. The properties of this style, such as  should be set in a fashion appropriate for ruby text.
    
3.  The  of the new style should be set, in order to move the ruby text above the baseline.
    
4.  The  field of the text's style should be set to the newly-created style, for both dialogue and history window text.
    

For example:

style ruby\_style is default:
    size 12
    yoffset \-20
    color None \# Use the same color as the parent text.

style say\_dialogue:
    ruby\_line\_leading 12
    ruby\_style style.ruby\_style

style history\_text:
    ruby\_line\_leading 12
    ruby\_style style.ruby\_style

(Use `style.style_name` to refer to a style for this purpose.)

Once Ren'Py has been configured, ruby text can be included in two way.

**Lenticular brackets.** Ruby text can be written by enclosing it full-width lenticular brackets (【】), with the full-width or half-width vertical line character (｜ or |) separating the bottom text from the top text. For example:

e "Ruby can be used for furigana (【東｜とう】 【京｜きょう】)."

e "It's also used for translations (【東京｜Tokyo】)."

Ruby text will only trigger if a vertical line is present. The left lenticular bracket can be quoted by doubling it. Lenticular ruby text may not contain other text tags.

**The {rt} and {rb} text tags.** The {rt} tag is used to mark one or more characters to be displayed as ruby text. If the ruby text is preceded by text enclosed in the {rb} tag, the ruby text is centered over that text. Otherwise, it is centered over the preceding character.

For example:

e "Ruby can be used for furigana (東{rt}とう{/rt} 京{rt}きょう{/rt})."

e "It's also used for translations ({rb}東京{/rb}{rt}Tokyo{/rt})."

It's the creator's responsibility to ensure that ruby text does not leave the boundaries of the text. It may be necessary to add leading or spaces to the left and right of the text to prevent these errors from occurring.

Ren'Py also supports alternate ruby text, which is a second kind of ruby top text. This is introduced with the {art} text tag (instead of {rt}), and the  property (instead of ).

## Fonts

Ren'Py supports TrueType/OpenType fonts and collections, and Image-Based fonts.

A TrueType or OpenType font is specified by giving the name of the font file. The file must be present in the game directory or one of the archive files.

Ren'Py also supports TrueType/OpenType collections that define more than one font. When accessing a collection, use the 0-based font index, followed by an at-sign and the file name. For example, "0@font.ttc" is the first font in a collection, "1@font.ttc" the second, and so on.

When looking for a font files, if the file is not found, Ren'Py will search in the `game/fonts` directory. For example, when looking for "test.ttf", Ren'Py will first search for `game/test.ttf`, and then for `game/fonts/test.ttf`.

### Font Replacement

The  variable is used to map fonts. The combination of font filename, boldness, and italics is mapped to a similar combination. This allows a font with proper italics to be used instead of the automatically-generated italics.

Once such mapping would be to replace the italic version of the Deja Vu Sans font with the official oblique version (You'll need to download the oblique font from the web):

init python:
    config.font\_replacement\_map\["DejaVuSans.ttf", False, True\] \= ("DejaVuSans-Oblique.ttf", False, False)

This mapping can improve the look of italic text.

### Font names and aliases

The  variable is used to give names or aliases to fonts. This allows two things : first, to make dialogues using the `{font}` tag shorter and easier to use, and second, to enable  to be used by these tags.

define config.font\_name\_map\["jap"\] \= "electroharmonix.ttf"
define config.font\_name\_map\["tjap"\] \= FontGroup().add("OrthodoxHerbertarian.ttf", "A", "Z").add("electroharmonix.ttf", None, None)

label yamato:
    e "Sorry, what does {font=jap}Black holes and revelations{/font} mean ?"
    y "You pronounce it {font=tjap}Black Holes And Revelations{/font}." \# the capital letters appear in OrthodoxHerbertarian

### Image-Based Fonts

Image based fonts can be registered by calling one of the following registration functions. Registering an image-based font requires the specification of a name, size, boldness, italicness, and underline. When all of these properties match the registered font, the registered font is used.

renpy.register\_bmfont(_name\=None_, _size\=None_, _bold\=False_, _italics\=False_, _underline\=False_, _filename\=None_)

This registers a BMFont with the given details. Please note that size, bold, italic, and underline are all advisory (used for matching), and do not change the appearance of the font.

Please see the  for the tool that creates BMFonts. Ren'Py expects that the filename parameter will be to a file in the BMFont text format, that describes a 32-bit font. The Alpha channel should contain the font information, while the Red, Green, and Blue channels should be set to one. The image files, kerning, and other control information is read out of the BMFont file.

We recommend including Latin and General Punctuation as part of your BMFont, to ensure all of the Ren'Py interface can render.

name

The name of the font being registered, a string.

size

The size of the font being registered, an integer.

bold

The boldness of the font being registered, a boolean.

italics

The italicness of the font being registered, a boolean.

underline

An ignored parameter.

filename

The file containing BMFont control information.

renpy.register\_mudgefont(_name\=None_, _size\=None_, _bold\=False_, _italics\=False_, _underline\=False_, _filename\=None_, _xml\=None_, _spacewidth\=10_, _default\_kern\=0_, _kerns\={}_)

This registers a MudgeFont with the given details. Please note that size, bold, italic, and underline are all advisory (used for matching), and do not change the appearance of the font.

Please see the  for the tool that creates MudgeFonts. Ren'Py assumes that character codes found in the MudgeFont xml file are unicode character numbers, and ignores negative character codes.

name

The name of the font being registered, a string.

size

The size of the font being registered, an integer.

bold

The boldness of the font being registered, a boolean.

italics

The italicness of the font being registered, a boolean.

underline

An ignored parameter.

filename

The file containing the MudgeFont image, a string. The image is usually a TGA file, but could be a PNG or other format that Ren'Py supports.

xml

The xml file containing information generated by the MudgeFont tool.

spacewidth

The width of a space character, an integer in pixels.

default\_kern

The default kern spacing between characters, in pixels.

kerns

A map from two-character strings to the kern that should be used between those characters.

renpy.register\_sfont(_name\=None_, _size\=None_, _bold\=False_, _italics\=False_, _underline\=False_, _filename\=None_, _spacewidth\=10_, _baseline\=None_, _default\_kern\=0_, _kerns\={}_, _charset\='!"#$%&()\*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\

This registers an SFont with the given details. Please note that size, bold, italic, and underline are all advisory (used for matching), and do not change the appearance of the font.

name

The name of the font being registered, a string.

size

The size of the font being registered, an integer.

bold

The boldness of the font being registered, a boolean.

italics

The italicness of the font being registered, a boolean.

underline

An ignored parameter.

filename

The file containing the sfont image, a string.

spacewidth

The width of a space character, an integer in pixels.

baseline

The distance from the top of the font to the baseline (the invisible line letters sit on), an integer in pixels. If this font is mixed with other fonts, their baselines will be aligned. Negative values indicate distance from the bottom of the font instead, and `None` means the baseline equals the height (i.e., is at the very bottom of the font).

default\_kern

The default kern spacing between characters, in pixels.

kerns

A map from two-character strings to the kern that should be used between those characters.

charset

The character set of the font. A string containing characters in the order in which they are found in the image. The default character set for a SFont is

! " # $ % & ' ( ) \* + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ?
@ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z \[ \] ^ \_
\` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~

As BMFont is the most complete of the three image font formats Ren'Py supports, it's the one recommended for new projects. An example of BMFont use is:

init python:
    renpy.register\_bmfont("bmfont", 22, filename\="bmfont.fnt")

define ebf \= Character('Eileen', what\_font\="bmfont", what\_size\=22)

label demo\_bmfont:

    ebf "Finally, Ren'Py supports BMFonts."

### Font Groups

When creating a multilingual game, it may not be possible to find a single font that covers every writing system the game use while projecting the the mood the creator intends. To support this, Ren'Py supports font groups that can take characters from two or more fonts and combine them into a single font.

To create a font group, create a  object and call the `.add` method on it once or more. A FontGroup can be used wherever a font name can be used. The add method takes the start and end of a range of Unicode character points, and the first range to cover a point is used.

For example:

style default:
    font FontGroup().add("english.ttf", 0x0020, 0x007f).add("japanese.ttf", 0x0000, 0xffff)

_class_ FontGroup

A group of fonts that can be used as a single font.

add(_font_, _start_, _end_, _target\=None_, _target\_increment\=False_)

Associates a range of characters with a font.

start

The start of the range. This may be a single-character string, or an integer giving a unicode code point. If start is None, then the font is used as the default.

end

The end of the range. This may be a single-character string, or an integer giving a unicode code point. This is ignored if start is None.

target

If given, associates the given range of characters with specific characters from the given font, depending on target\_increment. This may be a single-character string, or an integer giving a unicode code point. This is ignored if the character had already been added.

target\_increment

If True, the \[start, end\] range is mapped to the \[target, target+end-start\] range. If False, every character from the range is associated with the target character.

When multiple .add() calls include the same character, the first call takes precedence.

This returns the FontGroup, so that multiple calls to .add() can be chained together.

remap(_cha_, _target_)

Remaps one or a set of characters to a single target character.

cha

The character or characters to remap. This may be a single-character string, or an integer giving a unicode code point, or an iterable of either.

target

The character to remap to. This may be a single-character string, or an integer giving a unicode code point.

Any given character having already been remapped (either with add or with remap) will be ignored. However, if the FontGroup has no default font, any given character must have been previously added.

This method also returns the FontGroup, for the same reasons.

Note that while FontGroups can be given a name using , a FontGroup only takes filepaths as fonts, and does not recognize names or aliases defined using that variable.

## Text Displayables

Text can also be used as a , which allows you to apply transforms to text, displaying it as if it was an image and moving it around the screen.

_class_ ParameterizedText(_style\='default'_, _\*\*properties_)

This is a displayable that can be shown with an additional string parameter, which then shows that string as if it was an image. This is usually used as part of the pre-defined `text` image.

For example, one can do:

show text "Hello, World" at truecenter
with dissolve
pause 1
hide text
with dissolve

You can use ParameterizedText directly to define similar images with different style properties. For example, one can write:

image top\_text \= ParameterizedText(xalign\=0.5, yalign\=0.0)

label start:
    show top\_text "This text is shown at the center-top of the screen"

_class_ Text(_text_, _slow\=None_, _scope\=None_, _substitute\=None_, _slow\_done\=None_, _\*_, _tokenized\=False_, _\*\*properties_)

A displayable that displays text on the screen.

text

The text to display on the screen. This may be a string, or a list of strings and displayables.

slow

Determines if the text is displayed slowly, being typed out one character at the time. If None, slow text mode is determined by the  style property. Otherwise, the truth value of this parameter determines if slow text mode is used.

scope

If not None, this should be a dictionary that provides an additional scope for text interpolation to occur in.

substitute

If true, text interpolation occurs. If false, it will not occur. If None, they are controlled by .

slow\_done

If not None, and if slow text mode is enabled (see the slow parameter), this is a function or callable which is called with no arguments when the text finishes displaying.

tokenized

If true, text is expected to be a list of tokens, rather than a string. The tokens are introduced in the  page.

\*\*properties

Like other Displayables, Text takes style properties, including (among many others) the  property.

## Text Utility Functions

renpy.filter\_text\_tags(_s_, _allow\=None_, _deny\=None_)

Returns a copy of s with the text tags filtered. Exactly one of the allow and deny keyword arguments must be given.

allow

A set of tags that are allowed. If a tag is not in this list, it is removed.

deny

A set of tags that are denied. If a tag is not in this list, it is kept in the string.

renpy.substitute(_s_, _scope\=None_, _translate\=True_)

Applies translation and new-style formatting to the string s.

scope

If not None, a scope which is used in formatting, in addition to the default store.

translate

Determines if translation occurs.

Returns the translated and formatted string.

renpy.transform\_text(_s_, _function_)

Transforms s, while leaving text tags and interpolation the same.

function

A function that is called with strings corresponding to runs of text, and should return a second string that replaces that run of text.

init python:
    def upper(s):
        return s.upper()

$ upper\_string \= renpy.transform\_text("{b}Not Upper{/b}", upper)

## Slow Text Concerns

Ren'Py allows the creator or user to indicate that text should be displayed slowly. In this case, Ren'Py will render the text to a texture, and then draw rectangles from the texture to the screen.

Unfortunately, this means that it's possible to get rendering artifacts when characters overlap. To minimize these rendering artifacts, ensure that the  and  properties are large enough that lines do not overlap. If the bottoms of characters on the first line are clipped, especially if line\_spacing is negative, consider increasing .

Horizontal artifacts are also possible when characters are kerned together, but these artifacts are less severe, as they exist for only a single frame.

Artifacts aren't a problem for static text, like the text in menus and other parts of the user interface.

## Text Overflow Logging

Ren'Py can log cases where text expands outside of the area allocated for it. To enable text overflow logging, the following steps are necessary.

1.  Set the  variable to true.
    
2.  Set the  and  style properties on either the Text displayable, or a container enclosing it.
    
3.  Run the game.
    

Whenever text is displayed that overflows the available area, Ren'Py will log an error to the text\_overflow.txt file.

## Variable Fonts

Ren'Py has support for OpenType variable fonts. These fonts may support multiple axes, such as weight and width, and based on the value of these axes, the display of the font can change. Variable fonts may also have named instances, which provide different values for the axes. For example, the "bold" named instance will likely provide the bold version of a font, while "regular" will be a more normal version.

Variable fonts require the use of the harfbuzz text shaper, controlled by the  style property. Once this is set, the  property selects a named instance, while the  property sets the value of one or more axes.

These can also be set in the gui system. For example one can use:

define gui.text\_font \= "nunito.ttf"
define gui.text\_instance \= "light"
define gui.text\_axis \= {"width" : 125}

Will start with the light instance, and make it wide.

If no instance is given, Ren'Py will default to "regular" for non-bold text, and "bold" for bold text.

There are two text tags that support the use of variable fonts.

instance

The instance tag changes the instance that is being used. For example:

"This is {instance=heavy}heavy{/instance} text."

When the instance tag is used, the axis properties are overridden.

axis

The axis tag changes the value of one or more axes. For example:

"This is {axis:width=125}wide{/axis} text."

The axis tag can be used multiple times, and the values will be combined.

> "This is {axis:width=125}{axis:weight=200}wide and bold{/axis}{/axis} text."

The value of on the right side of the equals is expected to be a floating point number.

To get the available instances and axes of a font, use the  function. This function is intended to be called from the console. To access it, hit shift+O to open the console, and then type:

renpy.variable\_font\_info("nunito.ttf")

This will display information for the nunito.ttf font.

renpy.variable\_font\_info(_font_)

Returns information about a variable font, or None if the font is not variable.

font

The filename containing the font.

The return value is an object with the following fields:

instance

A dictionary where the keys are the names of the named instances of the font. (For example, 'light', 'regular', 'bold', and 'heavy'.) The values can be ignored.

axis

A dictionary that maps the names of the axes of the font to objects with the following fields:

minimum

The minimum value of the axis.

default

The default value of the axis.

maximum

The maximum value of the axis.

The object returned by this function and the data inside it should not be changed.

This function may only be called after the Ren'Py display has initialized, and is intended to be called from the console, where it will print in a human-readable form.
