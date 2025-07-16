
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

transform choice_delay(t=0):
    subpixel True
    xoffset -100 xanchor 0.0 alpha 0.0
    t * 0.10
    linear 0.3 xoffset 0 alpha 1.0

screen choice(items):
    style_prefix "choice"

    vbox:
        $ idx = -1
        for i in items:
            $ idx = idx + 1
            textbutton i.caption action i.action at choice_delay(t = idx)


style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 33

style choice_button:
    is default # This means it doesn't use the usual button styling
    xysize (926, None)
    background Frame("gui/button/choice_[prefix_]background.png",
        150, 25, 150, 25, tile=False)
    padding (42, 22)

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5
    idle_color "#fcd3e1"
    hover_color "#fff"
    insensitive_color "#444"
