
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences


screen preferences():

    default pref_page = "options"
    tag menu

    use game_menu(_("Preferences"))


    vbox:
        align(1.0, 0.5) offset(-100, 35) spacing -20
        add "gui/button/dec.png" xalign 0.5
        button:
            xysize(108,107)
            add "gui/button/cat_bg.png" align(0.5, 0.5)
            add "gui/icons/options_small.png" at button_fade
            at wiggle
            action SetScreenVariable("pref_page", "options")
        button:
            xysize(108,107) 
            add "gui/button/cat_bg.png" align(0.5, 0.5)
            add "gui/icons/help.png" at button_fade
            at wiggle
            action SetScreenVariable("pref_page", "help")
        button:
            xysize(108,107)
            add "gui/button/cat_bg.png" align(0.5, 0.5)
            add "gui/icons/about.png" at button_fade
            at wiggle
            action SetScreenVariable("pref_page", "about")
        button:
            xysize(108,107)
            add "gui/button/cat_bg.png" align(0.5, 0.5)
            add "gui/icons/help.png" at button_fade
            at wiggle
            action SetScreenVariable("pref_page", "accessibility")
        add "gui/button/dec.png" xalign 0.5

    if pref_page == "options":
        use options
    elif pref_page == "help":
        use help
    elif pref_page == "accessibility":
        use accessibility
    else:
        use about




screen options():
    viewport:
        style_prefix 'vport'
        mousewheel True draggable True pagekeys True xysize(1250, 598) pos(369,337)
        scrollbars "vertical"
        

        vbox:
            xsize 1200
            vbox:
                style_prefix "radio"
                label _("Display")
                button:
                    xysize(445,75)
                    add "gui/button/dis_bg.png"

                    if preferences.fullscreen == True:
                        text "Fullscreen":
                            idle_color u"#fcd3e1" hover_color u"#ffffff"
                            align(0.5, 0.5) size 45 yoffset -2
                    
                    else:
                        text "Windowed":
                            idle_color u"#fcd3e1" hover_color u"#ffffff"
                            align(0.5, 0.5) size 45 yoffset -2

                    action CaptureFocus("display_drop")

            vbox:
                style_prefix "check"
                label _("Skip")

                hbox:
                    
                    textbutton _("Unseen"):
                        action Preference("skip", "toggle")
                    textbutton _("After Choices"):
                        action Preference("after choices", "toggle")
                    textbutton _("Transitions"):
                        action InvertSelected(Preference("transitions", "toggle"))


            vbox:
                style_prefix "slider"
                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                vbox:
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

            vbox:
                style_prefix "slider"
                if config.has_music:
                    vbox:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                if config.has_sound:
                    vbox:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                if config.has_voice:
                    vbox:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height 15
                    textbutton _("Mute All"):
                        style_prefix "check"
                        action Preference("all mute", "toggle")


screen accessibility():
    viewport:
        style_prefix 'vport'
        mousewheel True draggable True pagekeys True xysize(1250, 598) pos(369,337)
        scrollbars "vertical"
        
        vbox:
            xsize 1200
            
            # Visual Accessibility
            vbox:
                style_prefix "accessibility"
                label _("Visual Accessibility")
                
                hbox:
                    textbutton _("Audio Cues"):
                        action persistentToggle("audio_cues")
                        selected persistent.audio_cues
                    textbutton _("Screen Shake"):
                        action persistentToggle("screenshake")
                        selected persistent.screenshake
                    textbutton _("Visual Text Help"):
                        action persistentToggle("visual_text_help")
                        selected persistent.visual_text_help
                
                vbox:
                    style_prefix "slider"
                    label _("Say Window Transparency")
                    bar value FieldValue(persistent, "say_window_alpha", range=1.0, offset=0.0)
            
            # Text Customization
            vbox:
                style_prefix "accessibility"
                label _("Text Customization")
                
                hbox:
                    textbutton _("OpenDyslexic"):
                        action changeFont("OpenDyslexic.otf")
                        selected persistent.pref_text_font == "OpenDyslexic.otf"
                    textbutton _("DejaVu Sans"):
                        action changeFont("DejaVuSans.ttf")
                        selected persistent.pref_text_font == "DejaVuSans.ttf"
                
                hbox:
                    textbutton _("Regular Size"):
                        action changeScale("regular")
                        selected persistent.pref_text_scale == "regular"
                    textbutton _("Large Size"):
                        action changeScale("large")
                        selected persistent.pref_text_scale == "large"
                
                vbox:
                    style_prefix "slider"
                    label _("Text Spacing")
                    bar value FieldValue(persistent, "say_dialogue_kerning", range=20, offset=-10)
            
            # Text Color Options
            vbox:
                style_prefix "accessibility"
                label _("Text Color")
                
                hbox:
                    textbutton _("Dark Gray"):
                        action changeColor("#333333")
                        selected persistent.pref_text_color == "#333333"
                    textbutton _("Black"):
                        action changeColor("#000000")
                        selected persistent.pref_text_color == "#000000"
                    textbutton _("Dark Blue"):
                        action changeColor("#1a1a2e")
                        selected persistent.pref_text_color == "#1a1a2e"
                    textbutton _("Dark Green"):
                        action changeColor("#1a2e1a")
                        selected persistent.pref_text_color == "#1a2e1a"
            
            # Live Preview
            vbox:
                style_prefix "accessibility"
                label _("Live Preview")
                
                frame:
                    background Frame("gui/textbox.png", 40, 10, 40, 40, tile=False)
                    xysize (800, 200)
                    padding (40, 20, 40, 40)
                    
                    text _("This is how your dialogue text will appear with the current settings. You can see the font, size, color, and spacing changes in real time as you adjust the options above."):
                        font persistent.pref_text_font
                        size persistent.pref_text_size
                        color persistent.pref_text_color
                        line_spacing persistent.pref_text_spacing
                        kerning persistent.say_dialogue_kerning
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5


    if GetFocusRect("display_drop"):

        # If the player clicks outside the frame, dismiss the dropdown.
        # The ClearFocus action dismisses this dropdown.
        dismiss action ClearFocus("display_drop")

        # This positions the displayable near (usually under) the button above.
        nearrect:
            focus "display_drop"

            style_prefix "dropdown"

            # Finally, this frame contains the choices in the dropdown, with
            # each using ClearFocus to dismiss the dropdown.
            frame:
                background Frame("gui/button/dropdown_bg.png", 10, 0, 10, 50) xsize 445 yoffset -31
                padding (0, 30, 0, 20)
                modal True

                has vbox

                frame xysize(300, 1) background Solid(u"#fcd3e154") xalign 0.5
                textbutton "Fullscreen" action [ Preference("display", "fullscreen"), ClearFocus("display_drop") ]
                frame xysize(300, 1) background Solid(u"#fcd3e154") xalign 0.5
                textbutton "Windowed" action [ Preference("display", "window"), ClearFocus("display_drop") ]

### PREF
style dropdown_vbox:
    spacing 10
style dropdown_button:
    xsize 445
style dropdown_button_text:
    xalign 0.5
    idle_color u"#fcd3e1" hover_color u"#ffffff"
style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338
    xalign 0.5
    spacing 30

## RADIO
style radio_label:
    is pref_label
    xalign 0.5
   

style radio_label_text:
    is pref_label_text
    textalign 0.5
    size 60

style radio_vbox:
    is pref_vbox
    spacing 5

style radio_button:
    xalign 0.0


## CHECK
style check_label:
    is pref_label
    xalign 0.5
style check_label_text:
    is pref_label_text
    textalign 0.5
    size 60

style check_vbox:
    is pref_vbox
    spacing 20

style check_button:
    xysize(319,71)
    idle_background "gui/button/check_unselected.png"
    hover_background "gui/button/check_selected.png"
    selected_idle_background "gui/button/check_selected.png"
    selected_hover_background "gui/button/check_selected.png"
    xalign 0.0
style check_button_text:
    size 35
    align(0.5, 0.5)
    yoffset -2
    idle_color u"#fcd3e1" hover_color u"#ffffff"
style check_hbox:
    spacing 30


## SLIDER
style slider_label:
    is pref_label
    xalign 0.5
style slider_label_text:
    is pref_label_text
    size 60

style slider_slider:
    xsize 900
    xalign 0.5

style slider_button:
    yalign 0.5
    left_margin 15

style slider_vbox:
    is pref_vbox
    xsize 675
    spacing -5


## ACCESSIBILITY
style accessibility_label:
    is pref_label
    xalign 0.5

style accessibility_label_text:
    is pref_label_text
    textalign 0.5
    size 60

style accessibility_vbox:
    is pref_vbox
    spacing 20

style accessibility_button:
    xysize(319,71)
    idle_background "gui/button/check_unselected.png"
    hover_background "gui/button/check_selected.png"
    selected_idle_background "gui/button/check_selected.png"
    selected_hover_background "gui/button/check_selected.png"
    xalign 0.0

style accessibility_button_text:
    size 35
    align(0.5, 0.5)
    yoffset -2
    idle_color u"#fcd3e1" hover_color u"#ffffff"

style accessibility_hbox:
    spacing 30

