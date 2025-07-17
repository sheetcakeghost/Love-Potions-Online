## Accessibility System
## Based on minute.itch.io accessibility script, adapted for Easy GUI

### Persistent Variables
default persistent.visual_text_help = _preferences.self_voicing
default persistent.audio_cues = True
default persistent.screenshake = True
default persistent.say_window_alpha = 0.75
default persistent.pref_text_scale = "regular"
default persistent.say_dialogue_kerning = 0
default persistent.pref_text_font = "gui/font/AtkinsonHyperlegibleNext-VariableFont_wght.ttf"
default persistent.pref_text_size = 30
default persistent.pref_text_weight = 400
default persistent.pref_text_color = "#f7f2e8"
default persistent.pref_text_spacing = 0

init python:
    ### Size Dictionary for Font Scaling
    size_dict = {
        "gui/font/AtkinsonHyperlegibleNext-VariableFont_wght.ttf": {
            "regular": 30,
            "large": 36,
            "line_spacing": 0,
        },
        "gui/font/AtkinsonHyperlegibleMono-VariableFont_wght.ttf": {
            "regular": 30,
            "large": 36,
            "line_spacing": 0,
        },
        "gui/font/Fortnight-Regular.otf": {
            "regular": 31,
            "large": 34,
            "line_spacing": -15,
        },
        "gui/font/DejaVuSans.ttf": {
            "regular": 32,
            "large": 35,
            "line_spacing": 0,
        },
        "gui/font/Levorotary_Medium.ttf": {
            "regular": 33,
            "large": 36,
            "line_spacing": 0,
        },
    }

    ### Audio Cues Setup
    # Define music aliases here
    music_dictionary = {
        # "music_alias": "Music Title",
    }

    # Define sound effect aliases here
    sfx_dictionary = {
        # "sound_alias": "Sound description",
    }

    ### Accessibility Functions
    def changeFont(newFont):
        """Change the text font and update related properties"""
        return [
            SetField(persistent, "pref_text_font", newFont),
            SetField(persistent, "pref_text_size", size_dict[newFont][persistent.pref_text_scale]),
            SetField(persistent, "pref_text_spacing", size_dict[newFont]['line_spacing'])
        ]

    def changeScale(newScale):
        """Change the text size scale"""
        return [
            SetField(persistent, "pref_text_scale", newScale),
            SetField(persistent, "pref_text_size", size_dict[persistent.pref_text_font][newScale])
        ]

    def changeColor(newColor):
        """Change the text color"""
        return SetField(persistent, "pref_text_color", newColor)

    def persistentToggle(persistentfield):
        """Toggle a persistent boolean field"""
        return ToggleField(persistent, persistentfield, true_value=True, false_value=False)

    ### Audio Cue Functions
    def play_sfx(sound_alias, fade=0):
        """Play a sound effect with optional audio cue notification"""
        renpy.sound.play(sound_alias, fadein=fade)
        if persistent.audio_cues and sound_alias in sfx_dictionary:
            renpy.notify("SFX: {i}" + sfx_dictionary[sound_alias] + "{/i}")

    def play_music(music_alias, fade=0):
        """Play music with optional audio cue notification"""
        renpy.music.play(music_alias, fadein=fade)
        if persistent.audio_cues and music_alias in music_dictionary:
            renpy.notify("Now Playing: " + music_dictionary[music_alias])

    ### Screen Shake Function
    def shake():
        """Shake the screen if enabled"""
        if persistent.screenshake:
            renpy.with_statement(hpunch)
        else:
            renpy.with_statement(fade)

### Visual Text Character
define vt = Character(None, condition="persistent.visual_text_help or _preferences.self_voicing", what_italic=True, 
    what_font=persistent.pref_text_font, 
    what_size=persistent.pref_text_size, 
    what_color=persistent.pref_text_color, 
    what_line_spacing=persistent.pref_text_spacing, 
    what_kerning=persistent.say_dialogue_kerning, 
    what_font_variables={"wght": persistent.pref_text_weight}) 