################################################################################
##
## Truncated Text for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.1
##
################################################################################
## This file contains code for a text truncation displayable in Ren'Py. There is
## both a CDD to handle the rendering of the text, and a screen language keyword
## so it can be easily declared in-game. It's a displayable that will cut off
## the text at pre-determined points if it's too long to fit its container.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## If you'd like to see how to use this tool, check the other file,
## truncate_text_examples.rpy! This is just the backend; you don't need to
## understand everything in this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**01_truncate_text.rpy", None)
    build.classify("**01_truncate_text.rpyc", "archive")
################################################################################
##
## HOW TO WRITE
##
## You will write truncate_text just like any other text displayable in Ren'Py
## e.g. `truncate_text "Some text."`
## It is a container + text like a textbutton, so you can style both the outer
## container and the text inside it. To pass text properties, they need
## to be prefixed with `text_` such as `text_size` or `text_color`.
## The container itself takes the same properties as a frame or button, such
## as padding, xsize, ysize, pos, etc.
##
## TRUNCATION METHODS - CUTTING OFF TEXT
##
## The first method to make text fit is by removing characters from the end
## until it fits e.g. "This is some long text." might become "This is some..."
## This is always the final method applied if the later two do not make it fit.
##
## RELEVANT PROPERTIES:
##
## separators - a string of characters that can be split on. If not provided,
## the text will be split on any character. For example, you can use
## `separators " "` to only split on spaces, or `separators "- "` to split on
## spaces and hyphens.
##
## suffix - the suffix to add to the text if it is truncated. By default,
## it is "...". You can change it to whatever you like, and use text tags or
## otherwise e.g. `suffix " {i}(continued){/i}"`
## You can also set it to "" so there is no suffix at all.
##
## has_tooltip - can be one of three values:
## True - the full text is displayed as a tooltip if the text is truncated.
## "rest" - the text which was cut off is displayed as a tooltip.
## False - no tooltip is displayed. This is the default.
## Note that you can still use the tooltip property to set a permanent tooltip,
## but has_tooltip will override it if the text is truncated.
##
## target_size - a tuple of (width, height) which the truncated text should
## attempt to fit inside. None by default, which means it will use the available
## space in the container. This can be helpful if you want to attempt to fit
## the text inside a specific space, but if it doesn't fit, then you want the
## displayable to reflect the actual size the text takes up (vs the container
## space that it's too big for).
## This is most helpful if you're using the tool in combination with viewports
## or my Marquee tool (https://feniksdev.itch.io/marquee-for-renpy)
##
## TRUNCATION METHODS - SHRINKING TEXT
##
## The next method is to adjust the size of the text until it fits. This uses
## the text size property, so it maintains crispness and formatting/it's not
## just zooming the text.
##
## RELEVANT PROPERTIES:
##
## shrink_to_fit - an integer which is the smallest text size that will be used
## to try to fit the text in the available space. So, if `shrink_to_fit 14`,
## the text size will be reduced until it fits or until it's 14px, whichever
## comes sooner.
##
## reset_size_on_overflow - if True, and shrink_to_fit is not 0, the text size
## will be reset to the original size if it does not fit after shrinking to its
## minimum size. If False, it will remain at the smallest size.
## Defaults to True.
##
## truncate_after_shrink - if True and shrink_to_fit is not 0, if the text
## does not fit inside the available space after being shrunk to the minimum
## size and/or having its line spacing adjusted, it will be truncated to fit.
## True by default.
##
## TRUNCATION METHODS - ADJUSTING LINE SPACING
##
## The final method is to adjust the line spacing of the text until it fits.
## This uses the line_spacing property, so it similarly maintains crispness
## and formatting.
##
## RELEVANT PROPERTIES:
##
## adjust_line_spacing_to_fit - an integer which is the smallest line spacing
## that will be used to try to fit the text in the available space. Typically,
## line_spacing starts at 0, so this is usually a negative number.
## If None, it will not be adjusted. Defaults to None.
## e.g. `adjust_line_spacing_to_fit -10` will reduce the line spacing until
## it fits or until it reaches -10, whichever comes sooner.
##
## reset_spacing_on_overflow - if True, and adjust_line_spacing_to_fit is not
## None, the line spacing will be reset to the original line spacing if it
## does not fit after applying the line spacing and/or text size adjustments.
## If False, it will remain at the smallest line spacing. Defaults to True.
##
## shrink_before_spacing - if True, the text will attempt to shrink to its
## smallest size first before it applies any line spacing adjustments to make
## it fit. If False, the default, it will loop through the line spacing
## adjustments before shrinking to the next smallest text size.
## Example: shrink_to_fit=22, the default size=24, adjust_line_spacing_to_fit=-2,
## and the default line_spacing=0
##      shrink_before_spacing=True:
## It will first check if size=24 line_spacing=0 fits, then size=24
## line_spacing=-1, then size=24 line_spacing=-2, then size=23 line_spacing=0,
## then size=23 line_spacing=-1, etc.
##      shrink_before_spacing=False:
## It will first check if size=24 line_spacing=0 fits, then size=23
## line_spacing=0, then size=22 line_spacing=0, then size=22 line_spacing=-1,
## then size=22 line_spacing=-2 etc.
##
## OTHER PROPERTIES
##
## refresh_per_interact - defaults to True, which means on a new interaction/
## screen refresh, it'll adjust the text to make sure it fits. This is usually
## what you want, but in the event that your container size and text contents
## will not change (i.e. you have no variables in them), you can set this to
## False to avoid the overhead of looping to make the text fit.

################################################################################
python early:

    class TruncateText(Button, Window):
        """
        Creates a special text displayable that truncates the text if it
        exceeds the provided size.

        Attributes:
        -----------
        text : str
            The text to display.
        remaining_text : str
            The remaining text that was omitted after truncation.
        has_tooltip : bool
            If True, the full text is displayed as a tooltip if the text is
            truncated. If "rest", the text which was cut off is displayed as
            a tooltip. If False, no tooltip is displayed.
        separators : str
            If provided, this is a string of characters that are considered
            separators for truncation. Text will only be split along these
            characters. Use this to only split on spaces or hyphens, for example.
        suffix : str
            The suffix to add to the text if it is truncated. By default,
            it is "...".
        refresh_per_interact : bool
            If True, the displayable is refreshed each new interaction. If
            False, it won't be. True by default.
        shrink_to_fit : int
            If not 0, this is an integer which is the smallest text size that
            will be used to try to fit the text in the available space.
        adjust_line_spacing_to_fit : int
            If not 0, the line spacing will be adjusted by a maximum of this
            amount to try to fit the text in the available space. If None, it
            will not be adjusted. Defaults to None. These numbers should usually
            be negative.
        reset_size_on_overflow : bool
            If True, and shrink_to_fit is not 0, the text size will be reset
            to the original size if it does not fit after shrinking to its
            minimum size. If False, it will remain at the smallest size.
            Defaults to True.
        reset_spacing_on_overflow : bool
            If True, and adjust_line_spacing_to_fit is not None, the line spacing
            will be reset to the original line spacing if it does not fit after
            adjusting the line spacing to its minimum size. If False, it will
            remain at the smallest line spacing. Defaults to True.
        truncate_after_shrink : bool
            If True and shrink_to_fit is not 0, if the text does not fit inside
            the available space after being shrunk to the minimum size and/or
            having its line spacing adjusted, it will be truncated to fit. If
            False, it will not be truncated. True by default. Can be used with
            reset_size_on_overflow to have truncation occur at the smallest
            size or the default size.
        shrink_before_spacing : bool
            If True, the text will attempt to shrink to its smallest size first
            before it applies any line spacing adjustments to make it fit. If
            False, the default, it will loop through the line spacing
            adjustments before shrinking to the next smallest text size.
        target_size : tuple
            A tuple of (width, height) which the truncated text should fit
            inside. Other size properties/container sizes should be used instead
            of this property such as xsize, ymaximum etc. except if you are
            using truncate_after_shrink False, in which case you may wish to
            use this so that it will work with viewport scrollbars with its
            actual size.
        text_properties : dict
            A dictionary of properties to pass to the Text displayable.
        was_truncated : bool
            True if the text was truncated.
        truncated_text : Text
            The truncated text displayable.
        """
        ## Character combinations that should never be split up
        UNSPLITTABLE = ["\%", "%%", "\n", "\\", "{{", "【【"]
        def __init__(self, text, *args, **kwargs):
            self.text = text
            self.remaining_text = ""
            self.has_tooltip = kwargs.pop("has_tooltip", False)
            self.text_properties = dict()
            self.separators = kwargs.pop("separators", None)
            self.suffix = kwargs.pop("suffix", "...")
            self.refresh_per_interact = kwargs.pop("refresh_per_interact", True)
            self.was_truncated = False
            self.shrink_to_fit = kwargs.pop("shrink_to_fit", 0)
            self.reset_size_on_overflow = kwargs.pop("reset_size_on_overflow", True)
            self.truncate_after_shrink = kwargs.pop("truncate_after_shrink", True)
            self.target_size = kwargs.pop("target_size", None)
            self.adjust_line_spacing_to_fit = kwargs.pop("adjust_line_spacing_to_fit", None)
            self.reset_spacing_on_overflow = kwargs.pop("reset_spacing_on_overflow", True)
            self.shrink_before_spacing = kwargs.pop("shrink_before_spacing", False)

            og_style = kwargs.pop('style', None)
            if og_style is None:
                style = ui.prefixed_style("tcontainer")
            else:
                style = og_style
            og_text_style = kwargs.pop('text_style', None)
            if og_text_style is None:
                text_style = renpy.style.get_text_style(style, ui.prefixed_style('text'))
            else:
                text_style = og_text_style

            ## Separate out text_ properties.
            self.text_properties, self.button_properties = renpy.easy.split_properties(kwargs, "text_", "")
            self.text_properties['style'] = text_style
            self.button_properties['style'] = style

            ## Ensure the text accounts for the current screen scope.
            cs = renpy.current_screen()
            if cs is None:
                scope = None
            else:
                scope = cs.scope
            self.text_properties['scope'] = scope
            child = Text(self.text, **self.text_properties)
            self.truncated_text = None
            if self.has_tooltip or 'tooltip' in self.button_properties:
                self.parent_class = Button
            else:
                self.parent_class = Window
                self.action = None
            self.parent_class.__init__(self, child, *args, **self.button_properties)
            if self.has_tooltip and not self.action:
                self.action = NullAction()


        def per_interact(self):
            """
            A method that runs once per interaction. Refreshes the truncated
            text if needed.
            """
            if self.refresh_per_interact:
                self.truncated_text = None
                renpy.redraw(self, 0)
            return self.parent_class.per_interact(self)

        def _get_tooltip(self):
            """Return the tooltip text."""
            if self.has_tooltip and self.was_truncated:
                if self.has_tooltip == "rest":
                    return self.remaining_text
                return self.text
            elif self.has_tooltip:
                return None
            return self.parent_class._get_tooltip(self)

        def get_container_size(self, width, height):
            """
            Return the size of the space that will be available to the child
            of this button (aka the text). Basically, accounts for padding,
            margins, and size.
            """
            style = self.style
            try:
                compute_raw = renpy.display.layout.compute_raw
            except AttributeError:
                def compute_raw(value, room):
                    if isinstance(value, (absolute, int)):
                        return value
                    elif isinstance(value, float):
                        return value * room
                    elif isinstance(value, position):
                        return value.relative * room + value.absolute
                    raise TypeError("Value {} of type {} not recognized as a position.".format(value, type(value)))

            xminimum, yminimum = renpy.display.layout.xyminimums(style, width, height)

            xmaximum = self.style.xmaximum
            ymaximum = self.style.ymaximum

            if type(xmaximum) is float:
                xmaximum = width
            if type(ymaximum) is float:
                ymaximum = height

            size_group = self.style.size_group
            if size_group and size_group in size_groups:
                xminimum = max(xminimum, size_groups[size_group].width(width, height, st, at))

            width = max(xminimum, width)
            height = max(yminimum, height)

            left_margin = compute_raw(style.left_margin, width)
            left_padding = compute_raw(style.left_padding, width)

            right_margin = compute_raw(style.right_margin, width)
            right_padding = compute_raw(style.right_padding, width)

            top_margin = compute_raw(style.top_margin, height)
            top_padding = compute_raw(style.top_padding, height)

            bottom_margin = compute_raw(style.bottom_margin, height)
            bottom_padding = compute_raw(style.bottom_padding, height)

            # c for combined.
            cxmargin = left_margin + right_margin
            cymargin = top_margin + bottom_margin

            cxpadding = left_padding + right_padding
            cypadding = top_padding + bottom_padding

            return (width - cxmargin - cxpadding, height - cymargin - cypadding)

        def test_fit(self, txt, properties, aw, ah, st, at):
            """
            Test if the provided text with the given properties fits inside
            the container size. Returns True if it fits, False otherwise.
            """
            txt_disp = Text(txt, **properties)
            txt_width, txt_height = txt_disp.render(aw, ah, st, at).get_size()
            if txt_width <= aw and txt_height <= ah:
                return txt_disp
            return False

        def get_text_property(self, properties, prop_name, default=None):
            ret = properties.get(prop_name, None)
            if ret is not None:
                return ret
            ## Otherwise, get it from the style
            tstyle = None
            if 'style' in properties:
                tstyle = properties['style']
            else:
                tstyle = self.text_properties.get('style', None)
            if tstyle is None:
                tstyle = 'tcontainer_text'
            if isinstance(tstyle, str):
                ## Grab the style object
                tstyle = getattr(style, tstyle, None)
            if tstyle is not None:
                tstyle = getattr(style, 'text')

            return getattr(tstyle, prop_name, default)

        def render(self, width, height, st, at):

            if not self.truncated_text:
                self.was_truncated = False
                ## Substitute text, so we aren't splitting up any variables.
                cs = renpy.current_screen()
                if cs is None:
                    scope = None
                else:
                    scope = cs.scope
                the_text = renpy.substitute(self.text, scope=scope)
                ## First, check if the full thing fits
                self.text_properties['substitute'] = False
                txt = Text(the_text, **self.text_properties)
                if self.target_size:
                    ## If we have a target size, use that instead of the
                    ## container size.
                    aw, ah = self.target_size
                    try:
                        compute_raw = renpy.display.layout.compute_raw
                    except AttributeError:
                        def compute_raw(value, room):
                            if isinstance(value, (absolute, int)):
                                return value
                            elif isinstance(value, float):
                                return value * room
                            elif isinstance(value, position):
                                return value.relative * room + value.absolute
                            raise TypeError("Value {} of type {} not recognized as a position.".format(value, type(value)))
                    aw = compute_raw(aw, width)
                    ah = compute_raw(ah, height)
                else:
                    ## Get the size of the area the text goes in (a=actual)
                    aw, ah = self.get_container_size(width, height)
                ## Render the current text
                txt_width, txt_height = txt.render(aw, ah, st, at).get_size()
                if txt_width <= aw and txt_height <= ah:
                    self.truncated_text = txt
                else:
                    new_text_properties = self.text_properties.copy()
                    successful_shrink = False
                    the_size = self.get_text_property(new_text_properties, "size", gui.text_size)
                    the_spacing = self.get_text_property(new_text_properties, "line_spacing", 0)
                    if (self.shrink_to_fit
                            or self.adjust_line_spacing_to_fit is not None):
                        ## First, we'll try to shrink the text down to fit.
                        while the_size > self.shrink_to_fit:
                            if (not self.shrink_before_spacing
                                    and self.adjust_line_spacing_to_fit is not None):
                                ## Loop through the line spacing at this size
                                while the_spacing > self.adjust_line_spacing_to_fit:
                                    the_spacing -= 1
                                    new_text_properties['line_spacing'] = the_spacing
                                    txt = self.test_fit(the_text, new_text_properties, aw, ah, st, at)
                                    if txt:
                                        self.truncated_text = txt
                                        successful_shrink = True
                                        self.was_truncated = False
                                        break
                            if successful_shrink or not self.shrink_to_fit:
                                break
                            elif (not self.shrink_before_spacing
                                    and self.adjust_line_spacing_to_fit is not None):
                                ## Reset the spacing
                                the_spacing = self.get_text_property(self.text_properties, "line_spacing", 0)

                            the_size -= 1
                            new_text_properties['size'] = the_size
                            txt = self.test_fit(the_text, new_text_properties, aw, ah, st, at)
                            if txt:
                                self.truncated_text = txt
                                successful_shrink = True
                                self.was_truncated = False
                                break

                        if (not successful_shrink
                                and self.adjust_line_spacing_to_fit is not None
                                and self.shrink_before_spacing):
                            ## Tried to shrink; need to try spacing now
                            while the_spacing > self.adjust_line_spacing_to_fit:
                                the_spacing -= 1
                                new_text_properties['line_spacing'] = the_spacing
                                txt = self.test_fit(the_text, new_text_properties, aw, ah, st, at)
                                if txt:
                                    self.truncated_text = txt
                                    successful_shrink = True
                                    self.was_truncated = False
                                    break

                    if not successful_shrink and self.truncate_after_shrink:
                        ## Reset the size to the original, if necessary
                        if self.reset_size_on_overflow:
                            new_text_properties['size'] = self.get_text_property(
                                self.text_properties, "size", 0)
                        if self.reset_spacing_on_overflow:
                            new_text_properties['line_spacing'] = self.get_text_property(
                                self.text_properties, "line_spacing", 0)
                        ## Otherwise, loop until it's truncated
                        i = len(the_text) - max(len(renpy.substitute(renpy.filter_text_tags(self.suffix, allow=[]), scope=scope)), 1)
                        splits = valid_split_points(the_text, self.separators)
                        for i in reversed(splits):
                            txt = Text(check_text_tags(the_text[:i]) + self.suffix,
                                **new_text_properties)
                            txt_width, txt_height = txt.render(aw, ah, st,
                                at).get_size()
                            if self.has_tooltip == "rest":
                                self.remaining_text = get_opening_tags(the_text,
                                    the_text[i:])
                            if txt_width <= aw and txt_height <= ah:
                                self.truncated_text = txt
                                self.was_truncated = True
                                break

                        if not self.truncated_text:
                            ## If we couldn't truncate, just use the last text.
                            self.truncated_text = txt

                    elif not successful_shrink:
                        ## Couldn't shrink, and no truncation. Reset size
                        ## and spacing if needed.
                        if self.reset_size_on_overflow:
                            new_text_properties['size'] = self.get_text_property(
                                self.text_properties, "size", 0)
                        if self.reset_spacing_on_overflow:
                            new_text_properties['line_spacing'] = self.get_text_property(
                                self.text_properties, "line_spacing", 0)
                        self.truncated_text = Text(the_text, **new_text_properties)


                ## Ensure the button displays this as the child.
                self._clear()
                self.add(self.truncated_text)
                self.set_style_prefix(self.style.prefix, True)
                renpy.redraw(self, 0)
            return self.parent_class.render(self, width, height, st, at)

        def _in_current_store(self):
            return self.parent_class._in_current_store(self)
        def predict_one_action(self):
            return self.parent_class.predict_one_action(self)
        def focus(self, default=False):
            return self.parent_class.focus(self, default)
        def unfocus(self, default=False):
            return self.parent_class.unfocus(self)
        def is_selected(self):
            return self.parent_class.is_selected(self)
        def is_sensitive(self):
            return self.parent_class.is_sensitive(self)
        def event(self, ev, x, y, st):
            return self.parent_class.event(self, ev, x, y, st)
        def set_style_prefix(self, prefix, root):
            return self.parent_class.set_style_prefix(self, prefix, root)
        def _tts(self):
            return self.parent_class._tts(self)
        def _tts_all(self):
            return self.parent_class._tts_all(self)
        def set_transform_event(self, event):
            self.child.set_transform_event(event)
            return self.parent_class.set_transform_event(self, event)
        def set_style_prefix(self, prefix, root):
            self.child.set_style_prefix(prefix, root)
            return self.parent_class.set_style_prefix(self, prefix, root)

    ## Register the truncate text as a screen language keyword.
    renpy.register_sl_displayable("truncate_text", TruncateText,
        "tcontainer", 0,
        ).add_positional("text"
        ).add_property("has_tooltip"
        ).add_property("separators"
        ).add_property("suffix"
        ).add_property("refresh_per_interact"
        ).add_property("shrink_to_fit"
        ).add_property("adjust_line_spacing_to_fit"
        ).add_property("reset_size_on_overflow"
        ).add_property("reset_spacing_on_overflow"
        ).add_property("truncate_after_shrink"
        ).add_property("shrink_before_spacing"
        ).add_property("target_size"
        ).add_property("text_style"
        ).add_property_group("text", prefix="text_"
        ).add_property_group("window"
        ).add_property_group("button"
        ).add_property_group("ui")

init python:
    from collections import Counter
    import re

    def valid_split_points(text, separators=None):
        """
        Returns a list of valid split points in the text based on the
        provided separators and parts of the string which include unsplittable
        character combinations or text tags.
        """
        split_points = range(len(text))
        if separators:
            split_points = [i for i in split_points if text[i] in separators]
        for unsplittable in TruncateText.UNSPLITTABLE:
            unsplittable_len = len(unsplittable)
            ## Can split just before the unsplittable or after, none of the
            ## values in between
            for i in range(len(text)-unsplittable_len):
                if text[i:i+unsplittable_len] == unsplittable:
                    split_points = [j for j in split_points if j <= i or j >= i+unsplittable_len]
        ## Remove split points that are inside text tags
        text_tags = re.findall(r"{[^}]+}", text)
        last_index = dict()
        for tag in text_tags:
            tag_start = text.index(tag, last_index.get(tag, 0))
            last_index[tag] = tag_start + len(tag)
            if tag_start < len(text)-1 and text[tag_start+1] == "{":
                ## It's a cancelled tag start {{
                continue
            tag_end = tag_start + len(tag)
            if tag == "{rb}":
                ## e.g. ({rb}東京{/rb}{rt}Tokyo{/rt})
                ## Do NOT split until we get to a {/rt} tag
                tag_end = text.index("{/rt}", tag_start) + len("{/rt}")
            elif tag == "{rt}":
                ## We also cannot split on the character before the {rt} tag
                tag_start -= 1
                ## Don't split until getting to the {/rt} tag
                tag_end = text.index("{/rt}", tag_start) + len("{/rt}")
            split_points = [i for i in split_points if i <= tag_start or i >= tag_end]
        ## Do the same for text inside 【】
        text_tags = re.findall(r"【[^】]+】", text)
        last_index = dict()
        for tag in text_tags:
            tag_start = text.index(tag, last_index.get(tag, 0))
            last_index[tag] = tag_start + len(tag)
            if tag_start < len(text)-1 and text[tag_start+1] == "【":
                ## It's a cancelled tag start 【【
                continue
            tag_end = tag_start + len(tag)
            split_points = [i for i in split_points if i <= tag_start or i >= tag_end]
        return split_points

    def get_opening_tags(text, remaining_text):
        """
        Returns remaining_text with any opening text tags that were cut off
        before the truncation.
        """
        open_text_tags1, closed_text_tags1, tag_arguments1 = check_text_tags(text, True)
        open_text_tags2, closed_text_tags2, tag_arguments2 = check_text_tags(remaining_text, True)
        ## Idea: a string like {size=30}{b}{i}start{/i}{font=DejaVuSans.ttf}end{/font}{/b}{/size} where the remaining
        ## text is end{/font}{/b}{/size} will need {b} and {size} and {font} at the start but not
        ## {i} since it's already done. open1 will be size, b, i, font and closed1 will be
        ## i, font, b, size; open2 will be empty and closed2 will be font, b, size
        if not open_text_tags1:
            return remaining_text
        if not closed_text_tags2:
            return remaining_text
        ## Idea: match the closed tags2 to the latest open tag in the open list.
        ## First eliminate open tags that are in both.
        while open_text_tags2 and open_text_tags1:
            if open_text_tags2[-1] == open_text_tags1[-1]:
                ## pop them both off
                open_text_tags1.pop()
                open_text_tags2.pop()
                tag_arguments1.pop()
                tag_arguments2.pop()
            else:
                break

        final_openings = ""
        ## Now we should be left with just closed tags and the opening tags
        ## that belong to them. However, they're not guaranteed to be in the
        ## same order.
        for tg in closed_text_tags2:
            i = len(open_text_tags1) - 1
            while i >= 0:
                if tg == open_text_tags1[i]:
                    final_openings += "{" + open_text_tags1[i]
                    if tag_arguments1[i]:
                        final_openings += "=" + tag_arguments1[i]
                    final_openings += "}"
                    open_text_tags1.pop(i)
                    tag_arguments1.pop(i)
                    break
                i -= 1
        return final_openings + remaining_text


    ## The following code is written by Windchimes from Wind Chimes Games!
    ## https://wind-chimes-games.itch.io/
    def multiple_replace(replacement_pattern, txt):
        for orig, replacement in replacement_pattern:
            txt = re.sub(orig, replacement, txt, flags=re.IGNORECASE)
        return txt

    def check_text_tags(txt, return_tag_lists=False):
        # Take out any curly brackets that are supposed to be displayed as text
        # and not intended to be a text tag
        if re.compile("|".join(["{{", r"\\{", "}}", "}}}"])).search(txt):
            replaced_double_curly_brackets = True
            txt = multiple_replace([("{{", "<001>"), (r"\\{", "<002>"), ("}}}",
                "<003>"), ("}}", "<004>")], txt)
        else:
            replaced_double_curly_brackets = False

        # Split text into separate strings of pure text and {} tags
        split_string = re.split(r"(?={)|(?<=})", txt)

        # If the last split string got cut off mid-text tag, remove it entirely,
        # because if it's an open text tag, it doesn't matter since the text
        # after it that the text tag applies to doesn't exist anymore anyway.
        # If it's a closing text tag, missing closing text tags based on open
        # text tags will be handled later
        if split_string[-1].startswith("{") and not split_string[-1].endswith("}"):
            split_string.pop()

        # Grab all the text tags only
        text_tags_strings_list = [x for x in split_string if x and x.startswith("{")]

        open_text_tags = []
        closed_text_tags = []
        tag_arguments = []

        # Sort the text tags into open text tags list and closing text tags list
        for text_tag in text_tags_strings_list:
            if text_tag.startswith("{/="):
                closed_text_tags.append("="+text_tag[text_tag.find("=")+1:text_tag.find("}")])
            elif text_tag.startswith("{/"):
                closed_text_tags.append(
                    text_tag[text_tag.find("{/")+2:text_tag.find("}")])
            else:
                if text_tag.startswith("{="): # for {=style tags
                    open_text_tags.append("="+text_tag[text_tag.find("=")+1:text_tag.find("}")])
                    tag_arguments.append("")
                elif "=" in text_tag:
                    # for tags that use = to provide arguments
                    # like {a=} hyperlink and {color=} {font=} etc.
                    open_text_tags.append(text_tag[text_tag.find("{")+1:text_tag.find("=")])
                    tag_arguments.append(text_tag[text_tag.find("=")+1:text_tag.find("}")])
                else:
                    open_text_tags.append(text_tag[text_tag.find("{")+1:text_tag.find("}")])
                    tag_arguments.append("")

        if return_tag_lists:
            # Return the lists of open and closed text tags
            return open_text_tags, closed_text_tags, tag_arguments

        # Make list of tags that are opened but not closed
        open_text_tags = list(Counter(open_text_tags) - Counter(closed_text_tags))
        if open_text_tags:
            # Add closing text tags for the remaining open text tags
            for remaining_tag in open_text_tags:
                split_string.append("{/"+remaining_tag+"}")

        # Re-compile the final text again
        final_string = "".join(split_string)

        # Revert the curly brackets replacements
        if replaced_double_curly_brackets:
            final_string = multiple_replace([("<001>", "{{"), ("<002>", "\{"),
                ("<003>", "}}}"), ("<004>", "}}")], final_string)

        return final_string

style tcontainer is empty
style tcontainer_text is text