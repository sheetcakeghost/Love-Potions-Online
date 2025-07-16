https://feniksdev.itch.io/sound-disabler-and-captions-tool-for-renpy

Overview
Provide audio accessibility options for players to disable individual sounds at will, for those who are sensitive to repetitive noises or have audio issues such as misophonia or hyperacusis. Sounds can be disabled across the whole game: in-game sound effects, UI, click-to-continue sounds, dialogue bleeps, and more. This accessibility and customization tool also adds audio captions to describe the sounds heard during gameplay, so no context is lost for players! A simplified declaration format + engine replacements mean no script changes are required for this code to work.

This tool was created in collaboration with Alaric from Just Write Studios.

Features
A customizable screen with sounds sorted into categories which players can toggle off individually or on a per-category basis (e.g. turning off all sudden slamming sounds).
Special actions for players to turn off the currently playing music or sound effects.
Audio captions can be toggled on/off by the player.
No in-game script modifications are needed for audio captions or the sound exclusion systems to work - play sound footsteps and play music sunflower etc. will automatically hook into the included systems. Excluded sounds are universal, so players can toggle off UI sounds played through things like activate_sound.
Compatible with translations.
Uses a class to organize audio captions and descriptions for your audio files. A function will automatically scan for undeclared files and copy the basic declarations to your clipboard to be easily pasted into your script.
For convenience, the folder name is used to automatically fill out the category field, and the name is used to automatically declare a variable in the audio namespace (i.e. if the name is "footsteps" then audio.footsteps is declared pointing to that file so you can write play sound footsteps)
Instructions
Download accessible_audio.zip and unzip it. Place the provided audio/ and accessibility/ folders into your project's game/ folder. The included special_silence.ogg file should be located at game/audio/special_silence.ogg. It is important that 01_audio_statements.rpy load before other files, but the other two rpy files in the accessibility folder can be placed wherever you like. accessible_audio_frontend.rpy has several examples and instructions to get started. The most basic requirement is to include a button somewhere on your settings screen to open the excluded audio screen, and a button to toggle audio captions on/off e.g.

textbutton _("Audio Captions"):
    action ToggleField(persistent, "audio_captions_on")
textbutton _("Toggle individual sounds"):
    action ShowMenu("excluded_sound_checklist")
Compatibility
This tool has been tested for compatibility with Ren'Py 8.2-8.3. It is expected to be compatible with some earlier Ren'Py versions but has not been tested. Leave a message in the stickied thread if you run into bugs.

Of note, audio captions will not appear for queued sounds when they play, nor will captions appear multiple times when a song loops. Excluded sounds, however, will not play when initiated from any format (queuing, UI sounds, looping, etc).

Terms of Use
You may:

Use this code during development of any kind of project, commercial or noncommercial.
Modify and edit the code to suit your needs
You may not:

Resell all or part of the code as-is or sell it with modifications
Release any projects created using this code without providing attribution
Attribution must be credited as Feniks and Alaric, with a link either to the page with this code or to https://feniksdev.com

Final Notes
This tool has an accompanying page on my website with recommended practices for labelling and categorizing sounds so players can decide if they want to hear those sounds or not. Find it here.

You may also be interested in the Controller Support Expansion for Ren'Py, a large collection of tools that improves navigation with controllers and keyboards in Ren'Py: