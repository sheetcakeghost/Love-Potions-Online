# Layered Parallax Backgrounds
# Dynamic backgrounds using layered images from bg folder with SnowBlossom effects

# Transform for gentle swaying (for trees and foliage)
transform gentle_sway(amplitude=5, duration=3.0):
    # Creates a gentle swaying motion
    # amplitude: How far the sway goes in pixels
    # duration: How long one complete sway cycle takes
    xpos 0
    ease duration xpos amplitude
    ease duration xpos -amplitude
    ease duration xpos 0
    repeat

# Transform for floating motion (for clouds and distant elements)
transform float_motion(amplitude=10, duration=4.0):
    # Creates a floating up and down motion
    # amplitude: How far the float goes in pixels
    # duration: How long one complete float cycle takes
    ypos 0
    ease duration ypos -amplitude
    ease duration ypos amplitude
    ease duration ypos 0
    repeat

# Manor Exterior Background (Day)
screen bg_manor_exterior_day(x=0, y=0, cloud_intensity=0.7, wind_intensity=1.0):
    # Bright manor exterior with moving clouds and gentle swaying
    # cloud_intensity: How many clouds to show (0.0 to 1.0)
    # wind_intensity: How much elements sway (0.0 to 2.0)
    layer "master"

    # Sky layer (static background)
    add "images/bg/sky_day.png" xpos x ypos y

    # Moving clouds using SnowBlossom
    add SnowBlossom(
        "images/FX/snowblossom/clouds/cloud_1.png",
        count=int(20 * cloud_intensity),
        xspeed=(-30, -10), yspeed=(5, 15), start=0, fast=True, horizontal=True
    ) xpos x ypos y
    add SnowBlossom(
        "images/FX/snowblossom/clouds/cloud_2.png",
        count=int(15 * cloud_intensity),
        xspeed=(-25, -5), yspeed=(10, 20), start=0.5, fast=True, horizontal=True
    ) xpos x ypos y
    add SnowBlossom(
        "images/FX/snowblossom/clouds/cloud_3.png",
        count=int(10 * cloud_intensity),
        xspeed=(-35, -15), yspeed=(8, 18), start=1.0, fast=True, horizontal=True
    ) xpos x ypos y

    # Manor building (static)
    add "images/bg/manor.png" xpos x ypos y

    # Grass base with gentle swaying
    add At("images/bg/grass_base.png", gentle_sway(2 * wind_intensity, 4.0)) xpos x ypos y

    # Hedges with swaying
    add At("images/bg/hedges.png", gentle_sway(3 * wind_intensity, 3.5)) xpos x ypos y

# Manor Exterior Background (Dusk)
screen bg_manor_exterior_dusk(x=0, y=0, cloud_intensity=0.5, wind_intensity=0.8):
    # Dusk manor exterior with atmospheric lighting
    layer "master"

    # Dusk sky layer
    add "images/bg/sky_dusk.png" xpos x ypos y

    # Fewer, slower clouds for dusk
    add SnowBlossom(
        "images/FX/snowblossom/clouds/cloud_1.png",
        count=int(10 * cloud_intensity),
        xspeed=(-20, -5), yspeed=(3, 10), start=0, fast=True, horizontal=True
    ) xpos x ypos y
    add SnowBlossom(
        "images/FX/snowblossom/clouds/cloud_2.png",
        count=int(8 * cloud_intensity),
        xspeed=(-15, -3), yspeed=(5, 12), start=0.7, fast=True, horizontal=True
    ) xpos x ypos y

    # Manor building
    add "images/bg/manor.png" xpos x ypos y

    # Grass base with gentle swaying
    add At("images/bg/grass_base.png", gentle_sway(1.5 * wind_intensity, 5.0)) xpos x ypos y

    # Hedges with swaying
    add At("images/bg/hedges.png", gentle_sway(2 * wind_intensity, 4.2)) xpos x ypos y

# Dark Forest Background
screen bg_dark_forest(x=0, y=0, fog_intensity=0.6, wind_intensity=1.2):
    # Dark, mysterious forest with fog and swaying trees
    # fog_intensity: How thick the fog is (0.0 to 1.0)
    # wind_intensity: How much trees sway (0.0 to 2.0)
    layer "master"

    # Dark forest base
    add "images/bg/dark_forest.png" xpos x ypos y

    # Fog effect using SnowBlossom
    if fog_intensity > 0:
        add SnowBlossom(
            "images/FX/snowblossom/fog/fog_0000.png",
            count=int(25 * fog_intensity),
            border=800, yspeed=(8, -8), xspeed=(40, -40), start=0, fast=True, horizontal=True
        ) xpos x ypos y
        add SnowBlossom(
            "images/FX/snowblossom/fog/fog_0001.png",
            count=int(20 * fog_intensity),
            border=700, yspeed=(-12, -4), xspeed=(30, -30), start=0.3, fast=True, horizontal=True
        ) xpos x ypos y
        add SnowBlossom(
            "images/FX/snowblossom/fog/fog_0002.png",
            count=int(22 * fog_intensity),
            border=900, yspeed=(6, -10), xspeed=(50, -50), start=0.6, fast=True, horizontal=True
        ) xpos x ypos y

    # Grass base with swaying
    add At("images/bg/grass_base.png", gentle_sway(4 * wind_intensity, 3.0)) xpos x ypos y

# Garden Background (Day)
screen bg_garden_day(x=0, y=0, wind_intensity=1.0, petal_intensity=0.8):
    # Bright garden with swaying hedges and falling petals
    # wind_intensity: How much elements sway (0.0 to 2.0)
    # petal_intensity: How many petals fall (0.0 to 1.0)
    layer "master"

    # Sky layer
    add "images/bg/sky_day.png" xpos x ypos y

    # Moving clouds
    add SnowBlossom(
        "images/FX/snowblossom/clouds/cloud_1.png",
        count=15,
        xspeed=(-25, -8), yspeed=(5, 12), start=0, fast=True, horizontal=True
    ) xpos x ypos y
    add SnowBlossom(
        "images/FX/snowblossom/clouds/cloud_2.png",
        count=12,
        xspeed=(-20, -5), yspeed=(8, 15), start=0.6, fast=True, horizontal=True
    ) xpos x ypos y

    # Grass base
    add "images/bg/grass.png" xpos x ypos y

    # Tall hedges with swaying
    add At("images/bg/hedges_tall.png", gentle_sway(3 * wind_intensity, 3.8)) xpos x ypos y

    # Regular hedges with swaying
    add At("images/bg/hedges.png", gentle_sway(2 * wind_intensity, 4.2)) xpos x ypos y

    # Falling petals
    if petal_intensity > 0:
        add SnowBlossom(
            "images/FX/snowblossom/petals/petals_1.png",
            count=int(20 * petal_intensity),
            xspeed=(15, 35), yspeed=(50, 100), start=0, fast=True, horizontal=False
        ) xpos x ypos y
        add SnowBlossom(
            "images/FX/snowblossom/petals/petals_2.png",
            count=int(15 * petal_intensity),
            xspeed=(20, 40), yspeed=(60, 110), start=0.4, fast=True, horizontal=False
        ) xpos x ypos y

# Stormy Manor Background
screen bg_manor_stormy(x=0, y=0, rain_intensity=0.8, wind_intensity=1.5):
    # Stormy manor exterior with rain and strong winds
    # rain_intensity: How heavy the rain is (0.0 to 1.0)
    # wind_intensity: How strong the wind is (0.0 to 2.0)
    layer "master"

    # Stormy sky
    add "images/bg/sky_base_storm.png" xpos x ypos y

    # Fast-moving storm clouds
    add SnowBlossom(
        "images/FX/snowblossom/clouds/cloud_1.png",
        count=30,
        xspeed=(-80, -40), yspeed=(10, 25), start=0, fast=True, horizontal=True
    ) xpos x ypos y
    add SnowBlossom(
        "images/FX/snowblossom/clouds/cloud_2.png",
        count=25,
        xspeed=(-70, -35), yspeed=(15, 30), start=0.3, fast=True, horizontal=True
    ) xpos x ypos y

    # Manor building
    add "images/bg/manor.png" xpos x ypos y

    # Grass base with violent swaying
    add At("images/bg/grass_base.png", gentle_sway(8 * wind_intensity, 1.5)) xpos x ypos y

    # Hedges with strong swaying
    add At("images/bg/hedges.png", gentle_sway(10 * wind_intensity, 1.2)) xpos x ypos y

    # Rain effect
    if rain_intensity > 0:
        use rain_heavy(0, 0)

# Indoor Backgrounds with Window Effects

# Living Room with Window
screen bg_livingroom_window(x=0, y=0, weather="clear", wind_intensity=0.5):
    # Living room with window showing outdoor weather
    # weather: "clear", "cloudy", "rainy", "stormy"
    # wind_intensity: How much curtains sway (0.0 to 2.0)
    layer "master"

    # Living room base
    add "images/bg/livingroom.png" xpos x ypos y

    # Window overlay
    add "images/bg/office_window.png" xpos x ypos y

    # Weather effects through window
    if weather == "clear":
        add "images/bg/sky_day.png" xpos x ypos y alpha 0.3
        add SnowBlossom(
            "images/FX/snowblossom/clouds/cloud_1.png",
            count=8,
            xspeed=(-15, -5), yspeed=(3, 8), start=0, fast=True, horizontal=True
        ) xpos x ypos y alpha 0.4
    elif weather == "cloudy":
        add "images/bg/sky_base_grey.png" xpos x ypos y alpha 0.4
        add SnowBlossom(
            "images/FX/snowblossom/clouds/cloud_2.png",
            count=12,
            xspeed=(-20, -8), yspeed=(5, 12), start=0, fast=True, horizontal=True
        ) xpos x ypos y alpha 0.5
    elif weather == "rainy":
        add "images/bg/sky_base_grey.png" xpos x ypos y alpha 0.5
        use rain_light(0, 0)
    elif weather == "stormy":
        add "images/bg/sky_base_storm.png" xpos x ypos y alpha 0.6
        use rain_heavy(0, 0)

# Dining Room with Window
screen bg_dining_window(x=0, y=0, weather="clear", wind_intensity=0.5):
    # Dining room with window showing outdoor weather
    layer "master"

    # Dining room base
    add "images/bg/dining.png" xpos x ypos y

    # Window overlay
    add "images/bg/dining_window.png" xpos x ypos y

    # Weather effects through window
    if weather == "clear":
        add "images/bg/sky_day.png" xpos x ypos y alpha 0.3
        add SnowBlossom(
            "images/FX/snowblossom/clouds/cloud_1.png",
            count=6,
            xspeed=(-12, -4), yspeed=(2, 6), start=0, fast=True, horizontal=True
        ) xpos x ypos y alpha 0.4
    elif weather == "cloudy":
        add "images/bg/sky_base_grey.png" xpos x ypos y alpha 0.4
        add SnowBlossom(
            "images/FX/snowblossom/clouds/cloud_2.png",
            count=10,
            xspeed=(-18, -6), yspeed=(4, 10), start=0, fast=True, horizontal=True
        ) xpos x ypos y alpha 0.5
    elif weather == "rainy":
        add "images/bg/sky_base_grey.png" xpos x ypos y alpha 0.5
        use rain_light(0, 0)
    elif weather == "stormy":
        add "images/bg/sky_base_storm.png" xpos x ypos y alpha 0.6
        use rain_heavy(0, 0)

# Helper functions for easy background management
init python:
    def show_layered_background(bg_type="manor_day", **kwargs):
        """
        Helper function to show layered backgrounds
        bg_type: "manor_day", "manor_dusk", "dark_forest", "garden_day", 
                "manor_stormy", "livingroom_window", "dining_window"
        **kwargs: Additional parameters for the specific background
        """
        background_screens = {
            "manor_day": "bg_manor_exterior_day",
            "manor_dusk": "bg_manor_exterior_dusk", 
            "dark_forest": "bg_dark_forest",
            "garden_day": "bg_garden_day",
            "manor_stormy": "bg_manor_stormy",
            "livingroom_window": "bg_livingroom_window",
            "dining_window": "bg_dining_window"
        }
        
        if bg_type in background_screens:
            renpy.show_screen(background_screens[bg_type], **kwargs)
    
    def hide_layered_background():
        """Helper function to hide all layered backgrounds"""
        all_screens = [
            "bg_manor_exterior_day", "bg_manor_exterior_dusk", "bg_dark_forest",
            "bg_garden_day", "bg_manor_stormy", "bg_livingroom_window", "bg_dining_window"
        ]
        
        for screen_name in all_screens:
            try:
                renpy.hide_screen(screen_name)
            except:
                pass  # Screen might not be showing, ignore errors
    
    def change_weather(weather_type, **kwargs):
        """
        Helper function to change weather for window backgrounds
        weather_type: "clear", "cloudy", "rainy", "stormy"
        """
        # This would need to be called with the specific background type
        # For now, just a placeholder for weather changes
        pass

# Example usage labels for testing
label test_layered_backgrounds:
    "Testing Layered Backgrounds with SnowBlossom Effects"

    "Manor Exterior (Day):"
    show screen bg_manor_exterior_day(cloud_intensity=0.8, wind_intensity=1.0)
    "This is the manor exterior during the day with moving clouds and swaying grass."

    "Manor Exterior (Dusk):"
    hide screen bg_manor_exterior_day
    show screen bg_manor_exterior_dusk(cloud_intensity=0.4, wind_intensity=0.8)
    "This is the manor exterior at dusk with a more atmospheric feel."

    "Dark Forest:"
    hide screen bg_manor_exterior_dusk
    show screen bg_dark_forest(fog_intensity=0.7, wind_intensity=1.2)
    "This is a dark, mysterious forest with fog effects."

    "Garden (Day):"
    hide screen bg_dark_forest
    show screen bg_garden_day(wind_intensity=1.0, petal_intensity=0.8)
    "This is a bright garden with falling petals and swaying hedges."

    "Stormy Manor:"
    hide screen bg_garden_day
    show screen bg_manor_stormy(rain_intensity=0.8, wind_intensity=1.5)
    "This is the manor during a storm with heavy rain and strong winds."

    "Living Room with Window (Clear):"
    hide screen bg_manor_stormy
    show screen bg_livingroom_window(weather="clear", wind_intensity=0.5)
    "This is the living room with a window showing clear weather outside."

    "Living Room with Window (Rainy):"
    hide screen bg_livingroom_window
    show screen bg_livingroom_window(weather="rainy", wind_intensity=0.8)
    "Now it's raining outside the window."

    "Dining Room with Window (Stormy):"
    hide screen bg_livingroom_window
    show screen bg_dining_window(weather="stormy", wind_intensity=1.0)
    "The dining room window shows a storm raging outside."

    hide screen bg_dining_window
    "All layered backgrounds hidden."

    return 