# Transitions

Transitions can be used as part of the , as well as in other parts of Ren'Py, to apply effects to changes in the scene (or sometimes to turn a displayable into another). Ren'Py comes with a small number of pre-defined transitions, which can be given directly to the with statement. For example:

show bg washington
with dissolve

## Pre-Defined Transitions

dissolve

Takes 0.5 seconds to dissolve from the old to the new screen. An instance of the  transition class.

fade

Takes 0.5 seconds to fade to black, and then 0.5 seconds to fade to the new screen. An instance of the  transition class.

pixellate

Pixellates the old scene for .5 seconds, and the new scene for another .5 seconds. An instance of the  transition class.

move

Takes 0.5 seconds to the move images that have changed location to their new locations. An instance of the  transition class.

Move transitions, and similar transitions like ease, can only be applied to a single layer or all layers at once, using the . It will not work in other contexts such as , , or other ways of applying transitions.

moveinright

Also: **moveinleft, moveintop, moveinbottom**

These move entering images onto the screen from the appropriate side, taking 0.5 seconds to do so.

moveoutright

Also: **moveoutleft, moveouttop, moveoutbottom**

These move leaving images off the screen via the appropriate side, taking 0.5 seconds to do so.

ease

Also: **easeinright, easeinleft, easeintop, easeinbottom, easeoutright, easeoutleft, easeouttop, easeoutbottom**

These are similar to the move- family of transitions, except that they use a cosine-based curve to slow down the start and end of the transition.

zoomin

This zooms in entering images, taking 0.5 seconds to do so.

zoomout

This zooms out leaving images, taking 0.5 seconds to do so.

zoominout

This zooms in entering images and zooms out leaving images, taking 0.5 seconds to do so.

vpunch

When invoked, this transition shakes the screen vertically for a quarter second. Imitating and customizing this transition and  is best done using .

hpunch

When invoked, this transition shakes the screen horizontally for a quarter second.

blinds

Transitions the screen in a vertical blinds effect lasting 1 second. An instance of the  transition class.

squares

Transitions the screen in a squares effect lasting 1 second.

wipeleft

Also: **wiperight, wipeup, wipedown**

Wipes the scene in the given direction. Instances of the  transition class.

slideleft

Also: **slideright, slideup, slidedown**

Slides the new scene in the given direction. Instances of the  transition class.

slideawayleft

Also: **slideawayright, slideawayup, slideawaydown**

Slides the old scene in the given direction. Instances of the  transition class.

pushright

Also: **pushleft, pushup, pushdown**

These use the new scene to slide the old scene out the named side. Instances of the  transition class.

irisin

Also: **irisout**

Use a rectangular iris to display the new screen, or hide the old screen. Instances of the  transition class.

## Transition Classes

Transition classes are functions that can be called to create new transitions. These functions are parameterized, allowing entire families of transitions to be created. Unlike what the term may imply, they are usually not classes in the Python sense and should not be treated as such.

Calling transition classes can be done as part of the with statement. For example:

\# A very long dissolve.
with Dissolve(10.0)

If the same transition class is used repeatedly, the  can be used to assign the transition to a variable:

define dissolve1 \= Dissolve(1.0)

label start:
    show bg washington
    with dissolve1

The time\_warp argument taken by many transition classes can be given built-in warpers found in the `_warper` module, see .

AlphaDissolve(_control_, _delay\=0.0_, _\*_, _reverse\=False_, _mipmap\=None_)

Returns a transition that uses a control displayable (almost always some sort of animated transform) to transition from one screen to another. The transform is evaluated. The new screen is used where the transform is opaque, and the old image is used when it is transparent.

control

The control transform.

delay

The time the transition takes, before ending.

reverse

If true, the alpha channel is reversed. Opaque areas are taken from the old image, while transparent areas are taken from the new image.

mipmap

When the dissolve will be scaled to less than half its natural size, this can be set to True. This will cause mipmaps to be generated, which will make the dissolve consume more GPU resources, but will reduce artifacts. See  for more information.

ComposeTransition(_trans_, _before_, _after_)

Returns a transition that composes up to three transitions. If not None, the before and after transitions are applied to the old and new scenes, respectively. These updated old and new scenes are then supplied to the trans transition.

\# Move the images in and out while dissolving. (This is a fairly expensive transition.)
define moveinoutdissolve \= ComposeTransition(dissolve, before\=moveoutleft, after\=moveinright)

CropMove(_time_, _mode\='slideright'_, _startcrop\=(0.0, 0.0, 0.0, 1.0)_, _startpos\=(0.0, 0.0)_, _endcrop\=(0.0, 0.0, 1.0, 1.0)_, _endpos\=(0.0, 0.0)_, _topnew\=True_)

Returns a transition that works by cropping a scene and positioning it on the screen. This can be used to implement a variety of effects, all of which involve changing rectangular slices of scenes.

time

The time the transition takes.

mode

The name of the mode of the transition. There are three groups of modes: wipes, slides, and other. This can also be "custom", to allow a custom mode to be defined.

In a wipe, the image stays fixed, and more of it is revealed as the transition progresses. For example, in "wiperight", a wipe from left to right, first the left edge of the image is revealed at the left edge of the screen, then the center of the image, and finally the right side of the image at the right of the screen. Other supported wipes are "wipeleft", "wipedown", and "wipeup".

In a slide, the image moves. So in a "slideright", the right edge of the image starts at the left edge of the screen, and moves to the right as the transition progresses. Other slides are "slideleft", "slidedown", and "slideup".

There are also slideaways, in which the old image moves on top of the new image. Slideaways include "slideawayright", "slideawayleft", "slideawayup", and "slideawaydown".

We also support a rectangular iris in with "irisin" and a rectangular iris out with "irisout".

The following parameters are only respected if the mode is "custom". Positions are relative to the size of the screen, while the crops are relative to the size of the image. So a crop of (0.25, 0.0, 0.5, 1.0) takes the middle half of an image.

startcrop

The starting rectangle that is cropped out of the top image. A 4-element tuple containing x, y, width, and height.

startpos

The starting place that the top image is drawn to the screen at, a 2-element tuple containing x and y.

endcrop

The ending rectangle that is cropped out of the top image. A 4-element tuple containing x, y, width, and height.

endpos

The ending place that the top image is drawn to the screen at, a 2-element tuple containing x and y.

topnew

If true, the scene that is cropped and moved (and is on top of the other scene) is the new scene. If false, it is the old scene.

define wiperight \= CropMove(1.0, "wiperight")
define wipeleft \= CropMove(1.0, "wipeleft")
define wipeup \= CropMove(1.0, "wipeup")
define wipedown \= CropMove(1.0, "wipedown")

define slideright \= CropMove(1.0, "slideright")
define slideleft \= CropMove(1.0, "slideleft")
define slideup \= CropMove(1.0, "slideup")
define slidedown \= CropMove(1.0, "slidedown")

define slideawayright \= CropMove(1.0, "slideawayright")
define slideawayleft \= CropMove(1.0, "slideawayleft")
define slideawayup \= CropMove(1.0, "slideawayup")
define slideawaydown \= CropMove(1.0, "slideawaydown")

define irisout \= CropMove(1.0, "irisout")
define irisin \= CropMove(1.0, "irisin")

Dissolve(_time_, _\*_, _time\_warp\=None_, _mipmap\=None_)

Returns a transition that dissolves from the old scene to the new scene.

time

The time the dissolve will take.

time\_warp

A . If not None, this should be a function that takes a fractional time between 0.0 and 1.0, and returns a number in the same range.

mipmap

When the dissolve will be scaled to less than half its natural size, this can be set to True. This will cause mipmaps to be generated, which will make the dissolve consume more GPU resources, but will reduce artifacts. See  for more information.

Fade(_out\_time_, _hold\_time_, _in\_time_, _\*_, _color\='#000'_)

Returns a transition that takes out\_time seconds to fade to a screen filled with color, holds at that screen for hold\_time seconds, and then takes in\_time to fade to then new screen.

\# Fade to black and back.
define fade \= Fade(0.5, 0.0, 0.5)

\# Hold at black for a bit.
define fadehold \= Fade(0.5, 1.0, 0.5)

\# Camera flash - quickly fades to white, then back to the scene.
define flash \= Fade(0.1, 0.0, 0.5, color\="#fff")

ImageDissolve(_image_, _time_, _ramplen\=8_, _\*_, _reverse\=False_, _time\_warp\=None_, _mipmap\=None_)

Returns a transition that dissolves the old scene into the new scene, using an image to control the dissolve process. This means that white pixels will dissolve in first, and black pixels will dissolve in last.

image

The control image. This can be any displayable. It should be the size of the scenes being dissolved, and if reverse=True, it should be fully opaque.

time

The time the dissolve will take.

ramplen

The length of the ramp to use. This must be an integer power of 2. When this is the default value of 8, when a white pixel is fully dissolved, a pixel 8 shades of gray darker will have completed one step of dissolving in.

reverse

If True, black pixels will dissolve in before white pixels.

time\_warp

A . If not None, this should be a function that takes a fractional time between 0.0 and 1.0, and returns a number in the same range.

mipmap

When the dissolve will be scaled to less than half its natural size, this can be set to True. This will cause mipmaps to be generated, which will make the dissolve consume more GPU resources, but will reduce artifacts. See  for more information.

define circirisout \= ImageDissolve("circiris.png", 1.0, time\_warp\=\_warper.easeout)
define circirisin \= ImageDissolve("circiris.png", 1.0, reverse\=True, time\_warp\=\_warper.easein)
define circiristbigramp \= ImageDissolve("circiris.png", 1.0, ramplen\=256)

MoveTransition(_delay_, _\*_, _enter\=None_, _leave\=None_, _old\=False_, _layers\=\

With these transitions, images changing position between the old and new scenes will be interpolated, which means their movement will be smooth instead of instantaneous.

As only layers have tags, MoveTransitions can only be applied to a single layer or all layers at once, using the . It will not work in other contexts such as , , or other ways of applying transitions.

delay

The time it takes for the interpolation to finish.

old

If true, when a tag gets its image changed during the transition, the old image will be used in preference to the new one. Otherwise, the new images will be used.

layers

A list of layers that moves are applied to.

The two following parameters take transforms, which should not be animated over time.

enter

If not None, images entering the scene will also be moved. The transform will be applied to the image to get it in its starting position.

leave

If not None, images leaving the scene will also be moved. The transform will be applied to the image to get it in its ending position.

The three following parameters take , which take a number between 0.0 and 1.0, and should return a number in the same range.

time\_warp

A time warp function that's applied to the images changing position between the old and new scenes.

enter\_time\_warp

A time warp function that's applied to images entering the scene.

leave\_time\_warp

A time warp function that's applied to images leaving the scene.

define longer\_easein \= MoveTransition(3.0, enter\=offscreenright, enter\_time\_warp\=\_warper.easein)

In the following code, "a" will be leaving the scene (using leave and leave\_time\_warp), "b" will be changing position (using time\_warp), and "c" will be entering (using enter and enter\_time\_warp). Because the same tag is applied before and after, "d" will not be counted as entering or leaving, but as changing position.

define some\_move\_trans \= MoveTransition(...)

label start:
    show a
    show b at left
    show ugly\_eileen as d at right
    e "This is a dialogue !"

    hide a
    show b at right
    show c
    show pretty\_eileen as d at left
    with some\_move\_trans

During the time when "d" is changing position, whether ugly or pretty eileen will be shown depends on the value of old : if old is False, the default, ugly\_eileen will instantly turn into pretty\_eileen and then move, and if old is True, ugly\_eileen will move and then instantly turn into pretty\_eileen.

MultipleTransition(_args_)

Returns a transition that allows multiple transitions to be displayed, one after the other.

args

A **list** containing an odd number of items. The first, third, and other odd-numbered items must be scenes, and the even items must be transitions. A scene can be one of:

*   A displayable.
    
*   False, to use the old scene.
    
*   True, to use the new scene.
    

Almost always, the first argument will be False and the last True.

Note that this is a single parameter taking a list, this is not `*args`.

The transitions in args are applied in order. For each transition, the old scene is the screen preceding it, and the new scene is the scene following it. For example:

define logodissolve \= MultipleTransition(\[
    False, Dissolve(0.5),
    "logo.jpg", Pause(1.0),
    "logo.jpg", dissolve,
    True\])

This example will dissolve to logo.jpg, wait 1 second, and then dissolve to the new scene.

Pause(_delay_)

Returns a transition that only displays the new screen for delay seconds. It can be useful as part of a MultipleTransition.

Pixellate(_time_, _steps_)

Returns a transition that pixellates out the old screen, and then pixellates in the new screen.

time

The total time the transition will take, in seconds.

steps

The number of steps that will occur, in each direction. Each step creates pixels about twice the size of those in the previous step, so a 5-step pixellation will create 32x32 pixels.

PushMove(_time_, _mode\='pushright'_)

Returns a transition that works by taking the new scene and using it to "push" the old scene off the screen.

time

The time the transition takes.

mode

There are four possible modes: "pushright", "pushleft", "pushup", and "pushdown", which push the old scene off the screen in the direction indicated.

define pushright \= PushMove(1.0, "pushright")
define pushleft \= PushMove(1.0, "pushleft")
define pushup \= PushMove(1.0, "pushup")
define pushdown \= PushMove(1.0, "pushdown")

Swing(_delay\=1.0_, _vertical\=False_, _reverse\=False_, _background\='#000'_, _flatten\=True_)

A transitions that rotates the old scene 90 degrees around an axis, so that it is edge on with the viewer, switches to the new scene, and then rotates that scene another 90 degrees to show the new scene to the viewer.

delay

How long the transition should take.

vertical

If true, the scene is rotate around the x-axis (pixels move vertically). If false, the scene is roated around the y axis, pixels moving horizontally.

reverse

When true, the rotation occurs in the reverse direction.

background

A displayable that is placed behind the scene as it rotates.

flatten

If true, the scenes are flattened into images the size of the screen before being rotated. Use this if images being not entirely on the screen causes undesired effects.

## Transition Families

Transition families are functions that define a large family of related transitions.

define.move\_transitions(_prefix_, _delay_, _time\_warp\=None_, _in\_time\_warp\=None_, _out\_time\_warp\=None_, _old\=False_, _layers\=\

This defines a family of , similar to the  and  transitions. For a given prefix, this defines the transitions:

*   _prefix_ - A transition that takes delay seconds to move images that changed positions to their new locations.
    
*   _prefix_inleft, _prefix_inright, _prefix_intop, _prefix_inbottom - Transitions that take delay seconds to move images that changed positions to their new locations, with newly shown images coming in from the appropriate side.
    
*   _prefix_outleft, _prefix_outright, _prefix_outtop, _prefix_outbottom - Transitions that take delay seconds to move images that changed positions to their new locations, with newly hidden images leaving via the appropriate side.
    

The other parameters are as  takes them:

time\_warp, in\_time\_warp, out\_time\_warp

 that are given a time from 0.0 to 1.0 representing the fraction of the move that is complete, and return a value in the same range giving the fraction of a linear move that is complete.

This can be used to define functions that ease the images around, rather than moving them at a constant speed.

The three arguments are used for images remaining on the screen, newly shown images, and newly hidden images, respectively.

old

If true, when a tag gets its image changed during the transition, the old image will be used in preference to the new one. Otherwise, the new images will be used.

layers

The layers the transition will apply to.

\# This defines all of the pre-defined transitions beginning
\# with "move".
init python:
    define.move\_transitions("move", 0.5)

## Dict Transitions

In many places where Ren'Py takes a transition, it's possible to instead specify a dictionary that maps layer names to this transition. When this is the case, Ren'Py applies each transition to the appropriate layer.

When a dict is used, the pause that usually occurs when a transition takes place does not occur. Instead, the statement taking the dictionary returns immediately, and the transitions are scheduled to occur at the start of the next interaction.

This can be used with the master layer to cause transitions to occur while dialogue is being shown on the screen. For example:

define dis \= { "master" : Dissolve(1.0) }

label start:
    show eileen happy
    with dis

    e "Hello, world."

The dissolve will take place while the text is displayed on the screen.

Dict layer transitions can't be used every place a transition can be used, only in places where applying transitions to a layer is possible. It can be used with the  and `with` cause of the , , and  statements. It can also be used with  and , the  and  actions, and various config variables that take transitions. Dict layer transitions _will not_ work inside things that don't work with layers, such as ,  and .

This can interact poorly with statements that cause a transition to occur themselves, like the transitions caused by `window auto`. That can often be solved with a second dict transition that applies to a different layer. For example, if you are seeing weird blinking when the dialogue window shows and hides, consider changing `options.rpy` to have:

define config.window\_show\_transition \= { "screens" : Dissolve(.25) }
define config.window\_hide\_transition \= { "screens" : Dissolve(.25) }

This works because the dialogue window exists entirely on the screens layer.

## ATL Transitions

_See also:_ 

It's possible to use an ATL transform to define a transition. These transitions need to accept the old\_widget and new\_widget arguments, which will receive displayables representing the screens that are transitioned from and to, respectively.

An ATL transition must set itself the  property to the number of seconds the transition lasts for. It may use the  property to prevent the old displayable from receiving events.

transform spin(duration\=1.0, \*, new\_widget\=None, old\_widget\=None):

    \# Set how long this transform will take to complete.
    delay duration

    \# Center it.
    xcenter .5
    ycenter .5

    \# Spin the old displayable.
    old\_widget
    events False
    rotate 0.
    easeout (duration / 2) rotate 360.0

    \# Spin the new displayable.
    new\_widget
    events True
    easein (duration / 2) rotate 720.0

## Python Transitions

A Python callable may be used as a transition. For that, it must take two keyword arguments described below, and return a displayable that performs the transition effect - usually by delegating that to another transition. The two keyword arguments are old\_widget, which represents the old screen, and new\_widget, which represents the new screen.

The displayable returned by the callable should have a `delay` attribute, set to the number of seconds that the transition should run for.

For example:

init python:
    def dissolve\_or\_pixellate(old\_widget\=None, new\_widget\=None):
        if persistent.want\_pixellate:
            return pixellate(old\_widget\=old\_widget, new\_widget\=new\_widget)
        else:
            return dissolve(old\_widget\=old\_widget, new\_widget\=new\_widget)

Accordingly, all kinds of transitions can be called and passed these two keyword arguments, resulting in a displayable animating the transition between the two passed displayables.

## Automatic Transitions after Scene, Show, and Hide

Ren'Py can automatically show a transition after a series of scene, show, and hide statements. This transition can be enabled by setting the  variable to the transition to be used.

The transition will occur after one or more , , and  statements, provided the statement are not followed by a  statement, or a transition caused by , like the various `window` statements. It's also disabled when in a menu context.

For example:

define \_scene\_show\_hide\_transition \= Dissolve(0.25)

label start:
    scene bg washington
    show eileen happy

    "The transition won't show here, because the dialogue window transitioned in."

    show lucy mad at right

    "The transition will happen here."

    hide lucy mad
    show eileen vhappy

    "And it will happen here, as well."
