## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 330
define config.thumbnail_height = 168
screen save():

    tag menu


    use file_slots(_("Save"))


screen load():

    tag menu


    use file_slots(_("Load"))



style page_button_text:
    size 45
    text_align 0.5
    xalign 0.5
    xsize 20
screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_("Page {}"), auto=_("Automatic saves"),
        quick=_("Quick saves"))

    use game_menu(title)


    ####Page buttons
    vbox:
        style_prefix "page"
        align(1.0, 0.5) offset(-150, 35) spacing 10


        ###page arrow
        button:
            xysize(34,31) xalign 0.5
            add "gui/button/page_btn.png":
                fit "contain"
                xysize(34,31)

            action FilePagePrevious()
            at button_fade



        if config.has_autosave:
            textbutton _("{#auto_page}A") action FilePage("auto") at page_wiggle_heavy

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick") at page_wiggle_heavy

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 6):
                textbutton "{size=15} {/size}[page]" action FilePage(page) at page_wiggle_heavy


        ###page arrow
        button:
            xysize(34,31) xalign 0.5 
            add "gui/button/page_btn.png":
                fit "contain"
                xysize(34,31)
                yzoom -1.0
            action FilePageNext()
            at button_fade

    fixed:
        xysize(1250, 598) pos(369,337)
        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on it.
        ## This can be pretty easily removed if you want.
        ## Don't forget to also remove the `default` at the top if so.
        button:
            style "page_label"
            key_events True
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid 2 2:
            style_prefix "slot"
            yspacing 40 xspacing 50

            for i in range(2*2):
                $ slot = i + 1

                button:
                    xysize(522,254)
                    background "gui/button/save_bg.png"
                    hbox:
                        yalign 0.5 xoffset 35 spacing 15

                        button:
                            yalign 0.5 xysize(315,182)
                            add "gui/button/thumbnail_bg.png"
                            add AlphaMask(FileScreenshot(slot), "gui/button/mask.png")

                            add "gui/button/mask.png" at slot_hover
                            text FileTime(slot,
                            format=_("{#file_time}%A, %B %d %Y, %H:%M"),
                            empty=_("empty slot")):
                                style "slot_time_text"
                                at slot_hover_text
                            
                            action NullAction() ## this is only here to make the hover animation work
                            key "save_delete" action FileDelete(slot)

                        vbox:
                            spacing -20
                            button:
                                xysize(89,94)
                                background "gui/button/save_btn.png"
                                add "gui/icons/save_small.png" at button_fade
                                action FileSave(slot)
                                at wiggle_heavy
                            button:
                                xysize(89,94)
                                background "gui/button/save_btn.png"
                                add "gui/icons/load.png" at button_fade
                                action FileLoad(slot)
                                at wiggle_heavy
                        # This means the player can hover this save
                        # slot and hit delete to delete it
                    






    hbox:
        pos(480,986) spacing 15
        button:
            xysize(291,59)
            background "gui/button/sync_btn.png"
            text "Upload Sync" align(0.5, 0.5) at button_fade
            action UploadSync()

        button:
            xysize(291,59)
            background "gui/button/sync_btn.png"
            text "Download Sync" align(0.5, 0.5)  at button_fade
            action DownloadSync()
    
    add "gui/button/save_dec.png"


style page_label:
    xpadding 75
    ypadding 5
    xalign 0.0
    yoffset -35 xoffset 10

style page_label_text:
    textalign 0.0
    size 45
    layout "subtitle"
    #hover_color '#ff8335'

style page_button_text:
    color u'#3b3738'

style slot_grid:
    xalign 0.5
    yalign 0.5
    spacing 15

style slot_time_text:
    size 25
    xalign 0.5
    align(0.5, 0.5)
    text_align 0.5
    xsize 150

style slot_vbox:
    spacing 12

    #background "gui/button/slot_[prefix_]background.png"

style slot_button_text:
    size 21
    xalign 0.5
    idle_color '#aaaaaa'
    hover_color '#ff8335'
    selected_idle_color '#ffffff'



