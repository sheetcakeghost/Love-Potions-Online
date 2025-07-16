# Screens and Python

## Screen Functions

The following functions support various operations related to screens.

renpy.call\_screen(_\_screen\_name_, _\*args_, _\_with\_none\=True_, _\_mode\='screen'_, _\*\*kwargs_)

The programmatic equivalent of the call screen statement.

This shows \_screen\_name as a screen, then causes an interaction to occur. The screen is hidden at the end of the interaction, and the result of the interaction is returned.

Positional arguments, and keyword arguments that do not begin with \_ are passed to the screen.

If \_with\_none is false, "with None" is not run at the end of end of the interaction.

If \_mode is passed, it will be the mode of this interaction, otherwise the mode will be "screen".

renpy.current\_screen()

Returns information about the screen currently being updated, rendered, or processed.

See  for documented fields on the returned object.

renpy.get\_adjustment(_bar\_value_)

Given bar\_value, a , returns the  it uses. The adjustment has the following attributes defined:

value

The current value of the bar.

range

The current range of the bar.

renpy.get\_displayable(_screen_, _id_, _layer\=None_, _base\=False_)

From the screen on layer, returns the displayable with id. Returns None if the screen doesn't exist, or there is no widget with that id on the screen.

renpy.get\_displayable\_properties(_id_, _screen\=None_, _layer\=None_)

Returns the properties for the displayable with id in the screen on layer. If screen is None, returns the properties for the current screen. This can be used from Python or property code inside a screen.

Note that this returns a dictionary containing the widget properties, and so to get an individual property, the dictionary must be accessed.

renpy.get\_screen(_name_, _layer\=None_, _tag\_only\=False_)

Returns information about the screen with the given name on layer. name is first interpreted as a tag name, and then as a screen name. If the screen is not showing, returns None.

This can also take a list of names, in which case the first screen that is showing is returned.

tag\_only

If true, only the tag is considered.

This function can be used to check whether a screen is showing:

if renpy.get\_screen("say"):
    text "The say screen is showing."
else:
    text "The say screen is hidden."

The objects returned by this function have the following documented fields:

layer

The layer the screen is being displayed on.

name

The name of the screen.

zorder

The zorder the screen is being displayed at.

Warning

Like other similar functions, the object this returns is meant to be used in the short term after the function is called. Including it in save data or making it participate in rollback is not advised.

renpy.get\_screen\_variable(_name_, _\*_, _screen\=None_, _layer\=None_)

Returns the value of a variable in the scope of a screen.

name

The name of the variable to return.

screen

The name of the screen to return the variable from. If None, the current screen is used. (The current screen is only defined when updating a screen, and in actions that are run inside the screen.)

layer

The layer to find the screen on, if screen is not None.

renpy.hide\_screen(_tag_, _layer\=None_, _immediately\=False_)

The programmatic equivalent of the hide screen statement.

Hides the screen with tag on layer.

If immediately is true, the screen is hidden immediately, without the 'on hide' event.

renpy.set\_focus(_screen_, _id_, _layer\='screens'_)

This attempts to focus the displayable with id in the screen screen. Focusing will fail if the displayable isn't found, the window isn't focused, or something else is grabbing focus.

The focus may change if the mouse moves, even slightly, after this call is processed.

renpy.set\_screen\_variable(_name_, _value_, _\*_, _screen\=None_, _layer\=None_)

Sets a variable to a value in the scope of a screen. Note that this will not immediately update the variable's value - call  to cause the screen to be updated.

name

The name of the variable to set. This should be a variable created with the  statement, as optimization may prevent changes to other variables from being visible.

value

The value to set the variable to.

screen

The name of the screen to return the variable from. If None, the current screen is used. (The current screen is only defined when updating a screen, and in actions that are run inside the screen.)

layer

The layer to find the screen on, if screen is not None.

renpy.show\_screen(_\_screen\_name_, _\*args_, _\_layer\=None_, _\_zorder\=None_, _\_tag\=None_, _\_widget\_properties\={}_, _\_transient\=False_, _\*\*kwargs_)

The programmatic equivalent of the show screen statement.

Shows the named screen. This takes the following keyword arguments:

\_screen\_name

The name of the screen to show.

\_layer

The layer to show the screen on. This is equivalent to the `onlayer` clause of the  statement.

\_zorder

The zorder to show the screen on. If not specified, defaults to the zorder associated with the screen. If that's not specified, it is 0 by default.

\_tag

The tag to show the screen with. If not specified, defaults to the tag associated with the screen. If that's not specified, defaults to the name of the screen.

This is equivalent to the `as` clause of the  statement.

\_widget\_properties

A map from the id of a widget to a property name -> property value dictionary. When a widget with that id is shown by the screen, the specified properties are added to it.

\_transient

If true, the screen will be automatically hidden at the end of the current interaction.

Non-keyword arguments, and keyword arguments that do not begin with an underscore, are passed to the screen.

renpy.start\_predict\_screen(_\_screen\_name_, _\*args_, _\*\*kwargs_)

Causes Ren'Py to start predicting the screen named \_screen\_name with the given arguments. This replaces any previous prediction of \_screen\_name. To stop predicting a screen, call .

Prediction will occur during normal gameplay. To wait for prediction to complete, use the predict argument to .

renpy.stop\_predict\_screen(_name_)

Causes Ren'Py to stop predicting the screen named name.

renpy.variant(_name_)

Returns true if name is a screen variant that corresponds to the context in which Ren'Py is currently executing. See  for more details. This function can be used as the condition in an if statement to switch behavior based on the selected screen variant.

name can also be a list of variants, in which case this function returns True if any of the variants would.

_class_ ui.adjustment(_range\=1_, _value\=0_, _step\=None_, _page\=None_, _changed\=None_, _adjustable\=None_, _ranged\=None_, _force\_step\=False_, _raw\_changed\=None_)

Adjustment objects represent a value that can be adjusted by a bar or viewport. They contain information about the value, the range of the value, and how to adjust the value in small steps and large pages.

The following parameters correspond to fields or properties on the adjustment object:

range

The range of the adjustment, a number.

value

The value of the adjustment, a number.

step

The step size of the adjustment, a number. If None, then defaults to 1/10th of a page, if set. Otherwise, defaults to the 1/20th of the range.

This is used when scrolling a viewport with the mouse wheel.

page

The page size of the adjustment. If None, this is set automatically by a viewport. If never set, defaults to 1/10th of the range.

It's can be used when clicking on a scrollbar.

The following parameters control the behavior of the adjustment.

adjustable

If True, this adjustment can be changed by a bar. If False, it can't.

It defaults to being adjustable if a changed function is given or if the adjustment is associated with a viewport, and not adjustable otherwise.

changed

This function is called with the new value when the value of the adjustment changes.

raw\_changed

This function is called when the value of the adjustment changes. Unlike changed, this function is called with the raw value, which may be out of range. It's called with two arguments, the adjustment and the new value.

ranged

This function is called with the adjustment object when the range of the adjustment is set by a viewport.

This function may be called multiple times, as part of the layout process.

force\_step

If True and this adjustment changes by dragging associated viewport or a bar, value will be changed only if the drag reached next step. If "release" and this adjustment changes by dragging associated viewport or a bar, after the release, value will be rounded to the nearest step. If False, this adjustment will changes by dragging, ignoring the step value.

change(_value_)

Changes the value of the adjustment to value, updating any bars and viewports that use the adjustment.

ui.interact(_\*_, _roll\_forward\=None_, _mouse\='default'_)

Causes an interaction with the user, and returns the result of that interaction. This causes Ren'Py to redraw the screen and begin processing input events. When a displayable returns a value in response to an event, that value is returned from ui.interact, and the interaction ends.

This function is rarely called directly. It is usually called by other parts of Ren'Py, including the say statement, menu statement, with statement, pause statement, call screen, , among many other functions. However, it can be called directly if necessary.

When an interaction ends, the transient layer and all screens shown with \_transient as true are cleared from the scene lists.

The following arguments are documented. As other, undocumented arguments exist for Ren'Py's internal use, please pass all arguments as keyword arguments.

roll\_forward

The information that will be returned by this function when a roll forward occurs. (If None, the roll forward is ignored.) This should usually be passed the result of the  function.

mouse

The style of mouse cursor to use during this function.

## Actions

Many of the displayables created in the screen language take actions as arguments. An action is one of three things:

*   A callable Python object (like a function or bound method) that takes no arguments.
    
*   An object of a class that inherits from the Action class.
    
*   A list of other Actions.
    

The advantage to inheriting from the Action class is that it allows you to override the methods that determine when a button should be sensitive, and when it is selected.

_class_ Action

To define a new action, inherit from this class. Override the methods in this class to change the behavior of the action.

\_\_call\_\_(_self_)

This is the method that is called when the action is activated. In many cases, returning a non-None value from the action will cause the current interaction to end.

This method must be overridden, as the default method will raise a NotImplementedError (and hence cause Ren'Py to report an error).

get\_sensitive(_self_)

This is called to determine if the button with this action should be sensitive. It should return true if the button is sensitive.

Note that \_\_call\_\_ can be called, even if this returns False.

The default implementation returns True.

get\_selected(_self_)

This should return true if the button should be rendered as a selected button, and false otherwise.

The default implemention returns False.

get\_tooltip(_self_)

This gets a default tooltip for this button, if a specific tooltip is not assigned. It should return the tooltip value, or None if a tooltip is not known.

This defaults to returning None.

periodic(_self_, _st_)

This method is called once at the start of each interaction, and then is called periodically thereafter. If it returns a number, it will be called before that many seconds elapse, but it might be called sooner.

The main use of this is to call  if the value of get\_selected or get\_sensitive should change.

It takes one argument:

st

The number of seconds since the screen or displayable this action is associated with was first shown.

unhovered(_self_)

When the action is used as the hovered parameter to a button (or similar object), this method is called when the object loses focus.

alt

The text-to-speech text used for buttons that use this Action, if the button does not have the  property set. This can set to a string in the class, or in the constructor, or it can be a Python property that returns a string.

To run an action from Python, use .

renpy.is\_selected(_action_)

Returns a true value if the provided action or list of actions indicates it is selected, and false otherwise.

renpy.is\_sensitive(_action_)

Returns a true value if the provided action or list of actions indicates it is sensitive, and false otherwise.

renpy.run(_action_)

Run an action or list of actions. A single action is called with no arguments, a list of actions is run in order using this function, and None is ignored.

Returns the result of the last action to return a value.

## BarValues

When creating a bar, vbar, or hotbar, a BarValue object can be supplied as the value property. Methods on the BarValue object are called to get the adjustment and styles.

_class_ BarValue

To define a new BarValue, inherit from this class and override some of the methods.

get\_adjustment(_self_)

This method is called to get an adjustment object for the bar. It should create the adjustment with , and then return the object created this way.

This method must be overridden, as the default method will raise NotImplementedError (and hence cause Ren'Py to report an error).

get\_style(_self_)

This is used to determine the style of bars that use this value. It should return a tuple of two style names or style objects. The first is used for a bar, and the second for vbar.

This defaults to ("bar", "vbar").

get\_tooltip(_self_)

This gets a default tooltip for this button, if a specific tooltip is not assigned. It should return the tooltip value, or None if a tooltip is not known.

This defaults to returning None.

replaces(_self_, _other_)

This is called when a BarValue replaces another BarValue, such as when a screen is updated. It can be used to update this BarValue from the other. It is called before get\_adjustment.

Note that other is not necessarily the same type as self.

periodic(_self_, _st_)

This method is called once at the start of each interaction. If it returns a number of seconds, it will be called before that many seconds elapse, but it might be called sooner. It is called after get\_adjustment.

It can be used to update the value of the bar over time, like  does. To do this, get\_adjustment should store the adjustment, and periodic should call the adjustment's changed method.

alt

The text-to-speech text used for bars that use this BarValue, if the bar does not have the  property set. This can set to a string in the class, or in the constructor, or it can be a Python property that returns a string.

## InputValue

When creating an input, an InputValue object can be supplied as the value property. Methods on the InputValue object are called to get and set the text, determine if the input is editable, and handle the enter key being pressed.

_class_ InputValue

To define a new InputValue, inherit from this class, override some or all of the methods, and set the value of the default field.

editable

If not true, disables the input field from being editable at all.

default

If true, the input is eligible to be editable by default. (That is, it may be given the caret when the screen is shown.)

get\_text(_self_)

Returns the default text of the input. This must be implemented.

set\_text(_self_, _s_)

Called when the text of the input is changed, with the new text. This must be implemented.

enter(_self_)

Called when the user presses enter. If this returns a non-None value, that value is returned from the interacton. This may also raise  to ignore the press. Otherwise, the enter-press is propagated to other displayables.

The following actions are available as methods on InputValue:

Enable()

Returns an action that enables text editing on the input.

Disable()

Returns an action that disables text editing on the input.

Toggle()

Returns an action that toggles text editing on the input.

## Creator-Defined Screen Language Statements

Ren'Py supports defining custom screen language statements. Creator-defined screen language statements are wrappers for the screen language . Positional arguments remain positional arguments, properties become keyword arguments, and if the statement takes a block, so does the use statement. For example, the custom screen language statement:

titledwindow "Test Window":
    icon "icon.png"

    text "This is a test."

becomes:

use titledwindow("Test Window", icon\="icon.png"):
    text "This is a test."

Creator-defined screen language statements must be registered in a `python early` block. What's more, the filename containing the creator-defined statement must be be loaded earlier than any file that uses it. Since Ren'Py loads files in the Unicode sort order of their paths, it generally makes sense to prefix the name of any file registering a user-defined statement with 01, or some other small number.

Creator-defined screen language statements are registered with the renpy.register\_sl\_statement function:

_class_ renpy.register\_sl\_displayable(_name_, _displayable_, _style_, _nchildren\=0_, _scope\=False_, _\*_, _replaces\=False_, _default\_keywords\={}_, _default\_properties\=True_, _unique\=False_)

Registers a screen language statement that creates a displayable.

name

The name of the screen language statement, a string containing a Ren'Py keyword. This keyword is used to introduce the new statement.

displayable

This is a function that, when called, returns a displayable object. All position arguments, properties, and style properties are passed as arguments to this function. Other keyword arguments are also given to this function, a described below.

This must return a Displayable. If it returns multiple displayables, the \_main attribute of the outermost displayable should be set to the "main" displayable - the one that children should be added to.

style

The base name of the style of this displayable. If the style property is not given, this will have the style prefix added to it. The computed style is passed to the displayable function as the `style` keyword argument.

nchildren

The number of children of this displayable. One of:

0

The displayable takes no children.

1

The displayable takes 1 child. If more than one child is given, the children are placed in a Fixed.

"many"

The displayable takes more than one child.

unique

This should be set to true if the function returns a displayable with no other references to it.

The following arguments should be passed in using keyword arguments:

replaces

If true, and the displayable replaces a prior displayable, that displayable is passed as a parameter to the new displayable.

default\_keywords

The default set of keyword arguments to supply to the displayable.

default\_properties

If true, the ui and position properties are added by default.

Returns an object that can have positional arguments and properties added to it by calling the following methods. Each of these methods returns the object it is called on, allowing methods to be chained together.

add\_positional(_name_)

Adds a positional argument with name

add\_property(_name_)

Adds a property with name. Properties are passed as keyword arguments.

add\_style\_property(_name_)

Adds a family of properties, ending with name and prefixed with the various style property prefixes. For example, if called with ("size"), this will define size, idle\_size, hover\_size, etc.

add\_prefix\_style\_property(_prefix_, _name_)

Adds a family of properties with names consisting of prefix, a style property prefix, and name. For example, if called with a prefix of text\_ and a name of size, this will create text\_size, text\_idle\_size, text\_hover\_size, etc.

add\_property\_group(_group_, _prefix\=''_)

Adds a group of properties, prefixed with prefix. Group may be one of the strings:

*   "bar"
    
*   "box"
    
*   "button"
    
*   "position"
    
*   "text"
    
*   "window"
    

These correspond to groups of . Group can also be "ui", in which case it adds the .

copy\_properties(_name_)

Adds all styles and positional/keyword arguments that can be passed to the name screen statement.

_class_ renpy.register\_sl\_statement(_name_, _children\='many'_, _screen\=None_)

Registers a custom screen language statement with Ren'Py.

name

This must be a word. It's the name of the custom screen language statement.

children

The number of children this custom statement takes. This should be 0, 1, or "many", which means zero or more.

screen

The screen to use. If not given, defaults to name.

Returns an object that can have positional arguments and properties added to it. This object has the same .add\_ methods as the objects returned by .

As an example of a creator-defined screen language statement, here's an implementation of the `titledwindow` statement given above. First, the statement must be registered in a `python early` block in a file that is loaded early – a name like 01custom.rpy will often load soon enough. The registration call looks like:

python early:
    renpy.register\_sl\_statement("titledwindow", children\=1).add\_positional("title").add\_property("icon").add\_property("pos")

Then, we define a screen that implements the custom statement. This screen can be defined in any file. One such screen is:

screen titledwindow(title, icon\=None, pos\=(0, 0)):
    drag:
        pos pos

        frame:
            background "#00000080"

            has vbox

            hbox:
                if icon is not None:
                    add icon

                text title

            null height 15

            transclude

When are used large property groups like a add\_property\_group, it makes sense to use the \*\*properties syntax with a properties keyword in some place. For example:

screen titledwindow(title, icon\=None, \*\*properties):
    frame:
        \# When background not in properties it will use it as default value.
        background "#00000080"

        properties properties

        has vbox

        hbox:
            if icon is not None:
                add icon

            text title

        null height 15

        transclude
