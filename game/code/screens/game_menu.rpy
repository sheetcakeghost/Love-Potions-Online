## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##

screen game_menu(title):

    style_prefix "game_menu"

    add "gui/game_menu/bg.png"

    vbox:
        xpos 128 yalign 0.5 yoffset 160
        spacing -45

        style_prefix "nav"

        button:
            add "gui/icons/save.png" at button_fade
            if not main_menu:
                action ShowMenu("save")
            else:
                action ShowMenu("load")
            sensitive True
            at wiggle_heavy

        button:
            add "gui/icons/options_big.png" at button_fade
            action ShowMenu("preferences")
            at wiggle_heavy

        button:
            add "gui/icons/history.png" at button_fade
            action ShowMenu("history")
            at wiggle_heavy


        button:
            add "gui/icons/gallery.png" at button_fade
            action ShowMenu("gallery")
            at wiggle_heavy

        button:
            add "gui/icons/quit.png" at button_fade
            action Quit()
            at wiggle_heavy


        ###there's space for one or two extra buttons, if needed
        ###just copy paste one of the previous ones and change as needed
            
            

    textbutton _("Return"):
        style "return_button"
        text_idle_color u"#fcd3e1" text_hover_color u"#ffffff"
        text_align(0.5, 0.5) text_xoffset -40 text_yoffset 5
        text_font "gui/font/Levorotary_Medium.ttf" text_size 65

        at return_slide
        action Return()

    ## Remove this line if you don't want to show the screen
    ## title text as a label (for example, if it's baked into
    ## the background image.)
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style nav_button:
    xysize(146,146)
    anchor(0.5, 0.5)
    background "gui/game_menu/btn_bg.png"
style return_button:
    xpos 1606 ypos 859 
    background "gui/game_menu/ret_btn.png" xysize(386,85)

style game_menu_viewport:
    xysize(1204, 598) pos(369,337)

#style game_menu_side:
#    yfill True
#    align (1.0, 0.5)

style game_menu_vscrollbar:
    unscrollable "hide"

style game_menu_label:
    padding (10, 10)
style game_menu_label_text:
    size 45
