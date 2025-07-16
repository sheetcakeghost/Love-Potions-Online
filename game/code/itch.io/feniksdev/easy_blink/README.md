https://feniksdev.itch.io/easy-blinking-for-renpy

Overview
Easily add blinking to your character sprites in Ren'Py with the EasyBlink displayable. Enjoy properly randomized blink times, automatic image sequences, custom timing, and more.

Description
The EasyBlink displayable has several properties, which can be adjusted on a per-displayable basis and set up as defaults:

Adjust the blink framerate between successive blink images.
Use the same number for all frames or provide a list for specific timing.
Never have synced blinking!
Provide a range of times to wait between blinks - a random number will be chosen between these ranges on each repeat.
"Double blink percent" to determine how often (if ever) characters blink twice in a row. Characters will never blink thrice in a row.
Provide a blink format through multiple formats:
Numbers (e.g. "eileen_happy_eyes0.png", "eileen_happy_eyes1.png", "eileen_happy_eyes2.png")
Names (e.g. "eileen_happy_eyes.png", "eileen_mid_eyes.png", "eileen_closed_eyes.png")
Use auto-generated blink frames by squishing the eye vertically.
For best results, the bottom of the eye should be at the bottom edge of the image itself (i.e. no transparent space below) and the character should be facing the camera mostly head-on.
Optionally reverse provided images (e.g. 0→1→2→1→0) or go in the order provided (e.g. 0→1→2→0)
Optionally prevent blinking from happening during transitions (e.g. when dissolving one eye image into another)
Include transitions between blink frames (e.g. dissolve)
Include a "startup" animation before looping
Includes a preference toggle so you can turn blinking on/off for the whole game.
Features
Free version
Extra Paid File
EasyBlink displayable class

Explanatory comments

Example declarations

All blink features described above
Drop-and-go layered image format_function to automatically declare blinking eye images for your whole layered image.

You provide the pattern(s) and group names (e.g. "eyes") and the format_function will take care of all the EasyBlink declarations.

You can add the format_function to a pre-existing layeredimage declaration without modifying anything else.

Fully compatible with existing format_functions - just pass in your function to the provided one.

Tweak any individual blinking images by supplying a dictionary to the attribute while letting the format_function take care of the rest.

The extra file also includes additional example declarations for layered images and the format_function.

Instructions
Download easy_blink.zip and unzip it. Place the provided rpy files into your project's game/ folder and the provided example images into your project's images/ folder (it is important you keep them in the easy_blink folder so it's images/easy_blink/agustina_base.png etc.). The bonus file, easy_blink_extras.rpy, can also go in your project's game/ folder.

Documentation and examples are included with the files, and can also be found at https://feniksdev.com/docs-category/easy-blinking/

Compatibility
This system has been tested for compatibility with Ren'Py 7.5-7.6 and 8.0-8.2. It is expected to be compatible with earlier versions as well but has not been tested. Leave a message in the stickied thread if you run into any bugs.

Terms of Use
Both the free version and any paid addons have the same terms of use.

You may:

Use this code in commercial and noncommercial projects, provided it is packaged into an archived .rpa file. The code to do so is included in the code file.
Modify and edit the code to suit your needs
You may not:

Resell all or part of the code as-is or sell it with modifications
Release any projects created using this code without providing attribution
Attribution must be credited as Feniks, with a link either to the page with this code or to https://feniksdev.com

Credits
Agustina sprite by DejiNyucu. A few modified Agustina images are included for examples in easy_blink.zip (as seen in the screenshots).

Final Notes
Huge thank you to my friends at Wind Chimes Games and Steamberry Studio for their help with testing and streamlining the tool for devs!

You might also be interested in my Ren'Py Layered Image Masks tool to easily make cut-ins for your layered images:



And check out my layered image visualizer and associated image tools for ways to preview your sprites before you add them to your game:

