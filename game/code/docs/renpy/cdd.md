# Creator-Defined Displayables

The most complex, but most powerful, way of customizing Ren'Py's behavior is to use a creator-defined displayable. A creator-defined displayable is allowed to take arbitrary pygame events. It can also render other displayables, and place them at arbitrary locations on the screen. This makes it suitable for creating 2D mini-games that cannot be expressed with the tools Ren'Py gives you. (But see also the section , which describes a higher-level way of accomplishing many of the same things.)

Creator-defined displayables are programmed entirely in Python, and we encourage you to have a reasonable degree of skill at object-oriented Python programming before you begin creating one.

## Example

Here's an example of a creator-defined displayable. This displayable changes renders its child with an alpha that is determined by the distance of the mouse pointer from the center of the child.

init python:

    import math

    class Appearing(renpy.Displayable):

        def \_\_init\_\_(self, child, opaque\_distance, transparent\_distance, \*\*kwargs):

            \# Pass additional properties on to the renpy.Displayable
            \# constructor.
            super(Appearing, self).\_\_init\_\_(\*\*kwargs)

            \# The child.
            self.child \= renpy.displayable(child)

            \# The distance at which the child will become fully opaque, and
            \# where it will become fully transparent. The former must be less
            \# than the latter.
            self.opaque\_distance \= opaque\_distance
            self.transparent\_distance \= transparent\_distance

            \# The alpha channel of the child.
            self.alpha \= 0.0

            \# The width and height of us, and our child.
            self.width \= 0
            self.height \= 0

        def render(self, width, height, st, at):

            \# Create a transform, that can adjust the alpha channel of the
            \# child.
            t \= Transform(child\=self.child, alpha\=self.alpha)

            \# Create a render from the child.
            child\_render \= renpy.render(t, width, height, st, at)

            \# Get the size of the child.
            self.width, self.height \= child\_render.get\_size()

            \# Create the render we will return.
            render \= renpy.Render(self.width, self.height)

            \# Blit (draw) the child's render to our render.
            render.blit(child\_render, (0, 0))

            \# Return the render.
            return render

        def event(self, ev, x, y, st):

            \# Compute the distance between the center of this displayable and
            \# the mouse pointer. The mouse pointer is supplied in x and y,
            \# relative to the upper-left corner of the displayable.
            distance \= math.hypot(x \- (self.width / 2), y \- (self.height / 2))

            \# Base on the distance, figure out an alpha.
            if distance <= self.opaque\_distance:
                alpha \= 1.0
            elif distance \>= self.transparent\_distance:
                alpha \= 0.0
            else:
                alpha \= 1.0 \- 1.0 \* (distance \- self.opaque\_distance) / (self.transparent\_distance \- self.opaque\_distance)

            \# If the alpha has changed, trigger a redraw event.
            if alpha != self.alpha:
                self.alpha \= alpha
                renpy.redraw(self, 0)

            \# Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return \[ self.child \]

To use the creator-defined displayable, we can create an instance of it, and add that instance to the screen.

screen alpha\_magic:
    add Appearing("logo.png", 100, 200):
        xalign 0.5
        yalign 0.5

label start:
    show screen alpha\_magic

    "Can you find the logo?"

    return

## renpy.Displayable

A creator-defined displayable is created by subclassing the renpy.Displayable class. A creator-defined displayable must override the render method, and may override other methods as well.

A displayable object must be pickleable, which means it may not contain references to objects that cannot be pickled. Most notably, Render objects cannot be stored in a creator-defined displayable.

Since we expect you to override the methods of the displayable class, we'll present them with the self parameter.

_class_ renpy.Displayable

Base class for creator-defined displayables.

\_\_init\_\_(_\*\*properties_)

A subclass may override the constructor, perhaps adding new parameters. If it does, it should pass all unknown keyword arguments to the renpy.Displayable constructor, with the call:

super(MyDisplayable, self).\_\_init\_\_(\*\*properties)

render(_self_, _width_, _height_, _st_, _at_)

Subclasses must override this, to return a  object. The render object determines what, if anything, is shown on the screen.

width, height

The amount of space available to this displayable, in pixels.

st

A float, the shown timebase, in seconds. The shown timebase begins when this displayable is first shown on the screen.

at

A float, the animation timebase, in seconds. The animation timebase begins when an image with the same tag was shown, without being hidden. (When the displayable is shown without a tag, this is the same as the shown timebase.)

The render method is called when the displayable is first shown. It can be called again if  is called on this object.

event(_self_, _ev_, _x_, _y_, _st_)

The event method is called to pass a pygame event to the creator-defined displayable. If the event method returns a value other than None, that value is returned as the result of the interaction. If the event method returns None, the event is passed on to other displayables.

To ignore the event without returning None, raise .

The event method exists on other displayables, allowing the creator-defined displayable to pass on the event.

ev

An 

x, y

The x and y coordinates of the event, relative to the upper-left corner of the displayable. These should be used in preference to position information found in the pygame event objects.

st

A float, the shown timebase, in seconds.

An event is generated at the start of each interaction, and  can be used to cause another event to occur.

per\_interact(_self_)

This method is called at the start of each interaction. It can be used to trigger a redraw, and probably should be used to trigger a redraw if the object participates in rollback.

visit(_self_)

If the displayable has child displayables, this method should be overridden to return a list of those displayables. This ensures that the per\_interact methods of those displayables are called, and also allows images used by those displayables to be predicted.

place(_self_, _dest_, _x_, _y_, _width_, _height_, _surf_, _main\=True_)

This places a render (which must be of this displayable) within a bounding area. Returns an (x, y) tuple giving the location the displayable was placed at.

dest

If not None, the surf will be blitted to dest at the computed coordinates.

x, y, width, height

The bounding area.

surf

The render to place.

main

This is passed to Render.blit().

## renpy.Render

Creator-defined displayables work with renpy.Render objects. Render objects are returned by calling the  function on a displayable. A creator-defined displayable should create a Render object by calling  from its render method.

Since the render object isn't intended to be subclassed, we will omit the implicit self parameter.

_class_ renpy.Render(_width_, _height_)

Creates a new Render object.

width, height

The width and height of the render object, in pixels.

blit(_source_, _pos_, _main\=True_)

Draws another render object into this render object.

source

The render object to draw.

pos

The location to draw into. This is an (x, y) tuple with the coordinates being pixels relative to the upper-left corner of the target render.

main

A keyword-only parameter. If true, source will be displayed in the style inspector.

place(_d_, _x\=0_, _y\=0_, _width\=None_, _height\=None_, _st\=None_, _at\=None_, _render\=None_, _main\=True_)

Renders d, a displayable, and places it into the rectangle defined by the x, y, width, and height, using Ren'Py's standard placement algorithm. Returns an (x, y) tuple giving the location the displayable was placed at. Location is computed by calling Displayable.place() method.

x, y, width, height

The rectangle to place in. If width or height, when None, are the width and height of this render, respectively.

st, at

The times passed to Render. If None, defaults to the times passed to the render method calling this method.

render

If not None, this is used instead of rendering d.

main

As for .blit().

canvas()

Returns a canvas object. A canvas object has methods corresponding to the  functions, with the first parameter (the surface) omitted.

In Ren'Py, the arc and ellipse functions aren't implemented.

Canvas objects also have a get\_surface() method that returns the pygame Surface underlying the canvas.

get\_size()

Returns a (width, height) tuple giving the size of this render.

subsurface(_rect_)

Returns a render consisting of a rectangle cut out of this render.

rect

A (x, y, width, height) tuple.

zoom(_xzoom_, _yzoom_)

Sets the zoom level of the children of this displayable in the horizontal and vertical axes. Only the children of the displayable are zoomed – the width, height, and blit coordinates are not zoomed.

The following attributes and methods are only used when model-based rendering is enabled:

mesh

This field enables model-based rendering for this Render. If true:

If set to True:

*   All of the children of this displayable are rendered to textures.
    
*   A mesh the size of the first child is associated with this displayable.
    
*   A model is created with the mesh, shaders, uniforms, and properties associated with this Render.
    

The model will then be drawn in a single operation.

add\_shader(_shader_)

This causes the shader part shader to be used when this Render or its children are drawn. The part should be a string, or can be a string beginning with "-" to prevent a shader from being drawn.

add\_uniform(_name_, _value_)

Causes the uniform name to have value when this Render or its children are drawn.

add\_property(_name_, _value_)

Causes the GL property name to have value when this Render or one of its children are drawn.

## Utility Functions and Classes

renpy.displayable(_d_, _scope\=None_)

This takes d, which may be a displayable object or a string. If it's a string, it converts that string into a displayable using the usual rules.

renpy.end\_interaction(_value_)

If value is not None, immediately ends the current interaction, causing the interaction to return value. If value is None, does nothing.

This can be called from inside the render and event methods of a creator-defined displayable.

renpy.is\_pixel\_opaque(_d_, _width_, _height_, _st_, _at_, _x_, _y_)

Returns whether the pixel at (x, y) is opaque when this displayable is rendered by `renpy.render(d, width, height, st, at)`.

renpy.load\_image(_im_)

Loads the image manipulator im using the image cache, and returns a render.

renpy.load\_rgba(_data_, _size_)

Loads the image data bytes into a texture of size size, and return it.

data

Should be a bytes object containing the image data in RGBA8888 order.

renpy.load\_surface(_im_)

Loads the image manipulator im using the image cache, and returns a pygame Surface.

renpy.map\_event(_ev_, _keysym_)

Returns true if the pygame event ev matches keysym

keysym

One of:

*   The name of a keybinding in .
    
*   A keysym, as documented in the  section.
    
*   A list containing one or more keysyms.
    

renpy.render(_d_, _width_, _height_, _/_, _st_, _at_)

Causes a displayable to be rendered, and a renpy.Render object to be returned.

d

The displayable to render.

width, height

The width and height available for the displayable to render into.

st, at

The shown and animation timebases.

Renders returned by this object may be cached, and should not be modified once they have been retrieved.

renpy.timeout(_seconds_)

Causes an event to be generated before seconds seconds have elapsed. This ensures that the event method of a user-defined displayable will be called.

renpy.redraw(_d_, _when_)

Causes the displayable d to be redrawn (the render method called) when when seconds have elapsed. The displayable may be redrawn before that time (for example, when a child is redrawn), in which case a pending redraw is forgotten.

_exception_ renpy.IgnoreEvent

This is an exception that, if raised, causes Ren'Py to ignore the event. To raise this inside the event method, write:

raise renpy.IgnoreEvent()
