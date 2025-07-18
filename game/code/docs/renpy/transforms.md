# Transforms

Transforms are used in order to turn a  into another displayable. There are several kinds of transforms, and various ways to create them. The built-in transforms are used to control where an image is placed on the screen, while user-defined transforms can cause more complex effects, like motion, zoom, rotation, up to complex color effects.

Transforms can be applied to images by passing them to the `at` clause of the  or scene statements. The following applies the `right` transform to the `eileen happy` image:

show eileen happy at right

Multiple transforms can be applied by separating them with commas. These transforms are applied from left-to-right.

show eileen happy at halfsize, right

## Applying transforms to displayables in Python

There are several ways to apply transform `t` to displayable `d` in Python:

1.  The most universal and most recommended way is `At(d, t)` (see below). It works with all transforms.
    
2.  `d(child=t)` works with all .
    
3.  `t(d)` works with all , as well as with ATL transforms that don't have any positional parameters.
    

At(_d_, _\*args_)

Given a displayable d, applies each of the transforms in args to it. The transforms are applied in left-to-right order, so that the outermost transform is the rightmost argument.

transform birds\_transform:
    xpos \-200
    linear 10 xpos 800
    pause 20
    repeat

image birds \= At("birds.png", birds\_transform)

Note

The resulting value may not be able to be displayed, if there remains parameters of the transform that have not been given a value, as can be the case with transforms defined using the .

Note

The resulting value may still be a transform that can be applied to yet another displayable (overriding its previous child) ; that's the case with ATL transforms which are still usable as transforms even when having their child set.

## Built-in Transforms

Ren'Py ships with a number of transforms defined by default. These transforms position things on the screen. Here's a depiction of where each built-in transform will position an image.

             +-----------------------------------------------------------+
             |topleft, reset               top                   topright|
             |                                                           |
             |                                                           |
             |                                                           |
             |                                                           |
             |                          truecenter                       |
             |                                                           |
             |                                                           |
             |                                                           |
             |                                                           |
offscreenleft|left                   center, default                right|offscreenright
             +-----------------------------------------------------------+

The  and  transforms position images off the edges of the screen. These transforms can be used to move things off the screen (remember to hide them afterwards, to ensure that they do not consume resources).

The transforms are:

center

Centers horizontally, and aligns to the bottom of the screen.

default

Centers horizontally, and aligns to the bottom of the screen. This can be redefined via  to change the default placement of images shown with the show or scene statements.

left

Aligns to the bottom-left corner of the screen.

offscreenleft

Places the displayable off the left side of the screen, aligned to the bottom of the screen.

offscreenright

Places the displayable off the left side of the screen, aligned to the bottom of the screen.

reset

Resets the transform. Places the displayable in the top-left corner of the screen, and also eliminates any zoom, rotation, or other effects.

right

Aligns to the bottom-right corner of the screen.

top

Centers horizontally, and aligns to the top of the screen.

topleft

Aligns to the top-left corner of the screen.

topright

Aligns to the top-right corner of the screen.

truecenter

Centers both horizontally and vertically.

## ATL - Animation and Transformation Language

The Animation and Transformation Language (ATL) is a high-level language which can create animations, move displayables across the screen, set their position, apply transformations, and more. These can be changed over time, and in response to events.

ATL transform objects, which are created using the  down below, are displayables and can be used as such (even though they will be transparent when their child displayable is not set) : they can be passed to a screen's  element, or to a  statement, or to the  function.

### Ren'Py script statements

There are three Ren'Py script statements which can include ATL code.

#### Transform Statement

The `transform` statement creates a new transform. The syntax is:

**atl\_transform** ::=  "transform" `qualname` ( "(" `parameters` ")" )? ":"
                      `atl_block`

The transform statement is run at . The transform may take a list of parameters, which works much the same way as a Python function definition, except that several kinds of parameters are currently forbidden, though they may be allowed in the future:

1.  Positional-only parameters
    
2.  Keyword-only parameters without a default value
    
3.  Variadic positional parameters (`*args`)
    
4.  Variadic keyword parameters (`**kwargs`)
    

The created object cannot be used as a transform until and unless all its parameters have been given a value.

_See also :_ 

qualname, the name of the transform, must be a set of dot-separated Python identifiers. The transform created by the ATL block will be bound to that name, within the provided  if one was provided.

transform left\_to\_right:
    xalign 0.
    linear 2 xalign 1.
    repeat

transform ariana.left:
    xalign .3

transform animated\_ariana\_disp:
    "ariana"
    pause 1.
    "ariana\_reverse"
    pause 1.
    repeat

The created object is both a transform and a displayable, but as opposed to the `image` statement, it is created as a variable (or a constant), rather than in the namespace of .

#### Image Statement with ATL Block

The second way to include ATL code in a script is as part of an . As its inline counterpart, it binds an image name (which may contain spaces) to the given transform. As there is no way to supply with parameters, it's only useful if the transform defines an animation. The syntax is:

**atl\_image** ::=  "image" `image_name` ":"
                  `atl_block`

image animated\_ariana\_img:
    "ariana"
    pause 1.
    "ariana\_reverse"
    pause 1.
    repeat

#### Scene and Show Statements with ATL Block

The final way to use ATL is as part of a  or scene statement. This wraps the image that's being shown inside an ATL transformation which is created on the fly and applied to the image. The syntax is:

**atl\_show ** ::=  `stmt_show` ":"
                  `atl_block`
**atl\_scene** ::=  `stmt_scene` ":"
                  `atl_block`

show eileen happy:
    xalign 1.

scene bg washington:
    zoom 2.

### ATL Syntax and Statements

ATL statements may be inline, or make up a block within the ATL block in which it is written. With some exceptions described in the relevant statements, the statements in an ATL block are executed in order, from top to bottom.

If an ATL statement requires an expression to be evaluated, such evaluation occurs when the transform is first executed (that is when using a `show` statement, or displaying the transform as part of a screen), and not when the particular ATL statement is executed.

The following are the ATL statements.

#### Inline Contains Statement

The inline contains statement takes a single expression evaluating to a .

**atl\_contains** ::=  "contains" `simple_expression`

This statement sets (or replaces) the child of the current ATL transform to the value of the expression, making it useful for animation.

transform an\_animation:
    "1.png"
    pause 2
    "2.png"
    pause 2
    repeat

image move\_an\_animation:
    contains an\_animation

    \# If we didn't use contains, we'd still be looping
    \# and would never reach here.
    xalign 0.0
    linear 1.0 yalign 1.0

The  is less explicit and bears ambiguity with the transform expression statement, but it allows for a  to be used for replacing the child. This statement can be particularly useful when an ATL transform wishes to contain, rather than include, a second ATL transform.

#### Number Statement

The number statement consists of a simple expression evaluating to an integer or floating-point number. It can optionally be preceded by the keyword "pause".

**atl\_number** ::=  "pause"? `simple_expression`

It is used as a number of seconds to pause execution for.

image atl example:
    \# Displays logo\_base.png
    contains "logo\_base.png"

    \# Pause for 1.0 seconds.
    pause 1.0

    \# Show logo\_bw.png, with a dissolve.
    "logo\_bw.png" with Dissolve(0.5, alpha\=True)

    \# Pause for 3 seconds
    3

    repeat

#### Properties Statement

This statement sets one or more transform properties to a new value.

**atl\_properties** ::=  +

**atl\_property** ::=  `transform_property` `simple_expression`

The statement first gives a series (at least one) of property names, each followed by the new value to set it to. See  for a list of transform properties, their meaning and the values they take.

transform rightoid:
    xalign .9

transform ariana.left:
    xanchor .3 xpos 100

#### Interpolation Statement

The interpolation statement is the main way of getting smoothly animated transformations.

**atl\_interp** ::=  ((`warper` `simple_expression`) | ("warp" `simple_expression` `simple_expression`)) (\+ | (":"
                   \+ ))

**atl\_interp\_target** ::=  (\+ ("knot" `simple_expression`)\* )
                       | 
                       | "clockwise"
                       | "counterclockwise"
                       | ("circles" `simple_expression`)

Some sample interpolations:

show logo base:
    \# Show the logo at the upper right side of the screen.
    xalign 1.0 yalign 0.0

    \# Take 1.0 seconds to move things back to the left.
    linear 1.0 xalign 0.0

    \# Take 1.0 seconds to move things to the location specified in the
    \# truecenter transform. Use the ease warper to do this.
    ease 1.0 truecenter

    \# Set the location to circle around.
    anchor (0.5, 0.5)

    \# Use circular motion to bring us to spiral out to the top of
    \# the screen. Take 2 seconds to do so.
    linear 2.0 yalign 0.0 clockwise circles 3

    \# Use a spline motion to move us around the screen.
    linear 2.0 align (0.5, 1.0) knot (0.0, .33) knot (1.0, .66)

    \# Changes xalign and yalign at the same time.
    linear 2.0 xalign 1.0 yalign 1.0

    \# The same thing, using a block.
    linear 2.0:
        xalign 1.0
        yalign 1.0

The first part of the interpolation is used to select a function that time-warps the interpolation. That means, a function that maps linear time to non-linear time, see  for more information about that. Selecting a warper can either be done by giving the name of a registered warper, or by giving the keyword "warp" followed by an expression giving a warping function.

In either case, it's followed by a number giving the number of seconds the interpolation should take.

transform builtin\_warper:
    xpos 0
    ease 5 xpos 520

init python:
    def my\_warper(t):
        return t\*\*4.4

define my\_warpers \= \[my\_warper\]

transform accessed\_as\_function:
    xpos 0
    warp my\_warpers\[0\] 5 xpos 520
    warp my\_warper 3 xpos 100

The interpolation will persist for the given amount of time, and at least one frame.

When  are given, the value each is given is the value it will be set to at the end of the interpolation statement. This can be tweaked in several ways:

*   If the value is followed by one or more knots, then spline motion is used. The starting point is the value of the property at the start of the interpolation, the end point is the given value, and the knots are used to control the spline. A quadratic curve is used for a single knot, Bezier is used when there are two and Catmull-Rom is used for three or more knots. In the former two cases, the knot or knots are simply control nodes. For Catmull-Rom, the first and last knot are control nodes (often outside the displayed path) and the other knots are points the path passes through.
    
*   If the interpolation statement contains a "clockwise" or "counterclockwise" clause, circular motion is used. In that case, Ren'Py will compare the start and end locations (which are set by , ,  and , ...) and figure out the polar coordinate center (which is ). Ren'Py will then compute the number of degrees it will take to go from the start angle to the end angle, in the specified direction of rotation. If the circles clause is given, Ren'Py will ensure that the appropriate number of circles will be made.
    
*   Otherwise, the value is linearly interpolated between the start and end locations.
    

It is also possible to interpolate a , which should in this case be an ATL transform containing only a single properties statement. The properties from the transform will be processed as if they were written directly in this interpolation.

A warper may be followed by a colon (:). In that case, it may be followed by one or more lines, in an indented block, containing the clauses described above. This lets you break an interpolation of many different things up into several lines.

#### Pass Statement

**atl\_pass** ::=  "pass"

The `pass` statement is a simple statement that causes nothing to happen : a no-op. This can be used when there's a desire to separate statements, like when two sets of choice statements (see below) would otherwise be back-to-back. It can also be useful when the syntax requires a block to be created but you need it to be empty, for example to make one of the choice blocks not do anything.

#### Repeat Statement

The `repeat` statement is a simple statement that causes the block containing it to resume execution from the beginning.

**atl\_repeat** ::=  "repeat" (`simple_expression`)?

If the expression is present, then it is evaluated to give an integer number of times the block will execute. (So a block ending with `repeat 2` will execute at most twice in total, and `repeat 1` does not repeat.)

The repeat statement must be the last statement in a block:

show logo base:
    xalign 0.0
    linear 1.0 xalign 1.0
    linear 1.0 xalign 0.0
    repeat

#### Block Statement

The `block` statement simply contains a block of ATL statements.

**atl\_block\_stmt** ::=  "block" ":"
                         `atl_block`

This can be used to group statements that will repeat:

show logo base:
    alpha 0.0 xalign 0.0 yalign 0.0
    linear 1.0 alpha 1.0

    block:
        linear 1.0 xalign 1.0
        linear 1.0 xalign 0.0
        repeat

#### Parallel Statement

The `parallel` statement defines a set of ATL blocks to execute in parallel.

**atl\_parallel** ::=  ("parallel" ":"
                     `atl_block`)+

Parallel statements are greedily grouped into a parallel set when more than one parallel block appears consecutively in a block. The set of all parallel blocks are then executed simultaneously. The parallel statement terminates when the last block terminates.

The blocks within a set should be independent of each other, and manipulate different . When two blocks change the same property, the result is undefined.

show logo base:
    parallel:
        xalign 0.0
        linear 1.3 xalign 1.0
        linear 1.3 xalign 0.0
        repeat
    parallel:
        yalign 0.0
        linear 1.6 yalign 1.0
        linear 1.6 yalign 0.0
        repeat

#### Choice Statement

The `choice` statement defines one of a set of potential choices. Ren'Py will pick one of the choices in the set, and execute the ATL block associated with it, and then continue execution after the last choice in the choice set.

**atl\_choice** ::=  ("choice" (`simple_expression`)? ":"
                    `atl_block`)+

Choice statements are greedily grouped into a choice set when more than one choice statement appears consecutively in a block. If the simple\_expression is supplied, it is a floating-point weight given to that block, otherwise 1.0 is assumed.

image eileen random:
    choice:
        "eileen happy"
    choice:
        "eileen vhappy"
    choice:
        "eileen concerned"

    pause 1.0
    repeat

The `pass` statement can be useful in order to break several sets of choice blocks into several choice statements, or to make an empty choice block.

#### Animation Statement

The `animation` statement must be the first statement in an ATL block, and tells Ren'Py that the block uses the animation timebase.

**atl\_animation** ::=  "animation"

As compared to the normal showing timebase, the animation timebase starts when an image or screen with the same tag is shown. This is generally used to have one image replaced by a second one at the same apparent time. For example:

image eileen happy moving:
    animation
    "eileen happy"
    xalign 0.0
    linear 5.0 xalign 1.0
    repeat

image eileen vhappy moving:
    animation
    "eileen vhappy"
    xalign 0.0
    linear 5.0 xalign 1.0
    repeat

label start:
    show eileen happy moving
    pause
    show eileen vhappy moving
    pause

This example will cause Eileen to change expression when the first pause finishes, but will not cause her position to change, as both animations share the same animation time, and hence will place her sprite in the same place. Without the animation statement, the position would reset when the player clicks.

#### On Statement

The `on` statement defines an event handler.

**atl\_on** ::=  "on" `name` ("," `name`)\* ":"
                 `atl_block`

`on` blocks are greedily grouped into a single statement. On statement can handle a single event name, or a comma-separated list of event names.

This statement is used to handle events. When an event is handled, handling of any other event ends and handing of the new event immediately starts. When an event handler ends without another event occurring, the `default` event is produced (unless the `default` event is already being handled).

Execution of the on statement will never naturally end. (But it can be ended by the time statement, or an enclosing event handler.)

See the event statement for a way to produce arbitrary events, and see  for a list of naturally-produced events.

show logo base:
    on show:
        alpha 0.0
        linear .5 alpha 1.0
    on hide:
        linear .5 alpha 0.0

transform pulse\_button:
    on hover, idle:
        linear .25 zoom 1.25
        linear .25 zoom 1.0

#### Transform Expression Statement

This statement includes another ATL transform as part of the current ATL block.

**atl\_transform\_expression** ::=  `simple_expression`

This only applies if the ATL transform has **not** been supplied a child (see the top of the page for how to do that), otherwise it will be interpreted as a . The contents of the provided ATL transform are included at the location of this statement.

transform move\_right:
    linear 1.0 xalign 1.0

image atl example:
    \# Display logo\_base.png
    "logo\_base.png"

    \# Run the move\_right transform.
    move\_right

#### Displayable Statement

The displayable statement consists of a simple Python expression evaluating to a , optionally followed by a with clause containing a second simple expression.

**atl\_displayable** ::=  `simple_expression` ("with" `simple_expression`)?

It is used to set or replace the child of the transform when the statement executes.

If a `with` clause is present, the second expression is evaluated as a , and the transition is applied between the old child and the new child. Be careful in that not all transitions will work in this situation, notably  and  and  transitions.

image atl example:
    \# Displays logo\_base.png
    "logo\_base.png"

    \# Pause for 1.0 seconds.
    1.0

    \# Show logo\_bw.png, with a dissolve.
    "logo\_bw.png" with Dissolve(0.5, alpha\=True)

Warning

If passing any child-less transform is pointless as it will make the transform transparent and ineffective, passing child-less ATL transforms may be interpreted as a , which will yield different results.

If the expression evaluates to an ATL transform **with** a child, the execution of this ATL block will only continue after the includee's ATL code runs.

#### Contains Block Statement

The contains block, like its , sets the child of the transform but in a different way.

**atl\_counts** ::=  "contains" ":"
                   `atl_block`

One or more contains blocks will be greedily grouped together inside a single contains statement, wrapped inside a , and set as the child of the transform.

Each block should define a displayable to use, otherwise an error will occur. The contains statement executes instantaneously, without waiting for the children to complete.

image test double:
    contains:
        "logo.png"
        xalign 0.0
        linear 1.0 xalign 1.0
        repeat

    contains:
        "logo.png"
        xalign 1.0
        linear 1.0 xalign 0.0
        repeat

#### Function Statement

The `function` statement allows ATL to use Python code.

**atl\_function** ::=  "function" `simple_expression`

The functions have the same signature as those used with :

*   The first argument is a transform object.  can be set as attributes on this object.
    
*   The second argument is the shown timebase, the number of seconds since the function began executing.
    
*   The third argument is the animation timebase, which is the number of seconds something with the same tag has been on the screen.
    
*   If the function returns a number, it will be called again after that number of seconds has elapsed. (0 seconds means to call the function as soon as possible.) If the function returns None, control will pass to the next ATL statement.
    

This function should not have side effects other than changing the transform object in the first argument, and may be called at any time with any value as part of prediction.

Note that `function` is not a transform property, and that it doesn't have the exact same behavior as 's function parameter.

init python:
    def slide\_vibrate(trans, st, at, /):
        if st \> 1.0:
            trans.xalign \= 1.0
            trans.yoffset \= 0
            return None
        else:
            trans.xalign \= st
            trans.yoffset \= random.randrange(\-10, 11)
            return 0

label start:
    show logo base:
        function slide\_vibrate
        pause 1.0
        repeat

#### Time Statement

The `time` statement is a control statement.

**atl\_time** ::=  "time" `simple_expression`

It contains a single expression, which is evaluated to give a time expressed as seconds from the start of execution of the containing block. When the time given in the statement is reached, the following statement begins to execute. This transfer of control occurs even if a previous statement is still executing, and causes any such prior statement to immediately terminate.

Time statements are implicitly preceded by a pause statement with an infinite time. This means that if control would otherwise reach the time statement, it waits until the time statement would take control.

When there are multiple time statements in a block, they must strictly increase in order.

image backgrounds:
    "bg band"
    xoffset 0
    block:
        linear 1 xoffset 10
        linear 1 xoffset 0
        repeat \# control would never exit this block

    time 2.0
    xoffset 0
    "bg whitehouse"

    time 4.0
    "bg washington"

#### Event Statement

The `event` statement is a simple statement that causes an event with the given name to be produced.

**atl\_event** ::=  "event" `name`

When an event is produced inside a block, the block is checked to see if an event handler for the given name exists. If it does, control is transferred to the event handler. Otherwise, the event propagates to any containing event handler.

### External events

The following events are triggered automatically within an ATL transform:

`start`

A pseudo-event, triggered on entering an `on` statement, if no event of higher priority has happened.

`show`

Triggered when the transform is shown using the show or scene statement, and no image with the given tag exists.

`replace`

Triggered when transform is shown using the `show` statement, replacing an image with the given tag.

`hide`

Triggered when the transform is hidden using the `hide` statement or its Python equivalent.

Note that this isn't triggered when the transform is eliminated via the  or exiting the  it exists in, such as when exiting the game menu.

`replaced`

Triggered when the transform is replaced by another. The image will not actually hide until the ATL block finishes.

`hover`, `idle`, `selected_hover`, `selected_idle`, `insensitive`, `selected_insensitive`

Triggered when a button containing this transform, or a button contained by this transform, enters the named state.

### ATL curry and partial parameter passing

An ATL transform defined using the  can have its parameters set at different times. When calling an ATL transform like a function, the resulting value is still a transform, and the parameters that were passed a value are treated as though the value is the new default value of the parameter.

For example:

transform screamer(child, screamee, wait\_time\=2, flash\_time\=.1):
    child
    pause wait\_time
    screamee
    pause flash\_time
    child

\# doing this doesn't raise an error (it would if it were a Python function)
define shorter\_screamer \= screamer(wait\_time\=1)

define eileen\_excited\_screamer \= screamer(screamee\="eileen excited", flash\_time\=.2)

label start:
    show hhannahh happy at screamer(screamee\="hhannahh surprised", wait\_time\=1.5)
    "Here is one way"

    show eileen vhappy at eileen\_excited\_screamer
    "Here is another"

    show patricia sad at eileen\_excited\_screamer(screamee\="patricia wow")
    "And you can also do this"

Note that the `shorter_screamer` transform, just as the `screamer` transform, cannot be used directly like `show eileen at screamer`, since their `screamee` parameters do not have a value.

Note also that, like labels and screens, the default values of the parameters of a transform directly created by the  will be evaluated at the time when the transform is _called_, not at the time when it is _defined_.

However, the transform resulting from calling another transform (such as `shorter_screamer` in the example above, or also the transform applied to patricia) has all the default values of its parameters already evaluated, whether they come from the evaluation of the default values in the original transform (such as `shorter_screamer`'s flash\_time parameter, or patricia's transform's wait\_time parameter), or from values passed to it in a call earlier in the line (such as `shorter_screamer`'s wait\_time parameter, or patricia's transform's screamee and flash\_time parameters).

### Special Child Parameter

If an ATL transform has a parameter named "child" and that parameter receives a value, **regardless of the kind of parameter or the way it receives a value** (by a positional argument or by keyword, and even if the parameter is positional-only or keyword-only, and defaulted or required), then in parallel the child of the transform is set to the value of the parameter.

Note that the default value of the parameter doesn't count, the parameter has to receive a value from the outside.

Conversely, when that ATL transform is used as a transform, the `child=` keyword argument will be passed, and so in addition to setting the child, if a parameter is there to receive it (excluding positional-only parameters, since it is passed by keyword), it will have the child's value when the transform executes.

For example, this enables to swap between the supplied child and another displayable:

transform lucy\_jump\_scare(child):
    \# the child is implicitly set as the child of the transform
    pause 5

    \# Jump scare
    "lucy mad"
    pause .2

    \# Go back to the original child
    child

It can also be used to place the original child inside a `contains` block:

transform marquee(width, height\=1.0, duration\=2.0, child\=None):
    xcenter 0.5
    ycenter 0.5

    crop (0, 0, 0.5, 500)

    contains:
        child
        xanchor 0.0 xpos 1.0
        linear duration xanchor 1.0 xpos 0.0

The old\_widget and new\_widget keyword-able parameters (meaning that they should not be positional-only) have a special use as part of .

## Warpers

A warper is a function that can change the amount of time an interpolation statement considers to have elapsed. They are defined as functions from t to t', where t and t' are floating point numbers, with t ranging from 0.0 to 1.0 over the given amount of time. (If the statement has 0 duration, then t is 1.0 when it runs.) t' should start at 0.0 and end at 1.0, but can be greater or less. The following warpers are defined by default.

`pause`

Pause, then jump to the new value. If `t == 1.0`, `t' = 1.0`. Otherwise, `t' = 0.0`.

`linear`

Linear interpolation. `t' = t`

`ease`

Start slow, speed up, then slow down. `t' = .5 - math.cos(math.pi * t) / 2.0`

`easein`

Start fast, then slow down. `t' = math.cos((1.0 - t) * math.pi / 2.0)`

`easeout`

Start slow, then speed up. `t' = 1.0 - math.cos(t * math.pi / 2.0)`

In addition, most of Robert Penner's easing functions are supported. To make the names match those above, the functions have been renamed somewhat. Graphs of these standard functions can be found at .

| Ren'Py Name | easings.net Name |
| --- | --- |
| ease\_back | easeInOut\_back |
| ease\_bounce | easeInOut\_bounce |
| ease\_circ | easeInOut\_circ |
| ease\_cubic | easeInOut\_cubic |
| ease\_elastic | easeInOut\_elastic |
| ease\_expo | easeInOut\_expo |
| ease\_quad | easeInOut\_quad |
| ease\_quart | easeInOut\_quart |
| ease\_quint | easeInOut\_quint |
| easein\_back | easeOut\_back |
| easein\_bounce | easeOut\_bounce |
| easein\_circ | easeOut\_circ |
| easein\_cubic | easeOut\_cubic |
| easein\_elastic | easeOut\_elastic |
| easein\_expo | easeOut\_expo |
| easein\_quad | easeOut\_quad |
| easein\_quart | easeOut\_quart |
| easein\_quint | easeOut\_quint |
| easeout\_back | easeIn\_back |
| easeout\_bounce | easeIn\_bounce |
| easeout\_circ | easeIn\_circ |
| easeout\_cubic | easeIn\_cubic |
| easeout\_elastic | easeIn\_elastic |
| easeout\_expo | easeIn\_expo |
| easeout\_quad | easeIn\_quad |
| easeout\_quart | easeIn\_quart |
| easeout\_quint | easeIn\_quint |

These warpers can be accessed in the `_warper` read-only module, which contains the functions listed above. It is useful for things in Ren'Py which take a time-warping function, such as , which you can use like:

with Dissolve(1, time\_warp\=\_warper.easein\_quad)

New warpers can be defined using the `renpy.atl_warper` decorator, in a `python early` block. It should be placed in a file that is parsed before any file that uses the warper. This looks like:

python early hide:

    @renpy.atl\_warper
    def linear(t):
        return t

## Replacing Transforms

When an ATL transform, a built-in transform or a transform defined using the  class is replaced by another transform of these categories, the properties of the outgoing transform are inherited by the incoming transform. That inheritance doesn't apply for other kinds of transforms.

When the  has multiple transforms in the `at` list, the transforms are matched from last to first, until one list runs out. For example:

show eileen happy at a, b, c
"Dialogue !"
show eileen happy at d, e

The `c` transform will be replaced by `e`, the `b` transform will be replaced by `d`, and nothing replaces the `a` transform.

At the moment of replacement, if both transforms are of suitable kinds, the values of the properties of the old transform are copied to the new transform. If the old transform was animated, the current intermediate value is inherited. For example:

transform bounce:
    linear 3.0 xalign 1.0
    linear 3.0 xalign 0.0
    repeat

transform headright:
    linear 15 xalign 1.0

label example:
    show eileen happy at bounce
    pause
    show eileen happy at headright
    pause

In this example, the image will bounce from left to right and back until the player clicks. When that happens, the `xalign` property of the `bounce` transform will be used to initialize the `xalign` property of the `headright` transform, and so the image will move from where it was when the player first clicked.

The position properties (, , , , and properties setting them such as  or / ) have a special rule for inheritance : a value set in the child will override a value set in the parent. That is because a displayable may have only one position, and a position that is actively set takes precedence.

Finally, when a `show` statement does not include an `at` clause, the same transforms are used, so no inheritance is necessary. To reset all transform properties, hide and then show the displayable again. To break the animations applied to a displayable (but keep the position), you can use:

show eileen happy at some\_animation
"Wow, so this is what antigravity feels like !"

show eileen:
    pass
"But I'm happy when it settles down."

## The Transform Class

One equivalent to to the simplest ATL transforms is the Transform class.

_class_ Transform(_child\=None_, _function\=None_, _\*\*properties_)

Creates a transform which applies operations such as cropping, rotation, scaling or alpha-blending to its child. A transform object has fields corresponding to the , which it applies to its child.

child

The child the transform applies to.

function(_trans: _, _st: float_, _at: float_, _/_) → int | None

If not None, this function will be called when the transform is rendered, with three positional arguments:

*   The transform object.
    
*   The shown timebase, in seconds.
    
*   The animation timebase, in seconds.
    

The function should return a delay, in seconds, after which it will be called again, or None to be called again at the start of the next interaction.

This function should not have side effects other than changing the Transform object in the first argument, and may be called at any time with any value as a part of prediction.

Additional keyword arguments are values that transform properties are set to. These particular transform properties will be set each time the transform is drawn, and so may not be changed after the Transform object is created. Fields corresponding to other transform properties, however, can be set and changed afterwards, either within the function passed as the function parameter, or immediately before calling the  method.

hide\_request

This attribute is set to true when the function is called, to indicate that the transform is being hidden.

hide\_response

If `hide_request` is true, this can be set to false to prevent the transform from being hidden.

set\_child(_child_)

Call this method with a new child to change the child of this transform.

update()

This should be called when a transform property field is updated outside of the function passed as the function argument, to ensure that the change takes effect.

## Callables as transforms

Finally, simple Python callables can be used as transforms. These callables should take a single  as an argument, and return a new Displayable. For example:

init python:

    \# this transform uses the right and left transforms
    def right\_or\_left(d):
        if switch:
            return At(d, right)
        else:
            return At(d, left)

That means that certain builtins which take a displayable and return a displayable, such as , are also transforms and can be used as such.
