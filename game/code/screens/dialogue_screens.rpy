
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    layer "screens"
    style_prefix "say"

    window:
        id "window"
        background Frame("gui/textbox.png", 45, 46, tile=True)
        xalign 0.5
        yalign 1.0
        xsize 1800
        yminimum 320
        padding (80, 44, 80, 43)

        vbox:
            spacing 0
            if who is not None:
                fixed:
                    xfill True
                    yfit True
                    window:
                        id "namebox"
                        style "namebox"
                        xalign 0.5
                        text who id "who"

            text what id "what":
                font persistent.pref_text_font
                size persistent.pref_text_size
                color persistent.pref_text_color
                line_spacing persistent.pref_text_spacing
                kerning persistent.say_dialogue_kerning
                xalign 0.0
                yalign 0.5
                text_align 0.0

    add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

# Style for the dialogue window
style window:
    xalign 0.5
    yalign 1.0
    yoffset -25
    padding (40, 10, 40, 40)

# Style for the dialogue
style say_dialogue:
    adjust_spacing False
    ypos 55
    font persistent.pref_text_font
    size persistent.pref_text_size
    color persistent.pref_text_color
    line_spacing persistent.pref_text_spacing
    kerning persistent.say_dialogue_kerning
    axis {"wght": persistent.pref_text_weight}

# The style for dialogue said by the narrator
style say_thought:
    is say_dialogue

# Style for the box containing the speaker's name
style namebox:
    xalign 0.5 #xoffset 40
    xysize (None, 81)
    yoffset -70
    background Frame("gui/namebox.png", 40, 20, 40, 20, tile=False, xalign=0.5)
    padding (40, 15, 40, 15)

# Style for the text with the speaker's name
style say_label:
    color '#fcd3e1'
    xalign 0.5
    yalign 0.5
    size gui.name_text_size
    font gui.name_text_font


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100


    if quick_menu:

        hbox:
            style_prefix "quick"

            button: 
                add "gui/qm/auto.png" xzoom -1 xoffset -2 at button_fade
                action Rollback()
            button:
                add "gui/qm/skip.png" at button_fade
                action Skip() alternate Skip(fast=True, confirm=True)
            button: 
                add "gui/qm/auto.png" at button_fade
                action Preference("auto-forward", "toggle")
            # Accessibility quick access button
            button:
                add "gui/qm/accessibility.png" at button_fade
                action [SetVariable('_open_pref_page', 'accessibility'), ShowMenu('preferences')]
                style "quick_accessibility_button"
                selected False

        

        mousearea:
            area (1570, 0, 350, 1.0)
            hovered Show("side_menu")
            unhovered Hide("side_menu")



screen side_menu():

    add "gui/qm/side_bg.png" xalign 1.0 at side_float
    add "gui/qm/menu_bg.png" xalign 1.0 offset (-50, 50) at side_float

    vbox:
        at side_float
        style_prefix "side"
        textbutton "Quick Save" action QuickSave()
        textbutton "Quick Load" action QuickLoad()
        textbutton "Save" action ShowMenu("save")
        textbutton "Options" action ShowMenu("preferences")
        textbutton "History" action ShowMenu("history")
        textbutton "Main Menu" action MainMenu(confirm=True)

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style side_vbox:
    xalign 1.0 offset(-80, 160)
    spacing 20
style side_button:
    xysize(246,55)
    background "gui/qm/btn.png"
style side_button_text:
    align (0.5,0.5)
    size 36
style quick_hbox:
    pos(800, 1005)
    spacing 15

style quick_button:
    background "gui/qm/small_bg.png"
    xysize(60,60)


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing 15

        use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

# The style for the NVL "textbox"
style nvl_window:
    is default
    xfill True yfill True
    background "gui/nvl.png"
    padding (0, 15, 0, 30)

# The style for the text of the speaker's name
style nvl_label:
    is say_label
    xpos 645 xanchor 1.0
    ypos 0 yanchor 0.0
    xsize 225
    min_width 225
    textalign 1.0

# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    xpos 675
    ypos 12
    xsize 885
    min_width 885

# The style for dialogue said by the narrator in NVL
style nvl_thought:
    is nvl_dialogue

style nvl_button:
    xpos 675
    xanchor 0.0


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window:
    is empty
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    is empty
    xalign 0.5

style bubble_who:
    is default
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    is default
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}

style quick_accessibility_button is quick_button
style quick_accessibility_button_text is quick_button_text
style quick_accessibility_button_text idle_color '#3b3738'
style quick_accessibility_button_text hover_color '#ffffff'
style quick_accessibility_button_text selected_color '#3b3738'
