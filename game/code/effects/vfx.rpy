# Screen Effects
# Handles webm effects with black backgrounds using screen blending

# Screen blending mode for transparency
init python:
    # Screen blending mode for black background removal
    def screen_blend_mode():
        return "screen"

# Base screen effect class
# Generic screen effect display
# Parameters:
# - effect_name: Name of the effect file (without extension)
# - x, y: Position coordinates
# - loop: Whether the effect should loop
# - y_offset: Vertical offset for fine-tuning alignment
# - scale_to_screen: If True, scales the effect to the full screen size
screen screen_effect(effect_name, x=0, y=0, loop=True, y_offset=0, scale_to_screen=False):
    frame:
        xpos x
        ypos y + y_offset
        background None

        if scale_to_screen:
            add Movie(play="images/FX/webm/" + effect_name + ".webm", loop=loop, channel="movie") size (config.screen_width, config.screen_height):
                additive 1.0
        else:
            add Movie(play="images/FX/webm/" + effect_name + ".webm", loop=loop, channel="movie"):
                additive 1.0

# Alternative WebM effect implementation using different approach
# This version uses a different method to handle transparency
screen webm_effect_alt(effect_name, x=0, y=0, loop=True):
    frame:
        xpos x
        ypos y
        background None
        
        # Alternative approach with additive blending
        add Movie(play="images/FX/webm/" + effect_name + ".webm", loop=loop, channel="movie"):
            additive 1.0

# Helper for vertical tiling
init python:
    def tiled_screen_effect(effect_name, x=0, y=0, loop=True, y_offset=0, scale_to_screen=True):
        return [
            Movie(play="images/FX/webm/" + effect_name + ".webm", loop=loop, channel="movie")
                .size((config.screen_width, config.screen_height))
                .at_list([Transform(ypos=y_offset)])
                .additive(1.0),
            Movie(play="images/FX/webm/" + effect_name + ".webm", loop=loop, channel="movie")
                .size((config.screen_width, config.screen_height))
                .at_list([Transform(ypos=(config.screen_height // 2 + y_offset))])
                .additive(1.0)
        ]

# Weather Effects
# Light rain effect
screen rain_light(x=0, y=0):
    use screen_effect("Rain_light", x, y, True)

# Heavy rain effect
screen rain_heavy(x=0, y=0):
    use screen_effect("Rain_heavy", x, y, True)

# Light snow effect using Ren'Py's snowblossom with custom snowflakes
screen snow_light(x=0, y=0):
    zorder 100
    frame:
        xpos x
        ypos y
        background None
        
        # Light snow using snowblossom with custom snowflake assets
        add SnowBlossom("images/FX/png/snow/snow_1.png", count=50, xspeed=(20, 50), yspeed=(100, 200), start=0, fast=True, horizontal=True)
        add SnowBlossom("images/FX/png/snow/snow_2.png", count=40, xspeed=(15, 45), yspeed=(80, 180), start=0.5, fast=True, horizontal=True)
        add SnowBlossom("images/FX/png/snow/snow_3.png", count=35, xspeed=(25, 55), yspeed=(120, 220), start=1.0, fast=True, horizontal=True)

# Heavy snow effect using Ren'Py's snowblossom with custom snowflakes
screen snow_heavy(x=0, y=0, y_offset=0):
    zorder 100
    frame:
        xpos x
        ypos y + y_offset
        background None
        
        # Heavy snow using snowblossom with custom snowflake assets
        add SnowBlossom("images/FX/png/snow/snow_4.png", count=80, xspeed=(30, 60), yspeed=(150, 250), start=0, fast=True, horizontal=True)
        add SnowBlossom("images/FX/png/snow/snow_5.png", count=70, xspeed=(25, 55), yspeed=(130, 230), start=0.3, fast=True, horizontal=True)
        add SnowBlossom("images/FX/png/snow/snow_6.png", count=65, xspeed=(35, 65), yspeed=(170, 270), start=0.6, fast=True, horizontal=True)
        add SnowBlossom("images/FX/png/snow/snow_7.png", count=60, xspeed=(20, 50), yspeed=(110, 210), start=0.9, fast=True, horizontal=True)

# Atmospheric Effects
# Fog effect
screen fog(x=0, y=0, y_offset=-100, vertical_tile=False):
    zorder 100
    if vertical_tile:
        add tiled_screen_effect("Fog", x, y, True, y_offset, True)[0]
        add tiled_screen_effect("Fog", x, y, True, y_offset, True)[1]
    else:
        use screen_effect("Fog", x, y, True, y_offset, True)

# Underwater effect
screen underwater(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Underwater", x, y, True, y_offset, True)

# God ray effect (left)
screen godray_left(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("GodRay_L", x, y, True, y_offset, True)

# God ray effect (right)
screen godray_right(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("GodRay_R", x, y, True, y_offset, True)

# Nature Effects
# Falling leaves effect
screen leaves(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Leaves", x, y, True, y_offset, True)

# Cherry blossoms effect
screen blossoms(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Blossoms", x, y, True, y_offset, True)

# Fireflies effect
screen fireflies(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Fireflies", x, y, True, y_offset, True)

# Star Effects (Multiple Colors)
# Blue stars effect
screen stars_blue(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Stars_blue", x, y, True, y_offset, True)

# Red stars effect
screen stars_red(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Stars_red", x, y, True, y_offset, True)

# Green stars effect
screen stars_green(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Stars_green", x, y, True, y_offset, True)

# Yellow stars effect
screen stars_yellow(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Stars_yellow", x, y, True, y_offset, True)

# Purple stars effect
screen stars_purple(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Stars_purple", x, y, True, y_offset, True)

# Pink stars effect
screen stars_pink(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Stars_pink", x, y, True, y_offset, True)

# Alternative star effects using different blend approach
# Blue stars effect (alternative)
screen stars_blue_alt(x=0, y=0):
    use webm_effect_alt("Stars_blue", x, y, True)

# Purple stars effect (alternative)
screen stars_purple_alt(x=0, y=0):
    use webm_effect_alt("Stars_purple", x, y, True)

# Sparkle effects (alternative)
screen sparkle_blue_alt(x=0, y=0):
    use webm_effect_alt("Sparkle_blue", x, y, True)

# Sparkle Effects (Multiple Colors)
# Blue sparkle effect
screen sparkle_blue(x=0, y=0, y_offset=-100, vertical_tile=False):
    zorder 100
    # y_offset can be fine-tuned for alignment
    if vertical_tile:
        add tiled_screen_effect("Sparkle_blue", x, y, True, y_offset, True)[0]
        add tiled_screen_effect("Sparkle_blue", x, y, True, y_offset, True)[1]
    else:
        use screen_effect("Sparkle_blue", x, y, True, y_offset, True)

# Red sparkle effect
screen sparkle_red(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Sparkle_red", x, y, True, y_offset, True)

# Green sparkle effect
screen sparkle_green(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Sparkle_green", x, y, True, y_offset, True)

# Yellow sparkle effect
screen sparkle_yellow(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Sparkle_yellow", x, y, True, y_offset, True)

# Purple sparkle effect
screen sparkle_purple(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Sparkle_purple", x, y, True, y_offset, True)

# Pink sparkle effect
screen sparkle_pink(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Sparkle_pink", x, y, True, y_offset, True)

# ---
# Portal Effects (Multiple Colors)
# Blue portal effect
screen portal_blue(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Portal_blue", x, y, True, y_offset, True)

# Red portal effect
screen portal_red(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Portal_red", x, y, True, y_offset, True)

# Green portal effect
screen portal_green(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Portal_green", x, y, True, y_offset, True)

# Yellow portal effect
screen portal_yellow(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Portal_yellow", x, y, True, y_offset, True)

# Purple portal effect
screen portal_purple(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Portal_purple", x, y, True, y_offset, True)

# Pink portal effect
screen portal_pink(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Portal_pink", x, y, True, y_offset, True)

# Plasma Effects (Multiple Colors)
# Blue plasma effect
screen plasma_blue(x=0, y=0, y_offset=0):
    zorder 100
    use screen_effect("Plasma_blue", x, y, True, y_offset, True)

# Red plasma effect
screen plasma_red(x=0, y=0, y_offset=0):
    zorder 100
    use screen_effect("Plasma_red", x, y, True, y_offset, True)

# Green plasma effect
screen plasma_green(x=0, y=0, y_offset=0):
    zorder 100
    use screen_effect("Plasma_green", x, y, True, y_offset, True)

# Yellow plasma effect
screen plasma_yellow(x=0, y=0, y_offset=0):
    zorder 100
    use screen_effect("Plasma_yellow", x, y, True, y_offset, True)

# Purple plasma effect
screen plasma_purple(x=0, y=0, y_offset=0):
    zorder 100
    use screen_effect("Plasma_purple", x, y, True, y_offset, True)

# White plasma effect
screen plasma_white(x=0, y=0, y_offset=0):
    zorder 100
    use screen_effect("Plasma_white", x, y, True, y_offset, True)

# Confetti Effects
# Warm colored confetti effect
screen confetti_warm(x=0, y=0, y_offset=-50):
    zorder 100
    use screen_effect("Confetti_warm", x, y, True, y_offset, True)

# Cool colored confetti effect
screen confetti_cool(x=0, y=0, y_offset=-50):
    zorder 100
    use screen_effect("Confetti_cool", x, y, True, y_offset, True)

# Colorful confetti effect
screen confetti_colorful(x=0, y=0, y_offset=-50):
    zorder 100
    use screen_effect("Confetti_colorful", x, y, True, y_offset, True)

# Special Effects
# Matrix-style effect
screen matrix(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("Matrix", x, y, True, y_offset, True)

# Night sky effect
screen night_sky(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("NightSky", x, y, True, y_offset, True)

# Shooting star effect
screen shooting_star(x=0, y=0, y_offset=-100):
    zorder 100
    use screen_effect("NightSky_ShootingStar", x, y, True, y_offset, True)

# Composite Effects (Multiple effects combined)
# Combined magical atmosphere effect
screen magical_atmosphere(x=0, y=0):
    frame:
        xpos x
        ypos y
        background None
        
        # Multiple effects layered
        use sparkle_blue(0, 0)
        use stars_purple(0, 0)
        use fireflies(0, 0)

# Combined storm weather effect
screen storm_weather(x=0, y=0):
    frame:
        xpos x
        ypos y
        background None
        
        # Multiple effects layered
        use rain_heavy(0, 0)
        use fog(0, 0)

# Combined celebration effect
screen celebration(x=0, y=0):
    frame:
        xpos x
        ypos y
        background None
        
        # Multiple effects layered
        use confetti_colorful(0, 0)
        use sparkle_yellow(0, 0)
        use stars_pink(0, 0) 

# PNG Effects System
# Handles sprite sheet animations from various effect categories

init python:
    # PNG Effect Categories and their frame counts
    PNG_EFFECTS = {
        "light": {
            "cast1": {"frames": 15, "fps": 30, "file": "30FPS_ASLight_01_Cast.png"},
            "cast2": {"frames": 23, "fps": 30, "file": "30FPS_ASLight_02_Cast2.png"},
            "glare": {"frames": 15, "fps": 30, "file": "30FPS_ASLight_03_Glare.png"},
            "ray": {"frames": 15, "fps": 30, "file": "30FPS_ASLight_04_Ray.png"},
            "sparkle": {"frames": 30, "fps": 30, "file": "30FPS_ASLight_05_Sparkle.png"},
            "scintillation": {"frames": 30, "fps": 30, "file": "30FPS_ASLight_06_Scintillation.png"},
            "gleam": {"frames": 38, "fps": 30, "file": "30FPS_ASLight_07_Gleam.png"},
            "twinkle": {"frames": 45, "fps": 30, "file": "30FPS_ASLight_08_Twinkle.png"},
            "photon": {"frames": 45, "fps": 30, "file": "30FPS_ASLight_09_Photon.png"},
            "radiance": {"frames": 90, "fps": 30, "file": "30FPS_ASLight_10_Radiance.png"}
        },
        "wind": {
            "cast": {"frames": 15, "fps": 30, "file": "30FPS_ASWind_01_Cast.png"},
            "cast2": {"frames": 23, "fps": 30, "file": "30FPS_ASWind_02_Cast2.png"},
            "whirlwind": {"frames": 15, "fps": 30, "file": "30FPS_ASWind_03_Whirlwind.png"},
            "breeze": {"frames": 15, "fps": 30, "file": "30FPS_ASWind_04_Breeze.png"},
            "twister": {"frames": 30, "fps": 30, "file": "30FPS_ASWind_05_Twister.png"},
            "gust": {"frames": 30, "fps": 30, "file": "30FPS_ASWind_06_Gust.png"},
            "vacuum": {"frames": 38, "fps": 30, "file": "30FPS_ASWind_07_Vacuum.png"},
            "cyclone": {"frames": 45, "fps": 30, "file": "30FPS_ASWind_08_Cyclone.png"},
            "updraft": {"frames": 45, "fps": 30, "file": "30FPS_ASWind_09_Updraft.png"},
            "tornado": {"frames": 90, "fps": 30, "file": "30FPS_ASWind_10_Tornado.png"}
        }
        # Add more categories as needed: ice, technology, esoteric, curses, nocturne, infernal
    }
    
    # Sprite sheet configuration
    SPRITE_SHEET_CONFIG = {
        "frame_width": 192,
        "frame_height": 192,
        "columns": 5,
        "rows": 20  # Maximum rows
    }

# Base PNG effect display
# Generic PNG effect display using sprite sheets
# Parameters:
# - category: Effect category (light, wind, ice, etc.)
# - effect_name: Name of the effect within the category
# - x, y: Position coordinates
# - fps: Frames per second (30 or 60)
# - loop: Whether the effect should loop
screen png_effect(category, effect_name, x=0, y=0, fps=30, loop=True):
    frame:
        xpos x
        ypos y
        background None
        
        if category in PNG_EFFECTS and effect_name in PNG_EFFECTS[category]:
            $ effect_data = PNG_EFFECTS[category][effect_name]
            $ frame_count = effect_data["frames"]
            $ frame_duration = 1.0 / fps
            
            # Create animated sprite from sprite sheet
            add "images/FX/png/" + category + "/" + str(fps) + "FPS/" + effect_data["file"]:
                size (SPRITE_SHEET_CONFIG["frame_width"], SPRITE_SHEET_CONFIG["frame_height"])
                # For now, just show the first frame - sprite sheet animation will be implemented later
                # when we have a proper ATL-based solution

# Note: PNG sprite sheet animation will be implemented using proper ATL transforms
# when we have individual frame images or a better sprite sheet solution

# Light Effects
# Light casting animation 1
screen light_cast1(x=0, y=0, fps=30):
    use png_effect("light", "cast1", x, y, fps, True)

# Light casting animation 2
screen light_cast2(x=0, y=0, fps=30):
    use png_effect("light", "cast2", x, y, fps, True)

# Light glare effect
screen light_glare(x=0, y=0, fps=30):
    use png_effect("light", "glare", x, y, fps, True)

# Light ray effect
screen light_ray(x=0, y=0, fps=30):
    use png_effect("light", "ray", x, y, fps, True)

# Light sparkle effect
screen light_sparkle(x=0, y=0, fps=30):
    use png_effect("light", "sparkle", x, y, fps, True)

# Light scintillation effect
screen light_scintillation(x=0, y=0, fps=30):
    use png_effect("light", "scintillation", x, y, fps, True)

# Light gleam effect
screen light_gleam(x=0, y=0, fps=30):
    use png_effect("light", "gleam", x, y, fps, True)

# Light twinkle effect
screen light_twinkle(x=0, y=0, fps=30):
    use png_effect("light", "twinkle", x, y, fps, True)

# Light photon effect (full screen)
screen light_photon(x=0, y=0, fps=30):
    use png_effect("light", "photon", x, y, fps, True)

# Light radiance effect (full screen)
screen light_radiance(x=0, y=0, fps=30):
    use png_effect("light", "radiance", x, y, fps, True)

# Wind Effects
# Wind casting animation
screen wind_cast(x=0, y=0, fps=30):
    use png_effect("wind", "cast", x, y, fps, True)

# Wind casting animation 2
screen wind_cast2(x=0, y=0, fps=30):
    use png_effect("wind", "cast2", x, y, fps, True)

# Wind whirlwind effect
screen wind_whirlwind(x=0, y=0, fps=30):
    use png_effect("wind", "whirlwind", x, y, fps, True)

# Wind breeze effect
screen wind_breeze(x=0, y=0, fps=30):
    use png_effect("wind", "breeze", x, y, fps, True)

# Wind twister effect
screen wind_twister(x=0, y=0, fps=30):
    use png_effect("wind", "twister", x, y, fps, True)

# Wind gust effect
screen wind_gust(x=0, y=0, fps=30):
    use png_effect("wind", "gust", x, y, fps, True)

# Wind vacuum effect
screen wind_vacuum(x=0, y=0, fps=30):
    use png_effect("wind", "vacuum", x, y, fps, True)

# Wind cyclone effect
screen wind_cyclone(x=0, y=0, fps=30):
    use png_effect("wind", "cyclone", x, y, fps, True)

# Wind updraft effect
screen wind_updraft(x=0, y=0, fps=30):
    use png_effect("wind", "updraft", x, y, fps, True)

# Wind tornado effect (full screen)
screen wind_tornado(x=0, y=0, fps=30):
    use png_effect("wind", "tornado", x, y, fps, True)

# Composite Light Effects
# Combined light magical attack
screen light_magical_attack(x=0, y=0, fps=30):
    frame:
        xpos x
        ypos y
        background None
        
        use light_cast1(0, 0, fps)
        use light_ray(0, 0, fps)
        use light_sparkle(0, 0, fps)

# Combined light healing effect
screen light_healing(x=0, y=0, fps=30):
    frame:
        xpos x
        ypos y
        background None
        
        use light_gleam(0, 0, fps)
        use light_twinkle(0, 0, fps)
        use light_scintillation(0, 0, fps)

# Composite Wind Effects
# Combined wind storm effect
screen wind_storm(x=0, y=0, fps=30):
    frame:
        xpos x
        ypos y
        background None
        
        use wind_whirlwind(0, 0, fps)
        use wind_gust(0, 0, fps)
        use wind_cyclone(0, 0, fps)

# Combined gentle wind effect
screen wind_gentle_breeze(x=0, y=0, fps=30):
    frame:
        xpos x
        ypos y
        background None
        
        use wind_breeze(0, 0, fps)
        use wind_twister(0, 0, fps) 

# PNG Effects Helper Functions
# Provides easy-to-use functions for PNG sprite sheet animations

init python:
    # PNG Effect Helper Functions
    def show_png_effect(category, effect_name, x=0, y=0, fps=30):
        """Helper function to show PNG effects"""
        screen_name = f"{category}_{effect_name}"
        if hasattr(renpy, 'show_screen'):
            renpy.show_screen(screen_name, x=x, y=y, fps=fps)
    
    def hide_png_effect(category, effect_name):
        """Helper function to hide PNG effects"""
        screen_name = f"{category}_{effect_name}"
        if hasattr(renpy, 'hide_screen'):
            renpy.hide_screen(screen_name)
    
    # Light effect helpers
    def show_light_effect(effect_name, x=0, y=0, fps=30):
        """Helper function to show light effects"""
        light_effects = {
            "cast1": "light_cast1",
            "cast2": "light_cast2", 
            "glare": "light_glare",
            "ray": "light_ray",
            "sparkle": "light_sparkle",
            "scintillation": "light_scintillation",
            "gleam": "light_gleam",
            "twinkle": "light_twinkle",
            "photon": "light_photon",
            "radiance": "light_radiance"
        }
        if effect_name in light_effects:
            renpy.show_screen(light_effects[effect_name], x=x, y=y, fps=fps)
    
    def hide_light_effect(effect_name):
        """Helper function to hide light effects"""
        light_effects = {
            "cast1": "light_cast1",
            "cast2": "light_cast2",
            "glare": "light_glare", 
            "ray": "light_ray",
            "sparkle": "light_sparkle",
            "scintillation": "light_scintillation",
            "gleam": "light_gleam",
            "twinkle": "light_twinkle",
            "photon": "light_photon",
            "radiance": "light_radiance"
        }
        if effect_name in light_effects:
            renpy.hide_screen(light_effects[effect_name])
    
    # Wind effect helpers
    def show_wind_effect(effect_name, x=0, y=0, fps=30):
        """Helper function to show wind effects"""
        wind_effects = {
            "cast": "wind_cast",
            "cast2": "wind_cast2",
            "whirlwind": "wind_whirlwind", 
            "breeze": "wind_breeze",
            "twister": "wind_twister",
            "gust": "wind_gust",
            "vacuum": "wind_vacuum",
            "cyclone": "wind_cyclone",
            "updraft": "wind_updraft",
            "tornado": "wind_tornado"
        }
        if effect_name in wind_effects:
            renpy.show_screen(wind_effects[effect_name], x=x, y=y, fps=fps)
    
    def hide_wind_effect(effect_name):
        """Helper function to hide wind effects"""
        wind_effects = {
            "cast": "wind_cast",
            "cast2": "wind_cast2",
            "whirlwind": "wind_whirlwind",
            "breeze": "wind_breeze", 
            "twister": "wind_twister",
            "gust": "wind_gust",
            "vacuum": "wind_vacuum",
            "cyclone": "wind_cyclone",
            "updraft": "wind_updraft",
            "tornado": "wind_tornado"
        }
        if effect_name in wind_effects:
            renpy.hide_screen(wind_effects[effect_name])
    
    # Composite effect helpers
    def show_light_composite(effect_name, x=0, y=0, fps=30):
        """Helper function to show light composite effects"""
        light_composites = {
            "magical_attack": "light_magical_attack",
            "healing": "light_healing"
        }
        if effect_name in light_composites:
            renpy.show_screen(light_composites[effect_name], x=x, y=y, fps=fps)
    
    def hide_light_composite(effect_name):
        """Helper function to hide light composite effects"""
        light_composites = {
            "magical_attack": "light_magical_attack",
            "healing": "light_healing"
        }
        if effect_name in light_composites:
            renpy.hide_screen(light_composites[effect_name])
    
    def show_wind_composite(effect_name, x=0, y=0, fps=30):
        """Helper function to show wind composite effects"""
        wind_composites = {
            "storm": "wind_storm",
            "gentle_breeze": "wind_gentle_breeze"
        }
        if effect_name in wind_composites:
            renpy.show_screen(wind_composites[effect_name], x=x, y=y, fps=fps)
    
    def hide_wind_composite(effect_name):
        """Helper function to hide wind composite effects"""
        wind_composites = {
            "storm": "wind_storm",
            "gentle_breeze": "wind_gentle_breeze"
        }
        if effect_name in wind_composites:
            renpy.hide_screen(wind_composites[effect_name])
    
    # Utility functions
    def hide_all_png_effects():
        """Hide all currently active PNG effects"""
        all_png_effects = [
            # Light effects
            "light_cast1", "light_cast2", "light_glare", "light_ray",
            "light_sparkle", "light_scintillation", "light_gleam", 
            "light_twinkle", "light_photon", "light_radiance",
            # Wind effects
            "wind_cast", "wind_cast2", "wind_whirlwind", "wind_breeze",
            "wind_twister", "wind_gust", "wind_vacuum", "wind_cyclone",
            "wind_updraft", "wind_tornado",
            # Composite effects
            "light_magical_attack", "light_healing", "wind_storm", "wind_gentle_breeze"
        ]
        
        for effect in all_png_effects:
            try:
                renpy.hide_screen(effect)
            except:
                pass  # Screen might not be showing, ignore errors
    
    # WebM Effect Helper Functions
    def show_atmospheric_effect(effect_name, x=0, y=0):
        """Helper function to show atmospheric WebM effects"""
        atmospheric_effects = {
            "fog": "fog",
            "underwater": "underwater",
            "godray_left": "godray_left",
            "godray_right": "godray_right",
            "leaves": "leaves",
            "blossoms": "blossoms",
            "fireflies": "fireflies"
        }
        if effect_name in atmospheric_effects:
            renpy.show_screen(atmospheric_effects[effect_name], x=x, y=y)
    
    def hide_atmospheric_effect(effect_name):
        """Helper function to hide atmospheric WebM effects"""
        atmospheric_effects = {
            "fog": "fog",
            "underwater": "underwater",
            "godray_left": "godray_left",
            "godray_right": "godray_right",
            "leaves": "leaves",
            "blossoms": "blossoms",
            "fireflies": "fireflies"
        }
        if effect_name in atmospheric_effects:
            renpy.hide_screen(atmospheric_effects[effect_name])
    
    def show_magical_effect(effect_type, color, x=0, y=0, fps=30):
        """Helper function to show magical WebM effects (stars, sparkles, etc.)"""
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
                renpy.show_screen(star_effects[color], x=x, y=y)
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
                renpy.show_screen(sparkle_effects[color], x=x, y=y)
    
    def hide_magical_effect(effect_type, color):
        """Helper function to hide magical WebM effects"""
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
    
    # Snow Effect Helper Functions
    def show_snow_effect(effect_name, x=0, y=0, y_offset=0):
        """Helper function to show snow effects"""
        snow_effects = {
            "light": "snow_light",
            "heavy": "snow_heavy"
        }
        if effect_name in snow_effects:
            if effect_name == "heavy":
                renpy.show_screen(snow_effects[effect_name], x=x, y=y, y_offset=y_offset)
            else:
                renpy.show_screen(snow_effects[effect_name], x=x, y=y)
    
    def hide_snow_effect(effect_name):
        """Helper function to hide snow effects"""
        snow_effects = {
            "light": "snow_light",
            "heavy": "snow_heavy"
        }
        if effect_name in snow_effects:
            renpy.hide_screen(snow_effects[effect_name])
    
    def hide_all_effects():
        """Hide all effects (both WebM and PNG)"""
        # Hide WebM effects (from vfx.rpy)
        all_webm_effects = [
            # Weather
            "rain_light", "rain_heavy", "snow_light", "snow_heavy",
            # Atmospheric
            "fog", "underwater", "godray_left", "godray_right",
            "leaves", "blossoms", "fireflies",
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
        
        # Hide WebM effects
        for effect in all_webm_effects:
            try:
                renpy.hide_screen(effect)
            except:
                pass
        
        # Hide PNG effects
        hide_all_png_effects() 