# Sprites

To support the display of a large number of images at once, Ren'Py supports a sprite system. This system allows one to create sprites, where each sprite contains a displayable. The sprites can then have their location on the screen and vertical ordering changed.

If one ignores performance, the sprite system is conceptually similar to a  wrapping s. Sprites are much faster than transforms, but also less flexible. The big performance improvement of sprites is that each Displayable is rendered only once per frame, even if that Displayable is used by many sprites. The limitation is that Sprites only allow one to change their xoffset and yoffset, rather than the many properties that a Transform has.

To use the sprite system, create a SpriteManager object, and then call its create method to create new particles. As necessary, update the xoffset, yoffset, and zorder fields of each sprite to move it around the screen. By supplying update and event arguments to SpriteManager, you can have the sprites change over time, and react to user input.

## Sprite Classes

_class_ Sprite

This represents a sprite that is managed by the SpriteManager. It contains fields that control the placement of the sprite on the screen. Sprites should not be created directly. Instead, they should be created by calling .

The fields of a sprite object are:

x, y

The x and y coordinates of the upper-left corner of the sprite, relative to the SpriteManager.

zorder

An integer that's used to control the order of this sprite in the relative to the other sprites in the SpriteManager. The larger the number is, the closer to the viewer the sprite is.

events

If True, then events are passed to child. If False, the default, the children ignore events (and hence don't spend time processing them).

The methods of a Sprite object are:

destroy()

Destroys this sprite, preventing it from being displayed and removing it from the SpriteManager.

set\_child(_d_)

Changes the Displayable associated with this sprite to d.

_class_ SpriteManager(_update\=None_, _event\=None_, _predict\=None_, _ignore\_time\=False_, _\*\*properties_)

This displayable manages a collection of sprites, and displays them at the fastest speed possible.

update

If not None, a function that is called each time a sprite is rendered by this sprite manager. It is called with one argument, the time in seconds since this sprite manager was first displayed. It is expected to return the number of seconds until the function is called again, and the SpriteManager is rendered again.

event

If not None, a function that is called when an event occurs. It takes as arguments: \* A pygame event object. \* The x coordinate of the event. \* The y coordinate of the event. \* The time since the sprite manager was first shown. If it returns a non-None value, the interaction ends, and that value is returned.

predict

If not None, a function that returns a list of displayables. These displayables are predicted when the sprite manager is.

ignore\_time

If True, then time is ignored when rendering displayables. This should be used when the sprite manager is used with a relatively small pool of images, and those images do not change over time. This should only be used with a small number of displayables, as it will keep all displayables used in memory for the life of the SpriteManager.

After being rendered once (before the update function is called), SpriteManagers have the following fields:

width, height

The width and height of this SpriteManager, in pixels.

SpriteManagers have the following methods:

create(_d_)

Creates a new Sprite for the displayable d, and adds it to this SpriteManager.

redraw(_delay\=0_)

Causes this SpriteManager to be redrawn in delay seconds.

SnowBlossom(_d_, _count\=10_, _border\=50_, _xspeed\=(20, 50)_, _yspeed\=(100, 200)_, _start\=0_, _fast\=False_, _horizontal\=False_)

The snowblossom effect moves multiple instances of a sprite up, down, left or right on the screen. When a sprite leaves the screen, it is returned to the start.

d

The displayable to use for the sprites.

border

The size of the border of the screen. The sprite is considered to be on the screen until it clears the border, ensuring that sprites do not disappear abruptly.

xspeed, yspeed

The speed at which the sprites move, in the horizontal and vertical directions, respectively. These can be a single number or a tuple of two numbers. In the latter case, each particle is assigned a random speed between the two numbers. The speeds can be positive or negative, as long as the second number in a tuple is larger than the first.

start

The delay, in seconds, before each particle is added. This can be allows the particles to start at the top of the screen, while not looking like a "wave" effect.

fast

If true, particles start in the center of the screen, rather than only at the edges.

horizontal

If true, particles appear on the left or right side of the screen, rather than the top or bottom.

## Sprite Examples

The SnowBlossom class is an easy-to use way of placing falling things on the screen.

image snow \= SnowBlossom("snow.png", count\=100)

This example shows how a SpriteManager can be used to create complex behaviors. In this case, it shows 400 particles, and has them avoid the mouse.

init python:
    import math

    def repulsor\_update(st):

        \# If we don't know where the mouse is, give up.
        if repulsor\_pos is None:
            return .01

        px, py \= repulsor\_pos

        \# For each sprite...
        for i in repulsor\_sprites:

            \# Compute the vector between it and the mouse.
            vx \= i.x \- px
            vy \= i.y \- py

            \# Get the vector length, normalize the vector.
            vl \= math.hypot(vx, vy)
            if vl \>= 150:
                continue

            \# Compute the distance to move.
            distance \= 3.0 \* (150 \- vl) / 150

            \# Move
            i.x += distance \* vx / vl
            i.y += distance \* vy / vl

            \# Ensure we stay on the screen.
            if i.x < 2:
                i.x \= 2

            if i.x \> repulsor.width \- 2:
                i.x \= repulsor.width \- 2

            if i.y < 2:
                i.y \= 2

            if i.y \> repulsor.height \- 2:
                i.y \= repulsor.height \- 2

        return .01

    \# On an event, record the mouse position.
    def repulsor\_event(ev, x, y, st):
        store.repulsor\_pos \= (x, y)

label repulsor\_demo:

    python:
        \# Create a sprite manager.
        repulsor \= SpriteManager(update\=repulsor\_update, event\=repulsor\_event)
        repulsor\_sprites \= \[ \]
        repulsor\_pos \= None

        \# Ensure we only have one smile displayable.
        smile \= Image("smile.png")

        \# Add 400 sprites.
        for i in range(400):
            repulsor\_sprites.append(repulsor.create(smile))

        \# Position the 400 sprites.
        for i in repulsor\_sprites:
            i.x \= renpy.random.randint(2, 798)
            i.y \= renpy.random.randint(2, 598)

        del smile
        del i

    \# Add the repulsor to the screen.
    show expression repulsor as repulsor

    "..."

    hide repulsor

    \# Clean up.
    python:
        del repulsor
        del repulsor\_sprites
        del repulsor\_pos
