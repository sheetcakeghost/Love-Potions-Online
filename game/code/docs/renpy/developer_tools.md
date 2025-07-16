# Developer Tools

Ren'Py includes a number of features to make a developer's life easier. Many of them need the variable  to be set to True to operate.

## Lint

The Lint tool (available from the launcher) checks the game for potential errors or misoptimizations, and advises the developing team about how to best improve it. Since some of these errors will only affect users on other platforms, it’s recommended to understand and fix all errors, even if the problem can't be triggered locally.

Lint also includes useful infos and stats about the game.

Note that using Lint is not a substitute for thorough testing.

## Shift+O Console

The debug console makes it possible to interactively run Ren'Py script and Python statements, and immediately see the results. The console is available in developer mode or when  is True, and can be accessed by pressing Shift+O.

The console can be used to:

*   Jump to a label.
    
*   Interactively try out Ren'Py script statements.
    
*   Evaluate a Python expression or statement to see the result.
    
*   Trace Python expressions as the game progresses.
    

commands:

*   clear: clear the console history
    
*   escape: Enables escaping of unicode symbols in unicode strings.
    
*   exit: exit the console
    
*   help: show this help
    
*   help <expr>: show signature and documentation of <expr>
    
*   jump <label>: jumps to label
    
*   load <slot>: loads the game from slot
    
*   long: Print the full representation of objects on the console.
    
*   reload: reloads the game, refreshing the scripts
    
*   save <slot>: saves the game in slot
    
*   short: Shorten the representation of objects on the console (default).
    
*   stack: print the return stack
    
*   unescape: Disables escaping of unicode symbols in unicode strings and print it as is (default).
    
*   unwatch <expression>: stop watching an expression
    
*   unwatchall: stop watching all expressions
    
*   watch <expression>: watch a python expression
    
*   watch short: makes the representation of traced expressions short (default)
    
*   watch long: makes the representation of traced expressions as is
    
*   <renpy script statement>: run the statement
    
*   <python expression or statement>: run the expression or statement
    

## Shift+E Editor Support

Shift+E opens the default text editor, as set in the launcher and customizable using , to open the script file in and line number at which the current statement is written.

## Shift+D Developer Menu

When  is true, hitting Shift+D will display a developer menu that provides easy access to some of the features given below.

## Shift+R Reloading

When  is True, hitting Shift+R will save the current game, reload the game script, and reload the game. This will often place you at the last unchanged statement encountered before Shift+R was pressed.

After the first reload, the game will be in autoreload mode, and any changes to files accessed since the last reload will cause the game to be reloaded again.

This allows the developer to make script changes with an external editor, and not have to exit and restart Ren'Py to see the effect of the changes.

Note that game state, which includes variable values and scene lists, is preserved across the reload. This means that if one of those statements is changed, it is necessary to rollback and re-execute the statement to see its new effect.

Shift+R reloading does not work in a replay.

The following functions implement the same behavior in pure python. Note that they are only meant to be used in developer mode.

renpy.get\_autoreload()

Gets the autoreload flag.

renpy.reload\_script()

Causes Ren'Py to save the game, reload the script, and then load the save.

This should only be called during development. It works on Windows, macOS, and Linux, but may not work on other platforms.

renpy.set\_autoreload(_autoreload_)

Sets the autoreload flag, which determines if the game will be automatically reloaded after file changes. Autoreload will not be fully enabled until the game is reloaded with .

## Shift+I Style Inspecting

When  is true, pressing Shift+I will cause style inspection to occur. This will display a list of displayables underneath the mouse, in the order they are drawn to the screen (that is, the last displayable is the one on top of the others). For each displayable, it will display the type, the style used, and the size it is being rendered at.

Clicking on the style name will display the styles the displayable inherits from, and the properties each style contributes to the final displayable.

## \> Fast Skipping

When  or  is True, pressing the fast\_skip key (by default, ">") causes the game to immediately skip to the next important interaction. For this purpose, an important interaction is one that is not caused by a say statement, transition, or pause command. Usually, this means skipping to the next menu, but it will also stop when user-defined forms of interaction occur.

## Warping to a Line

Ren'Py supports warping to a line in the script, without the developer to play through the entire game to get there. While this warping technique has a number of warnings associated with it, it still may be useful in providing a live preview.

To invoke warping, run Ren'Py with the `--warp` command-line argument followed by a filename:line combination, to specify where you would like to warp to. For example:

renpy.exe my\_project \--warp script.rpy:458

(Where my\_project is the full path to the base directory of your project.)

When warping is invoked, Ren'Py does a number of things. It first finds all of the scene statements in the program. It then tries to find a path from the scene statements to every reachable statement in the game. It then picks the reachable statement closest to, but before or at, the given line. It works backwards from that statement to a scene statement, recording the path it took. Ren'Py then executes the scene statement and any show or hide statements found along that path. Finally, it transfers control to the found statement.

There are a number of fairly major caveats to the warp feature. The first is that it only examines a single path, which means that while the path may be representative of some route of execution, it's possible that there may be a bug along some other route. In general, the path doesn't consider game logic, so it's also possible to have a path that isn't actually reachable. (This is only really a problem on control-heavy games, especially those that use a lot of Python.

The biggest problem, though, is that Python is not executed before the statement that is warped to. This means that all variables will be uninitialized, which can lead to crashes when they are used. To overcome this, one can define a label `after_warp`, which is called after a warp but before the warped-to statement executes. This label can set up variables in the program, and then return to the preview.

The warp feature requires  to be True to operate.

## Debug Functions

renpy.get\_filename\_line()

Returns a pair giving the filename and line number of the current statement.

renpy.log(_msg_)

If  is not set, this does nothing. Otherwise, it opens the logfile (if not already open), formats the message to  columns, and prints it to the logfile.

renpy.unwatch(_expr_)

Stops watching the given Python expression.

renpy.warp\_to\_line(_warp\_spec_)

This takes as an argument a filename:linenumber pair, and tries to warp to the statement before that line number.

This works samely as the \--warp command.

renpy.watch(_expr_)

This watches the given Python expression, by displaying it in the upper-right corner of the screen.
