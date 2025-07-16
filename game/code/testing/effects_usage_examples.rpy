# Effects Usage Examples
# Demonstrates how to use the consolidated visual effects system (WebM + PNG)
# All effects are now in vfx.rpy

# Define test backgrounds for proper testing
image bg testing = "images/bg/testing.jpg"  

# Individual Effects Test - Using testing.jpg background
label individual_effects_test:
    scene bg testing
    
    "Individual Effects Test - Each effect will be shown separately with testing.jpg background"
    
    # Weather Effects
    "Testing light rain effect:"
    show screen rain_light
    "Light rain falls gently across the scene."
    hide screen rain_light
    
    "Testing heavy rain effect:"
    show screen rain_heavy
    "Heavy rain pours down dramatically."
    hide screen rain_heavy
    
    "Testing light snow effect:"
    show screen snow_light
    "Light snowflakes drift down peacefully."
    hide screen snow_light
    
    "Testing heavy snow effect:"
    show screen snow_heavy
    "Heavy snow blankets the scene."
    hide screen snow_heavy
    
    # Atmospheric Effects
    "Testing fog effect:"
    show screen fog
    "Mysterious fog rolls in, creating atmosphere."
    hide screen fog
    
    "Testing underwater effect:"
    show screen underwater
    "The scene takes on an underwater quality."
    hide screen underwater
    
    "Testing left god ray effect:"
    show screen godray_left
    "Divine light rays shine from the left."
    hide screen godray_left
    
    "Testing right god ray effect:"
    show screen godray_right
    "Divine light rays shine from the right."
    hide screen godray_right
    
    # Nature Effects
    "Testing falling leaves effect:"
    show screen leaves
    "Autumn leaves fall gently from above."
    hide screen leaves
    
    "Testing cherry blossoms effect:"
    show screen blossoms
    "Cherry blossoms dance in the breeze."
    hide screen blossoms
    
    "Testing fireflies effect:"
    show screen fireflies
    "Magical fireflies light up the night."
    hide screen fireflies
    
    # Star Effects (All Colors)
    "Testing blue stars effect:"
    show screen stars_blue
    "Blue stars twinkle in the sky."
    hide screen stars_blue
    
    "Testing red stars effect:"
    show screen stars_red
    "Red stars glow with warmth."
    hide screen stars_red
    
    "Testing green stars effect:"
    show screen stars_green
    "Green stars shimmer with nature's energy."
    hide screen stars_green
    
    "Testing yellow stars effect:"
    show screen stars_yellow
    "Yellow stars shine like distant suns."
    hide screen stars_yellow
    
    "Testing purple stars effect:"
    show screen stars_purple
    "Purple stars pulse with magical energy."
    hide screen stars_purple
    
    "Testing pink stars effect:"
    show screen stars_pink
    "Pink stars sparkle with romance."
    hide screen stars_pink
    
    # Sparkle Effects (All Colors)
    "Testing blue sparkles effect:"
    show screen sparkle_blue
    "Blue sparkles dance around the scene."
    hide screen sparkle_blue
    
    "Testing red sparkles effect:"
    show screen sparkle_red
    "Red sparkles add fiery energy."
    hide screen sparkle_red
    
    "Testing green sparkles effect:"
    show screen sparkle_green
    "Green sparkles bring life to the scene."
    hide screen sparkle_green
    
    "Testing yellow sparkles effect:"
    show screen sparkle_yellow
    "Yellow sparkles shine like gold."
    hide screen sparkle_yellow
    
    "Testing purple sparkles effect:"
    show screen sparkle_purple
    "Purple sparkles weave magical patterns."
    hide screen sparkle_purple
    
    "Testing pink sparkles effect:"
    show screen sparkle_pink
    "Pink sparkles create a romantic atmosphere."
    hide screen sparkle_pink
    
    # Portal Effects (All Colors)
    "Testing blue portal effect:"
    show screen portal_blue
    "A blue portal opens to another dimension."
    hide screen portal_blue
    
    "Testing red portal effect:"
    show screen portal_red
    "A red portal pulses with dark energy."
    hide screen portal_red
    
    "Testing green portal effect:"
    show screen portal_green
    "A green portal leads to nature's realm."
    hide screen portal_green
    
    "Testing yellow portal effect:"
    show screen portal_yellow
    "A yellow portal radiates with light."
    hide screen portal_yellow
    
    "Testing purple portal effect:"
    show screen portal_purple
    "A purple portal crackles with magic."
    hide screen portal_purple
    
    "Testing pink portal effect:"
    show screen portal_pink
    "A pink portal glows with love's power."
    hide screen portal_pink
    
    # Plasma Effects (All Colors)
    "Testing blue plasma effect:"
    show screen plasma_blue
    "Blue plasma flows with electric energy."
    hide screen plasma_blue
    
    "Testing red plasma effect:"
    show screen plasma_red
    "Red plasma burns with intense heat."
    hide screen plasma_red
    
    "Testing green plasma effect:"
    show screen plasma_green
    "Green plasma swirls with organic energy."
    hide screen plasma_green
    
    "Testing yellow plasma effect:"
    show screen plasma_yellow
    "Yellow plasma crackles with lightning."
    hide screen plasma_yellow
    
    "Testing purple plasma effect:"
    show screen plasma_purple
    "Purple plasma pulses with dark magic."
    hide screen plasma_purple
    
    "Testing white plasma effect:"
    show screen plasma_white
    "White plasma glows with pure energy."
    hide screen plasma_white
    
    # Confetti Effects
    "Testing warm confetti effect:"
    show screen confetti_warm
    "Warm colored confetti celebrates the moment."
    hide screen confetti_warm
    
    "Testing cool confetti effect:"
    show screen confetti_cool
    "Cool colored confetti creates a festive mood."
    hide screen confetti_cool
    
    "Testing colorful confetti effect:"
    show screen confetti_colorful
    "Colorful confetti fills the air with joy."
    hide screen confetti_colorful
    
    # Special Effects
    "Testing matrix effect:"
    show screen matrix
    "Digital rain falls in matrix style."
    hide screen matrix
    
    "Testing night sky effect:"
    show screen night_sky
    "A beautiful night sky appears above."
    hide screen night_sky
    
    "Testing shooting star effect:"
    show screen shooting_star
    "A shooting star streaks across the sky."
    hide screen shooting_star
    
    # PNG Light Effects
    "Testing light cast1 effect:"
    show screen light_cast1
    "Light magic begins to form."
    hide screen light_cast1
    
    "Testing light cast2 effect:"
    show screen light_cast2
    "Advanced light magic takes shape."
    hide screen light_cast2
    
    "Testing light glare effect:"
    show screen light_glare
    "Intense light glare blinds the scene."
    hide screen light_glare
    
    "Testing light ray effect:"
    show screen light_ray
    "Pure light rays pierce through darkness."
    hide screen light_ray
    
    "Testing light sparkle effect:"
    show screen light_sparkle
    "Light sparkles dance with divine energy."
    hide screen light_sparkle
    
    "Testing light scintillation effect:"
    show screen light_scintillation
    "Light scintillates with magical power."
    hide screen light_scintillation
    
    "Testing light gleam effect:"
    show screen light_gleam
    "Light gleams with healing energy."
    hide screen light_gleam
    
    "Testing light twinkle effect:"
    show screen light_twinkle
    "Light twinkles like distant stars."
    hide screen light_twinkle
    
    "Testing light photon effect:"
    show screen light_photon
    "Photon light fills the entire scene."
    hide screen light_photon
    
    "Testing light radiance effect:"
    show screen light_radiance
    "Divine radiance illuminates everything."
    hide screen light_radiance
    
    # PNG Wind Effects
    "Testing wind cast effect:"
    show screen wind_cast
    "Wind magic begins to gather."
    hide screen wind_cast
    
    "Testing wind cast2 effect:"
    show screen wind_cast2
    "Advanced wind magic takes form."
    hide screen wind_cast2
    
    "Testing wind whirlwind effect:"
    show screen wind_whirlwind
    "A small whirlwind spins rapidly."
    hide screen wind_whirlwind
    
    "Testing wind breeze effect:"
    show screen wind_breeze
    "A gentle breeze rustles through."
    hide screen wind_breeze
    
    "Testing wind twister effect:"
    show screen wind_twister
    "A wind twister twists through the air."
    hide screen wind_twister
    
    "Testing wind gust effect:"
    show screen wind_gust
    "A powerful wind gust blows through."
    hide screen wind_gust
    
    "Testing wind vacuum effect:"
    show screen wind_vacuum
    "Wind creates a vacuum effect."
    hide screen wind_vacuum
    
    "Testing wind cyclone effect:"
    show screen wind_cyclone
    "A wind cyclone spins with force."
    hide screen wind_cyclone
    
    "Testing wind updraft effect:"
    show screen wind_updraft
    "Wind creates an upward draft."
    hide screen wind_updraft
    
    "Testing wind tornado effect:"
    show screen wind_tornado
    "A massive tornado dominates the scene."
    hide screen wind_tornado
    
    # Composite Effects
    "Testing magical atmosphere effect:"
    show screen magical_atmosphere
    "Multiple magical effects create an enchanting atmosphere."
    hide screen magical_atmosphere
    
    "Testing storm weather effect:"
    show screen storm_weather
    "Rain and fog combine for a stormy scene."
    hide screen storm_weather
    
    "Testing celebration effect:"
    show screen celebration
    "Confetti and sparkles create a festive celebration."
    hide screen celebration
    
    "Testing light magical attack effect:"
    show screen light_magical_attack
    "Light magic combines for a powerful attack."
    hide screen light_magical_attack
    
    "Testing light healing effect:"
    show screen light_healing
    "Gentle light effects create a healing atmosphere."
    hide screen light_healing
    
    "Testing wind storm effect:"
    show screen wind_storm
    "Multiple wind effects create a powerful storm."
    hide screen wind_storm
    
    "Testing wind gentle breeze effect:"
    show screen wind_gentle_breeze
    "Gentle wind effects create a peaceful breeze."
    hide screen wind_gentle_breeze
    
    "Individual effects test complete! All effects have been demonstrated with the testing.jpg background."
    
    return

label effects_demo:
    scene bg meadow
    
    "Let's demonstrate the complete effects system!"
    
    # WebM Effects Demo with proper overlay testing
    "First, let's show some WebM effects with proper transparency."
    
    "Testing rain effect with screen blend mode:"
    show screen rain_light
    "It starts to rain lightly. The black background should be transparent."
    hide screen rain_light
    
    "Testing sparkle effect:"
    show screen sparkle_blue
    "Blue sparkles appear in the top-left area."
    hide screen sparkle_blue
    
    "Testing stars effect:"
    show screen stars_purple
    "Purple stars twinkle in the center area."
    hide screen stars_purple
    

    
    # PNG Effects Demo
    "Now let's show some PNG sprite sheet effects."
    
    show screen light_sparkle
    "Light magic sparkles around us."
    hide screen light_sparkle
    
    show screen wind_tornado
    "A powerful tornado appears!"
    hide screen wind_tornado
    
    # Helper Functions Demo
    "Let's use the helper functions for easier management."
    
    $ show_light_effect("sparkle", 0, 0, 30)
    "Using helper function for light sparkle."
    $ hide_light_effect("sparkle")
    
    $ show_wind_effect("tornado", 0, 0, 60)
    "Using helper function for wind tornado."
    $ hide_wind_effect("tornado")
    
    $ show_magical_effect("stars", "purple", 0, 0)
    "Using helper function for purple stars."
    $ hide_magical_effect("stars", "purple")
    
    # Composite Effects Demo
    "Let's see some combined effects."
    
    show screen light_magical_attack(0, 0, 30)
    "A combined light magical attack!"
    hide screen light_magical_attack
    
    show screen magical_atmosphere(0, 0)
    "A magical atmosphere fills the area."
    hide screen magical_atmosphere
    
    # Multiple Effects Demo
    "Let's combine multiple effects."
    
    $ show_light_effect("sparkle", 100, 100, 30)
    $ show_wind_effect("breeze", 300, 400, 30)
    $ show_magical_effect("stars", "blue", 200, 200)
    
    "Multiple effects create a magical atmosphere."
    
    $ hide_all_effects()
    "All effects are cleared."
    
    return

# WebM Effects Overlay Test
label webm_overlay_test:
    scene bg room
    
    "Testing WebM effects overlay capabilities..."
    
    "Single effect test:"
    show screen sparkle_blue(0, 0)
    "Blue sparkles should appear with transparent background."
    hide screen sparkle_blue
    
    "Multiple effects overlay test:"
    show screen rain_light(0, 0)
    show screen sparkle_yellow(200, 100)
    show screen stars_purple(400, 200)
    show screen fireflies(100, 300)
    
    "Multiple WebM effects should overlay properly without black backgrounds."
    "Each effect should blend with the others and the background."
    
    hide screen rain_light
    hide screen sparkle_yellow
    hide screen stars_purple
    hide screen fireflies
    
    "Effects cleared. The overlay test is complete."
    
    return

# WebM Blend Mode Comparison Test
label webm_blend_test:
    scene bg meadow
    
    "Testing different WebM effect blend modes..."
    
    "Testing additive blending (should remove black background):"
    show screen sparkle_blue(100, 100)
    "Blue sparkles with additive blending - black should be transparent."
    hide screen sparkle_blue
    
    "Testing additive blending for stars:"
    show screen stars_yellow(200, 200)
    "Yellow stars with additive blending - should be bright and glowing."
    hide screen stars_yellow
    
    "Testing additive blending for fireflies:"
    show screen fireflies(300, 100)
    "Fireflies with additive blending - should blend naturally with background."
    hide screen fireflies
    
    "Testing multiple effects with different blend modes:"
    show screen rain_light(0, 0)
    show screen sparkle_purple(400, 100)
    show screen stars_blue(200, 300)
    
    "Multiple effects should all have transparent backgrounds and blend together."
    
    hide screen rain_light
    hide screen sparkle_purple
    hide screen stars_blue
    
    "Blend mode test complete."
    
    "Testing alternative blend approach:"
    show screen stars_blue_alt(100, 100)
    "Alternative blue stars - should also have transparent background."
    hide screen stars_blue_alt
    
    show screen sparkle_blue_alt(200, 200)
    "Alternative blue sparkles - testing different blend method."
    hide screen sparkle_blue_alt
    
    return

# WebM Performance and Quality Test
label webm_quality_test:
    scene bg battlefield
    
    "Testing WebM effect quality and performance..."
    
    "Testing high-quality effects:"
    show screen plasma_blue(0, 0)
    "Blue plasma effect - should be smooth and high quality."
    hide screen plasma_blue
    
    show screen portal_purple(200, 0)
    "Purple portal effect - should have smooth animation."
    hide screen portal_purple
    
    "Testing weather effects:"
    show screen snow_heavy(0, 0)
    "Heavy snow - should cover the entire screen properly."
    hide screen snow_heavy
    
    show screen fog(0, 0)
    "Fog effect - should create atmospheric overlay."
    hide screen fog
    
    "Testing special effects:"
    show screen matrix(0, 0)
    "Matrix effect - should have the digital rain effect."
    hide screen matrix
    
    show screen night_sky(0, 0)
    show screen shooting_star(0, 0)
    "Night sky with shooting star - layered effects."
    hide screen night_sky
    hide screen shooting_star
    
    "Quality test complete."
    
    return

# Magic Battle Scene Example
label magic_battle_scene:
    scene bg battlefield
    
    "A magical battle begins!"
    
    # WebM effects for atmosphere
    $ show_atmospheric_effect("fog")
    "Fog rolls in as the battle begins."
    
    # PNG effects for magic
    $ show_light_effect("cast1", 0, 0, 30)
    "The light mage begins casting."
    $ hide_light_effect("cast1")
    
    $ show_light_composite("magical_attack", 0, 0, 30)
    "A powerful light spell is unleashed!"
    $ hide_light_composite("magical_attack")
    
    # Wind magic counter
    $ show_wind_effect("cast", 0, 0, 30)
    "The wind mage counters with wind magic."
    $ hide_wind_effect("cast")
    
    $ show_wind_composite("storm", 0, 0, 30)
    "A wind storm counters the attack!"
    $ hide_wind_composite("storm")
    
    # Ultimate spells
    $ show_light_effect("radiance", 0, 0, 60)
    "The final light spell fills the battlefield."
    $ hide_light_effect("radiance")
    
    $ show_wind_effect("tornado", 0, 0, 60)
    "A massive tornado appears!"
    $ hide_wind_effect("tornado")
    
    $ hide_all_effects()
    "The battle reaches its climax!"
    
    return

# Healing Scene Example
label healing_scene:
    scene bg temple
    
    "In the sacred temple..."
    
    # Gentle healing sequence
    $ show_light_composite("healing", 0, 0, 30)
    "Divine light begins to heal the wounded."
    $ hide_light_composite("healing")
    
    $ show_wind_composite("gentle_breeze", 0, 0, 30)
    "A gentle breeze carries the healing magic."
    $ hide_wind_composite("gentle_breeze")
    
    $ show_light_effect("gleam", 0, 0, 30)
    "The healing light gleams with divine power."
    $ hide_light_effect("gleam")
    
    $ show_light_effect("twinkle", 0, 0, 30)
    "Magical twinkles dance in the air."
    $ hide_light_effect("twinkle")
    
    "The healing is complete."
    
    return

# Performance Test
label effects_performance_test:
    scene bg room
    
    "Testing effects performance..."
    
    # Test multiple effects simultaneously
    $ show_light_effect("sparkle", 0, 0, 30)
    $ show_wind_effect("breeze", 200, 0, 30)
    $ show_magical_effect("stars", "blue", 400, 0, 30)
    $ show_atmospheric_effect("fog")
    $ show_magical_effect("sparkle", "yellow", 0, 200, 30)
    
    "Multiple effects are running simultaneously."
    
    $ hide_all_effects()
    "Performance test complete."
    
    return 