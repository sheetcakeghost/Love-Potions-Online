# Screen Language Optimization

Ren'Py uses a number of techniques to optimize screen language speed. When using Ren'Py to create complex interfaces, such as those used by simulation games, it may help to understand how screen language works so you can achieve maximal performance.

This guide is applicable to the second implementation of screen language, which was added to Ren'Py 6.18. If your game was created in Ren'Py 6.17 or earlier, it may be necessary to choose the "Force Recompile" option in the launcher to ensure its screens are upgraded to the latest version.

This guide isn't a substitute for good programming practice. If a screen uses nested loops to do a lot of unproductive work, it will be slower than a screen that avoids such looping. While understanding the techniques in this guide is important, avoiding work entirely is always better than letting Ren'Py optimize the work for you.

## Parameter List

For best performance, all screens should be defined with a parameter list. When a screen doesn't take parameters, it should be defined with an empty parameter list. The screen:

screen test():
    vbox:
        for i in range(10):
            text "\[i\]"

is faster than:

screen test:
    vbox:
        for i in range(10):
            text "\[i\]"

When a screen is defined without a parameter list, any name used in that screen can be redefined when the screen is shown. This requires Ren'Py to be more conservative when analyzing the screen, which can limit the optimization it performs.

## Prediction

Screens perform better when they're predicted in advance. That's because Ren'Py will execute the screen during prediction time, and load in images that are used by the screen.

There are two ways Ren'Py automatically predicts screens:

*   Ren'Py will predict screens shown by the `show screen` and `call screen` statements.
    
*   Ren'Py will predict screens that will be shown by the  and  actions.
    

If screens are shown from Python, it's a good idea to start predicting the screen before it is shown. To start predicting a screen, use the  function. To stop predicting a screen, use the  function.

## Displayable Reuse

When evaluating a screen language statement that creates a displayable, Ren'Py will check to see if the positional arguments and properties given to that displayable are equal to the positional arguments and properties given the last time that statement was evaluated. If they are, instead of making a new displayable, Ren'Py will reuse the existing displayable.

Displayable reuse has a number of performance implications. It saves the cost of creating a new displayable, which may be significant for displayables that contain a lot of internal states. More importantly, reusing a displayable means that in many cases, Ren'Py will not need to re-render the displayable before showing it to the user, which can lead to another significant speedup.

To compare positional arguments and properties, Ren'Py uses the notion of equality embodied by Python's == operator. We've extended this notion of equality to actions by deciding two actions should be equal when they are indistinguishable from each other – when it doesn't matter which action is invoked, or which action is queried to determine sensitivity or selectedness.

All actions provided with Ren'Py conform to this definition. When defining your own actions, it makes sense to provide them with this notion of equality. This can be done by supplying an appropriate `__eq__` method. For example:

class TargetShip(Action):
    def \_\_init\_\_(self, ship):
        self.ship \= ship

    def \_\_eq\_\_(self, other):
        if not isinstance(other, TargetShip):
            return False

        return self.ship is other.ship

    def \_\_call\_\_(self):
        global target
        target \= self.ship

It's important to define the `__eq__` function carefully, making sure it compares all fields, and uses equality (==) and identity (is) comparison as appropriate.

## Const Expressions and Pure Functions

Ren'Py can exploit the properties of const variables and pure functions to improve the speed of screen evaluation, and to entirely avoid the evaluation of some parts of screens.

### Definitions

An expression is **const** (short for constant) if it always represents the same value when it is evaluated. For Ren'Py's purposes, an expression is const if and only if the following expressions always evaluate to the same const value or are undefined:

*   Applying any unary, binary, or ternary operator to the expression, provided the other operands are also const.
    
*   Accessing a field on the expression.
    
*   Indexing the expression, either using a number or an object.
    

Python numbers and strings are const, as are list, tuple, set, and dict literals for which all components are const. Ren'Py marks variables defined using the `define` statement as const. The  and  functions can be used to further control what Ren'Py considers to be const. The default list of const names is given in the  section below.

If you have a variable that will never change, it makes sense to use `define` to both define it and declare it const. For example:

define GRID\_WIDTH \= 20
define GRID\_HEIGHT \= 10

A callable function, class, or action is **pure** if, when all of its arguments are const values, it always gives the same const value. Alternatively, an expression that invokes a pure function with const expression is also a const expression.

A large number of default functions, classes, and actions are marked as pure. These functions are listed in the  section below.

Functions are declared pure using the  function, which can be used as a decorator for functions declared in the default store.

Const expressions and pure functions do not need to retain the same value across the following events:

*   The end of the init phase.
    
*   A change of the language.
    
*   A style rebuild.
    

### How Const Optimizes Screen Language

There are three advantages to ensuring that screen language arguments and properties are const.

The first is that const arguments and properties are evaluated when screens are prepared, which is at the end of the init phase, when the language is changed, or when styles are rebuilt. After that, it is no longer necessary to spend time evaluating const arguments and properties.

The second is that const works well with displayable reuse. When all of the arguments and properties of a displayable are const, the displayable can always be reused, which gains all the benefits of displayable reuse.

Lastly, when Ren'Py encounters a tree of displayables such that all arguments, properties, and expressions affecting control flow are also const, Ren'Py will reuse the entire tree without evaluating expressions or creating displayables. This can yield a significant performance boost.

For example, the following screen does not execute any Python or create any displayables after the first time it is predicted or shown:

screen mood\_picker():
    hbox:
        xalign 1.0
        yalign 0.0

        textbutton "Happy" action SetVariable("mood", "happy")
        textbutton "Sad" action SetVariable("mood", "sad")
        textbutton "Angry" action SetVariable("mood", "angry")

### Const Text

When defining text, please note that strings containing new-style text substitutions are const:

$ t \= "Hello, world."
text "\[t\]"

Supplying a variable containing the text directly is generally not const:

$ t \= "Hello, world."
text t

Neither is using percent-substitution:

$ t \= "Hello, world."
text "%s" % t

Lastly, note that the \_ text translation function is pure, so if it contains a string, the entire expression is const:

text \_("Your score is: \[score\]")

If a variable containing the text contains substitution, it's necessary to use the `!i` conversion flag:

$ who \= "Jane"
$ t \= "Hello, \[who\]!"
text 'Then I told her, "\[t!i\]"'

### Const Functions

renpy.const(_name_)

Declares a variable in the store to be constant.

A variable is constant if nothing can change its value, or any value reached by indexing it or accessing its attributes. Variables must remain constant out of define, init, and translate python blocks.

name

A string giving the name of the variable to declare constant.

renpy.not\_const(_name_)

Declares a name in the store to be not constant.

This undoes the effect of calls to  and .

name

The name to declare not constant.

renpy.pure(_fn_)

Declares a function as pure. A pure function must always return the same value when it is called with the same arguments, outside of define, init, and translate python blocks.

fn

The name of the function to declare pure. This may either be a string containing the name of the function, or the function itself. If a string is passed and the function is inside a module, this string should contain the module name with the dot.

Returns fn, allowing this function to be used as a decorator.

## Profiling

Ren'Py supports profiling screen execution through the `renpy.profile_screen` function:

_class_ renpy.profile\_screen(_name_, _predict\=False_, _show\=False_, _update\=False_, _request\=False_, _time\=False_, _debug\=False_, _const\=False_)

Requests screen profiling for the screen named name, which must be a string.

Apart from name, all arguments must be supplied as keyword arguments. This function takes three groups of arguments.

The first group of arguments determines when profiling occurs.

predict

If true, profiling occurs when the screen is being predicted.

show

If true, profiling occurs when the screen is first shown.

update

If true, profiling occurs when the screen is updated.

request

If true, profiling occurs when requested by pressing F8.

The second group of arguments controls what profiling output is produced when profiling occurs.

time

If true, Ren'Py will log the amount of time it takes to evaluate the screen.

debug

If true, Ren'Py will log information as to how screens are evaluated, including:

*   Which displayables Ren'Py considers constant.
    
*   Which arguments, if any, needed to be evaluated.
    
*   Which displayables were reused.
    

Producing and saving this debug information takes a noticeable amount of time, and so the time output should not be considered reliable if debug is set.

The last group of arguments controls what output is produced once per Ren'Py run.

const

Displays the variables in the screen that are marked as const and not-const.

All profiling output will be logged to profile\_screen.txt in the game directory.

## Const Names

The following names are const by default.

*   False
    
*   None
    
*   True
    
*   `config`
    
*   
    

## Pure Names

The following names are both pure and const by default.

*   ADVCharacter
    
*   ADVSpeaker
    
*   
    
*   Alpha
    
*   
    
*   
    
*   
    
*   
    
*   Animation
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   DynamicCharacter
    
*   
    
*   
    
*   
    
*   
    
*   FactorZoom
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   ImageReference
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   LiveComposite
    
*   LiveCrop
    
*   LiveTile
    
*   
    
*   
    
*   Motion
    
*   
    
*   Move
    
*   MoveFactory
    
*   MoveIn
    
*   MoveOut
    
*   
    
*   
    
*   
    
*   NVLCharacter
    
*   
    
*   
    
*   
    
*   OldMoveTransition
    
*   
    
*   
    
*   Pan
    
*   
    
*   Particles
    
*   
    
*   
    
*   
    
*   Play
    
*   
    
*   Position
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   Revolve
    
*   RevolveInOut
    
*   
    
*   
    
*   RotoZoom
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   SizeZoom
    
*   
    
*   
    
*   
    
*   Speaker
    
*   
    
*   
    
*   Stop
    
*   
    
*   SubTransition
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   Viewport
    
*   
    
*   Window
    
*   Zoom
    
*   ZoomInOut
    
*   
    
*   \_CharacterVolumeValue
    
*   \_DisplayReset
    
*   \_InputValueAction
    
*   \_TouchKeyboardBackspace
    
*   \_TouchKeyboardReturn
    
*   \_TouchKeyboardTextInput
    
*   \_\_renpy\_\_dict\_\_
    
*   \_\_renpy\_\_list\_\_
    
*   \_\_renpy\_\_set\_\_
    
*   \_m1\_00gallery\_\_GalleryAction
    
*   \_m1\_00gallery\_\_GalleryToggleSlideshow
    
*   \_m1\_00musicroom\_\_MusicRoomPlay
    
*   \_m1\_00musicroom\_\_MusicRoomRandomPlay
    
*   \_m1\_00musicroom\_\_MusicRoomStop
    
*   \_m1\_00musicroom\_\_MusicRoomTogglePause
    
*   \_m1\_00musicroom\_\_MusicRoomTogglePlay
    
*   \_m1\_00preferences\_\_DisplayAction
    
*   \_m1\_00preferences\_\_ResetPreferences
    
*   \_movebottom
    
*   \_moveleft
    
*   \_moveright
    
*   \_movetop
    
*   \_notify\_transform
    
*   
    
*   \_touch\_keyboard
    
*   abs
    
*   
    
*   all
    
*   any
    
*   ascii
    
*   bin
    
*   
    
*   bool
    
*   bytes
    
*   callable
    
*   chr
    
*   color
    
*   complex
    
*   dict
    
*   dir
    
*   dissolve
    
*   divmod
    
*   enumerate
    
*   
    
*   filter
    
*   float
    
*   format
    
*   frozenset
    
*   getattr
    
*   
    
*   
    
*   
    
*   hasattr
    
*   hash
    
*   hex
    
*   
    
*   int
    
*   
    
*   irisout
    
*   isinstance
    
*   issubclass
    
*   len
    
*   list
    
*   map
    
*   max
    
*   min
    
*   oct
    
*   ord
    
*   
    
*   
    
*   pow
    
*   pushdown
    
*   pushleft
    
*   
    
*   pushup
    
*   range
    
*   renpy.Keymap
    
*   renpy.ParameterizedText
    
*   
    
*   renpy.curried\_call\_in\_new\_context
    
*   renpy.curried\_invoke\_in\_new\_context
    
*   renpy.curry
    
*   renpy.easy\_displayable
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   renpy.has\_screen
    
*   renpy.image\_exists
    
*   
    
*   
    
*   
    
*   
    
*   renpy.munged\_filename
    
*   renpy.partial
    
*   
    
*   renpy.unelide\_filename
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   
    
*   repr
    
*   reversed
    
*   round
    
*   set
    
*   slice
    
*   slideawaydown
    
*   
    
*   slideawayright
    
*   slideawayup
    
*   slidedown
    
*   
    
*   slideright
    
*   slideup
    
*   sorted
    
*   
    
*   str
    
*   sum
    
*   tuple
    
*   type
    
*   ui.callsinnewcontext
    
*   ui.gamemenus
    
*   ui.invokesinnewcontext
    
*   ui.jumps
    
*   ui.jumpsoutofcontext
    
*   ui.returns
    
*   
    
*   
    
*   wipedown
    
*   
    
*   wiperight
    
*   wipeup
    
*   zip
    
*   
    
*   
    
*   
    
