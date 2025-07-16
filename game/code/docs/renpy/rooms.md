# Image Gallery, Music Room, and Replay Actions

## Image Gallery

A image gallery is a screen that allows the player to unlock images, and then view those images. The screen has one or more buttons associated with it, and each button has one or more associated images. Buttons and images also have conditions that determine if they have unlocked.

Image galleries are managed by instances of the Gallery class. A single instance of the gallery class may be shared between multiple image gallery screens.

A gallery has one or more buttons associated with it, a button has one or more images associated with it, and each image has one or more displayables associated with it. Conditions can be assigned to buttons and images. A button is unlocked when all of the conditions associated with it are satisfied and at least one image associated with that button is unlocked. An image is unlocked when all associated conditions are satisfied.

Creating an image gallery consists of the following four steps.

1.  Create an instance of Gallery.
    
2.  Add buttons and images to that gallery, along with conditions that determine if the buttons and images they belong to are unlocked. This is also a multi-step process.
    
    1.  Declare a new button by calling .
        
    2.  Optionally, add one or more unlock conditions to the button by calling  or .
        
    3.  Declare an image by calling  with one or more displayables as arguments. Or call the convenience method  instead.
        
    4.  Optionally, call  to associate transforms with the displayables.
        
    5.  Optionally, add one or more unlock conditions to the image by calling , , or .
        
    
    Additional images can be added to a button by repeating steps 3-5, while additional buttons can be added to the gallery by repeating all five steps.
    
3.  Create an image gallery screen. The screen should display a background, and should contain navigation that allows the user to show other image galleries, or to return to the main or extras menu.
    
4.  Add a way to display the image gallery screen to the main or extras menu.
    

Here's an example:

init python:

    \# Step 1. Create the gallery object.
    g \= Gallery()

    \# Step 2. Add buttons and images to the gallery.

    \# A button with an image that is always unlocked.
    g.button("title")
    g.image("title")

    \# A button that contains an image that automatically unlocks.
    g.button("dawn")
    g.image("dawn1")
    g.unlock("dawn1")

    \# This button has multiple images assocated with it. We use unlock\_image
    \# so we don't have to call both .image and .unlock. We also apply a
    \# transform to the first image.
    g.button("dark")
    g.unlock\_image("bigbeach1")
    g.transform(slowpan)
    g.unlock\_image("beach1 mary")
    g.unlock\_image("beach2")
    g.unlock\_image("beach3")

    \# This button has a condition associated with it, allowing the game
    \# to choose which images unlock.
    g.button("end1")
    g.condition("persistent.unlock\_1")
    g.image("transfer")
    g.image("moonpic")
    g.image("girlpic")
    g.image("nogirlpic")
    g.image("bad\_ending")

    g.button("end2")
    g.condition("persistent.unlock\_2")
    g.image("library")
    g.image("beach1 nomoon")
    g.image("bad\_ending")

    \# The last image in this button has an condition associated with it,
    \# so it will only unlock if the user gets both endings.
    g.button("end3")
    g.condition("persistent.unlock\_3")
    g.image("littlemary2")
    g.image("littlemary")
    g.image("good\_ending")
    g.condition("persistent.unlock\_3 and persistent.unlock\_4")

    g.button("end4")
    g.condition("persistent.unlock\_4")
    g.image("hospital1")
    g.image("hospital2")
    g.image("hospital3")
    g.image("heaven")
    g.image("white")
    g.image("good\_ending")
    g.condition("persistent.unlock\_3 and persistent.unlock\_4")

    \# The final two buttons contain images that show multiple pictures
    \# at the same time. This can be used to compose character art onto
    \# a background.
    g.button("dawn mary")
    g.unlock\_image("dawn1", "mary dawn wistful")
    g.unlock\_image("dawn1", "mary dawn smiling")
    g.unlock\_image("dawn1", "mary dawn vhappy")

    g.button("dark mary")
    g.unlock\_image("beach2", "mary dark wistful")
    g.unlock\_image("beach2", "mary dark smiling")
    g.unlock\_image("beach2", "mary dark vhappy")

    \# The transition used when switching images.
    g.transition \= dissolve

\# Step 3. The gallery screen we use.
screen gallery:

    \# Ensure this replaces the main menu.
    tag menu

    \# The background.
    add "beach2"

    \# A grid of buttons.
    grid 3 3:

        xfill True
        yfill True

        \# Call make\_button to show a particular button.
        add g.make\_button("dark", "gal-dark.png", xalign\=0.5, yalign\=0.5)
        add g.make\_button("dawn", "gal-dawn.png", xalign\=0.5, yalign\=0.5)
        add g.make\_button("end1", "gal-end1.png", xalign\=0.5, yalign\=0.5)

        add g.make\_button("end2", "gal-end2.png", xalign\=0.5, yalign\=0.5)
        add g.make\_button("end3", "gal-end3.png", xalign\=0.5, yalign\=0.5)
        add g.make\_button("end4", "gal-end4.png", xalign\=0.5, yalign\=0.5)

        add g.make\_button("dark mary", "gal-dark\_mary.png", xalign\=0.5, yalign\=0.5)
        add g.make\_button("dawn mary", "gal-dawn\_mary.png", xalign\=0.5, yalign\=0.5)
        add g.make\_button("title", "title.png", xalign\=0.5, yalign\=0.5)

    \# The screen is responsible for returning to the main menu. It could also
    \# navigate to other gallery screens.
    textbutton "Return" action Return() xalign 0.5 yalign 0.5

Step 4 will vary based on how your game is structured, but one way of accomplishing it is to add the following line:

textbutton "Gallery" action ShowMenu("gallery")

to the main menu screen.

_class_ Gallery

This class supports the creation of an image gallery by handling the locking of images, providing an action that can show one or more images, and a providing method that creates buttons that use that action.

transition

The transition that is used when changing images.

locked\_button

The default displayable used by make\_button for a locked button.

hover\_border

The default hover border used by make\_button.

idle\_border

The default idle border used by make\_button.

unlocked\_advance

If true, the gallery will only advance through unlocked images.

navigation

If true, the gallery will display navigation and slideshow buttons on top of the images.

To customize the look of the navigation, you may override the gallery\_navigation screen. The default screen is defined in renpy/common/00gallery.rpy

span\_buttons

If true, the gallery will advance between buttons.

slideshow\_delay

The time it will take for the gallery to advance between images in slideshow mode.

image\_screen \= "\_gallery"

The screen that is used to show individual images in this gallery. This screen is supplied the following keyword arguments:

locked

True if the image is locked.

displayables

A list of transformed displayables that should be shown to the user.

index

A 1-based index of the image being shown.

count

The number of images attached to the current button.

gallery

The image gallery object.

Additional arguments may be supplied by prefixing them with show\_ in calls to Gallery.image and Gallery.unlock image.

The default screen is defined at the bottom of renpy/common/00gallery.rpy.

Action(_name_)

An action that displays the images associated with the given button name.

Next(_unlocked\=False_)

Advances to the next image in the gallery.

unlocked

If true, only considers unlocked images.

Previous(_unlocked\=False_)

Goes to the previous image in the gallery.

unlocked

If true, only considers unlocked images.

Return()

Stops displaying gallery images.

ToggleSlideshow()

Toggles slideshow mode.

allprior()

A condition that is true if all prior images associated with the current button have been unlocked.

button(_name_)

Creates a new button, named name.

name

The name of the button being created.

condition(_expression_)

A condition that is satisfied when an expression evaluates to true.

expression

A string giving a Python expression.

get\_fraction(_name_, _format\='{seen}/{total}'_)

Returns a text string giving the number of unlocked images and total number of images in the button named name.

format

A Python format string that's used to format the numbers. This has three values that can be substituted in:

{seen}

The number of images that have been seen.

{total}

The total number of images in the button.

{locked}

The number of images that are still locked.

image(_\*displayables_, _\*\*properties_)

Adds a new image to the current button, where an image consists of one or more displayables.

Properties beginning with show\_ have that prefix stripped off, and are passed to the gallery.image\_screen screen as additional keyword arguments.

This takes one keword argument:

movie

This should be set to true if one of the displayables is a movie with sound. This will cause the movie to be hidden during a transition.

make\_button(_name_, _unlocked_, _locked\=None_, _hover\_border\=None_, _idle\_border\=None_, _style\=None_, _\*\*properties_)

This creates a button that displays the images associated with the given button name.

name

The name of the button that will be created.

unlocked

A displayable that is displayed for this button when it is unlocked.

locked

A displayable that is displayed for this button when it is locked. If None, the locked\_button field of the gallery object is used instead.

hover\_border

A displayable that is used to overlay this button when it is unlocked and has focus. If None, the hover\_border field of the gallery object is used.

idle\_border

A displayable that is used to overlay this button when it is unlocked but unfocused. If None, the idle\_border field of the gallery object is used.

style

The style the button inherits from. When None, defaults to the "empty" style, so as not to inherit borders and so on.

Additional keyword arguments become style properties of the created button object.

transform(_\*transforms_)

Applies transforms to the last image registered. This should be called with the same number of transforms as the image has displayables. The transforms are applied to the corresponding displayables.

If a transform is None, the default transform is used.

unlock(_\*images_)

A condition that takes one or more image names as argument, and is satisfied when all the named images have been seen by the player. The image names should be given as strings.

unlock\_image(_\*images_, _\*\*properties_)

A convenience method that is equivalent to calling image and unlock with the same parameters. (Keyword arguments beginning with `show_` are only passed to image.) This will cause an image to be displayed if it has been seen before.

The images should be specified as strings giving image names.

## Music Room

A music room is a screen that allows the user to select and play music tracks from the game. These tracks may start off locked when the user first begins playing a particular game, and will be unlocked as the user listens to the music while playing the game.

A music room is managed by an instance of the MusicRoom class. There can be more than one MusicRoom instance in a game, allowing a game to have multiple music rooms. Creating a music room consists of the following four steps:

1.  Create an instance of MusicRoom. The MusicRoom constructor takes parameters to control the channel on which music is played back, and how long it takes to fade music out and back in.
    
2.  Add music files to the instance.
    
3.  Create a screen that uses the MusicRoom instance to create actions for buttons, imagebuttons, or hotspots. These actions can pick a track, the next or previous track, or stop and start the music.
    
    Note that the actions used are members of a MusicRoom instance, so if the MusicRoom instance is named `mr`, then `mr.Play("track1.ogg")` is how you'd use the play action.
    
4.  Add the music room screen to the main menu, or an extras menu.
    

Here's an example:

init python:

    \# Step 1. Create a MusicRoom instance.
    mr \= MusicRoom(fadeout\=1.0)

    \# Step 2. Add music files.
    mr.add("track1.ogg", always\_unlocked\=True)
    mr.add("track2.ogg")
    mr.add("track3.ogg")

\# Step 3. Create the music room screen.
screen music\_room:

    tag menu

    frame:
        has vbox

        \# The buttons that play each track.
        textbutton "Track 1" action mr.Play("track1.ogg")
        textbutton "Track 2" action mr.Play("track2.ogg")
        textbutton "Track 3" action mr.Play("track3.ogg")

        null height 20

        \# Buttons that let us advance tracks.
        textbutton "Next" action mr.Next()
        textbutton "Previous" action mr.Previous()

        null height 20

        \# The button that lets the user exit the music room.
        textbutton "Main Menu" action ShowMenu("main\_menu")

    \# Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    \# Restore the main menu music upon leaving.
    on "replaced" action Play("music", "track1.ogg")

Step 4 will vary based on how your game is structured, but one way of accomplishing it is to add the following line:

textbutton "Music Room" action ShowMenu("music\_room")

to the main menu screen.

Using the `Preferences()` function, especially `Preferences("music volume")`, it's possible to include a volume slider on the music screen.

_class_ MusicRoom(_channel\='music'_, _fadeout\=0.0_, _fadein\=0.0_, _loop\=True_, _single\_track\=False_, _shuffle\=False_, _stop\_action\=None_)

A music room that contains a series of songs that can be unlocked by the user, and actions that can play entries from the list in order.

channel

The channel that this music room will operate on.

fadeout

The number of seconds it takes to fade out the old music when changing tracks.

fadein

The number of seconds it takes to fade in the new music when changing tracks.

loop

Determines if playback will loop or stop when it reaches the end of the playlist.

single\_track

If true, only a single track will play. If loop is true, that track will loop. Otherwise, playback will stop when the track finishes.

shuffle

If true, the tracks are shuffled, and played in the shuffled order. If false, the tracks are played in the order they're added to the MusicRoom.

stop\_action

An action to run when the music has stopped.

Single\_track and shuffle conflict with each other. Only one should be true at a time. (Actions that set single\_track and shuffle enforce this.)

Next()

An action that causes the music room to play the next unlocked file in the playlist.

Play(_filename\=None_)

This action causes the music room to start playing. If filename is given, that file begins playing. Otherwise, the currently playing file starts over (if it's unlocked), or the first file starts playing.

If filename is given, buttons with this action will be insensitive while filename is locked, and will be selected when filename is playing.

Previous()

An action that causes the music room to play the previous unlocked file in the playlist.

RandomPlay()

This action causes the music room to start playing a randomly selected unlocked music track.

SetLoop(_value_)

This action sets the value of the loop property.

SetShuffle(_value_)

This action sets the value of the shuffle property.

SetSingleTrack(_value_)

This action sets the value of the single\_track property.

Stop()

This action stops the music.

ToggleLoop()

This action toggles the value of the loop property.

TogglePause()

If music is playing, pauses or unpauses the music as appropriate.

This button is selected when the music is paused.

TogglePlay()

If no music is currently playing, this action starts playing the first unlocked track. Otherwise, stops the currently playing music.

This button is selected when any music is playing.

ToggleShuffle()

This action toggles the value of the shuffle property.

ToggleSingleTrack()

This action toggles the value of the single\_track property.

add(_filename_, _always\_unlocked\=False_, _action\=None_)

Adds the music file filename to this music room. The music room will play unlocked files in the order that they are added to the room.

always\_unlocked

If true, the music file will be always unlocked. This allows the file to show up in the music room before it has been played in the game.

action

This is a action or the list of actions. these are called when this file is played.

For example, These actions is used to change a screen or background, description by the playing file.

is\_unlocked(_filename_)

Returns true if the filename has been unlocked (or is always unlocked), and false if it is still locked.

## Replay

Ren'Py also includes the ability to replay a sequence from inside the main or game menu. This can be used to create a "sequence gallery", or memory gallery that allows the player to repeat important sequence. After the sequence finishes, Ren'Py returns to where the replay was launched.

Sequence replay is also possible using the  action. The difference between the two modes are:

*   A replay can be launched from any screen while Start can only be used in the main menu or screens shown by the main menu.
    
*   When a replay finishes, control returns to the point where the replay was invoked. That point can be inside the main or game menu, for example. If a game is in progress when replay is called, game state is preserved.
    
*   Saving is disabled while in replay mode. Reloading, which requires saving, is also disabled.
    
*   While in replay mode, a call to  will end the replay. In normal mode, end\_replay does nothing.
    

To take advantage of the replay mode, a sequence should begin with a label, and end with a call to . The sequence should make no assumption as to the state of the layers or variables, which can be very different in normal and replay mode (except those set through the scope parameter when entering replay). When a replay begins, the label is invoked from a black screen.

For example:

    "And finally, I met the wizard himself."

label meaning\_of\_life:

    scene revelation

    "Mage" "What is the meaning of life, you say?"

    "Mage" "I've thought about it long and hard. A long time, I've
            spent pondering that very thing."

    "Mage" "And I'll say - the answer - the meaning of life
            itself..."

    "Mage" "Is forty-three."

    $ renpy.end\_replay()

    "Mage" "Something like that, anyway."

With the sequence defined like that, the replay can be invoked with the Replay action:

textbutton "The meaning of life" action Replay("meaning\_of\_life")

There is one store variable used by replay mode:

\_in\_replay

When in replay mode, this is sent to the label at which replay mode was started - the label that was called, not the one the call originated from. Outside of replay mode, this is None.

In addition,  and  are used when entering and exiting replay mode, respectively.  adds variables to the cleaned store when entering a replay, and by default sets  to cause right-clicking in a replay to default to showing the preferences screen.

The following variables and actions are used in replay mode:

EndReplay(_confirm\=True_)

Ends the current replay.

confirm

If true, prompts the user for confirmation before ending the replay.

Replay(_label_, _scope\={}_, _locked\=None_)

An action that starts label as a replay.

scope

A dictionary mapping variable name to value. These variables are set when entering the replay.

locked

If true, this action is insensitive and will not do anything when triggered. If false, it will behave normally. If None, it will be locked if the label has not been seen in any playthrough.

renpy.call\_replay(_label_, _scope\={}_)

Calls a label as a memory.

The scope argument is used to set the initial values of variables in the memory context.

renpy.end\_replay()

If we're in a replay, ends the replay immediately. Otherwise, does nothing.
