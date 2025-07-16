# Drag and Drop

Ren'Py includes drag and drop displayables that allow things to be moved around the screen with the mouse. Some of the uses of dragging are:

*   Allowing windows to be repositioned by the user, storing the window positions.
    
*   Card games that require cards to be dragged around the screen. (For example, solitaire.)
    
*   Inventory systems.
    
*   Drag-to-reorder systems.
    

The drag and drop displayables make it possible to implement these and other uses of drag and drop. There are two classes involved here. The Drag class represents either something that can be dragged around the screen, something that can have a draggable dropped onto it, or something that can do both. The DragGroup class represents a group of Drags – for a drag and drop to occur, both Drags must be part of the same drag group.

The drag and drop system can be used either through the  or directly as displayables. It makes sense to use the screen language when you don't need to refer to the Drags that you create after they've been created. This might be the case if the draggable represents a window that the user places on the screen. If you need to refer to the drags after they've been created, then it's often better to create Drags directly, and add them to a DragGroup.

## Dropping

There are two ways Ren'Py can process a drop:

*   If mouse\_drop is true, the drag will be dropped onto the droppable that is directly below the mouse cursor.
    
*   If mouse\_drop is false, the default, the drop will occur onto the droppable that most fully overlaps with the drag.
    

Unlike when starting a drag, where focus\_mask is used, dropping considers the entire rectangular areas of the draggable and droppable, including any transparent pixels. You may need to design your drag and drop displayables to take this into account, by being generally rectangular in shape.

## Displayables

_class_ Drag(_d\=None_, _drag\_name\=None_, _draggable\=True_, _droppable\=True_, _drag\_raise\=True_, _dragging\=None_, _dragged\=None_, _dropped\=None_, _drag\_handle\=(0.0, 0.0, 1.0, 1.0)_, _drag\_joined\=..._, _clicked\=None_, _hovered\=None_, _unhovered\=None_, _mouse\_drop\=False_, _\*\*properties_)

A displayable that represents an object that can be dragged around its enclosing area. A Drag can also represent an area that other Drags can be dropped on.

A Drag can be moved around inside is parent. Generally, its parent should be either a  or .

A Drag has one child. The child's state reflects the status of the drag and drop operation:

*   `selected_hover` - when it is being dragged.
    
*   `selected_idle` - when it can be dropped on.
    
*   `hover` - when the draggable will be dragged when the mouse is clicked.
    
*   `idle` - otherwise.
    

The drag handle is a rectangle inside the child. The mouse must be over a pixel inside the drag handle for dragging or clicking to occur. If the  property is True, that pixel must not be transparent.

A newly-created draggable is added to the default DragGroup. A draggable can only be in a single DragGroup - if it's added to a second group, it's removed from the first.

When a Drag is first rendered, if it's position cannot be determined from the DragGroup it is in, the position of its upper-left corner is computed using the standard layout algorithm. Once that position has been computed, the layout properties are ignored in favor of the position stored inside the Drag.

Transforms should not be applied to a Drag directly. Instead, apply the transform to the child of the Drag.

d

If present, the child of this Drag. Drags use the child style in preference to this, if it's not None.

drag\_name

If not None, the name of this draggable. This is available as the name property of draggable objects. If a Drag with the same name is or was in the DragGroup, the starting position of this Drag is taken from that Draggable.

draggable

If true, the Drag can be dragged around the screen with the mouse.

droppable

If true, other Drags can be dropped on this Drag.

drag\_raise

If true, this Drag is raised to the top when it is dragged. If it is joined to other Drags, all joined drags are raised.

activated

A callback (or list of callbacks) that is called when the mouse is pressed down on the drag. It is called with one argument, a list of Drags that are being dragged. The return value of this callback is ignored.

dragging

A callback (or list of callbacks) that is called when the Drag is being dragged. It is called with one argument, a list of Drags that are being dragged. If the callback returns a value other than None, that value is returned as the result of the interaction.

dragged

A callback (or list of callbacks) that is called when the Drag has been dragged. It is called with two arguments. The first is a list of Drags that are being dragged. The second is either a Drag that is being dropped onto, or None of a drop did not occur. If the callback returns a value other than None, that value is returned as the result of the interaction.

dropped

A callback (or list of callbacks) that is called when this Drag is dropped onto. It is called with two arguments. The first is the Drag being dropped onto. The second is a list of Drags that are being dragged. If the callback returns a value other than None, that value is returned as the result of the interaction.

When a dragged and dropped callback are triggered for the same event, the dropped callback is only called if dragged returns None.

clicked

A callback that is called when the Drag is clicked without being moved. It is called with one argument, the Drag being clicked on. A droppable can also be focused and clicked. If the callback returns a value other than None, that value is returned as the result of the interaction.

alternate

An action that is run when the Drag is right-clicked (on the desktop) or long-pressed without moving (on mobile). It may be necessary to increase  if this triggers to early on mobile platforms.

hovered

An action to run when the drag gains focus.

unhovered

An action to run when the drag loses focus.

tooltip

A tooltip to display when the drag is hovered over.

drag\_handle

A (x, y, width, height) tuple, giving the position of the drag handle within the child. This tuple takes .

drag\_joined

This is called with the current Drag as an argument. It's expected to return a list of \[ (drag, x, y) \] tuples, giving the draggables to drag as a unit. x and y are the offsets of the drags relative to each other, they are not relative to the corner of this drag. drag is either the Drag object to be joined or the drag\_name of such a Drag.

drag\_offscreen

Determines the conditions under which the drag is allowed to be dragged offscreen. Allowing offscreen dragging can be dangerous to use with drag\_joined or drags that can change size, as the drags can leave the screen entirely, with no way to get them back on the screen.

This should be one of:

False

To disallow dragging the drag offscreen. (The default)

True

To allow dragging offscreen, in any direction.

"horizontal"

To allow dragging offscreen in the horizontal direction only.

"vertical"

To allow dragging offscreen in the vertical direction only.

(width, height)

Both width and height must be integers. The drag can be dragged offscreen as long as a (width, height)-sized part of it remains on-screen. So, (100, 100) will ensure that at least a 100x100 pixel area of the displayable will remain on-screen even while the rest of the displayable can be dragged offscreen. Setting this to the width and height of the displayable being dragged is equivalent to not allowing the drag to go offscreen at all.

(min\_x, max\_x, min\_y, max\_y)

Where each of min\_x, max\_x, min\_y, and max\_y are integers. min\_x is the number of pixels away from the left border, and max\_x is the number of pixels away from the right border. The same goes for min\_y and max\_y on the top and bottom borders respectively. The drag can be moved until one of its edges hit the specified border. (0, 0, 0, 0) is equivalent to not allowing dragging offscreen at all.

For example, (-100, 200, 0, 0) would allow the drag to be dragged 100 pixels off the left edge of the screen and 200 pixels off the right edge of the screen, but does not allow it to be dragged offscreen at the top nor bottom.

This can also be used to constrain the drag within the screen bounds. (200, -200, 200, -200) would only allow the drag within 200 pixels of the edges of the screen.

You can envision this as an additional "border" around the drag, which may go outside the bounds of the screen, that constrains the drag to remain within it.

callable

A callable can be provided to drag\_offscreen. It must take two arguments: an x and a y position which represents the dragged position of the top left corner of the drag, and it must return an (x, y) tuple which is the new (x, y) position the drag should be in. This callable is called frequently, whenever the drag is moved. For example, the following function snaps the drag into place every 300 pixels:

def drag\_snap(x, y):

    if y < 300:
        y \= 0
    elif y < 600:
        y \= 300
    else:
        y \= 600

    return 200, y

mouse\_drop

If true, the drag is dropped on the first droppable under the cursor. If false, the default, the drag is dropped onto the droppable with the largest degree of overlap.

drop\_allowable

A callback that is called to determine whether this drop will allow the current drags to be dropped onto it. It is called with two arguments. The first is the Drag which determines its sensitivity. The second is a list of Drags that are being dragged.

snapped

A callback (or list of callbacks) that is called when the Drag completes a snap animation. It is called with four arguments. The first is the Drag which was undergoing the snap animation. The second and third are the x and y coordinates where the Drag was set to snap to. The fourth is a boolean which is True if the snap animation was successfully completed, and False if it was interrupted (e.g. from being grabbed in the middle of snapping). For example, the following function sets the drag's start\_x and start\_y position to its intended end position if the snap animation was interrupted:

def snapped\_callback(drag, x, y, completed):
    if not completed:
        drag.start\_x \= x
        drag.start\_y \= y

Except for d, all of the parameters are available as fields (with the same name) on the Drag object. In addition, after the drag has been rendered, the following fields become available:

x, y

The position of the Drag relative to its parent, in pixels.

start\_x, start\_y

The drag start position of the Drag relative to its parent, in pixels.

grab\_x, grab\_y

The x and y positions, relative to its parent, where the drag was picked up, in pixels.

last\_drop

The last Drag that the current Drag can be dropped on if released, or None if no valid Drag currently exists.

snapping

True if this Drag is in the middle of a snapping animation.

w, h

The width and height of the Drag's child, in pixels.

bottom()

Lowers this displayable to the bottom of its drag\_group.

set\_child(_d_)

Changes the child of this drag to d.

snap(_x_, _y_, _delay\=0_, _warper\=None_)

Changes the position of the drag. If the drag is not showing, then the position change is instantaneous. Otherwise, the position change takes delay seconds and an optional warper. If no warper is provided, the transition is linear.

top()

Raises this displayable to the top of its drag\_group.

_class_ DragGroup(_\*children_, _\*\*properties_)

Represents a group of Drags. A Drag is limited to the boundary of its DragGroup. Dropping only works between Drags that are in the same DragGroup. Drags may only be raised when they are inside a DragGroup.

A DragGroup is laid out like a .

All positional parameters to the DragGroup constructor should be Drags, that are added to the DragGroup.

min\_overlap

An integer which means the minimum number of pixels at the overlap for the drop to be allowed.

add(_child_)

Adds child, which must be a Drag, to this DragGroup. This child will be added above all other children of this DragGroup.

get\_child\_by\_name(_name_)

Returns the first child of this DragGroup that has a drag\_name of name.

remove(_child_)

Removes child from this DragGroup.

## Examples

An example of a say screen that allows the user to choose the location of the window by dragging it around the screen.:

screen say(who, what):

    drag:
        drag\_name "say"
        yalign 1.0
        drag\_handle (0, 0, 1.0, 30)

        xalign 0.5

        window id "window":
            \# Ensure that the window is smaller than the screen.
            xmaximum 600

            has vbox

            if who:
                text who id "who"

            text what id "what"

Here's a more complicated example, one that shows how dragging can be used to influence gameplay. It shows how dragging can be used to send a character to a location:

init python:

    def detective\_dragged(drags, drop):

        if not drop:
            return

        store.detective \= drags\[0\].drag\_name
        store.city \= drop.drag\_name

        return True

screen send\_detective\_screen:

    \# A map as background.
    add "europe.jpg"

    \# A drag group ensures that the detectives and the cities can be
    \# dragged to each other.
    draggroup:

        \# Our detectives.
        drag:
            drag\_name "Ivy"
            droppable False
            dragged detective\_dragged
            xpos 100 ypos 100

            add "ivy.png"
        drag:
            drag\_name "Zack"
            droppable False
            dragged detective\_dragged
            xpos 150 ypos 100

            add "zack.png"

        \# The cities they can go to.
        drag:
            drag\_name "London"
            draggable False
            xpos 450 ypos 140

            add "london.png"

        drag:
            drag\_name "Paris"
            draggable False
            xpos 500 ypos 280

            add "paris.png"

label send\_detective:
    "We need to investigate! Who should we send, and where should they go?"

    call screen send\_detective\_screen

    "Okay, we'll send \[detective\] to \[city\]."

More complicated systems take significant programming skill to get right.

The `as` clause can be used to bind a drag to variable, which can then be used to call methods on the drag.

screen snap():

    drag:
        as carmen
        draggable True
        xpos 100 ypos 100
        frame:
            style "empty"
            background "carmen.png"
            xysize (100, 100)

            vbox:
                textbutton "London" action Function(carmen.snap, 450, 140, 1.0)
                textbutton "Paris" action Function(carmen.snap, 500, 280, 1.0)
