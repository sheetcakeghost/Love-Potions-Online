# Incompatible Changes

This is a list of changes that may require intervention in the form of changes to scripts or your development environment. Our intent is that all other changes should not affect existing scripts.

Note that setting  will cause many of these changes to be reverted, at the cost of losing access to recent features.

Incompatible changes to the GUI are documented at , as such changes only take effect when the GUI is regenerated.

## Pending Deprecations

Ren'Py 7.8 is the last release to support Python 2.

Ren'Py 8.4 will drop support for the original OpenGL renderer (gl1), and for Windows 7, 8, and 8.1.

## 8.3.4 / 7.8.4

**Dissolving Different-Sized Displayables, part two.** When ImageDissolving or AlphaDissolving between displayables of different sizes, Ren'Py will give the result the size of the largest displayable, in each access. To revert to the pre-8.1.2 behavior (the smallest size on each axis), add to your game:

define config.dissolve\_shrinks \= True

**Removal of the ATL 'update' event.** Previous versions of Ren'Py could deliver and "update" event to ATL inside screens when the screen was changed in major ways, such as when changing translations. This event was not delivered reliably, and is unlikely to have been used, so it has been removed.

## 8.3.0 / 7.8.0

**Box\_reverse and Box\_align** The  property now no longer adjusts the box alignment. To adjust the box alignment, set the  property to 1.0, or use:

> define config.box\_reverse\_align = true

To get the 8.2 behavior.

**Retained speech bubbles** are now automatically cleared away when other say, menu, or call screen statements are invoked. This is controlled by the  variable.

To disable this, add to your game:

define bubble.clear\_retain\_statements \= \[ \]

**How ATL sets the child from parameters** The rules as for how and when ATL transforms get their child set, based upon the parameters they accept and the arguments they are passed, has slightly changed. It is unlikely to have any impact on existing games, especially if you were only using documented features.

*   The old\_widget parameter taking a value from a positional argument does not set the child anymore. That was an undocumented misuse of .
    
    transform t(old\_widget):
        ...
    
    t("eileen") \# will no longer have a child set to the "eileen" image
    
*   A child keyword argument being passed to a transform having a child parameter now sets the child, just as it would in a transform with no child parameter, or if the child parameter got a value from a positional argument. The documentation was ambiguous about this.
    
    transform t1(child):
        ...
    
    transform t2(delay\=1.0):
        ...
    
    t1(child\="eileen happy") \# will now have a child set to the "eileen happy" image, but previously didn't.
    t2(child\="eileen happy") \# the child is set, as before.
    t1("eileen happy")       \# the child is set, as before.
    

**Character Callbacks** have been changed to take a large number of additional arguments, as documented at . This should not require changes as character callbacks should have been written to ignore unknown keyword arguments, but if not the character callbacks may need to be updated.

**Window Statement** The `window show` annd `window hide` statements no longer disable the `window auto` flag. If you'd like to do this, then either use the new `window auto False` statement, or change your game to include:

define config.window\_functions\_set\_auto \= True

When a `window show` occurs after `window hide`, Ren'Py will look forward to the next say statement to determine the type of thr window to show. Previously, it looked back to the last say statement. To revert this change, include:

define config.window\_next \= False

**String Munging** Munging of names beginning with \_\_ but not containing a second instance of \_\_ will now occur inside a string just like it does in the rest of a script. What this means is that:

> $ \_\_foo = 1 "Add one and \_\_foo and you get \[1 + \_\_foo\]."

will be rewritten to:

> $ \_m1\_script\_\_foo = 1 "Add one and \_m1\_script\_\_foo and you get \[1 + \_m1\_script\_\_foo\]."

To disable this, in a file named 01nomunge.rpy in your game directory, write:

define config.munge\_in\_strings \= False

**Cropping Outside the Bounds of a Displayable** The behavior of cropping a displayable with a box larger than the displayable has changed. As of this release, values passed to , ,  and  are not bound by the original boundaries of the displayable.

In 8.2.x and 7.7.x releases of Ren'Py, the behavior was to crop the right/bottom of the displayable, but unconstrain the left/top. This behavior can be restored by adding to your game:

define config.limit\_transform\_crop \= True

Before 8.2 and 7.7, the behavior was to crop the right/bottom of the displayable if the value was a float, and leave left/top unconstrained. This behavior can be restored by adding to your game:

define config.limit\_transform\_crop \= "only\_float"

## 8.2.2 / 7.7.2

**Fill and Frames** In certain cases in 8.2.1 and earlier, the  and  style properties could cause Frames, Windows, and Buttons to shrink in size. Now, only expansion in size is allowed. To revert this, add:

define config.fill\_shrinks\_frame \= True

## 8.2.1 / 7.7.1

**\*Vertical Text** Vertical text had been improved in the harfbuzz shaper, with the text now being rendered in the correct place. This may cause position changes, but since the previous version was wildly incorrect, no compatibility define is provided.

## 8.2.0 / 7.7.0

**Stringified annotations and the aborted future of PEP 563** Since Ren'Py version 8.0.2, Python code in Ren'Py 8 was always compiled using the `from __future__ import annotations` directive, with no possible opt-out for creators.

Given that this change will most likely not be implemented by default in future versions of Python, we rolled that change back.

In order to keep using the `annotations` future for stringified annotations, you can add the following line at the top of your files:

rpy python annotations

**Text Changes** Ren'Py uses harfbuzz for shaping, which may produce different glyphs than would have been produced differently, and may change the spacing of text. The positioning of vertical text has also been changed by harfbuzz rendering.

To revert this changes, include in your game:

style default:
    shaper "freetype"

Ren'Py will automatically use an Emoji font when required. To disable this, add:

style default:
    emoji\_font None

**Interpolation Changes** Interpolations in strings are now treated as Python expressions, this results in mostly equivelent behaviour when interpreting fields except when item getters are in use. For example:

\# Previously
e "\[player\[money\]\]" #=> player\['money'\]
\# But now
e "\[player\[money\]\]" #=> player\[money\]

To revert this behaviour, add the following to your game:

define config.interpolate\_exprs \= False

To help other developers work while you're migrating your game to the new behavior, there is a fallback mode that will first try the new behavior, and then fall back to the old behavior if the new behavior fails. To enable this, add the following to your game:

define config.interpolate\_exprs \= "fallback"

**Polar Coordinate Changes** Ren'Py now enforces that the angles given to the  and  properties are in the range 0 to 360 degrees, inclusive of 0 but not of 360. Previously, angles outside this range gave undefined behavior, now the angles will be clamped to this range. A 360 degree change will no longer cause motion, but will instead be treated as a 0 degree change.

When animating  and  with ATL, if a direction is not supplied, the shortest arc will be used, even if it passes through 0.

There is not a compatibility define for these changes, as they are unlikely to affect the visible behavior of games in practice.

**Empty ATL Blocks Forbidden** Previously, Ren'Py would allow an empty ATL block. Now it will report that a block is required. You'll need to change:

show eileen happy:
"..."

to:

show eileen happy
"..."

In the unlikely case that you have an empty ATL block.

**Box Reverse** The  style property has changed its behavior in two ways:

*   Space is offered to displayables in the order the displayables are presented in the screen, where previously the space was offered in reverse order when  was enabled. This can change the sizes of some displayables.
    
*   A hbox that has  set will wrap from top to bottom, rather than bottom to top. A vbox with  set will wrap from left to right, rather than right to left.
    

The goal of these changes is to make the behavior of box\_reverse more useful for laying out interfaces in right-to-left languages. To revert these changes, add to your game:

define config.simple\_box\_reverse \= True

**build.itch\_channels** That variable was always documented as a dict but was mistakenly implemented as a list of tuples. It's now truly a dict. If you were using list operations on it, you'll need to change your code:

\# formerly
$ build.itch\_channels.append(("pattern", "channel"))
$ build.itch\_channels.extend(\[("pattern", "channel")\])
define build.itch\_channels += \[("pattern", "channel")\]

\# now
$ build.itch\_channels\["pattern"\] \= "channel"
$ build.itch\_channels.update({"pattern": "channel"})
define build.itch\_channels\["pattern"\] \= "channel"
define build.itch\_channels |= {"pattern": "channel"}

**New position type** The new  type has been added to the list of  types. As a result, it can be returned by the  function at any time, even in cases when it previously returned another type or if you don't use the new type anywhere in your game.

To prevent this, add to your game:

define config.mixed\_position \= False

**Drag Group Add Changes** Adding a displayable to a  now adds it above the other displayables in the group, rather than below them.

To change this, add to your game:

define config.drag\_group\_add\_top \= False

**Translate Statements and config.statement\_callbacks** Translate statements (including internal statements that Ren'Py automatically generates) will no longer cause  to be called.

**Transitions Use Child Placements** If the child of a transitions provides placement information, that will be used by the transition itself. This only makes sense when the transition is used by an ATL transition, and both the old and new children provide the same placement information.

To disable this, add to your game:

define config.transitions\_use\_child\_placement \= False

**Containers Pass Transform Events** Containers (including fixed, hbox, vbox, side, grid, viewport, and vpgrid) now pass some transform events (hover, idle, insensitive, selected\_hover, and selected\_idle) to their children, meaning that children of a button can have their own transforms to respond to those events.

To disable this, add to your game:

define config.containers\_pass\_transform\_events \= set()

**Say Screens Are Supplied the Replace Event.** Say screens are now supplied the "replace" (rather than "show") transform event for the second and subsequent pauses.

To disable this, add to your game:

define config.say\_replace\_event \= False

**Re-showing A Screen No Longer Cancels a Hide Event** Previously, if a screen was hidden and re-shown, a hide or replace transform event associated with the same screen would be cancelled, and the hiding or replaced screen would instantly disappear. Now, the event will be allowed to run to completion.

To disable this, add to your game:

define config.screens\_never\_cancel\_hide \= False

## 8.1.2 / 7.6.2

**Dissolving Different-Sized Displayables** When dissolving between two displayables of different sizes, Ren'Py will give the result the size of the largest displayable, in each access. To revert to the previous behavior (the smallest size on each axis), add to your game:

define config.dissolve\_shrinks \= True

## 8.1.1 / 7.6.1

**Android Key Migration** We've received reports of games uploaded to the Google Play as bundles having their APKs rejected for having different keys. This was caused by an old release of Ren'Py that used the APK key for bundles. In the Play Console, this produced an error message like:

You uploaded an APK that is not signed with the upload certificate. You must use
the same certificate. The upload certificate has fingerprint:

    SHA1: ...

and the certificate used to sign the APK you uploaded has fingerprint:

    SHA1: ...

While this can be cause by other problems (like simply using entirely incorrect keys), one potential fix is:

1.  In your project's base directory, rename `bundle.keystore` to `bundle.keystore.bak`.
    
2.  In your project's base directory, copy `android.keystore` to `bundle.keystore`.
    

Then rebuild and re-upload your bundle.

## 8.1.0 / 7.6.0

**Conflicting properties** The former default input screen, which may have found its way into your game, contains conflicting style properties. The fix for that is as follows:

+define config.check\_conflicting\_properties = True

 screen input(prompt):
     style\_prefix "input"
     window:

         vbox:
\-            xalign gui.dialogue\_text\_xalign
\+            xanchor gui.dialogue\_text\_xalign
             xpos gui.dialogue\_xpos
             xsize gui.dialogue\_width
             ypos gui.dialogue\_ypos
             text prompt style "input\_prompt"
             input id "input"

**Speech Bubbles** Adding bubble support to an existing game requires adding files and script to the game. The  documentation includes the required changes.

**Live2D** Ren'Py now requires Live2D Cubism 4 SDK for Native R6\_2 or later. It may refuse to run if an older version is used.

**Texture Memory** Ren'Py now accounts for texture memory more precisely. In general, games can raise  by 33%, and use the same amount of memory.

**Audio Fadeout** When audio is stopped or changed using `play`, there is now a default fadeout of 0.016 seconds, to prevent pops. This is controlled by the  variable. To disable the fadeout:

define config.fadeout\_audio \= 0.0

Fading is now logarithmic, which sounds smoother to the human ear as it matches the way ears perceive sound. To revert to the old linear fades:

define config.linear\_fades \= True

**Translate None** Ren'Py will now produce an error when encountering an explicit `translate None` statement that does not translate strings, styles, or python. These should be rare, in practice. The recommended change is to replace:

translate None start\_abcd1234:
    e "This is a test"

with:

e "This is a test" id start\_abcd1234

This change can also be reverted with:

define config.check\_translate\_none \= False

**Keymap** The  has changed substantially, which means that if your game changes the default keymap - usually a bad idea - it will need to be updated to reflect the new keysyms.

**File Search** Ren'Py will now only look for image files in game/images, rather than all files. To look for all files in game/images, use:

define config.search\_prefixes += \[ "images/" \]

The paths that are searched consider the purpose of the file, rather than the type or extensions. So `renpy.loadable("dlc.jpg")` won't look for game/images/dlc.jpg. If you'd like to find that file, write `renpy.loadable("images/dlc.jpg")`. If you'd like to search for a file that can be in either game/ or game/images, write `renpy.loadable("dlc.jpg", "images")`.

**Android** Android has been changed so that the `android.keystore` file and `bundle.keystore` file are expected to be found in the project's base directory, and not in the rapt directory. This allows projects to be built with different keys, and helps ensure the same keys are used with multiple Android versions.

If you'd like to use your own keys, configure your game, edit `android.json` to set update\_keystores to false, and then edit `local.properties` and `bundle.properties` in `rapt/project` to point to your own keystore files.

The android configuration file has been renamed from `.android.json` to `android.json`. Ren'Py will automatically create the new file if the old exists.

**Dialogue history** Dialogue is now present in the history list (and hence the history screen) during the statement in which the dialogue is shown. Previously, it was only present at the end of the statement. During the statement, the dialogue is shown with a kind of "current".

In rare cases, your game might have relied on the old behavior. If so, it can be disabled with:

define config.history\_current\_dialogue \= False

**Steam appid** When  is not set, Ren'Py will delete any existing `steam_appid.txt` file in the game directory. This is to prevent the wrong app id from being used.

**Sticky layers** This release introduces the concept of sticky layers which help automatically manage tags being placed on layers other than their default. In the rare case that a game requires multiple of the same tag, to be displayed at the same time, on different layers then this may not be desirable.

To disable sticky layers entirely, add to your game:

define config.sticky\_layers \= \[ \]

Alternatively, to prevent only specific layers from being sticky, update their definitions to include `sticky=False`:

init python:
    renpy.add\_layer("ptfe", sticky\=False)

**Lenticular bracket ruby text** This release of Ren'Py introduces lenticular bracket ruby text, an easier way of writing ruby text. If a game included a literal 【, it needs to be doubled, to "【【", to quote it properly. (This is only strictly necessary when the text is succeded by a full-width vertical bar, but works always.)

To disable lenticular bracket ruby text, add to your game:

define config.lenticular\_bracket\_ruby \= False

**Constant stores.** This release of Ren'Py introduces , and makes some of the built-in stores constant. Constant stores should not change outside of the init phase. The following stores are constant:

> \_errorhandling \_gamepad \_renpysteam \_warper audio achievement build director iap layeredimage updater

If your game changes a variable in one of these stores, outside of the init, the store can be set to non-constant with (for example):

define audio.\_constant \= False

**Mixer volumes** now must be specified using a new format, where 0.0 is -40 dB (power) and 1.0 is 0 dB (power). To use the old format, where the samples were multiplied by volume \*\* 2, use:

define config.quadratic\_volumes \= True

Alternatively, you can determine new default volumes for `config.default_music_volume`, `config.default_sfx_volume`, and `config.default_voice_volume` variables. If any of these is 0.0 or 1.0, it can be left unchanged.

**At Transform and Global Variables** An at transform block that uses a global variable is not re-evaluated when the variable changes. This matches the behavior for ATL that is not in screens.

The recommended fix is to capture the global variable into a local, by changing:

screen test():
    test "Test":
        at transform:
            xpos global\_xpos

to:

screen test():
    $ local\_xpos \= global\_xpos

    test "Test":
        at transform:
            xpos local\_xpos

This change can be reverted with:

define config.at\_transform\_compare\_full\_context \= True

## 8.0.2 / 7.5.2

A modal screen now blocks the `pause` statement and ``renpy.pause`()`` function from timing out. This was the indended behavior, but didn't work in some cases. This change can be reverted with:

define config.modal\_blocks\_pause \= False

The default games no longer filter Ruby/Furigana text tags from the history. This requires the line in screens.rpy that sets `gui.history_allow_tags` to be changed to:

define gui.history\_allow\_tags \= { "alt", "noalt", "rt", "rb", "art" }

This change is only required if your game uses Ruby/Furigana text tags.

## 8.0.0 / 7.5.0

The "Windows, Mac, and Linux for Markets" distribution has been changed to no longer prefix the contents of the zip file created with the directory name and version number. If you'd like to retain the old behavior, add to your game:

init python:
    build.package("market", "zip", "windows linux mac renpy all", "Windows, Mac, Linux for Markets")

For the noalt text tag to work with history, you'll need to edit screens.rpy to make sure that `gui.history_allow_tags` contains "noalt". The defaultfor this variable is:

define gui.history\_allow\_tags \= { "alt", "noalt" }

(This change was necessary in 7.4, but only documented now.)

The behavior of Ren'Py changed sometime in the 7.4 series, such that rollback through a load behaved correctly, and reverted the changes performed in the `after_load` label, and by . (The previous behavior was undefined, with some changes reverted and some not, leaving the game in an inconsistent state.) If your game has to migrate data after a load, it's now recommended to call  to prevent the changes from being rolled back.

The  variable now defaults to True. It's been set to true in the default screens.rpy for some time. In the unlikely event it was false in your game, restore the old behavior with:

define config.narrator\_menu \= False

The sound and voice channels are now stopped when ending the main menu. To revert to the prior behavior (only the movie channel was stopped), add to your game:

define config.main\_menu\_stop\_channels \= \[ "movie" \]

Screens called by `call screen` no longer support roll forward by default. See  for the problems it can cause. Roll forward can be enabled on a per screen basis with the roll\_forward property, or for all screens with:

define config.call\_screen\_roll\_forward \= True

Key and timer statements no longer take up space inside a vbox or hbox, and the showif statement does not take up space when its child is hidden. To revert this change:

define config.box\_skip \= False

The  style property now defaults to None for drag displayables. This improves performance, but means that the displayable can be dragged by transparent pixels. To revert this, the focus\_mask property can be set to True for individual drags, or globally with:

style drag:
    focus\_mask True

Both options reduce performance.

The  style property now defaults to "linear". This means the window scaling factor is applied to the outline size, and then rounded to an integer. This can cause multiple outlines of similar sizes to disappear. To revert this, the outline\_scaling property can be set to "step" for individual text elements, or globally with:

style default:
    outline\_scaling "step"

The  transform property now defaults to True instead of False. Absolute numbers of pixels to set the cropping should be expressed with ints or `absolute` numbers. To revert to the former default behavior, which casts floats to an absolute number of pixels, use:

define config.crop\_relative\_default \= False

However, be warned that like most things documented only on this page, this will conflict with - and cannot be used at the same time as - some other new features. This setting applies to , and also now to  and .

The platform-specific directories inside lib/ have had name changes. The `lib/windows-x86_64` directory is now `lib/py2-windows-x86_64`. This change helps support the development of the Python 3 powered Ren'Py 8. These directories are not documented, and may change between Ren'Py versions, but we do guarantee that `sys.executable` is set.

Vpgrids cannot be overfull anymore, and can only be underfull if the `allow_underfull` property is passed, or if `config.allow_underfull_grids` is set to True.

The way  place their children, and how children with variable size are sized, has changed. Instead of taking into account the available area in the context the layeredimage is displayed, it now presumes the size of the screen is available, unless an explicit size has been given with ,  or . To revert to the old behavior, where a layeredimage can display differently in different contexts, you can use:

define config.layeredimage\_offer\_screen \= False

Or you can also toggle it for specific layeredimages by passing them the `offer_screen` property.

The `function` statement in ATL will only block catch-up in cases where it executes more than once. To revert to the old behavior, where ATL would block at a function, use:

define config.atl\_function\_always\_blocks \= True

## 7.4.11

Ren'Py will now run a button's unhovered property even when focus is changed by default, such as when a screen is shown or unshown. To revert to the old behavior, use:

define config.always\_unfocus \= False

## 7.4.9

Ren'Py will now interpret floating point numbers given to a Transform's  or  properties as a size relative to the area available to the Transform. To revert this change:

define config.relative\_transform\_size \= False

The order in which Ren'Py's self-voicing reads out layers, screens, and displayables in screens has changed so that screens and displayables closest to the player are read first. To revert to the old order:

define config.tts\_front\_to\_back \= False

## 7.4.7

When  and  are both floats, the minimum is interpreted as being a fraction of the available area. This means that  will have the expected result when being given a float. This may cause some displayables to change size. To revert this change:

define config.adjust\_minimums \= False

An ATL displayable will now start its animation when it first appears, rather than when the screen itself is shown. To revert this change:

define config.atl\_start\_on\_show \= False

Input carets now blink by default. To change this:

define config.input\_caret\_blink \= False

## 7.4.6

The change regarding the layer at list in 7.4.5 was reverted. The new `camera` statement defaults to the new semantics, while leaving `show layer` alone.

## 7.4.5

Games produced with this version use the model-based renderer by default. To disable the model-based renderer, use:

define config.gl2 \= False

**Reverted in 7.4.6** The `scene` statement no longer clears the layer at list. To clear the layer at list, use:

show layer master

Where "master" is the name of the layer. Alternatively, the old behavior can be restored with:

define config.scene\_clears\_layer\_at\_list \= True

## 7.4.3

It is now possible to click to dismiss transitions introduced with , and places that use it like the `with` clause of say or `call screen` statement. To prevent this, use:

define config.dismiss\_blocking\_transitions \= False

## 7.4.1

Pause with a delay now uses  rather than `with Pause(...)`. This means that the user will have to click to bypass multiple pauses in a row. To revert to the old behavior, use:

define config.pause\_with\_transition \= True

## 7.4

Mobile platforms now use hardware, rather than software, video playback. To restore the old behavior, use:

define config.hw\_video \= True

Ren'Py will now only show side images if with at least one attribute in addition to the image tag. To disable this, use:

define config.side\_image\_requires\_attributes \= False

While setting config variables, like , outside of the init phase was never supported, it will not work in 7.4. Consider using the  variable to set a custom mouse cursor, instead.

## 7.3.3

Callbacks registered with  are now run after `default` statements in all cases. To restore the old behavior (where callbacks were run before `default` statements during game but not replay start), use:

define config.early\_start\_store \= True

When given to a viewport or vpgrid with scrollbars, the minimum, xminimum, and yminimum side properties now apply to the side containing the scrollbars and viewport, and not solely the viewport.

To work around this, either use `viewport_minimum`, `viewport_xminimum`, and `viewport_yminimum`, or include:

define config.compat\_viewport\_minimum \= True

## 7.3.0

Screen language now produces the error "a non-constant keyword argument ... is not allowed after a python block." when it encounters screens similar to the following:

screen test():

    default a \= 0

    button:
        $ a \= 1
        action Return(a)

        text "Test"

This is because the property action is run before the python assignment, meaning this was returning 0 when clicked, not 1. To disable this check, add

define config.keyword\_after\_python \= True

to a file named 01compat.rpy in your game's game directory. However, your game will have the old behavior.

The order in which children of the `side` layout are drawn is now taken from the control string. To revert to the old fixed order, use:

define config.keep\_side\_render\_order \= False

The interface of  has been changed in an incompatible way, to allow sets of old and new tags to be given. To revert to the old interface, use:

define config.say\_attribute\_transition\_callback\_attrs \= False

It's mode parameter has also been slightly changed, and will now return a value of `both` when both a `permanent` and `temporary` attribute transition is occuring.

## 7.2.2

 has been changed to accept a new argument, the image being displayed.

## 7.1.1

Ren'Py's window auto function will now determine if dialogue or a caption is associated with a menu statement, and will attempt to hide or show the dialogue window as appropriate. A "Force Recompile" is necessary to include the information that enables this feature. While it should work with older games, this can be disabled and the old behavior restored with:

define config.menu\_showed\_window \= True
define config.window\_auto\_show \= \[ "say" \]
define config.window\_auto\_hide \= \[ "scene", "call screen" \]

While not technically an incompatible change, there is a recommend change to the history screen. Please see  for details of how to update your game.

## 7.1

When an image is not being show, say-with-attributes now resolves a side image, rather than just using the attributes given. To disable this, add:

define config.say\_attributes\_use\_side\_image \= False

## 7.0

Ren'Py now defines automatic images at init 0, rather than at a very late init level. To revert to the prior behavior, add to your game:

init \-1:
    define config.late\_images\_scan \= True

The , , and  transitions now default to using the alpha channel of the source displayables, as if `alpha=True` was given. To revert this change, add:

define config.dissolve\_force\_alpha \= False

Showing a movie sprite that is already showing will now replay the movie. To revert to the previous behavior:

define config.replay\_movie\_sprites \= False

## 6.99.13

The size of a hyperlink is now inherited from the size of the enclosing text. To disable this, add:

define config.hyperlink\_inherit\_size \= False

The {nw} text tag now waits until voice and self-voicing are finished before it continues. To disable this behavior, add:

define config.nw\_voice \= False

ATL Transforms now show at least one frame whenever a pause or interpolation occurs. When a game doesn't expect this, it can show up as a series of rapidly displayed single frames. This can be disabled with:

define config.atl\_one\_frame \= False

The show layer at statement now persists the state of a transform like any other ATL transform. This can lead to a behavior change in which, for example, an offset persists between multiple show layer at statements. To disable this, write:

define config.keep\_show\_layer\_state \= False

While not an incompatible change,  has been changed to sort its output in a standard order. The causes Ren'Py to commit to behavior that had been ambiguous. For example, when multiple files in the images directory had the same name, Ren'Py would pick one at random. (The file picked could change from system to system.) Now, the same file is chosen wherever Ren'Py is run.

## 6.99.12.3

Ren'Py will no longer search for system-installed fonts when in developer mode. If you game was using a system installed font, the font file should be copied into the game/ directory. (But please make sure that this is compatible with the font file's license.)

## 6.99.11

The order of execution of `style` and `translate` statements has changed, as documented in . To revent this change, add the code:

define config.new\_translate\_order \= False

Note that reverting this change may prevent the new GUI from working.

The  variable has changed its default to one that causes the quit prompt to be displayed of the in-game context. To revert to the old behavior, add the code:

define config.quit\_action \= ui.gamemenus("\_quit\_prompt")

Ren'Py now enforces maximum sizes given to buttons and windows. To disable this behavior, add the code:

define config.enforce\_window\_max\_size \= False

## 6.99.9

Ren'Py now plays interface sounds on a channel named "audio", that supports multiple sound playback at once. This channel might not have the same settings as a customized sound channel. The audio channel settings can be changed by adjusting , or the sound channel can be used by adding the code:

define config.play\_channel \= "sound"

## 6.99.2

Ren'Py will now scan the an image directory (the directory named images underneath the game directory) for images, and define them based on their filename. To disable this behavior, use the code:

init python:
    config.image\_directory \= None

## 6.18

The `show screen` and `call screen` statements may now evaluate their arguments as part of the screen prediction process. If evaluating the arguments to a screen causes side effects to occur, the `show screen` or `call screen` statements should be given the new `nopredict` clause, which prevents prediction.

Screens now participate in transitions – transitions now go from the old state of the screen to the new state. To disable this, set  to false.

Ren'Py no longer uses structural equality to transfer state (for example, the state of a transform) when a screen replaces a screen with the same tag. Instead, the  now supports an `id` property, which can be used to explicitly transfer state.

## 6.16

The meaning of the loop parameter to  has changed. To get the old behavior, set both loop and single\_track to true.

## 6.15.7

Ren'Py now expects auto-forward mode to be controlled by the "auto-forward" . To have it controlled by the auto-forward mode slider, set `config.default_afm_enable` to None.

## 6.14

Previously, Ren'Py moved archived files into the archived/ directory. It would search this directory automatically when running a game or building archives. One-click builds make this unnecessary, and files in archived/ should be moved back into the game directory.

 has changed its interface. The old version of MoveTransition can be accessed as OldMoveTransition, if you don't want to rewrite your code. (The changes only matter if you use factories with MoveTransition.)

 has changed its behavior with regards to asymmetrically scaled and rotated images. It's unlikely the old behavior was ever used.

## 6.13.8

Old-style string interpolation has been re-enabled by default. If you wrote code (between 6.13 and 6.13.7) that uses % in say or menu statements, you should either write %% instead, or include the code:

init python:
    config.old\_substitutions \= False

## 6.13

The changes to text behavior can affect games in development in many ways. The biggest change is the introduction of new-style (square-bracket) text substitutions, and the elimination of old-style (percent-based) substitutions. These changes can be reverted with the code:

init python:
    config.old\_substitutions \= True
    config.new\_substitutions \= False

New- and old-style substitutions can coexist in the same game, by setting both variables to True.

Ren'Py has also changed the default line-wrapping behavior. While the new behavior should never increase the number of lines in a paragraph, it may change which words fall on each line. To restore the old behavior, add the code:

init python:
    style.default.layout \= "greedy"
    style.default.language \= "western"

A bug with negative line\_spacing was fixed. This fix can cause blocks of text to shrink in height. To revert to the old behavior, use:

init python:
    config.broken\_line\_spacing \= True

Finally, the new text code may lead to artifacts when displaying slow text, especially in conjunction with a negative line spacing. Consider adjusting  to fix this.

## 6.12.1

Image names have changed from being static names to being attribute-based. This can lead to image names that were previously distinct becoming ambiguous. To disable attribute-based image names, set `config.image_attributes` to False.

Showing an image without providing a transform or ATL block will now continue the previous transform that the image was using. This means that a moving image may continue moving once it has changed. To revert to the old behavior, set  to False.

The image argument to  has changed meaning. While the old meaning was unsupported in the screens-based environment, it can be restored for compatibility purposes by setting `config.new_character_image_argument` to False.

## 6.12.0

The definition of the items parameter of the  and `nvl_choice` screens has changed. The `nvl_choice` screen is deprecated in favor of the  screen.

Screens may be invoked at any time, in order to allow for image prediction, unless they have a predict property of False. When the predict property is not False, screens should not cause side effects to occur upon their initial display.

For performance reason, Ren'Py now ignores the position properties of ImageReferences. This means that the position properties of style.image\_placement are now ignored. To revert to the old behavior, set `config.imagereference_respects_position` to True.

## 6.11.1

MoveTransition has been modified to respect the xoffset and yoffset parameters of the displayables it is moving. The factory functions that are used for movement now take xoffset and yoffset parameters. While the built-in movement factories take these parameters without problem, user-defined factories may need to be upgraded to use or ignore these additional parameters.

## 6.11.0

*   The transform specified by the  variable is used to initialize the transform properties of images shown using the show and hide statements. The default value of this transform sets  and  to 0.5, and  and  to 1.0.
    
    This represents a change in the default value of these style properties, which were previously uninitialized and hence defaulted to 0.
    
    By including the  transform in ATL transforms, these properties can be reset back to 0. Alternatively, one can stop using the default transform, and revert to the old behavior, using the code:
    
    init python:
        style.image\_placement.xpos \= 0.5
        style.image\_placement.ypos \= 1.0
        style.image\_placement.xanchor \= 0.5
        style.image\_placement.yanchor \= 1.0
    
        config.default\_transform \= None
    
*   If a transform does not define one of the position properties , , , or , that property will be taken from the transform's child, if the defines that property.
    
    This makes it possible to have one transform control a displayable's vertical motion, and the other control the horizontal. But this is incompatible with previous behavior, and so can be disabled with the  variable.
    
    init python:
        config.transform\_uses\_child\_position \= False
    

## 6.10.0

*   The default positions (left, right, center, truecenter, offscreenleft, and offscreenright) are now defined as ATL transforms. This means that showing an image at such a position will cause the position to be remembered. If you do not want this behavior, you need to redefine these positions, by adding the code:
    
    define left \= Position(xalign\=0.0)
    define center \= Position(xalign\=0.5)
    define truecenter \= Position(xalign\=0.5, yalign\=0.5)
    define right \= Position(xalign\=1.0)
    define offscreenleft \= Position(xpos\=0.0, xanchor\=1.0)
    define offscreenright \= Position(xpos\=1.0, xanchor\=0.0)
    

## 6.9.2

*   To migrate your game from Ren'Py 6.9.2 or later, copy the directory containing your game into your projects directory. You can choose a projects directory by clicking "Options", "Projects Directory" in the Launcher. Please see the  for information about migrating from older releases.
    
