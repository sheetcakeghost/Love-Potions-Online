
## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

define config.history_length = 250

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False


    use game_menu(_("History"))

    viewport:
        style_prefix "vport"
        mousewheel True draggable True pagekeys True xysize(1250, 598) pos(369,337)
        scrollbars "vertical" yinitial 1.0

        #has vbox



        #style_prefix "history"

        vbox:
            style_prefix "history"
            spacing 30
            for h in _history_list:

                frame:
                    has vbox
                    if h.who:
                        label h.who style 'history_name':
                            substitute False
                            ## Take the color of the who text
                            ## from the Character, if set
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                    else:
                        null width 200


                    ##easy divider
                    text "- - - - - - - - - - - - - - - -" xalign 0.5  color "#fcd3e1"

                    

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False
                    text "- - - - - - - - - - - - - - - -" xalign 0.5  color "#fcd3e1"

            if not _history_list:
                label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_frame:
    xsize 1195
    ysize None
    background Frame("gui/frame.png",  left=30, top=40, right=30, bottom=40, tile=False)
    padding(30, 10, 30, 20)

style history_hbox:
    spacing 20

style history_vbox:
    spacing 5
    xsize 1100

style history_name:
    xalign 0.5
    yoffset 10

style history_name_text:
    textalign 0.5
    align (0.5, 0.0)
    color "#fcd3e1"
    size 45

style history_text:
    textalign 0.0
    justify True

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

style vport_vscrollbar:
    xoffset -15
