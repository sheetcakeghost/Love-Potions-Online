
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu



screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    style_prefix "mm"


    add "gui/main_menu/bg.png"


    label "Love Potions Online" 


    ###The black border + strip
    add "gui/main_menu/foreground.png"

    textbutton "Start" action Start():
        text_size 150 
        ypos 783 yanchor 0.5 xalign 0.5
        text_idle_color u"#3b3738" text_hover_color u"#ffffff"
        text_outlines [ (absolute(7), "#fcd3e1", absolute(0), absolute(0)) ]

        at wiggle


    textbutton "Continue" action ShowMenu("load"):
        text_size 95 
        pos(494, 748) anchor (0.5, 0.5)
        text_idle_color u"#fcd3e1" text_hover_color u"#3b3738"
        #text_idle_outlines [ (absolute(6), "#3b3738", absolute(0), absolute(0)) ]
        text_hover_outlines [ (absolute(6), "#ffffff", absolute(0), absolute(0)) ]

        at wiggle

    textbutton "Options" action ShowMenu("preferences"):
        text_size 95 
        pos(1400, 810) anchor (0.5, 0.5)
        text_idle_color u"#fcd3e1" text_hover_color u"#3b3738"
        #text_idle_outlines [ (absolute(6), "#3b3738", absolute(0), absolute(0)) ]
        text_hover_outlines [ (absolute(6), "#ffffff", absolute(0), absolute(0)) ]

        at wiggle



style mm_button_text:
    font "gui/font/Levorotary_Medium.ttf"

style mm_label_text:
    font "gui/font/Fortnight-Regular.otf" 
    size 180
    textalign 0.5
    outlines [ (absolute(6), "#ffffff", absolute(0), absolute(0)) ]
style mm_label:
    align(0.5, 0.5)
    yoffset -100


