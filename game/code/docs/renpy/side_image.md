# Side Images

Many visual novels include a picture of the character that is speaking as part of their interface. Ren'Py calls this image a side image, and has support for automatically selecting and displaying a side image as part of the dialogue.

The side image support assumes that a  is declared with a linked image tag:

define e \= Character("Eileen", image\="eileen")

When a character with a linked image tag speaks, Ren'Py creates a pool of image attributes. The linked image tag is added to this pool, as are the current image attributes that are associated with that tag.

In addition to the tag, there must be at least one attribute in the pool. If not, no side image is shown.

To determine the side image associated with a tag, Ren'Py tries to find an image with the tag "side", and the largest number of attributes from the pool. If no image can be found, or more than one image has the same number of attributes, a  is shown instead.

For example, say we have the following script:

define e \= Character("Eileen", image\="eileen")

image eileen happy \= "eileen\_happy.png"
image eileen concerned \= "eileen\_concerned.png"

image side eileen happy \= "side\_eileen\_happy.png"
image side eileen \= "side\_eileen.png"

label start:

    show eileen happy

    e "Let's call this line Point A."

    e concerned "And this one is point B."

At point A, the character `e` is speaking, which is linked to the image tag "eileen". The "eileen happy" image is showing, so the pool of attributes is "eileen" and "happy". We look for an image with the "side" tag, and as many of those attributes as possible – and we match "side eileen happy", which is the side image Ren'Py will display.

At point B, the "eileen concerned" image is showing. The pool of attributes is now "eileen" and "concerned". The only matching image is "side eileen", so that's what Ren'Py selects. If there was a "side concerned" image, there would be ambiguity, and Ren'Py wouldn't display an image.

## Invisible Characters

Another use of the side image is to show an image of the player character, when that character has dialogue. The way to do this is to link an image to the character, and then use the say with attributes construct to select the side image to show.

For example:

define p \= Character("Player", image\="player")

image side player happy \= "side\_player\_happy.png"
image side player concerned \= "side\_player\_concerned.png"

label start:

    p happy "This is shown with the 'side player happy' image."

    p "This is also shown with 'side player happy'."

    p concerned "This is shown with 'side player concerned'."

## Config and Store Variables

There are a number of attributes of side images that can be controlled using config variables.

\_side\_image\_tag \= None

define config.side\_image\_tag \= None

If \_side\_image\_tag is not None, it takes precedence over config.side\_image\_tag.

If this is given, then the side image will track the given image tag, rather than the image associated with the currently speaking character. For example,

define e \= Character("Eileen", image\="eileen")
define config.side\_image\_tag \= "eileen"

Will make the side image track the "eileen" image tag, which is associated with the `e` character.

define config.side\_image\_only\_not\_showing \= False

When set to true, the side image will only show if an image with that tag is not already being shown on the screen.

\_side\_image\_prefix\_tag \= None

define config.side\_image\_prefix\_tag \= 'side'

If \_side\_image\_prefix\_tag is not None, it takes preference over config.side\_image\_prefix\_tag.

The prefix that is used when searching for a side image.

define config.side\_image\_null \= Null()

The Null displayable to use when not displaying a side image. This can be changed, but only to other Null objects. One reason for doing so would be to set the side of the Null (eg. `Null(width=200, height=150)`) to prevent dissolves from being cut off.

define config.side\_image\_same\_transform \= None

If not None, a transform that is used when the new side image shares the same image tag as the previous side image.

define config.side\_image\_change\_transform \= None

If not None, a transform that is used when the new side image does not share the name image tag (or one of the new or old side images does not exist).

## Transforms and Transitions

The  and  transforms are called with two arguments – old and new side image displayables – each time the side image is displayed. These can be used to move around side images, or use a transition to go between side images.

This causes the side image to slide in and out when the character associated with that image changes:

transform change\_transform(old, new):
    contains:
        old
        yalign 1.0
        xpos 0.0 xanchor 0.0
        linear 0.2 xanchor 1.0
    contains:
        new
        yalign 1.0
        xpos 0.0 xanchor 1.0
        linear 0.2 xanchor 0.0

define config.side\_image\_change\_transform \= change\_transform

This is used to dissolve between old and new side images when the character remains the same. (For example, when the character changes emotion.) For the  to work correctly, both side images must be the same size.

transform same\_transform(old, new):
    old
    new with Dissolve(0.2, alpha\=True)

define config.side\_image\_same\_transform \= same\_transform

When the  is scaled down, it might make sense to enable mipmapping in the :

transform same\_transform(old, new):
    old
    new with Dissolve(0.2, alpha\=True, mipmap\=True)

define config.side\_image\_same\_transform \= same\_transform

## Functions

renpy.get\_side\_image(_prefix\_tag_, _image\_tag\=None_, _not\_showing\=None_, _layer\=None_)

This attempts to find an image to show as the side image.

It begins by determining a set of image attributes. If image\_tag is given, it gets the image attributes from the tag. Otherwise, it gets them from the image property suplied to the currently showing character. If no attributes are available, this returns None.

It then looks up an image with the tag prefix\_tag, and attributes consisting of:

*   An image tag (either from image\_tag or the image property supplied to the currently showing character).
    
*   The attributes.
    

If such an image exists, it's returned.

not\_showing

If not showing is True, this only returns a side image if an image with the tag that the attributes are taken from is not currently being shown. If False, it will always return an image, if possible. If None, takes the value from .

layer

If given, the layer to look for the image tag and attributes on. If None, uses the default layer for the tag.

renpy.set\_tag\_attributes(_name_, _layer\=None_)

This sets the attributes associated with an image tag when that image tag is not showing. The main use of this would be to directly set the attributes used by a side image.

For example:

$ renpy.set\_tag\_attributes("lucy mad")
$ renpy.say(l, "I'm rather cross.")

and:

l mad "I'm rather cross."

are equivalent.
