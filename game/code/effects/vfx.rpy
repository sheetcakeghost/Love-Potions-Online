
# Screen Effects
# WebM image definitions are now in webm_images.rpy with init -2 priority

# Transform for screen blend mode (makes black transparent)
transform screen_blend:
    blend "add"

# Base screen effect class for PNG sequences
# Generic screen effect display for static animations
# Parameters:
# - effect_name: Name of the effect folder in images/FX/animated/
# - x, y: Position coordinates
# - loop: Whether the effect should loop
# - fps: Frames per second for the animation
screen png_sequence_effect(effect_name, x=0, y=0, loop=True, fps=30):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None
        
        # Create animated image from PNG sequence
        add At("images/FX/animated/" + effect_name + "/" + effect_name + "_0000.png", png_sequence_transform(effect_name, loop, fps))

# ATL transform for PNG sequence animation
transform png_sequence_transform(effect_name, loop=True, fps=30):
    # Get the number of frames by checking the directory
    function get_png_sequence_frames_with_params(effect_name, loop, fps)

# Python function to handle PNG sequence animation
init python:
    def get_png_sequence_frames_with_params(effect_name, loop, fps):
        """Create a function that captures the parameters and returns the animation function"""
        def animation_function(trans, st, at):
            """Handle PNG sequence animation using ATL function"""
            import os
            
            # Calculate frame duration
            frame_duration = 1.0 / fps
            
            # Calculate current frame based on time
            frame_number = int(st / frame_duration)
            
            # Get the directory path
            dir_path = "game/images/FX/animated/" + effect_name
            
            # Check if directory exists
            if not os.path.exists(dir_path):
                return 0.1  # Return small delay if directory doesn't exist
            
            # Count frames in directory
            frame_count = 0
            for file in os.listdir(dir_path):
                if file.startswith(effect_name + "_") and file.endswith(".png"):
                    frame_count += 1
            
            if frame_count == 0:
                return 0.1  # Return small delay if no frames found
            
            # Calculate current frame (with looping)
            if loop:
                current_frame = frame_number % frame_count
            else:
                current_frame = min(frame_number, frame_count - 1)
            
            # Format frame number with leading zeros
            frame_str = f"{current_frame:04d}"

            # Debug log for fog animation
            if effect_name == "fog":
                renpy.log("Fog animation: frame_count=%d, current_frame=%d, file=%s", frame_count, current_frame, "images/FX/animated/" + effect_name + "/" + effect_name + "_" + frame_str + ".png")

            # Set the displayable to the current frame
            trans.child = "images/FX/animated/" + effect_name + "/" + effect_name + "_" + frame_str + ".png"
            
            # Return delay until next frame
            return frame_duration
        
        return animation_function

# Weather Effects using SnowBlossom
# Light rain effect using SnowBlossom
screen rain_light(x=0, y=0):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None
        
        # Grey filter overlay for gloomy atmosphere
        add Solid("#404040") alpha 0.15
        
        # Light rain using SnowBlossom with rain drops - extremely fast aggressive downward movement with random positioning, varied transparency, and size variation
        add SnowBlossom("images/FX/snowblossom/rain/rain_1.png", count=30, xspeed=(0, 5), yspeed=(1200, 1500), start=0, fast=True, horizontal=False, border=50) alpha 0.4 zoom 0.8
        add SnowBlossom("images/FX/snowblossom/rain/rain_2.png", count=25, xspeed=(0, 3), yspeed=(1100, 1400), start=0.5, fast=True, horizontal=False, border=50) alpha 0.2 zoom 0.5
        add SnowBlossom("images/FX/snowblossom/rain/rain_3.png", count=20, xspeed=(0, 7), yspeed=(1300, 1600), start=1.0, fast=True, horizontal=False, border=50) alpha 0.5 zoom 1.0

# Heavy rain effect using SnowBlossom
screen rain_heavy(x=0, y=0):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None
        
        # Grey filter overlay for gloomy atmosphere (slightly darker for heavy rain)
        add Solid("#303030") alpha 0.2
        
        # Heavy rain using SnowBlossom with rain drops - extremely fast aggressive downward movement with high density, varied transparency, and size variation
        add SnowBlossom("images/FX/snowblossom/rain/rain_4.png", count=80, xspeed=(0, 8), yspeed=(1400, 1800), start=0, fast=True, horizontal=False, border=50) alpha 0.3 zoom 1.2
        add SnowBlossom("images/FX/snowblossom/rain/rain_5.png", count=70, xspeed=(0, 5), yspeed=(1300, 1700), start=0.2, fast=True, horizontal=False, border=50) alpha 0.2 zoom 0.9
        add SnowBlossom("images/FX/snowblossom/rain/rain_6.png", count=65, xspeed=(0, 10), yspeed=(1500, 1900), start=0.4, fast=True, horizontal=False, border=50) alpha 0.35 zoom 1.0
        add SnowBlossom("images/FX/snowblossom/rain/rain_1.png", count=60, xspeed=(0, 6), yspeed=(1200, 1600), start=0.6, fast=True, horizontal=False, border=50) alpha 0.15 zoom 0.7
        add SnowBlossom("images/FX/snowblossom/rain/rain_2.png", count=55, xspeed=(0, 4), yspeed=(1350, 1750), start=0.8, fast=True, horizontal=False, border=50) alpha 0.25 zoom 1.1

# Light snow effect using SnowBlossom
screen snow_light(x=0, y=0):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None
        
        # Light snow using SnowBlossom with custom snowflake assets
        add SnowBlossom("images/FX/snowblossom/snow/snow_1.png", count=50, xspeed=(-40, 40), yspeed=(60, 160), start=0, fast=True, horizontal=False)
        add SnowBlossom("images/FX/snowblossom/snow/snow_2.png", count=40, xspeed=(-35, 35), yspeed=(50, 140), start=0.5, fast=True, horizontal=False)
        add SnowBlossom("images/FX/snowblossom/snow/snow_3.png", count=35, xspeed=(-45, 45), yspeed=(70, 170), start=1.0, fast=True, horizontal=False)

# Heavy snow effect using SnowBlossom
screen snow_heavy(x=0, y=0, y_offset=0):
    layer "special_fx"
    frame:
        xpos x
        ypos y + y_offset
        background None
        
        # Heavy snow using SnowBlossom with custom snowflake assets - varied sizes
        add SnowBlossom("images/FX/snowblossom/snow/snow_4.png", count=120, xspeed=(-60,60), yspeed=(70,40), start=0, fast=True, horizontal=False) zoom 1.4
        add SnowBlossom("images/FX/snowblossom/snow/snow_5.png", count=100, xspeed=(-50,50), yspeed=(60, 130), start=0.2, fast=True, horizontal=False) zoom 0.8
        add SnowBlossom("images/FX/snowblossom/snow/snow_6.png", count=90, xspeed=(-70,70), yspeed=(80, 150), start=0.4, fast=True, horizontal=False) zoom 1.2
        add SnowBlossom("images/FX/snowblossom/snow/snow_7.png", count=80, xspeed=(-40,40), yspeed=(50, 120), start=0.6, fast=True, horizontal=False) zoom 0.6
        add SnowBlossom("images/FX/snowblossom/snow/snow_1.png", count=70, xspeed=(-55,55), yspeed=(65, 135), start=0.8, fast=True, horizontal=False) zoom 1.0
        add SnowBlossom("images/FX/snowblossom/snow/snow_2.png", count=60, xspeed=(-45,45), yspeed=(75, 145), start=1.0, fast=True, horizontal=False) zoom 1.6
        add SnowBlossom("images/FX/snowblossom/snow/snow_3.png", count=50, xspeed=(-65,65), yspeed=(55, 125), start=1.2, fast=True, horizontal=False) zoom 0.7

# Blizzard effect using SnowBlossom
screen blizzard(x=0, y=0, y_offset=0):
    layer "special_fx"
    frame:
        xpos x
        ypos y + y_offset
        background None
        
        # Bluish-grey filter overlay for blustery atmosphere
        add Solid("#2a3a4a") alpha 0.25        
        # Blizzard using SnowBlossom with custom snowflake assets - intense varied sizes and speeds
        add SnowBlossom("images/FX/snowblossom/snow/snow_4.png", count=100, xspeed=(-200, 200), yspeed=(400, 700), start=0, fast=True, horizontal=False) zoom 2.0
        add SnowBlossom("images/FX/snowblossom/snow/snow_5.png", count=90, xspeed=(-180, 180), yspeed=(350, 650), start=0.1, fast=True, horizontal=False) zoom 0.7
        add SnowBlossom("images/FX/snowblossom/snow/snow_6.png", count=80, xspeed=(-220, 220), yspeed=(500, 900), start=0.2, fast=True, horizontal=False) zoom 1.8
        add SnowBlossom("images/FX/snowblossom/snow/snow_7.png", count=70, xspeed=(-160, 160), yspeed=(300, 600), start=0.3, fast=True, horizontal=False) zoom 0.4
        add SnowBlossom("images/FX/snowblossom/snow/snow_1.png", count=65, xspeed=(-210, 210), yspeed=(450, 800), start=0.4, fast=True, horizontal=False) zoom 1.5
        add SnowBlossom("images/FX/snowblossom/snow/snow_2.png", count=60, xspeed=(-150, 150), yspeed=(600, 1000), start=0.5, fast=True, horizontal=False) zoom 2.5
        add SnowBlossom("images/FX/snowblossom/snow/snow_3.png", count=55, xspeed=(-230, 230), yspeed=(350, 900), start=0.6, fast=True, horizontal=False) zoom 0.3

# Weather Effects using webm
# Light rain effect using webm
screen rain_light_webm(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("rain_light_mov", screen_blend) xpos x ypos y + y_offset

# Heavy rain effect using webm
screen rain_heavy_webm(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("rain_heavy_mov", screen_blend) xpos x ypos y + y_offset

# Light snow effect using webm
screen snow_light_webm(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("snow_light_mov", screen_blend) xpos x ypos y + y_offset

# Heavy snow effect using webm
screen snow_heavy_webm(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("snow_heavy_mov", screen_blend) xpos x ypos y + y_offset

# Fog effect using webm
screen fog_webm(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("fog_mov", screen_blend) xpos x ypos y + y_offset

# Atmospheric Effects using PNG sequences
# Fog effect
transform fog_offset:
    time 0.5

# Layered fog effect using SnowBlossom
screen fog_light(x=0, y=0, alpha=0.85):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None

        add SnowBlossom("images/FX/snowblossom/fog/fog_0000.png", count=18, border=800, yspeed=(8, -8), xspeed=(40, -40), start=0, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0001.png", count=16, border=700, yspeed=(-12, -4), xspeed=(30, -30), start=0.3, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0002.png", count=20, border=900, yspeed=(6, -10), xspeed=(50, -50), start=0.6, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0003.png", count=14, border=850, yspeed=(10, -6), xspeed=(35, -35), start=0.9, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0004.png", count=15, border=750, yspeed=(-8, 8), xspeed=(45, -45), start=1.2, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0005.png", count=13, border=950, yspeed=(7, -7), xspeed=(38, -38), start=1.5, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0006.png", count=17, border=800, yspeed=(-9, 9), xspeed=(42, -42), start=1.8, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0007.png", count=12, border=700, yspeed=(11, -11), xspeed=(36, -36), start=2.1, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0008.png", count=19, border=850, yspeed=(-10, 10), xspeed=(44, -44), start=2.4, fast=True, horizontal=True) alpha alpha

# Heavy fog effect using SnowBlossom
screen fog_heavy(x=0, y=0, alpha=1.0):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None

        add SnowBlossom("images/FX/snowblossom/fog/fog_0000.png", count=48, border=400, yspeed=(12, -12), xspeed=(60, -60), start=0, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0001.png", count=42, border=350, yspeed=(-18, -8), xspeed=(50, -50), start=0.3, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0002.png", count=54, border=500, yspeed=(10, -16), xspeed=(70, -70), start=0.6, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0003.png", count=38, border=450, yspeed=(14, -10), xspeed=(55, -55), start=0.9, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0004.png", count=40, border=300, yspeed=(-14, 14), xspeed=(65, -65), start=1.2, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0005.png", count=34, border=550, yspeed=(13, -13), xspeed=(58, -58), start=1.5, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0006.png", count=45, border=400, yspeed=(-15, 15), xspeed=(62, -62), start=1.8, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0007.png", count=36, border=350, yspeed=(16, -16), xspeed=(56, -56), start=2.1, fast=True, horizontal=True) alpha alpha
        add SnowBlossom("images/FX/snowblossom/fog/fog_0008.png", count=52, border=450, yspeed=(-13, 13), xspeed=(64, -64), start=2.4, fast=True, horizontal=True) alpha alpha

# Underwater effect
screen underwater(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("underwater_mov", screen_blend) xpos x ypos y + y_offset

# God ray effect (left)
screen godray_left(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("godrays_left_mov", screen_blend) xpos x ypos y + y_offset

# God ray effect (right)
screen godray_right(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("godrays_right_mov", screen_blend) xpos x ypos y + y_offset

# Nature Effects using video
# Falling leaves effect
screen leaves(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("leaves_mov", screen_blend) xpos x ypos y + y_offset

# Cherry blossoms effect
screen blossoms(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("blossom_mov", screen_blend) xpos x ypos y + y_offset

# Fireflies effect using SnowBlossom
screen fireflies(x=0, y=0, y_offset=-100):
    layer "special_fx"
    frame:
        xpos x
        ypos y + y_offset
        background None
        
        # Fireflies using SnowBlossom with firefly assets
        add SnowBlossom("images/FX/snowblossom/fireflies/fireflies_1.png", count=20, xspeed=(10, 30), yspeed=(20, 60), start=0, fast=True, horizontal=True)
        add SnowBlossom("images/FX/snowblossom/fireflies/fireflies_2.png", count=15, xspeed=(15, 35), yspeed=(15, 55), start=0.5, fast=True, horizontal=True)
        add SnowBlossom("images/FX/snowblossom/fireflies/fireflies_3.png", count=12, xspeed=(20, 40), yspeed=(25, 65), start=1.0, fast=True, horizontal=True)

# Star Effects using video (Multiple Colors)
# Blue stars effect
screen stars_blue(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("stars_blue_mov", screen_blend) xpos x ypos y + y_offset

# Red stars effect
screen stars_red(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("stars_red_mov", screen_blend) xpos x ypos y + y_offset

# Green stars effect
screen stars_green(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("stars_green_mov", screen_blend) xpos x ypos y + y_offset

# Yellow stars effect
screen stars_yellow(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("stars_yellow_mov", screen_blend) xpos x ypos y + y_offset

# Purple stars effect
screen stars_purple(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("stars_purple_mov", screen_blend) xpos x ypos y + y_offset

# Pink stars effect
screen stars_pink(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("stars_pink_mov", screen_blend) xpos x ypos y + y_offset

# Sparkle Effects using video (Multiple Colors)
# Blue sparkle effect
screen sparkle_blue(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("sparkle_blue_mov", screen_blend) xpos x ypos y + y_offset

# Red sparkle effect
screen sparkle_red(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("sparkle_red_mov", screen_blend) xpos x ypos y + y_offset

# Green sparkle effect
screen sparkle_green(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("sparkle_green_mov", screen_blend) xpos x ypos y + y_offset

# Yellow sparkle effect
screen sparkle_yellow(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("sparkle_yellow_mov", screen_blend) xpos x ypos y + y_offset

# Purple sparkle effect
screen sparkle_purple(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("sparkle_purple_mov", screen_blend) xpos x ypos y + y_offset

# Pink sparkle effect
screen sparkle_pink(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("sparkle_pink_mov", screen_blend) xpos x ypos y + y_offset

# Portal Effects using video (Multiple Colors)
# Blue portal effect
screen portal_blue(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("portal_blue_mov", screen_blend) xpos x ypos y + y_offset

# Red portal effect
screen portal_red(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("portal_red_mov", screen_blend) xpos x ypos y + y_offset

# Green portal effect
screen portal_green(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("portal_green_mov", screen_blend) xpos x ypos y + y_offset

# Yellow portal effect
screen portal_yellow(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("portal_yellow_mov", screen_blend) xpos x ypos y + y_offset

# Purple portal effect
screen portal_purple(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("portal_purple_mov", screen_blend) xpos x ypos y + y_offset

# Pink portal effect
screen portal_pink(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("portal_pink_mov", screen_blend) xpos x ypos y + y_offset

# Plasma Effects using video (Multiple Colors)
# Blue plasma effect
screen plasma_blue(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("plasma_blue_mov", screen_blend) xpos x ypos y + y_offset

# Red plasma effect
screen plasma_red(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("plasma_red_mov", screen_blend) xpos x ypos y + y_offset

# Green plasma effect
screen plasma_green(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("plasma_green_mov", screen_blend) xpos x ypos y + y_offset

# Yellow plasma effect
screen plasma_yellow(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("plasma_yellow_mov", screen_blend) xpos x ypos y + y_offset

# Purple plasma effect
screen plasma_purple(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("plasma_purple_mov", screen_blend) xpos x ypos y + y_offset

# White plasma effect
screen plasma_white(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("plasma_white_mov", screen_blend) xpos x ypos y + y_offset

# Confetti Effects using video
# Warm colored confetti effect
screen confetti_warm(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("confetti_warm_mov", screen_blend) xpos x ypos y + y_offset

# Cool colored confetti effect
screen confetti_cool(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("confetti_cool_mov", screen_blend) xpos x ypos y + y_offset

# Colorful confetti effect
screen confetti_colorful(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("confetti_colorful_mov", screen_blend) xpos x ypos y + y_offset

# Special Effects using video
# Matrix-style effect
screen matrix(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("matrix_blue_mov", screen_blend) xpos x ypos y + y_offset

# Night sky effect
screen night_sky(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("nightsky_mov", screen_blend) xpos x ypos y + y_offset

# Shooting star effect
screen shooting_star(x=0, y=0, y_offset=0):
    layer "special_fx"
    add At("nightsky_star_mov", screen_blend) xpos x ypos y + y_offset

# Dust effect using SnowBlossom
screen dust(x=0, y=0, y_offset=-100):
    layer "special_fx"
    frame:
        xpos x
        ypos y + y_offset
        background None
        
        # Dust particles using SnowBlossom
        add SnowBlossom("images/FX/snowblossom/dust/dust_1.png", count=40, xspeed=(5, 15), yspeed=(10, 30), start=0, fast=True, horizontal=True)
        add SnowBlossom("images/FX/snowblossom/dust/dust_2.png", count=35, xspeed=(8, 18), yspeed=(8, 28), start=0.3, fast=True, horizontal=True)
        add SnowBlossom("images/FX/snowblossom/dust/dust_3.png", count=30, xspeed=(12, 22), yspeed=(12, 32), start=0.6, fast=True, horizontal=True)

# Petals effect using SnowBlossom
screen petals(x=0, y=0, y_offset=-100):
    layer "special_fx"
    frame:
        xpos x
        ypos y + y_offset
        background None
        
        # Falling petals using SnowBlossom
        add SnowBlossom("images/FX/snowblossom/petals/petals_1.png", count=25, xspeed=(15, 35), yspeed=(50, 100), start=0, fast=True, horizontal=False)
        add SnowBlossom("images/FX/snowblossom/petals/petals_2.png", count=20, xspeed=(20, 40), yspeed=(60, 110), start=0.4, fast=True, horizontal=False)
        add SnowBlossom("images/FX/snowblossom/petals/petals_3.png", count=18, xspeed=(25, 45), yspeed=(70, 120), start=0.8, fast=True, horizontal=False)

# Composite Effects (Multiple effects combined)
# Combined magical atmosphere effect
screen magical_atmosphere(x=0, y=0):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None
        
        # Multiple effects layered
        add At("sparkle_blue_mov", screen_blend) xpos 0 ypos 0
        add At("stars_purple_mov", screen_blend) xpos 0 ypos 0
        use fireflies(0, 0)

# Combined storm weather effect
screen storm_weather(x=0, y=0):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None
        
        # Multiple effects layered
        use rain_heavy(0,0)
        add At("fog_mov", screen_blend) xpos 0 ypos 0

# Combined celebration effect
screen celebration(x=0, y=0):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None
        
        # Multiple effects layered
        add At("confetti_colorful_mov", screen_blend) xpos 0 ypos 0
        add At("sparkle_yellow_mov", screen_blend) xpos 0 ypos 0
        add At("stars_pink_mov", screen_blend) xpos 0 ypos 0

# Helper Functions for PNG Effects
init python:
    # PNG Effect Helper Functions
    def show_png_effect(effect_name, x=0, y=0, fps=30):
        """Helper function to show PNG sequence effects"""
        if hasattr(renpy, 'show_screen'):
            renpy.show_screen(effect_name, x=x, y=y, fps=fps)
    
    def hide_png_effect(effect_name):
        """Helper function to hide PNG sequence effects"""
        if hasattr(renpy, 'hide_screen'):
            renpy.hide_screen(effect_name)
    
    # Weather effect helpers
    def show_weather_effect(effect_name, x=0, y=0, y_offset=0):
        """Helper function to show weather effects"""
        weather_effects = {
            "rain_light": "rain_light",
            "rain_heavy": "rain_heavy",
            "snow_light": "snow_light",
            "snow_heavy": "snow_heavy"
        }
        if effect_name in weather_effects:
            if effect_name == "snow_heavy":
                renpy.show_screen(weather_effects[effect_name], x=x, y=y, y_offset=y_offset)
            else:
                renpy.show_screen(weather_effects[effect_name], x=x, y=y)
    
    def hide_weather_effect(effect_name):
        """Helper function to hide weather effects"""
        weather_effects = {
            "rain_light": "rain_light",
            "rain_heavy": "rain_heavy",
            "snow_light": "snow_light",
            "snow_heavy": "snow_heavy"
        }
        if effect_name in weather_effects:
            renpy.hide_screen(weather_effects[effect_name])
    
    # Atmospheric effect helpers
    def show_atmospheric_effect(effect_name, x=0, y=0, y_offset=-100):
        """Helper function to show atmospheric effects"""
        atmospheric_effects = {
            "fog": "fog",
            "underwater": "underwater",
            "godray_left": "godray_left",
            "godray_right": "godray_right",
            "leaves": "leaves",
            "blossoms": "blossoms",
            "fireflies": "fireflies",
            "dust": "dust",
            "petals": "petals"
        }
        if effect_name in atmospheric_effects:
            renpy.show_screen(atmospheric_effects[effect_name], x=x, y=y, y_offset=y_offset)
    
    def hide_atmospheric_effect(effect_name):
        """Helper function to hide atmospheric effects"""
        atmospheric_effects = {
            "fog": "fog",
            "underwater": "underwater",
            "godray_left": "godray_left",
            "godray_right": "godray_right",
            "leaves": "leaves",
            "blossoms": "blossoms",
            "fireflies": "fireflies",
            "dust": "dust",
            "petals": "petals"
        }
        if effect_name in atmospheric_effects:
            renpy.hide_screen(atmospheric_effects[effect_name])
    
    # Magical effect helpers
    def show_magical_effect(effect_type, color, x=0, y=0, y_offset=-100):
        """Helper function to show magical effects (stars, sparkles, etc.)"""
        if effect_type == "stars":
            star_effects = {
                "blue": "stars_blue",
                "red": "stars_red",
                "green": "stars_green",
                "yellow": "stars_yellow",
                "purple": "stars_purple",
                "pink": "stars_pink"
            }
            if color in star_effects:
                renpy.show_screen(star_effects[color], x=x, y=y, y_offset=y_offset)
        elif effect_type == "sparkle":
            sparkle_effects = {
                "blue": "sparkle_blue",
                "red": "sparkle_red",
                "green": "sparkle_green",
                "yellow": "sparkle_yellow",
                "purple": "sparkle_purple",
                "pink": "sparkle_pink"
            }
            if color in sparkle_effects:
                renpy.show_screen(sparkle_effects[color], x=x, y=y, y_offset=y_offset)
        elif effect_type == "portal":
            portal_effects = {
                "blue": "portal_blue",
                "red": "portal_red",
                "green": "portal_green",
                "yellow": "portal_yellow",
                "purple": "portal_purple",
                "pink": "portal_pink"
            }
            if color in portal_effects:
                renpy.show_screen(portal_effects[color], x=x, y=y, y_offset=y_offset)
        elif effect_type == "plasma":
            plasma_effects = {
                "blue": "plasma_blue",
                "red": "plasma_red",
                "green": "plasma_green",
                "yellow": "plasma_yellow",
                "purple": "plasma_purple",
                "white": "plasma_white"
            }
            if color in plasma_effects:
                renpy.show_screen(plasma_effects[color], x=x, y=y, y_offset=y_offset)
    
    def hide_magical_effect(effect_type, color):
        """Helper function to hide magical effects"""
        if effect_type == "stars":
            star_effects = {
                "blue": "stars_blue",
                "red": "stars_red",
                "green": "stars_green",
                "yellow": "stars_yellow",
                "purple": "stars_purple",
                "pink": "stars_pink"
            }
            if color in star_effects:
                renpy.hide_screen(star_effects[color])
        elif effect_type == "sparkle":
            sparkle_effects = {
                "blue": "sparkle_blue",
                "red": "sparkle_red",
                "green": "sparkle_green",
                "yellow": "sparkle_yellow",
                "purple": "sparkle_purple",
                "pink": "sparkle_pink"
            }
            if color in sparkle_effects:
                renpy.hide_screen(sparkle_effects[color])
        elif effect_type == "portal":
            portal_effects = {
                "blue": "portal_blue",
                "red": "portal_red",
                "green": "portal_green",
                "yellow": "portal_yellow",
                "purple": "portal_purple",
                "pink": "portal_pink"
            }
            if color in portal_effects:
                renpy.hide_screen(portal_effects[color])
        elif effect_type == "plasma":
            plasma_effects = {
                "blue": "plasma_blue",
                "red": "plasma_red",
                "green": "plasma_green",
                "yellow": "plasma_yellow",
                "purple": "plasma_purple",
                "white": "plasma_white"
            }
            if color in plasma_effects:
                renpy.hide_screen(plasma_effects[color])
    
    # Special effect helpers
    def show_special_effect(effect_name, x=0, y=0, y_offset=-100):
        """Helper function to show special effects"""
        special_effects = {
            "matrix": "matrix",
            "night_sky": "night_sky",
            "shooting_star": "shooting_star",
            "confetti_warm": "confetti_warm",
            "confetti_cool": "confetti_cool",
            "confetti_colorful": "confetti_colorful"
        }
        if effect_name in special_effects:
            renpy.show_screen(special_effects[effect_name], x=x, y=y, y_offset=y_offset)
    
    def hide_special_effect(effect_name):
        """Helper function to hide special effects"""
        special_effects = {
            "matrix": "matrix",
            "night_sky": "night_sky",
            "shooting_star": "shooting_star",
            "confetti_warm": "confetti_warm",
            "confetti_cool": "confetti_cool",
            "confetti_colorful": "confetti_colorful"
        }
        if effect_name in special_effects:
            renpy.hide_screen(special_effects[effect_name])
    
    # Composite effect helpers
    def show_composite_effect(effect_name, x=0, y=0):
        """Helper function to show composite effects"""
        composite_effects = {
            "magical_atmosphere": "magical_atmosphere",
            "storm_weather": "storm_weather",
            "celebration": "celebration"
        }
        if effect_name in composite_effects:
            renpy.show_screen(composite_effects[effect_name], x=x, y=y)
    
    def hide_composite_effect(effect_name):
        """Helper function to hide composite effects"""
        composite_effects = {
            "magical_atmosphere": "magical_atmosphere",
            "storm_weather": "storm_weather",
            "celebration": "celebration"
        }
        if effect_name in composite_effects:
            renpy.hide_screen(composite_effects[effect_name])
    
    # Utility functions
    def hide_all_effects():
        """Hide all currently active effects"""
        all_effects = [
            # Weather effects
            "rain_light", "rain_heavy", "snow_light", "snow_heavy",
            # Atmospheric effects
            "fog", "underwater", "godray_left", "godray_right",
            "leaves", "blossoms", "fireflies", "dust", "petals",
            # Stars (all colors)
            "stars_blue", "stars_red", "stars_green", "stars_yellow", "stars_purple", "stars_pink",
            # Sparkles (all colors)
            "sparkle_blue", "sparkle_red", "sparkle_green", "sparkle_yellow", "sparkle_purple", "sparkle_pink",
            # Portals (all colors)
            "portal_blue", "portal_red", "portal_green", "portal_yellow", "portal_purple", "portal_pink",
            # Plasma (all colors)
            "plasma_blue", "plasma_red", "plasma_green", "plasma_yellow", "plasma_purple", "plasma_white",
            # Confetti
            "confetti_warm", "confetti_cool", "confetti_colorful",
            # Special
            "matrix", "night_sky", "shooting_star",
            # Composite
            "magical_atmosphere", "storm_weather", "celebration"
        ]
        
        for effect in all_effects:
            try:
                renpy.hide_screen(effect)
            except:
                pass  # Screen might not be showing, ignore errors 

# Parallax fog effect using static base + animated layers
screen fog_parallax(x=0, y=0, alpha=0.8):
    layer "special_fx"
    frame:
        xpos x
        ypos y
        background None

        # Static fog base layer
        add "images/FX/parallax/fog_base.png" alpha 1.0
        
        # Animated fog layers on top (reduced alpha for visibility of base)
        add SnowBlossom("images/FX/snowblossom/fog/fog_0000.png", count=8, border=1200, yspeed=(5, -5), xspeed=(30, -30), start=0, fast=True, horizontal=True) alpha (alpha * 0.15)
        add SnowBlossom("images/FX/snowblossom/fog/fog_0001.png", count=6, border=1000, yspeed=(-8, -2), xspeed=(25, -25), start=0.5, fast=True, horizontal=True) alpha (alpha * 0.10)
        add SnowBlossom("images/FX/snowblossom/fog/fog_0002.png", count=10, border=1400, yspeed=(3, -8), xspeed=(35, -35), start=1.0, fast=True, horizontal=True) alpha (alpha * 0.18)
        add SnowBlossom("images/FX/snowblossom/fog/fog_0003.png", count=7, border=1100, yspeed=(7, -3), xspeed=(28, -28), start=1.5, fast=True, horizontal=True) alpha (alpha * 0.08)
        add SnowBlossom("images/FX/snowblossom/fog/fog_0004.png", count=9, border=1300, yspeed=(-6, 6), xspeed=(32, -32), start=2.0, fast=True, horizontal=True) alpha (alpha * 0.13) 
