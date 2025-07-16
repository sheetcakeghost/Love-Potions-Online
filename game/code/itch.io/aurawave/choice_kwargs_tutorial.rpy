# You will need to replace the code in screen choice(items) in screens.rpy with the following.
# I just moved it to this file so you don't have to scroll down to it.

# https://aura-wave.itch.io/

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

# You should probably use this config along with the rest of the code.
# You may want to place it in options.rpy with other configs.
#define config.menu_include_disabled = True

screen choice(items, background=None):
    style_prefix "choice"

    if background is not None:
        # This adds a specific background image behind the choices.
        # By default, there will be no background unless you pass a menu argument.
        # 'background' must be a string matching an image filename (without .png).
        # The image must exist in your game/images folder or you’ll get an error.
        add "[background].png" xalign 0.5 ypos 405 yanchor 0.5 # Positioning matches the default "choice_vbox", feel free to change.

    vbox:
        $ visible_items = [i for i in items if i.kwargs.get("condition", True)]
        for i in visible_items:
            $ color = i.kwargs.get("color", None)
            $ hover = i.kwargs.get("hover", None)
            $ tooltip_text = i.kwargs.get("tooltip_text", None) # Optional: Only needed for tooltip functionality.

            textbutton i.caption:
                action i.action
                sensitive i.kwargs.get("sensitive", True)

                # Only apply custom colors if the button is active.
                # Disabled choices will use gui.choice_button_text_insensitive_color
                if i.kwargs.get("sensitive", True):
                    if color is not None:
                        text_color color
                    if hover is not None:
                        text_hover_color hover

## Tooltip Functionality ###############################################################
                # If you want tooltip functionality in your choice menus, keep this part.
                # If not, only copy and paste up to the above line.
                
                if tooltip_text is not None:
                    tooltip tooltip_text
    
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame: # Feel free to customize the appearance of this tooltip.
                xalign 1.0
                background "#0008"
                xmaximum 500
                text tooltip size 20 color "#fff"


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing 20

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