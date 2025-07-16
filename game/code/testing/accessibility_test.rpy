## Accessibility System Test
## This file tests the accessibility features

label test_accessibility:
    "This is a test of the accessibility system."
    
    "You can now access accessibility options in the preferences menu."
    
    "The accessibility tab includes:"
    "- Visual accessibility options (audio cues, screen shake, visual text help)"
    "- Text customization (fonts, sizes, colors)"
    "- Text spacing and transparency controls"
    
    "To test screen shake, I'll trigger it now:"
    $ shake()
    
    "To test audio cues, you can use the play_sfx() and play_music() functions in your script."
    
    "To test visual text help, use the 'vt' character for additional descriptions."
    
    vt "This is additional visual text that appears when visual text help is enabled."
    
    "The accessibility system is now integrated into your preferences menu!"
    
    return 