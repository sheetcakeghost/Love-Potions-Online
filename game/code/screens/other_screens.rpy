
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():

    viewport:
        style_prefix 'vport'
        mousewheel True draggable True pagekeys True xysize(1250, 598) pos(369,337)
        scrollbars "vertical"

        has vbox
        style_prefix "about"

        label "[config.name!t]"
        text _("Version [config.version!t]\n")

        if gui.about:
            text "[gui.about!t]\n" line_spacing -10

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label_text:
    size 70
style about_label:
    xalign 0.5
style about_text:
    xalign 0.5
    color u"#3b3738"
    text_align 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():


    default device = "keyboard"
    
    hbox:
        style_prefix "help"
        align(0.5, 0.5) spacing 80 yoffset 110
        frame:
            padding(50,40,50,85)
            xysize(484,642)
            background "gui/about/info_bg.png"
            viewport:
                scrollbars "vertical" draggable True mousewheel True 
                vbox:
                    spacing 20
                    style_prefix "lh"
                    use keyboard_help

        frame:
            padding(50,40,50,70)
            xysize(484,642)
            background "gui/about/info_bg.png"
            viewport:
                scrollbars "vertical" draggable True mousewheel True 
                vbox:
                    spacing 20
                    style_prefix "lh"
                    use mouse_help
        

style lh_vbox:
    spacing 5
style lh_text:
    justify True
    size 28
    xsize 350
    xalign 0.5
    text_align 0.5

style lh_button:
    xalign 0.5 xoffset 7
style lh_button_text:
    idle_color u"#fcd3e1"
    hover_color u"#ffffff"
    size 35

style help_vbox:
    xalign 0.5
    xoffset 10
    spacing 10

style lh_vbox:
    xalign 0.5
    xoffset 10
    spacing 0

style lh_label:
    xalign 0.5

style lh_label_text:
    color u"#fcd3e1"
    text_align 0.5
style help_vscrollbar:
    xoffset 10


screen wop:
    viewport:
        vbox:
            xalign 0.5 xsize 600
            #style_prefix "help"
            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")



            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help


screen keyboard_help():

    vbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    vbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    vbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    vbox:
        label _("Escape")
        text _("Accesses the game menu.")

    vbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    vbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    vbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    vbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    vbox:
        label "H"
        text _("Hides the user interface.")

    vbox:
        label "S"
        text _("Takes a screenshot.")

    vbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    vbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    if GamepadExists():

        vbox:
            label _("Right Trigger\nA/Bottom Button")
            text _("Advances dialogue and activates the interface.")

        vbox:
            label _("Left Trigger\nLeft Shoulder")
            text _("Rolls back to earlier dialogue.")

        vbox:
            label _("Right Shoulder")
            text _("Rolls forward to later dialogue.")


        vbox:
            label _("D-Pad, Sticks")
            text _("Navigate the interface.")

        vbox:
            label _("Start, Guide, B/Right Button")
            text _("Accesses the game menu.")

        vbox:
            label _("Y/Top Button")
            text _("Hides the user interface.")

        vbox:
            spacing 5
            text "•" color u"#fcd3e1"
            textbutton _("Calibrate") action GamepadCalibrate()
            text "•" color u"#fcd3e1"


    vbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    vbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    vbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    vbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    vbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")

    
