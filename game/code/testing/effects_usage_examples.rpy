# Effects Usage Examples
# Demonstrates how to use the new video-based effects system
# All effects are now in vfx.rpy

# Define test backgrounds for proper testing
image bg testing = "images/bg/testing.jpg"  

# Individual Effects Test - Using testing.jpg background
label individual_effects_test:
    scene bg testing
    show spw glitter with dissolve:
        xalign 0.5 yalign 0.5
        ease 2.0 yoffset 5
        ease 2.0 yoffset 0
        repeat
    bpw "Hello!"
    hide spw
    show pw closedhappy mouthneutral with dissolve:
        xalign 0.5 yalign 0.5
        ease 2.0 yoffset 5
        ease 2.0 yoffset 0
        repeat
    
    bpw "It's time for some effects!"
    
    # Weather Effects (SnowBlossom)
    "Testing light rain effect (SnowBlossom):"
    show screen rain_light
    "Light rain falls gently across the scene using SnowBlossom particles."
    hide screen rain_light
    
    "Testing heavy rain effect (SnowBlossom):"
    show screen rain_heavy
    "Heavy rain pours down dramatically using SnowBlossom particles."
    hide screen rain_heavy
    
    "Testing light snow effect (SnowBlossom):"
    show screen snow_light
    "Light snowflakes drift down peacefully using SnowBlossom particles."
    hide screen snow_light
    
    "Testing heavy snow effect (SnowBlossom):"
    show screen snow_heavy
    "Heavy snow blankets the scene using SnowBlossom particles."
    hide screen snow_heavy
    
    "Testing blizzard effect (SnowBlossom):"
    show screen blizzard
    "An intense blizzard rages with varied snowflake sizes and blustery atmosphere using SnowBlossom particles."
    hide screen blizzard

    "Testing fog effect (SnowBlossom):"
    show screen fog_light
    "Mysterious fog rolls in, created with SnowBlossom and transparent PNGs."
    hide screen fog_light

    "Testing heavy fog effect (SnowBlossom):"
    show screen fog_heavy
    "A thick, dense fog covers the scene using many SnowBlossom layers."
    hide screen fog_heavy

    "Testing underwater effect (Video):"
    show underwater_anim
    "The scene takes on an underwater quality using video animation."
    hide underwater_anim
    
    "Testing left god ray effect (Video):"
    show godrays_anim
    "Divine light rays shine from the left using video animation."
    hide godrays_anim
    
    "Testing right god ray effect (Video):"
    show godrays_r_anim
    "Divine light rays shine from the right using video animation."
    hide godrays_r_anim
    
    # Nature Effects
    "Testing falling leaves effect (Video):"
    show leaves_anim
    "Autumn leaves fall gently from above using video animation."
    hide leaves_anim
    
    "Testing cherry blossoms effect (Video):"
    show blossom_anim
    "Cherry blossoms dance in the breeze using video animation."
    hide blossom_anim
    
    "Testing fireflies effect (SnowBlossom):"
    show screen fireflies
    "Magical fireflies light up the night using SnowBlossom particles."
    hide screen fireflies
    
    "Testing dust effect (SnowBlossom):"
    show screen dust
    "Dust particles float through the air using SnowBlossom particles."
    hide screen dust
    
    "Testing petals effect (SnowBlossom):"
    show screen petals
    "Falling petals dance in the wind using SnowBlossom particles."
    hide screen petals
    
    # Star Effects (Video - All Colors)
    "Testing blue stars effect (Video):"
    show stars_blue_anim
    "Blue stars twinkle in the sky using video animation."
    hide stars_blue_anim
    
    "Testing red stars effect (Video):"
    show stars_red_anim
    "Red stars glow with warmth using video animation."
    hide stars_red_anim
    
    "Testing green stars effect (Video):"
    show stars_green_anim
    "Green stars shimmer with nature's energy using video animation."
    hide stars_green_anim
    
    "Testing yellow stars effect (Video):"
    show stars_yellow_anim
    "Yellow stars shine like distant suns using video animation."
    hide stars_yellow_anim
    
    "Testing purple stars effect (Video):"
    show stars_purple_anim
    "Purple stars pulse with magical energy using video animation."
    hide stars_purple_anim
    
    "Testing pink stars effect (Video):"
    show stars_pink_anim
    "Pink stars sparkle with romance using video animation."
    hide stars_pink_anim
    
    # Sparkle Effects (Video - All Colors)
    "Testing blue sparkles effect (Video):"
    show sparkle_blue_anim
    "Blue sparkles dance around the scene using video animation."
    hide sparkle_blue_anim
    
    "Testing red sparkles effect (Video):"
    show sparkle_red_anim
    "Red sparkles add fiery energy using video animation."
    hide sparkle_red_anim
    
    "Testing green sparkles effect (Video):"
    show sparkle_green_anim
    "Green sparkles bring life to the scene using video animation."
    hide sparkle_green_anim
    
    "Testing yellow sparkles effect (Video):"
    show sparkle_yellow_anim
    "Yellow sparkles shine like gold using video animation."
    hide sparkle_yellow_anim
    
    "Testing purple sparkles effect (Video):"
    show sparkle_purple_anim
    "Purple sparkles weave magical patterns using video animation."
    hide sparkle_purple_anim
    
    "Testing pink sparkles effect (Video):"
    show sparkle_pink_anim
    "Pink sparkles create a romantic atmosphere using video animation."
    hide sparkle_pink_anim
    
    # Portal Effects (Video - All Colors)
    "Testing blue portal effect (Video):"
    show portal_blue_anim
    "A blue portal opens to another dimension using video animation."
    hide portal_blue_anim
    
    "Testing red portal effect (Video):"
    show portal_red_anim
    "A red portal pulses with dark energy using video animation."
    hide portal_red_anim
    
    "Testing green portal effect (Video):"
    show portal_green_anim
    "A green portal leads to nature's realm using video animation."
    hide portal_green_anim
    
    "Testing yellow portal effect (Video):"
    show portal_yellow_anim
    "A yellow portal radiates with light using video animation."
    hide portal_yellow_anim
    
    "Testing purple portal effect (Video):"
    show portal_purple_anim
    "A purple portal crackles with magic using video animation."
    hide portal_purple_anim
    
    "Testing pink portal effect (Video):"
    show portal_pink_anim
    "A pink portal glows with love's power using video animation."
    hide portal_pink_anim
    
    # Plasma Effects (Video - All Colors)
    "Testing blue plasma effect (Video):"
    show plasma_blue_anim
    "Blue plasma flows with electric energy using video animation."
    hide plasma_blue_anim
    
    "Testing red plasma effect (Video):"
    show plasma_red_anim
    "Red plasma burns with intense heat using video animation."
    hide plasma_red_anim
    
    "Testing green plasma effect (Video):"
    show plasma_green_anim
    "Green plasma swirls with organic energy using video animation."
    hide plasma_green_anim
    
    "Testing yellow plasma effect (Video):"
    show plasma_yellow_anim
    "Yellow plasma crackles with lightning using video animation."
    hide plasma_yellow_anim
    
    "Testing purple plasma effect (Video):"
    show plasma_purple_anim
    "Purple plasma pulses with dark magic using video animation."
    hide plasma_purple_anim
    
    "Testing white plasma effect (Video):"
    show plasma_white_anim
    "White plasma glows with pure energy using video animation."
    hide plasma_white_anim
    
    # Confetti Effects (Video)
    "Testing warm confetti effect (Video):"
    show confetti_warm_anim
    "Warm colored confetti celebrates the moment using video animation."
    hide confetti_warm_anim
    
    "Testing cool confetti effect (Video):"
    show confetti_cool_anim
    "Cool colored confetti creates a festive mood using video animation."
    hide confetti_cool_anim
    
    "Testing colorful confetti effect (Video):"
    show confetti_colorful_anim
    "Colorful confetti fills the air with joy using video animation."
    hide confetti_colorful_anim
    
    # Special Effects (Video)
    "Testing matrix effect (Video):"
    show matrix_anim
    "Digital rain falls in matrix style using video animation."
    hide matrix_anim
    
    "Testing night sky effect (Video):"
    show nightsky_anim
    "A beautiful night sky appears above using video animation."
    hide nightsky_anim
    
    "Testing shooting star effect (Video):"
    show shootingstar_anim
    "A shooting star streaks across the sky using video animation."
    hide shootingstar_anim
    
    # Composite Effects
    "Testing magical atmosphere effect (combined):"
    show screen magical_atmosphere
    "Multiple magical effects create an enchanting atmosphere."
    hide screen magical_atmosphere
    
    "Testing storm weather effect (combined):"
    show screen storm_weather
    "Rain and fog combine for a stormy scene."
    hide screen storm_weather
    
    "Testing celebration effect (combined):"
    show screen celebration
    "Confetti and sparkles create a festive celebration."
    hide screen celebration
    
    "Individual effects test complete! All effects have been demonstrated with the testing.jpg background."
    
    return

# Helper Functions Test
label helper_functions_test:
    scene bg testing
    
    "Helper Functions Test - Testing the new helper functions"
    
    # Weather effect helpers
    "Testing weather effect helpers:"
    $ show_weather_effect("rain_light", 0, 0)
    "Light rain using helper function."
    $ hide_weather_effect("rain_light")
    
    $ show_weather_effect("snow_heavy", 0, 0, 0)
    "Heavy snow using helper function."
    $ hide_weather_effect("snow_heavy")
    
    # Atmospheric effect helpers
    "Testing atmospheric effect helpers:"
    show fog_anim
    "Fog using video image."
    hide fog_anim
    
    $ show_atmospheric_effect("fireflies", 0, 0, -100)
    "Fireflies using helper function."
    $ hide_atmospheric_effect("fireflies")
    
    # Magical effect helpers
    "Testing magical effect helpers:"
    show stars_blue_anim
    "Blue stars using video image."
    hide stars_blue_anim
    
    $ show_magical_effect("sparkle", "purple", 0, 0, -100)
    "Purple sparkles using helper function."
    $ hide_magical_effect("sparkle", "purple")
    
    show portal_green_anim
    "Green portal using video image."
    hide portal_green_anim
    
    $ show_magical_effect("plasma", "red", 0, 0, 0)
    "Red plasma using helper function."
    $ hide_magical_effect("plasma", "red")
    
    # Special effect helpers
    "Testing special effect helpers:"
    show matrix_anim
    "Matrix effect using video image."
    hide matrix_anim
    
    $ show_special_effect("confetti_colorful", 0, 0, -50)
    "Colorful confetti using helper function."
    $ hide_special_effect("confetti_colorful")
    
    # Composite effect helpers
    "Testing composite effect helpers:"
    $ show_composite_effect("magical_atmosphere", 0, 0)
    "Magical atmosphere using helper function."
    $ hide_composite_effect("magical_atmosphere")
    
    $ show_composite_effect("celebration", 0, 0)
    "Celebration using helper function."
    $ hide_composite_effect("celebration")
    
    # Utility function
    "Testing utility function:"
    $ show_weather_effect("rain_light", 0, 0)
    show fog_anim
    show stars_blue_anim
    "Multiple effects are showing..."
    $ hide_all_effects()
    hide fog_anim
    hide stars_blue_anim
    "All effects cleared using hide_all_effects()."
    
    "Helper functions test complete!"
    
    return

# Performance Test
label effects_performance_test:
    scene bg testing
    
    "Performance Test - Testing multiple effects simultaneously"
    
    # Test multiple video effects
    "Testing multiple video effects:"
    show fog_anim
    show sparkle_blue_anim
    show stars_purple_anim
    show plasma_red_anim
    "Multiple video effects running simultaneously."
    hide fog_anim
    hide sparkle_blue_anim
    hide stars_purple_anim
    hide plasma_red_anim
    
    # Test multiple SnowBlossom effects
    "Testing multiple SnowBlossom effects:"
    show screen rain_light
    show screen fireflies
    show screen dust
    "Multiple SnowBlossom effects running simultaneously."
    hide screen rain_light
    hide screen fireflies
    hide screen dust
    
    # Test mixed effects
    "Testing mixed video and SnowBlossom effects:"
    show fog_anim
    show screen rain_heavy
    show sparkle_yellow_anim
    show screen fireflies
    show matrix_anim
    "Mixed effects running simultaneously."
    hide fog_anim
    hide screen rain_heavy
    hide sparkle_yellow_anim
    hide screen fireflies
    hide matrix_anim
    
    # Test composite effects
    "Testing composite effects:"
    show screen magical_atmosphere
    "Composite effect running."
    hide screen magical_atmosphere
    
    show screen storm_weather
    "Storm weather composite effect running."
    hide screen storm_weather
    
    "Performance test complete!"
    
    return

# Scene Examples
label magical_battle_scene:
    scene bg testing
    
    "Magical Battle Scene Example"
    
    "The battle begins!"
    
    # Atmospheric setup
    show fog_anim
    "Fog rolls in as the battle begins."
    
    # Magical attacks
    show sparkle_blue_anim
    "Blue magical sparkles fly through the air!"
    hide sparkle_blue_anim
    
    show stars_purple_anim
    "Purple stars of power appear!"
    hide stars_purple_anim
    
    show portal_red_anim
    "A red portal opens, unleashing dark energy!"
    hide portal_red_anim
    
    # Weather effects
    $ show_weather_effect("rain_heavy", 0, 0)
    "Heavy rain falls as the battle intensifies!"
    $ hide_weather_effect("rain_heavy")
    
    # Final attack
    show plasma_white_anim
    "Pure white plasma energy fills the battlefield!"
    hide plasma_white_anim
    
    hide fog_anim
    "The battle reaches its climax!"
    
    return

label peaceful_scene:
    scene bg testing
    
    "Peaceful Scene Example"
    
    "A peaceful moment..."
    
    # Gentle effects
    $ show_atmospheric_effect("fireflies", 0, 0, -100)
    "Gentle fireflies light up the night."
    
    show stars_blue_anim
    "Blue stars twinkle peacefully above."
    hide stars_blue_anim
    
    $ show_atmospheric_effect("petals", 0, 0, -100)
    "Cherry petals fall gently in the breeze."
    
    "The peaceful atmosphere is complete."
    
    $ hide_all_effects()
    "The moment passes."
    
    return

label celebration_scene:
    scene bg testing
    
    "Celebration Scene Example"
    
    "A celebration begins!"
    
    # Celebration effects
    $ show_composite_effect("celebration", 0, 0)
    "Confetti and sparkles fill the air!"
    
    show confetti_colorful_anim
    "More colorful confetti joins the celebration!"
    hide confetti_colorful_anim
    
    show sparkle_yellow_anim
    "Golden sparkles add to the festive mood!"
    hide sparkle_yellow_anim
    
    "The celebration is in full swing!"
    
    $ hide_all_effects()
    "The celebration winds down."
    
    return 