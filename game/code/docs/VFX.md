# Visual Effects System

## Overview

This directory contains all visual effects for the Love Potions Online visual novel. The system is designed to handle webm video effects with black backgrounds by using screen blending for transparency.

## File Structure

```
LPO/game/code/effects/
└── vfx.rpy                    # Complete visual effects system (WebM + PNG)

LPO/game/code/testing/
└── effects_usage_examples.rpy # Testing and example usage (temporary)

LPO/game/code/docs/
└── VFX.md                     # This documentation file

LPO/game/images/FX/webm/
├── Rain_light.webm
├── Snow_heavy.webm
├── Stars_blue.webm
└── ... (all webm effect files)

LPO/game/images/FX/png/
├── light/                     # Light magic effects
├── wind/                      # Wind magic effects
├── ice/                       # Ice magic effects
├── technology/                # Technology effects
├── esoteric/                  # Esoteric magic effects
├── curses/                    # Curse magic effects
├── nocturne/                  # Night magic effects
└── infernal/                  # Dark magic effects
```

### Testing and Development
- **Testing files** should be placed in `LPO/game/code/testing/` for easy removal later
- **Usage examples** and **temporary scripts** go in the testing folder
- **Production code** stays in the main effects folder

## How It Works

The system uses Ren'Py's `movie` displayable with `blend_mode="screen"` to composite the effects over your background. The screen blend mode makes black pixels transparent, allowing the effects to blend naturally with your scenes.

### Technical Implementation

**WebM Effects:**
- Uses Ren'Py's `Movie` displayable with `blend_mode "screen"`
- Black backgrounds become transparent
- Supports 30 FPS playback
- File format: WebM with VP8/VP9 codec

**PNG Effects (Sprite Sheets):**
- Uses Ren'Py's `crop` transform for frame-by-frame animation
- Sprite sheet format: 5 columns × up to 20 rows (192×192 pixels per frame)
- Supports both 30 FPS and 60 FPS playback
- Frame counts vary by effect (15-90 frames)
- Categories: Light, Wind, Ice, Technology, Esoteric, Curses, Nocturne, Infernal
- EasyStarAnimations format with RPG Maker compatibility

## Folder Organization

Effects are organized by file type for better management:

- **`images/FX/webm/`** - WebM video effects (current system)
- **`images/FX/png/`** - PNG animation effects (sprite sheet system)

This organization allows for easy management of different effect types and future expansion.

### PNG Effects Structure
```
LPO/game/images/FX/png/
├── light/                     # Light magic effects
│   ├── 30FPS/                # 30 FPS sprite sheets
│   ├── 60FPS/                # 60 FPS sprite sheets
│   └── AS - Light MZ Demo/   # EasyStarAnimations demo
├── wind/                      # Wind magic effects
│   ├── 30FPS/                # 30 FPS sprite sheets
│   ├── 60FPS/                # 60 FPS sprite sheets
│   └── AS - Wind MZ Demo/    # EasyStarAnimations demo
├── ice/                       # Ice magic effects
├── technology/                # Technology effects
├── esoteric/                  # Esoteric magic effects
├── curses/                    # Curse magic effects
├── nocturne/                  # Night magic effects
└── infernal/                  # Dark magic effects
```

## Available Effects

### Weather Effects
- `rain_light(x, y)` - Light rain
- `rain_heavy(x, y)` - Heavy rain
- `snow_light(x, y)` - Light snow
- `snow_heavy(x, y)` - Heavy snow

### Atmospheric Effects
- `fog(x, y)` - Fog/mist
- `underwater(x, y)` - Underwater distortion
- `godray_left(x, y)` - God rays from left
- `godray_right(x, y)` - God rays from right

### Nature Effects
- `leaves(x, y)` - Falling leaves
- `blossoms(x, y)` - Cherry blossoms
- `fireflies(x, y)` - Fireflies

### Star Effects (6 colors)
- `stars_blue(x, y)`, `stars_red(x, y)`, `stars_green(x, y)`
- `stars_yellow(x, y)`, `stars_purple(x, y)`, `stars_pink(x, y)`

### Sparkle Effects (6 colors)
- `sparkle_blue(x, y)`, `sparkle_red(x, y)`, `sparkle_green(x, y)`
- `sparkle_yellow(x, y)`, `sparkle_purple(x, y)`, `sparkle_pink(x, y)`

### Portal Effects (6 colors)
- `portal_blue(x, y)`, `portal_red(x, y)`, `portal_green(x, y)`
- `portal_yellow(x, y)`, `portal_purple(x, y)`, `portal_pink(x, y)`

### Plasma Effects (6 colors)
- `plasma_blue(x, y)`, `plasma_red(x, y)`, `plasma_green(x, y)`
- `plasma_yellow(x, y)`, `plasma_purple(x, y)`, `plasma_white(x, y)`

### Confetti Effects
- `confetti_warm(x, y)` - Warm colors
- `confetti_cool(x, y)` - Cool colors
- `confetti_colorful(x, y)` - All colors

### Special Effects
- `matrix(x, y)` - Matrix-style effect
- `night_sky(x, y)` - Night sky
- `shooting_star(x, y)` - Shooting star

### Composite Effects
- `magical_atmosphere(x, y)` - Combined magical effects
- `storm_weather(x, y)` - Rain + fog
- `celebration(x, y)` - Confetti + sparkles + stars

## PNG Effects (Sprite Sheet Animations)

### Light Effects
- `light_cast1(x, y, fps)` - Light casting animation 1 (15 frames)
- `light_cast2(x, y, fps)` - Light casting animation 2 (23 frames)
- `light_glare(x, y, fps)` - Light glare effect (15 frames)
- `light_ray(x, y, fps)` - Light ray effect (15 frames)
- `light_sparkle(x, y, fps)` - Light sparkle effect (30 frames)
- `light_scintillation(x, y, fps)` - Light scintillation effect (30 frames)
- `light_gleam(x, y, fps)` - Light gleam effect (38 frames)
- `light_twinkle(x, y, fps)` - Light twinkle effect (45 frames)
- `light_photon(x, y, fps)` - Light photon effect (45 frames, full screen)
- `light_radiance(x, y, fps)` - Light radiance effect (90 frames, full screen)

### Wind Effects
- `wind_cast(x, y, fps)` - Wind casting animation (15 frames)
- `wind_cast2(x, y, fps)` - Wind casting animation 2 (23 frames)
- `wind_whirlwind(x, y, fps)` - Wind whirlwind effect (15 frames)
- `wind_breeze(x, y, fps)` - Wind breeze effect (15 frames)
- `wind_twister(x, y, fps)` - Wind twister effect (30 frames)
- `wind_gust(x, y, fps)` - Wind gust effect (30 frames)
- `wind_vacuum(x, y, fps)` - Wind vacuum effect (38 frames)
- `wind_cyclone(x, y, fps)` - Wind cyclone effect (45 frames)
- `wind_updraft(x, y, fps)` - Wind updraft effect (45 frames)
- `wind_tornado(x, y, fps)` - Wind tornado effect (90 frames, full screen)

### PNG Composite Effects
- `light_magical_attack(x, y, fps)` - Combined light magical attack
- `light_healing(x, y, fps)` - Combined light healing effect
- `wind_storm(x, y, fps)` - Combined wind storm effect
- `wind_gentle_breeze(x, y, fps)` - Combined gentle wind effect

## Basic Usage

### Simple Effect
```renpy
# Show a rain effect
show screen rain_light(0, 0)

# Your dialogue here
"It's raining."

# Hide the effect
hide screen rain_light
```

### Multiple Effects
```renpy
# Show multiple effects
show screen sparkle_blue(100, 100)
show screen stars_purple(200, 150)
show screen fireflies(300, 200)

"The room is magical."

# Hide all effects
hide screen sparkle_blue
hide screen stars_purple
hide screen fireflies
```

### Composite Effects
```renpy
# Show a combined effect
show screen magical_atmosphere(0, 0)

"The forest has a magical glow."

hide screen magical_atmosphere
```

### PNG Effects
```renpy
# Show a light effect
show screen light_sparkle(0, 0, 30)

"Light magic sparkles around us."

hide screen light_sparkle

# Show a wind effect with different FPS
show screen wind_tornado(0, 0, 60)

"A powerful tornado appears!"

hide screen wind_tornado

# Show a composite PNG effect
show screen light_magical_attack(0, 0, 30)

"The mage casts a powerful light spell."

hide screen light_magical_attack
```

## Enhanced Helper Functions

The system includes comprehensive helper functions in `vfx.rpy`:

### Weather Effects
```renpy
$ show_weather_effect("rain_light")
$ hide_weather_effect("rain_light")
```

### Magical Effects
```renpy
$ show_magical_effect("stars", "purple")
$ hide_magical_effect("stars", "purple")
```

### Atmospheric Effects
```renpy
$ show_atmospheric_effect("fog")
$ hide_atmospheric_effect("fog")
```

### Composite Effects
```renpy
$ show_composite_effect("magical_atmosphere")
$ hide_composite_effect("magical_atmosphere")
```

### Special Effects
```renpy
$ show_special_effect("matrix")
$ hide_special_effect("matrix")
```

### Confetti Effects
```renpy
$ show_confetti_effect("confetti_colorful")
$ hide_confetti_effect("confetti_colorful")
```

### Utility Functions
```renpy
$ hide_all_effects()  # Hide all active effects
```

### PNG Effect Functions
```renpy
# Show light effects
$ show_light_effect("sparkle", 0, 0, 30)
$ show_light_effect("radiance", 0, 0, 60)
$ show_light_composite("magical_attack", 0, 0, 30)

# Show wind effects
$ show_wind_effect("tornado", 0, 0, 30)
$ show_wind_effect("breeze", 0, 0, 60)
$ show_wind_composite("storm", 0, 0, 30)

# Hide effects
$ hide_light_effect("sparkle")
$ hide_light_composite("magical_attack")
$ hide_wind_effect("tornado")
$ hide_wind_composite("storm")

# Hide all effects (both WebM and PNG)
$ hide_all_effects()
```

## Advanced Usage Examples

### Enhanced Helper Functions
```renpy
label example_enhanced_helper_functions:
    scene bg meadow
    
    # Using weather helper functions
    $ show_weather_effect("rain_light")
    "It starts to rain lightly."
    
    $ hide_weather_effect("rain_light")
    $ show_weather_effect("snow_heavy")
    "The weather changes to heavy snow."
    
    $ hide_weather_effect("snow_heavy")
    
    # Using magical effect helpers
    $ show_magical_effect("stars", "purple")
    $ show_magical_effect("sparkle", "yellow")
    "Magical effects appear."
    
    $ hide_magical_effect("stars", "purple")
    $ hide_magical_effect("sparkle", "yellow")
    
    # Using atmospheric helpers
    $ show_atmospheric_effect("fog")
    "Fog rolls in."
    
    $ hide_atmospheric_effect("fog")
    
    # Using composite helpers
    $ show_composite_effect("magical_atmosphere")
    "A magical atmosphere fills the area."
    
    $ hide_composite_effect("magical_atmosphere")
    
    # Using utility function
    $ hide_all_effects()
    "All effects are cleared."
    
    return
```

### Advanced Positioning
```renpy
label example_advanced_positioning:
    scene bg room
    
    # Position effects at specific coordinates
    $ show_magical_effect("sparkle", "blue", 100, 100)
    $ show_magical_effect("stars", "purple", 400, 200)
    $ show_atmospheric_effect("fireflies", 300, 400)
    
    "Effects are positioned around the room."
    
    $ hide_all_effects()
    
    return
```

## Seasonal Themes

### Spring
```renpy
$ show_atmospheric_effect("blossoms")
"It's cherry blossom season."
$ hide_atmospheric_effect("blossoms")
```

### Summer
```renpy
$ show_atmospheric_effect("fireflies")
"Summer nights bring fireflies."
$ hide_atmospheric_effect("fireflies")
```

### Autumn
```renpy
$ show_atmospheric_effect("leaves")
"Autumn leaves dance in the wind."
$ hide_atmospheric_effect("leaves")
```

### Winter
```renpy
$ show_weather_effect("snow_heavy")
"Winter brings heavy snowfall."
$ hide_weather_effect("snow_heavy")
```

## Color Themes

### Blue Theme
```renpy
$ show_magical_effect("stars", "blue")
$ show_magical_effect("sparkle", "blue")
$ show_magical_effect("plasma", "blue")
"A blue magical realm."
$ hide_magical_effect("stars", "blue")
$ hide_magical_effect("sparkle", "blue")
$ hide_magical_effect("plasma", "blue")
```

### Red Theme
```renpy
$ show_magical_effect("stars", "red")
$ show_magical_effect("sparkle", "red")
$ show_magical_effect("plasma", "red")
"A red magical realm."
$ hide_magical_effect("stars", "red")
$ hide_magical_effect("sparkle", "red")
$ hide_magical_effect("plasma", "red")
```

## Complete Example Scenarios

### Romantic Scene
```renpy
scene bg garden
$ show_atmospheric_effect("blossoms")
$ show_magical_effect("sparkle", "pink")
$ show_atmospheric_effect("fireflies")

"The garden is perfect for romance."

$ hide_all_effects()
```

### Battle Scene
```renpy
scene bg battlefield
$ show_magical_effect("plasma", "red")
$ show_magical_effect("stars", "red")

"The battle intensifies!"

$ hide_magical_effect("plasma", "red")
$ hide_magical_effect("stars", "red")
$ show_composite_effect("celebration")

"Victory!"

$ hide_composite_effect("celebration")
```

### Mystical Scene

### Magic Battle Scene (PNG Effects)
```renpy
scene bg battlefield

# Light magic attack
$ show_light_effect("cast1", 0, 0, 30)
"The mage begins casting light magic."
$ hide_light_effect("cast1")

$ show_light_composite("magical_attack", 0, 0, 30)
"A powerful light spell is unleashed!"
$ hide_light_composite("magical_attack")

# Wind magic counter
$ show_wind_effect("cast", 0, 0, 30)
"The opponent casts wind magic."
$ hide_wind_effect("cast")

$ show_wind_composite("storm", 0, 0, 30)
"A wind storm counters the attack!"
$ hide_wind_composite("storm")

# Ultimate light spell
$ show_light_effect("radiance", 0, 0, 60)
"The final light spell fills the battlefield."
$ hide_light_effect("radiance")
```

### Healing Scene (PNG Effects)
```renpy
scene bg temple

# Gentle healing light
$ show_light_composite("healing", 0, 0, 30)
"Divine light heals the wounded."
$ hide_light_composite("healing")

# Gentle breeze
$ show_wind_composite("gentle_breeze", 0, 0, 30)
"A gentle breeze carries the healing magic."
$ hide_wind_composite("gentle_breeze")
```
```renpy
scene bg cave
$ show_atmospheric_effect("fog")
$ show_magical_effect("portal", "blue", 400, 300)

"A mysterious portal appears in the fog."

$ hide_atmospheric_effect("fog")
$ hide_magical_effect("portal", "blue")
```

### Dynamic Effect Changes
```renpy
label example_dynamic_effects:
    scene bg battlefield
    
    # Start with light effects
    $ show_magical_effect("sparkle", "yellow")
    "The battle begins with a gentle glow."
    
    # Intensify with more effects
    $ show_magical_effect("stars", "red")
    $ show_magical_effect("plasma", "red")
    "The intensity builds!"
    
    # Add celebration effects
    $ show_confetti_effect("confetti_colorful")
    "Victory is achieved!"
    
    # Remove all effects
    $ hide_all_effects()
    
    return
```

## Performance Considerations

1. **Multiple Effects**: Running many effects simultaneously may impact performance
2. **Looping**: All effects loop by default, which is good for continuous atmosphere
3. **Memory**: Webm files are loaded into memory, so be mindful of file sizes
4. **Positioning**: Effects positioned off-screen still consume resources

## Troubleshooting

### Effect Not Showing
- Check that the webm file exists in `images/FX/webm/`
- Ensure the filename matches exactly (case-sensitive)
- Verify the screen name is correct

### Black Background Visible
- The system uses screen blending to remove black backgrounds
- If you see black, check that `blend_mode="screen"` is being used
- Some effects may have slight artifacts due to the conversion process

### Performance Issues
- Reduce the number of simultaneous effects
- Consider using lighter effects for mobile devices
- Test on target platforms

## Customization

### Adding New WebM Effects
1. Place your webm file in `images/FX/webm/`
2. Add a new screen definition in `vfx.rpy`:
```renpy
screen my_custom_effect(x=0, y=0):
    """My custom effect"""
    use screen_effect("My_Custom_Effect", x, y, True, "screen")
```

### Future: PNG Animation Effects
PNG animation effects will be supported in the future. These will be stored in `images/FX/png/` and will use a different system for handling transparency and animation frames.

The PNG system will likely use:
- Individual PNG frames for animations
- Built-in transparency support (no need for screen blending)
- Different performance characteristics than WebM files

### Modifying Blend Modes
You can change the blend mode for different effects:
```renpy
screen my_effect(x=0, y=0):
    use screen_effect("My_Effect", x, y, True, "add")  # Different blend mode
```

### Creating Custom Composite Effects
```renpy
screen my_composite_effect(x=0, y=0):
    """My custom composite effect"""
    frame:
        xpos x
        ypos y
        background None
        
        use sparkle_blue(0, 0)
        use stars_purple(0, 0)
        use my_custom_effect(0, 0)
```

## Integration Tips

1. **Scene Transitions**: Hide effects before scene changes
2. **Character Dialogue**: Effects work well with character sprites
3. **Menu Integration**: Consider hiding effects during menus
4. **Save/Load**: Effects don't persist across saves, so re-show them if needed

## Complete Helper Function Reference

### Weather Effect Helpers
```renpy
def show_weather_effect(weather_type, x=0, y=0):
    """Helper function to show weather effects"""
    # Supports: "rain_light", "rain_heavy", "snow_light", "snow_heavy"

def hide_weather_effect(weather_type):
    """Helper function to hide weather effects"""
    # Supports: "rain_light", "rain_heavy", "snow_light", "snow_heavy"
```

### Magical Effect Helpers
```renpy
def show_magical_effect(effect_type, color="blue", x=0, y=0):
    """Helper function to show magical effects"""
    # effect_type: "stars", "sparkle", "portal", "plasma"
    # color: "blue", "red", "green", "yellow", "purple", "pink", "white"

def hide_magical_effect(effect_type, color="blue"):
    """Helper function to hide magical effects"""
    # Same parameters as show_magical_effect
```

### Atmospheric Effect Helpers
```renpy
def show_atmospheric_effect(effect_type, x=0, y=0):
    """Helper function to show atmospheric effects"""
    # Supports: "fog", "underwater", "godray_left", "godray_right", 
    #          "leaves", "blossoms", "fireflies"

def hide_atmospheric_effect(effect_type):
    """Helper function to hide atmospheric effects"""
    # Same parameters as show_atmospheric_effect
```

### Composite Effect Helpers
```renpy
def show_composite_effect(effect_type, x=0, y=0):
    """Helper function to show composite effects"""
    # Supports: "magical_atmosphere", "storm_weather", "celebration"

def hide_composite_effect(effect_type):
    """Helper function to hide composite effects"""
    # Same parameters as show_composite_effect
```

### Special Effect Helpers
```renpy
def show_special_effect(effect_type, x=0, y=0):
    """Helper function to show special effects"""
    # Supports: "matrix", "night_sky", "shooting_star"

def hide_special_effect(effect_type):
    """Helper function to hide special effects"""
    # Same parameters as show_special_effect
```

### Confetti Effect Helpers
```renpy
def show_confetti_effect(effect_type, x=0, y=0):
    """Helper function to show confetti effects"""
    # Supports: "confetti_warm", "confetti_cool", "confetti_colorful"

def hide_confetti_effect(effect_type):
    """Helper function to hide confetti effects"""
    # Same parameters as show_confetti_effect
```

### Utility Functions
```renpy
def hide_all_effects():
    """Hide all currently active screen effects"""
    # This function attempts to hide all possible effects
    # It's safe to call even if effects aren't currently showing
```

This system provides a powerful and flexible way to add atmospheric effects to your Ren'Py visual novel while handling the technical challenges of webm transparency.
