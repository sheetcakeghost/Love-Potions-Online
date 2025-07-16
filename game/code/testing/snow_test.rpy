# Snow Effects Test
# Demonstrates the new snowblossom-based snow effects

label test_snow_effects:
    scene bg manor bedroom 1
    
    "Testing the new snow effects using Ren'Py's snowblossom with custom snowflake assets."
    
    "First, let's test light snow:"
    $ show_snow_effect("light")
    "This is light snow using snowblossom with custom snowflakes."
    
    $ renpy.pause(3.0)
    
    "Now let's test heavy snow:"
    $ hide_snow_effect("light")
    $ show_snow_effect("heavy")
    "This is heavy snow using snowblossom with custom snowflakes."
    
    $ renpy.pause(3.0)
    
    "Let's test both together:"
    $ show_snow_effect("light")
    "Now we have both light and heavy snow together."
    
    $ renpy.pause(3.0)
    
    "Clearing all snow effects:"
    $ hide_snow_effect("light")
    $ hide_snow_effect("heavy")
    "All snow effects have been cleared."
    
    "Test complete!"
    
    return 