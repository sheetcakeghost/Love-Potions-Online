https://feniksdev.itch.io/truncated-text-for-renpy

Overview
This screen language add-on includes a truncate_text displayable which acts like text, but will truncate (cut off) and/or shrink words that won't fit inside the available space otherwise. Useful for message previews, adapting to different text sizes for accessibility, shortening long notifications or player-inputted text, shortening on-screen UI for quests or inventory items, translations, read-more buttons, and more.

Features
Can be used anywhere in screens that regular text is - it's just truncate_text "Some text" instead of text "Some text"
Handles all the text formatting I could think to add to it - interpolated variables (global and local screen variables), text tags (including hyperlinks), ruby text (both input forms), and escaped characters (e.g. [[)
has_tooltip property can be set to True to automatically set the tooltip to the full text when it is cut off, or to "rest" to set it to only the text which was cut off. If the text is not truncated, it will not have a tooltip (though you can use the tooltip property normally for regular tooltip behaviour)
Use the suffix property to set what is shown when text is truncated (e.g. "..." or " {i}(continued){/i}")
separators property can be set to a string of characters that it's okay to split on, e.g. " -" will split the text only on spaces and hyphens. The default will split on any available character (after accounting for things like text tags etc.)
shrink_to_fit property takes an integer, which is the smallest text size the text can be shrunk down to before it starts truncating the text to fit
Note that the text is adjusted via text size to fit, not zooming, so it both keeps the text sharp and allows it to adapt dynamically as the text size shrinks
adjust_line_spacing_to_fit property can be set to a number like -10, which is the minimum line_spacing value that will be used when trying to fit. Can be used in combination with shrink_to_fit, and you can decide the order via shrink_before_spacing True/False.
reset_size_on_overflow and reset_spacing_on_overflow properties let you control whether the text stays at the shrink_to_fit size when it's too large to fit the provided space even after shrinking to fit, or is reset to its original size
truncate_after_shrink property lets you control whether the text will be truncated after it is shrunk down if it is still too large for the provided space at the minimum size.
target_size lets you set a "soft" target for the size, even if the available space is larger. It will use the other properties to try to fit the space, such as shrinking or truncating.
In combination with using shrink_to_fit and setting truncate_after_shrink to False, it can be used to do things such as place text in a viewport which shrinks slightly if it's only a little larger than the viewport window, but otherwise is allowed to overflow so the scrollbars will kick in.
It is also compatible with my Marquee tool!
Instructions
Download truncated_text.zip and unzip it to get 01_truncate_text.rpy and truncate_text_examples.rpy. Drop these files into your project's game/ folder. Several examples are provided in truncate_text_examples.rpy, which you can try out by jumping to the label test_truncate_text.

Compatibility
This tool has been tested for compatibility with Ren'Py 7.6-7.8 and 8.1-8.3, and is expected to be compatible with earlier Ren'Py versions but has not been tested. Notably, however, ruby text is bugged on v7.6 (for all ruby text, not just the tool), so please update to v8.3+ to use ruby text. Leave a message in the stickied thread if you run into any bugs.

Terms of Use
You may:

Use this code in commercial and noncommercial projects, provided you package the code into an rpa file for release - the code to do so is included in the files.
Modify and edit this code to suit your needs.
You may not:

Resell all or part of this code as-is or sell it with modifications
Release any projects created using this code without providing attribution
Attribution must be credited as Feniks, with a link to either the page with this code or to https://feniksdev.com.

Credits
Special credit to Windchimes of Wind Chimes Games, who wrote the code to handle closing open text tags! Windchimes also provided the quest tracker and glossary search screenshots.

Final Notes
I also have a Marquee tool, which serves a similar purpose but will apply an animation to the text if it doesn't fit inside its container. It can even be used in combination with this tool to attempt first to shrink the text, and animate it if it still doesn't fit. Find it here!