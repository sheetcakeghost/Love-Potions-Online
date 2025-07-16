# Skins

Ren'Py supports skinning the launcher – changing what the launcher looks like. To do this, follow the following steps:

Skins are specific to the Ren'Py version in use, and can't be expected to be forward or backwards compatible.

1.  Open the launcher in the launcher. This can be done from the preferences screen.
    
2.  Create the `skin.rpy` script file.
    
3.  Copy the following into `skin.rpy`:
    
    init \-2 python:
        \# The color of non-interactive text.
        custom\_text \= "#545454"
    
        \# Colors for buttons in various states.
        custom\_idle \= "#42637b"
        custom\_hover \= "#d86b45"
        custom\_disable \= "#808080"
    
        \# Colors for reversed text buttons (selected list entries).
        custom\_reverse\_idle \= "#78a5c5"
        reverse\_hover \= "#d86b45"
        custom\_reverse\_text \= "#ffffff"
    
        \# Colors for the scrollbar thumb.
        custom\_scrollbar\_idle \= "#dfdfdf"
        custom\_scrollbar\_hover \= "#d86b45"
        \# An image used as a separator pattern.
        custom\_pattern \= "images/pattern.png"
    
        \# A displayable used for the background of everything.
        custom\_background \= "images/background.png"
    
        \# A displayable used for the background of the projects list.
        custom\_projects\_window \= Null()
    
        \# A displayable used the background of information boxes.
        custom\_info\_window \= "#f9f9f9c0"
    
        \# Colors for the titles of information boxes.
        custom\_error\_color \= "#d15353"
        custom\_info\_color \= "#545454"
        custom\_interaction\_color \= "#d19753"
        custom\_question\_color \= "#d19753"
    
        \# The color of input text.
        custom\_input\_color \= "#d86b45"
    
        \# A displayable used for the background of windows
        \# containing commands, preferences, and navigation info.
        custom\_window \= Frame(Fixed(Solid(custom\_reverse\_idle, xsize\=4, xalign\=0), Solid(custom\_info\_window, xsize\=794, xalign\=1.0), xsize\=800, ysize\=600), 0, 0, tile\=True)
    
4.  Modify `skin.rpy` to skin the launcher. Place the image files you use into the launcher's game directory. Recommended size for background 800x600 pixels.
    
5.  Select Custom theme in preferences.
    

An incorrect `skin.rpy` file could prevent the launcher from starting. To fix it, you'll need to remove `skin.rpy` and `skin.rpyc` from the launcher's game directory, start the launcher, and then put them back.
