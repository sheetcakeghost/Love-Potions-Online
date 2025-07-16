################################################################################
##
## Truncated Text for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.1
##
################################################################################
## This file contains an example screen demonstrating how to use the truncate_text
## screen language statement. You are free to delete this file if you don't
## need the examples; all the backend code is in 01_truncate_text.rpy.
##
## To see the example truncated text screen, jump to the included
## test_truncate_text label e.g.
##
# label start:
#     jump test_truncate_text
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
default tt_test_variable = "This is a test variable"
define tt_ruby_demo = "Ruby text is also handled. (東{rt}とう{/rt} 京{rt}きょう{/rt}) ({rb}東京{/rb}{rt}Tokyo{/rt}) (【東｜とう】 【京｜きょう】) (【東京｜Tokyo】) - Make sure your font handles Japanese characters." if renpy.version(True) >= (8, 3) else "Ruby text is also handled. However, in earlier Ren'Py versions, there is a bug with displaying all ruby text. Please update to 8.3+ for ruby text support!"
screen truncate_text_examples():

    default the_text_size = gui.text_size
    default frame_x = int(config.screen_width/3.0)
    default frame_y = int(config.screen_height/5.0)
    default possible_colors = [ "periwinkle", "red", "a very dark shade of purple", "pale green" ]
    default a_color = renpy.random.choice(possible_colors)
    default example_page = 1


    add "#21212d"
    ## Note that truncate_text is a container + text, like a textbutton, so
    ## style prefixes mean it will get the <prefix>_tcontainer and
    ## <prefix>_tcontainer_text styles (e.g. truncation_tcontainer and
    ## truncation_tcontainer_text).
    ## The default tcontainer and tcontainer_text styles are in 01_truncate_text.rpy
    style_prefix 'truncation'

    vbox:
        spacing 20
        if example_page == 1:
            frame:
                xsize frame_x ysize frame_y
                truncate_text _("Here is some sample text, which will only cut off on spaces. This is because of the separators property, which is set to \" \""):
                    yalign 0.5
                    ## Separators are a string of characters that can be used to
                    ## split the text. In this case, it will only split on
                    ## spaces. You could include more characters, like hyphens
                    ## e.g. " -". If not provided, it'll split on any character.
                    separators " "
                    ## truncate_text is a container + text, like a textbutton.
                    ## To pass properties to the text, it needs the text_ prefix.
                    ## So, text_size changes the size of the text.
                    text_size the_text_size

            frame:
                xsize frame_x ysize frame_y
                truncate_text _("Notice that the text for this one will have a tooltip for the full text if it can't fit. It doesn't have separators so it can split on any character. The suffix is also different."):
                    text_size the_text_size yalign 0.5
                    ## This one uses the suffix property to change what's shown
                    ## when the text is cut off. The default is "...".
                    suffix "—"
                    ## has_tooltip will automatically add a tooltip to the text
                    ## container if the text is cut off. It's a shortcut to
                    ## having the tooltip be identical to the text, and it only
                    ## happens when the text isn't fully displayed.
                    has_tooltip True

            frame:
                xsize frame_x ysize frame_y
                truncate_text _("This text will try to reduce line spacing to fit before it is truncated. It will reset the line spacing upon being truncated. It does not reduce the text size."):
                    ## The default line spacing is 0. This means it will go to
                    ## a minimum of -10 when trying to make it fit.
                    adjust_line_spacing_to_fit -10
                    ## Ensures the string still truncates if it doesn't fit.
                    truncate_after_shrink True
                    ## This will reset the spacing to the default if it
                    ## doesn't fit.
                    reset_spacing_on_overflow True
                    text_size the_text_size yalign 0.5

            frame:
                xsize frame_x ysize frame_y
                truncate_text _("This text will both adjust line spacing and also shrink to fit. It will try to adjust the line spacing before every size change."):
                    ## We're giving this a larger text spacing so the
                    ## effect is more obvious.
                    text_line_spacing 12
                    ## shrink_to_fit 10 means it will go to a minimum of size 10
                    ## when trying to fit in the available space.
                    ## adjust_line_spacing_to_fit -10 means it will try to
                    ## set the line_spacing to a minimum of -10 when trying to
                    ## fit.
                    shrink_to_fit 10 adjust_line_spacing_to_fit -10
                    ## This means it will loop through the spacing adjustments
                    ## before going to the next size down.
                    shrink_before_spacing False
                    text_size the_text_size yalign 0.5
        else:
            frame:
                xsize frame_x ysize frame_y
                truncate_text _("The {=test_style}text will also {/=test_style}{size=+20}{b}intelligently{/b}{/size} handle things like {i}text tags,{/i} as well as {a=https://renpy.org}hyperlinks, so they will work even when truncated{/a}."):
                    ## Text tags are automatically adjusted when the text is
                    ## truncated, so that hyperlinks will still work on whatever
                    ## text is inside the hyperlink tags where possible.
                    text_size the_text_size yalign 0.5

            frame:
                xsize frame_x ysize frame_y
                truncate_text _("This text will shrink to fit the available space rather than being truncated, unless it's still too big. It will stay at the smaller size if it is truncated."):
                    ## This means that the text can go as small as size 18 to
                    ## try to fit in the available space.
                    shrink_to_fit 18
                    ## This means that if the text still doesn't fit at the
                    ## smallest size, when it's truncated it won't be reset to
                    ## its original size. By default, reset_size_on_overflow is
                    ## True, which will reset the size when the text is
                    ## truncated.
                    reset_size_on_overflow False
                    text_size the_text_size yalign 0.5

            frame:
                xsize frame_x ysize frame_y
                viewport:
                    scrollbars "vertical" scrollbar_unscrollable "hide"
                    truncate_text _("This text gets shrunk down, but if it doesn't fit, it will reset to its original size. It's in a viewport which will add a scrollbar if necessary since it has a target_size but not a set size."):
                        text_size the_text_size yalign 0.5
                        ## This text will try to shrink down to size 24 to
                        ## fit. It will not attempt truncation if shrinking
                        ## doesn't work.
                        shrink_to_fit 24 truncate_after_shrink False
                        ## If the text is too big after shrinking, this resets
                        ## its size to the original size.
                        reset_size_on_overflow True
                        ## Since the viewport has infinite space and we want
                        ## to take advantage of that, we give a "soft" target
                        ## size for the text to fit. If it can't fit, it won't
                        ## truncate due to truncate_after_shrink being False,
                        ## and it will reset to its original size because of
                        ## reset_size_on_overflow. That means the scroll bar
                        ## will kick in.
                        target_size (frame_x-30, frame_y-30)

            frame:
                xsize frame_x ysize frame_y
                viewport:
                    scrollbars "vertical" scrollbar_unscrollable "hide"
                    truncate_text _("This text is similar to the last one, but it will prioritize shrinking text before adjusting line spacing, and then if neither makes it fit, it will reset to the original size."):
                        text_size the_text_size yalign 0.5
                        shrink_to_fit 24 truncate_after_shrink False
                        ## This means that the text will try to shrink down to
                        ## size 24 before it adjusts the line spacing.
                        shrink_before_spacing True
                        ## This will adjust the line spacing to a minimum of
                        ## -10 when trying to fit in the available space.
                        adjust_line_spacing_to_fit -10
                        ## If the text is too big after shrinking, this resets
                        ## its size to the original size.
                        reset_size_on_overflow True
                        ## This is the same, but to reset spacing
                        reset_spacing_on_overflow True
                        ## Since the viewport has infinite space and we want
                        ## to take advantage of that, we give a "soft" target
                        ## size for the text to fit. If it can't fit, it won't
                        ## truncate due to truncate_after_shrink being False,
                        ## and it will reset to its original size because of
                        ## reset_size_on_overflow. That means the scroll bar
                        ## will kick in.
                        target_size (frame_x-30, frame_y-30)

    vbox:
        spacing 20 xalign 1.0
        hbox:
            spacing 40 xalign 0.5
            textbutton "EXAMPLE SET 1" action SetScreenVariable("example_page", 1):
                background "#ff8335" text_color "#fff" text_outlines [ (1, "#000")]
                hover_background "#ffb35c" padding (15, 15) selected_background "#ca5f1c"
            textbutton "EXAMPLE SET 2" action SetScreenVariable("example_page", 2):
                background "#ff8335" text_color "#fff" text_outlines [ (1, "#000")]
                hover_background "#ffb35c" padding (15, 15) selected_background "#ca5f1c"
        hbox:
            spacing 20 xalign 1.0
            text "Change text size" min_width 360
            bar value ScreenVariableValue("the_text_size", range=gui.text_size*3, offset=1):
                xsize 0.3
        hbox:
            spacing 20 xalign 1.0
            text "Change frame width" min_width 360
            bar value ScreenVariableValue("frame_x", range=int(config.screen_width/2.0)) xsize 0.3
        hbox:
            spacing 20 xalign 1.0
            text "Change frame height" min_width 360
            bar value ScreenVariableValue("frame_y", range=int(config.screen_height/3.5)) xsize 0.3

        if example_page == 1:
            textbutton _("Cycle color: [a_color]") action SetScreenVariable("a_color",
                possible_colors[(possible_colors.index(a_color) + 1) % len(possible_colors)])

        null height 20
        if example_page == 1:
            frame:
                xsize frame_x ysize frame_y
                truncate_text _("It will also substitute variables, both global and local to the screen. For example, a random color is [a_color], which we might use in many places, such as this chair, which is [a_color]. A global variable is [tt_test_variable]."):
                    text_size the_text_size yalign 0.5
                    ## The suffix can be quite long if so desired.
                    separators ' ' suffix _(" {i}(continued){/i}")
                    ## This will add a tooltip if the text doesn't fit. Unlike
                    ## the previous example, setting it to "rest" means it will
                    ## only have the text that didn't fit (rather than the
                    ## whole thing).
                    has_tooltip "rest"

            frame:
                xsize frame_x ysize frame_y
                truncate_text _("It can handle escaped characters like \"quotes\" \\backslashes\\ [[square brackets] {{curly braces} \'apostrophes\'"):
                    text_size the_text_size yalign 0.5

        else:

            frame:
                xsize frame_x ysize frame_y
                truncate_text tt_ruby_demo:
                    text_style 'tt_ruby_tcontainer_text' text_size the_text_size yalign 0.5

            frame:
                xsize frame_x ysize frame_y
                truncate_text _("This text will shrink to fit the available space rather than being truncated, unless it's still too big. It will reset to its original size if it's truncated."):
                    ## This means that the text can go as small as size 20 to
                    ## try to fit in the available space.
                    shrink_to_fit 20
                    ## Unlike the other example, this text *will* reset to its
                    ## original size if it's truncated.
                    reset_size_on_overflow True
                    text_size the_text_size yalign 0.5


    ## In order for truncate_text with the has_tooltip property to show a
    ## tooltip, you need to set up the tooltip in the screen like you
    ## usually would.
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            frame:
                xmaximum 0.5
                text tooltip align (0.5, 0.5)

style tt_ruby_style is default:
    size 20
    yoffset -36
    color None # Use the same color as the parent text.
    ## NOTE: if your font doesn't support Japanese characters, they will
    ## show up as boxes. You can set the font to a different one here.
    # font "SourceHanSansLite.ttf"

define tt_ruby_properties = dict(ruby_line_leading=25) if renpy.version(True)>= (8, 3) else dict(line_leading=25)
style tt_ruby_tcontainer_text:
    is gui_text
    properties tt_ruby_properties
    size 36
    ruby_style style.tt_ruby_style
    ## NOTE: if your font doesn't support Japanese characters, they will
    ## show up as boxes. You can set the font to a different one here.
    # font "SourceHanSansLite.ttf"
style truncate_example_hyperlink:
    underline True color "#66f" size 70 hover_color "#22f"

init python:
    def custom_hyperlink_styler(val):
        return style.truncate_example_hyperlink

style truncation_tcontainer_text:
    is gui_text
    hyperlink_functions (custom_hyperlink_styler, hyperlink_function, None, hyperlink_sensitive)

style test_style:
    color "#F0F"
    font "DejaVuSans.ttf"
    hyperlink_functions (custom_hyperlink_styler, hyperlink_function, None, hyperlink_sensitive)

style my_hyperlink_text_style:
    color "#ff8335"
    hyperlink_functions (custom_hyperlink_styler, hyperlink_function, None, hyperlink_sensitive)


label test_truncate_text():
    "This is a demonstration of the truncate_text screen displayable."
    call screen truncate_text_examples
    "The End."
    return