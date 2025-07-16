################################################################################
##
## Sound Disabler and Captions Tool for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## and Alaric (just-write-studios.itch.io) v1.0
##
################################################################################
## This file contains the code for the front end of the accessible audio system.
## It has several configuration variables, and a screen for players to adjust
## which audio files are played in-game.
##
## If you use this tool, credit us as Feniks and Alaric @ feniksdev.com.
##
## Leave a comment on the tool page on itch.io if you run into any issues!
################################################################################


################################################################################
## before_main_menu - Auto declaration code
################################################################################
## If you already have a before_main_menu label, add this code to it. It will
## automatically figure out which audio files you have that are missing
## declarations and copy them to your clipboard to fill out.
label before_main_menu():
    if config.developer and persistent.missing_audio_declarations:
        $ renpy.run(CopyToClipboard(persistent.missing_audio_declarations))
        centered "You are missing audio declarations. The missing declarations have been copied to your clipboard.\nPress Ctrl+V (or Cmd+V) in your code editor to paste it into your script."
        $ print(persistent.missing_audio_declarations)
        $ persistent.missing_audio_declarations = None
    return
################################################################################

## The default folder for any audio declarations. If a file is found in this
## folder, it is expected to have an AAudioData declaration to give it a caption
## and description. Use this to point to sub-folders in case you don't want it
## to categorize some folders, such as voice files.
define aaudio.DEFAULT_FOLDER = "audio"
## The default extension for audio files, if the path is automatically
## constructed. If you're using the text copied to your clipboard on startup,
## this property is irrelevant.
define aaudio.DEFAULT_EXTENSION = "ogg"
## The channels used for sounds the player can turn off. Add custom
## channels to this. e.g. if you play ambient ocean sounds on an "ambient"
## channel and the player can toggle the ambient ocean sounds off, add
## "ambient" to this list. This is so we can loop over these channels to
## stop sounds if needed.
define aaudio.USED_CHANNELS = [ "music", "sound" ]

################################################################################
## SCREEN SETUP
################################################################################
##
## You will need buttons on your preferences screen to toggle audio captions
## on/off and to take players to the individual sound exclusion screen.
## Here's an example of two buttons you can add to your preferences screen:
##
# textbutton _("Audio Captions"):
#     action ToggleField(persistent, "audio_captions_on")
# textbutton _("Toggle individual sounds"):
#     action ShowMenu("excluded_sound_checklist")
################################################################################

init python:
    ## Here is an example of the AudioData that will be automatically copied
    ## to your clipboard if you have missing audio declarations, and how you
    ## might adjust it.
    ##
    ## The first argument is a name that will be used to declare the
    ## audio.some_name reference to this file, so you can do `play sound some_name`
    ## in your script.
    ## categories is a list of strings that will be used to categorize the sound
    ## in the sound exclusion menu. Some may only have one category, and others
    ## may have multiple.
    ## The path is always automatically filled out; it's just the path to the
    ## audio file.
    ## caption is what will appear as an audio caption when the sound plays
    ## in-game. It can be set to None if this sound is never played in-game
    ## (e.g. if it's a UI button sound).
    ## description is what will appear in the sound exclusion menu. If it's
    ## set to None, it'll be the same as the caption.
    ##
    ## There's one option not seen here; replacement_file. If you have a sound
    ## where the timing is important, you might want to set this to
    ## replacement_file="<silence 3.2>" for example, so the replaced sound also
    ## lasts for 3.2 seconds. Useful if you queue sounds.
    ##
    ## Note that "<silence 1.0>" can only be used for in-game sounds, not for UI
    ## sounds played via activate_sound or hover_sound. The included
    ## special_silence.ogg file is 1 second of silence and can be used to
    ## replace UI sounds. It is the default value of replacement_file.
    AAudioData("delight", categories=["music"], path="audio/music/Delight.mp3",
        caption=_("\"Delight\" (Gentle happy music)"), description=None)
    AAudioData("pleasant", categories=["music"], path="audio/music/Pleasant.mp3",
        caption=_("\"Pleasant\" (Upbeat waltz music)"), description=None)

    ## Here's an example of a sound that has multiple categories, and a
    ## different caption and description.
    AAudioData("footsteps_running_leaves", categories=["footsteps", "repetitive"], path="audio/sfx/footsteps/footsteps_running_leaves.mp3",
        caption=_("footsteps"), description=_("footsteps on leaves"))
    AAudioData("wet_footsteps", categories=["footsteps", "repetitive"], path="audio/sfx/footsteps/footsteps_wet_2.mp3",
        caption=_("footsteps"), description=_("footsteps on a wet surface"))

    AAudioData("open_door", categories=["sudden"], path="audio/sfx/sudden/open_door_loud_1.mp3",
        caption=_("door opening"), description=None)

    ## This file has no caption as it's a UI sound, but the description means
    ## it'll be called "a sharp UI click" in the sound exclusion menu.
    AAudioData("click", categories=["ui"], path="audio/sfx/ui/click2.ogg",
        caption=None, description=_("a sharp UI click"))


## Here you can set up the "proper" names of the categories, so they're
## ready for translation.
define aaudio.CATEGORY_NAMES["music"] = _("Background Music")
define aaudio.CATEGORY_NAMES["sudden"] = _("Sudden Sounds")
define aaudio.CATEGORY_NAMES["ui"] = _("UI")
define aaudio.CATEGORY_NAMES["paper"] = _("Paper Sounds")
define aaudio.CATEGORY_NAMES["footsteps"] = _("Footsteps")
define aaudio.CATEGORY_NAMES["repetitive"] = _("Repetitive Sounds")

## Here you can set up a prefix to be used when a sound is played on a
## particular channel. For example, when `play sound wet_footsteps` is used,
## the caption will read "Sound Effect: footsteps".
define aaudio.CHANNEL_TO_CAPTION_PREFIX["sound"] = _("Sound Effect:")

## This screen will allow the player to toggle on and off individual sounds
## or categories of sounds.
## Note: It is designed for screens that are 1920x1080. You will need to adjust
## the styling if your UI is a different size.
screen excluded_sound_checklist():
    ############################################################################
    ## Keep this code as-is!
    modal True

    default original_excluded = persistent.excluded_sounds.copy()
    default sorted_categories = sorted(AAudioData.category_dict.keys(), key=lambda x: aaudio.CATEGORY_NAMES[x])
    default current_category = sorted_categories.copy()
    ## end
    ############################################################################

    ## The background; adjust to whatever you like.
    add "#21212d"

    style_prefix "exclude"

    vbox:
        xpos 40 ypos 40
        label _("Toggle Sounds") padding (0, 5)
        text _("Toggle on and off individual sounds or categories of sounds here.")
        text _("Use the buttons on the left to turn off currently playing sounds.")

    vbox:
        xpos 40 ycenter 0.4 xsize 450 spacing 25
        ## These buttons have a special action that will toggle off all audio
        ## on the provided channel(s). If you have multiple background music
        ## channels (for example, for crossfading), you can add them to a single
        ## action like TurnOffAudio(["music", "music2"])
        textbutton _("Turn off current background music"):
            action TurnOffAudio(["music"])
        textbutton _("Turn off current sound effects"):
            action TurnOffAudio(["sound"])
        null height 25
        ## Options to expand/collapse all categories.
        textbutton _("Expand all categories"):
            action SetScreenVariable("current_category", sorted_categories.copy())
        textbutton _("Collapse all categories"):
            action SetScreenVariable("current_category", set())
        ## This clears the excluded sounds list, so all sounds will play.
        textbutton _("Reset all sounds"):
            selected False sensitive persistent.excluded_sounds
            action Function(persistent.excluded_sounds.clear)

    frame:
        area (550, 200, 1350, 840) padding (15, 15)
        has viewport
        scrollbars "vertical" mousewheel True draggable True
        vbox:
            for category in sorted_categories:
                hbox:
                    first_spacing 5
                    textbutton "▼":
                        style 'exclude_label' text_font "DejaVuSans.ttf"
                        xalign 0.5 yalign 1.0 padding (0, 0)
                        action ToggleSetMembership(current_category, category)
                        if category in current_category:
                            at transform:
                                rotate 0
                        else:
                            at transform:
                                rotate 270
                    textbutton aaudio.CATEGORY_NAMES[category]:
                        style 'exclude_label'
                        action ToggleSetMembership(current_category, category)
                    textbutton _("Mute category"):
                        style_prefix 'check' align (0.5, 1.0)
                        ## Mutes or unmutes all sounds in the category.
                        action Function(toggle_category_membership, category)
                        selected set([x.path for x in AAudioData.category_dict[category]]) <= persistent.excluded_sounds

                null height 10
                add "#ff8335" ysize 3
                null height 15

                showif category in current_category:
                    hbox:
                        at drop_in
                        style_prefix "check"
                        spacing 20
                        box_wrap True
                        for aadata in sorted(AAudioData.category_dict[category], key=lambda x: x.description):
                            ## Individual buttons to remove individual sounds
                            textbutton aadata.description:
                                action InvertSelected(ToggleSetMembership(
                                    persistent.excluded_sounds, aadata.path))
                                text_size 30
                                bottom_padding 15

    textbutton _("RETURN TO\nSETTINGS"):
        action Hide('excluded_sound_checklist')
        pos (40, 929)

    ## Keep this here! This ensures that if there were any sounds added to the
    ## excluded list, they will be stopped when the game resumes.
    on 'hide' action Function(check_stop_sounds, original_excluded)

## A transform that allows for dropdowns.
transform drop_in:
    on show, start:
        crop (0.0, 0.0, 1.0, 1.0)
    on hide:
        crop (0.0, 0.0, 1.0, 0.0)

style exclude_hbox:
    spacing 25
style exclude_label:
    yalign 0.5 top_padding 40 right_padding 50
style exclude_label_text:
    yalign 0.5
    size 38
    color "#ff8335"
    hover_color "#f93c3e"
style exclude_vbox:
    spacing 0