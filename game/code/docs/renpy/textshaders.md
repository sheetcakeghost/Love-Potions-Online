# Text Shaders

Ren'Py contains a text shader system that makes it possible to control how Ren'Py displays text. When enabled, the text shader system uses  to render two triangles for each unicode character. Shader parts, either specified from the creator or generated by Ren'Py, are applied to the model, and can change how text is displayed.

The text shader documentation is in three parts:

1.  How to use text shaders
    
2.  What text shaders are included in Ren'Py
    
3.  How to create new text shaders
    

Note that while text shaders are intended to be easily used by game creators, making your own text shaders requires some knowledge of GLSL, the OpenGL Shading Language, as well as , and hence is more advanced than most Ren'Py features.

## Using Text Shaders

There are three ways to use text shaders:

**Default Text Shader** The first is to set the default text shader, using `config.default_textshader`.

define config.default\_textshader \= "wave:10"

When set this way, the text shader will be used for all text that does not specify a text shader. It will also be combined with text shaders that include the default text shader, which is most of them.

Generally, the default textshader should take care of slow text and shouldn't add more complicated effects.

**Styles** The second way to use text shaders is to set the `textshader` style property, either directly or in one of the many ways provided by Ren'Py to set styles.

style default:
    textshader "dissolve"

define goldfinger \= Character("Goldfinger", what\_textshader\="linetexture:gold.png")

screen purchase():
    vbox:
        text "Buy the DLC for more!" textshader "wave"
        textbutton "Buy Now":
            text\_textshader "wave" action iap.Purchase("dlc")

**Text Tags** The third way to use text shaders is to use the  to change the look of a portion of text.

"What's this? A letter from {shader=zoom}out of nowhere{/shader}?"

**Note** A text block should either use text shaders or not - mixing is not supported. For example, you should set `config.default_textshader` or `textshader` style property if you use the text tag like above.

### Specifying Text Shaders

Text shaders are specified as strings like:

"dissolve"
"jitter:u\_\_jitter=1.0, 3.0"
"texture:gold.png"

The first part of the string, before the first colon, is the name of the text shader. The rest of the string is a series of uniforms that are passed to the shader, separated by colons. (Uniforms are parameters that are passed to the shader, that can be used to control how the shader works.)

Uniforms can be specified by name followed by =, or the name can be omitted to set each uniform in order. (Omitting the name is not supported in Ren'Py 7.) While internally all uniforms begin with u\_, the u\_ can be omitted for brevity.

The value of a uniform can be:

*   Between 1 and 4 numbers, separated by commas. These can be used with the the float, vec2, vec3, or vec4 types.
    
*   A color, beginning with #. (For example, #f00 or #ff0000 for red.) This creates a vec4 corresponding to that color. This color will be premultiplied by its alpha channel.
    
*   A  that will be used as a texture. This creates a sampler2D that can be used to sample the texture.
    

Uniform values can't be expressions or access variables, though it is possible to use text interpolation to create a string that can be evaluated as a textshader tag or its parameter.

Finally, text shaders can be combined with each other using the | operator. For example:

"jitter:1.0, 3.0|wave"

This will apply both the jitter and wave shaders to the text. This only works if the shaders are compatible with each other, and do not use the same uniforms (or use the uniform in a way that is compatible with each other, in which case it takes the value from the last shader in the list).

Unless a textshader has include\_default set to False, the default textshader will be combined with the textshader specified in the style or tag.

### Text Shader Callbacks

The  variable can be used to set a callback that is run when a text shader is applied. This can be used to customize the text shader based on a preference.

default persistent.dissolve\_text \= True

init python:
    def get\_default\_textshader():
        if persistent.dissolve\_text:
            return "dissolve"
        else:
            return "typewriter"

define config.default\_textshader \= "default"
define config.textshader\_callbacks\["default"\] \= get\_default\_textshader

## Built-In Text Shaders

Ren'Py includes a number of built-in text shaders. These are:

dissolve

The dissolve text shader handles text by dissolving it in slowly, with the start dissolving in first, and the end dissolving in last.

u\_\_duration = 10.0

The number of characters that will be changing alpha at a time. If set to 0, the wave will move across the text one pixel at a time.

Using this shader will prevent the default text shader from being used.

flip

The flip shader flips slow text by flipping the text horizontally, with the start flipping in first, and the end flipping in last.

u\_\_duration = 10.0

The number of characters that will be changing alpha at a time. If set to 0, the characters will instantly flip.

Using this shader will prevent the default text shader from being used.

jitter

The jitter text shader moves the text to random positions relative to where it would be normally drawn. The position changes once per frame.

u\_\_jitter = (3.0, 3.0)

The amount of jitter to apply to the text, in pixels.

linetexture

Multiplies the text with a texture, one line at a time. The texture is aligned with the left side of the text. The vertical center of the texture is aligned with the baseline of the text - this means that most of the lower half of the texture will not be visible.

u\_\_texture = ...

The texture to multiply the text by.

u\_\_scale = (1.0, 1.0)

A factor to scale the texture by. For example (1.0, 0.5) will make the texture half as tall as it otherwise would be.

offset

The offset text shader moves the text by a fixed amount.

u\_\_offset = (0.0, 0.0)

The amount to move the text by, in virtual pixels.

slowalpha

The slowalpha shader is intended to be used with another slow text shader, like typewriter or dissolve. It causes the text that has yet to be revealed to be drawn with an alpha value of u\_\_alpha = 0.2, rather than being invisible.

u\_\_alpha = 0.2

The alpha value of the text that has not been revealed yet.

texture

The texture text shader multiplies the text with the colors from a texture. This is not done to outlines or offset text. The texture is aligned with the top left of the text.

u\_\_texture = ...

The texture to multiply the text by.

typewriter

The typewriter text shader handles slow text by making the text appear one character at a time, as if it were being typed out by a typewriter.

Using this shader will prevent the default text shader from being used.

wave

The wave text shader makes the text bounce up and down in a wave.

u\_\_amplitude = 5.0

The number of pixels up and down the text will move.

u\_\_frequency = 2.0

The number of waves per second.

u\_\_wavelength = 20.0

The number of characters between peaks in the wave.

zoom

The zoom text shader handles slow text to cause it to zoom in from an initial size of u\_\_zoom = 0.0 to full size.

u\_\_zoom = 0.0

The initial amount of zoom to apply to a character when it first starts showing.

u\_\_duration = 10.0

The number of characters that will be changing alpha at a time. If set to 0, the characters will instantly flip.

Using this shader will prevent the default text shader from being used.

## Creating Text Shaders

Text shaders are GLSL programs that are run on the GPU. These shaders are registered using the renpy.register\_text\_shader function.

renpy.register\_textshader(_name_, _shaders\=()_, _extra\_slow\_time\=0.0_, _extra\_slow\_duration\=0.0_, _redraw\=None_, _redraw\_when\_slow\=0.0_, _include\_default\=True_, _adjust\_function\=None_, _doc\=None_, _\*\*kwargs_)

This creates a textshader and registers it with the name name.

This function takes the following arguments:

name

This is the name of the textshader. It's also used to register a shader part named textshader.\`name\`.

shaders

Shader parts to apply to the text. This can be a string, or a list or tuple of strings. This should be a shader part registered with , or this function. If a shader part begins with '-', then it is removed from the list of shader parts. (For example, '-textshader.typewriter' will remove that part.)

Note that the shader parts registered with this function are prefixed with textshader., which needs to be supplied when used with this function.

extra\_slow\_time

Extra time to add to the slow time effect beyond what Ren'Py will compute from the current characters per second. This is useful for shaders that might take more time to transition a character than the default time. If True, the shader is always updated.

extra\_slow\_duration

Added to extra\_slow\_time, but this is multiplied by the time per character to get the extra time to add to the slow time effect. (Time per character is 1 / characters per second.)

redraw

The amount in time in seconds before the text is redrawn, after all slow text has been show and extra\_slow\_time has passed.

redraw\_when\_slow

The amount of time in seconds before the text is redrawn when showing slow text.

include\_default

If True, when this textshader is used directly, it will be combined with `config.default_textshader`.

adjust\_function

A function that is called with an object and the uniforms being passed to the text shader as keyworkd arguments. This function can set the extra\_slow\_time, extra\_slow\_duration, redraw, and redraw\_when\_slow fields of the object

doc

A string containing documetation information. This is mostly intended for Ren'Py's documentation system.

Keyword argument beginning with `u_` are passed as uniforms to the shader, with strings beginning with `#` being interpreted as colors. Most uniforms should begin with `u__`, using  to prevent conflicts with other shaders.

A keyword argument named variables and all keyword arguments that begin with fragment\_ or vertex\_ are passed to , which registers the shader part.

### Variables in Text Shaders

In additions to the uniforms you provided to the text shader (generally beginning with `u__`), Ren'Py makes the following variables available to text shaders. To use a variable in a text shader, it needs to be declared in the variables argument to renpy.register\_text\_shader.

In addition to these, the model  are available, with a\_position, a\_tex\_coord, u\_time and u\_random being particularly useful.

#### Uniforms

`float u_text_depth`

The depth of the text from the top. The topmost text has a depth of 0.0, the first outline or shadow has a depth of 1.0, the second outline or shadow has a depth of 2.0, and so on.

`float u_text_main`

If this is 1.0, the text is the main text. If this is 0.0, the text is the outline or shadow of the main text.

`float u_text_max_depth`

The maximum value of u\_text\_depth. This is the number of outlines and shadows that will be drawn. When u\_text\_depth is equal to this value, the texct is the last outline or shadow, which may be useful for drawing backgrounds.

`vec2 u_text_offset`

The offset of the text from the center of the character. This is in drawable pixels in x, y order.

`float u_text_outline`

The width of the outline around the text. This is in drawable pixels, and is the distance from the edge of the text to the edge of the outline.

`float u_text_slow_duration`

The duration of a single slow character, when showing slow text. 0.0 if not showing slow text.

`float u_text_slow_time`

The time in seconds since the start of the slow text effect. This will only increase until the end of slow text, when it will max out. If the user clicks to terminate slow text, this will max out. It should only be used for slow text - use

`float u_text_to_drawable`

The ratio of virtual pixels to drawable pixels. This is used to convert from virtual pixels to drawable pixels.

`float u_text_to_virtual`

The ratio of drawable pixels to virtual pixels. This is used to convert from drawable pixels to virtual pixels.

`sampler2D tex0`

This texture contains the rendered text at the current depth.

`vec2 res0`

The resolution of tex0, in drawable pixels.

#### Attributes

When drawing text, each vertex corresponds to a single glyph. Multiple glyphs may have vertices that share locations, but these are passed to the shader as different vertices.

`float a_text_ascent`

The ascent of the current glyph's font above the baseline, in drawable pixels.

`vec2 a_text_center`

The position of the center of the glyphs's baseline, in drawable pixels. This is not the center of the rectangle, it's a point on the baseline and around the center of the character.

`float a_text_descent`

The descent of the current glyph below the baseline, in drawable pixels.

`float a_text_index`

The index of the glyph being drawn. This is 0 for the first vertex and goes up by one for each vertex.

`vec2 a_text_min_time`

The minimum time at which any vertex of the glyph should be shown. When showing from left-to-right, this is the time the leftmost vertices should be shown. When the text is meant to be shown instantly but `u_text_slow_duration` is not 0.0, this will be -3600.0.

`vec2 a_text_max_time`

The maximum time at which any vertex of the glyph should be shown. When showing from left-to-right, this is the time the rightmost vertices should be shown. When the text is meant to be shown instantly but `u_text_slow_duration` is not 0.0, this will be -3600.0.

`float a_text_time`

The time at which this vertex should be shown. When the text is meant to be shown instantly but `u_text_slow_duration` is not 0.0, this will be -3600.0.

`vec4 a_text_pos_rect`

The rectangle containing the glyph, in drawable pixels. This is a vec4 with the x, y, width, and height of the rectangle, in drawable pixels. This can be converted to texture coordinates by dividing it by `res0`.

### Pseudo-Glyphs

Ren'Py will creates pseudo-glyphs that cover the start and end of each line. If a line is blank, one pseudo-glyph is created covering the whole line. These pseudo-glyphs are necessary to cover areas where outlines may extend into a line above or below the current line.

### Example

This is an example of a text shader that spins text when shown.

init python:

    def adjust\_extra\_slow\_time(ts, u\_\_delay, \*\*kwargs):
        """
        Adjusts a text shader's extra slow time to support the spinning text shader.
        """
        ts.extra\_slow\_time \= u\_\_delay

    renpy.register\_textshader(
        "spin",
        adjust\_function \= adjust\_extra\_slow\_time,

        variables \= """
        uniform float u\_\_delay;
        uniform float u\_\_offset;
        uniform float u\_text\_slow\_time;
        attribute vec2 a\_text\_center;
        attribute float a\_text\_min\_time;
        """,

        vertex\_50 \= """
        float l\_\_angle = clamp((u\_text\_slow\_time - a\_text\_min\_time) / u\_\_delay, 0.0, 1.0) \* 2.0 \* 3.1415926536;
        float l\_\_sin = sin(l\_\_angle);
        float l\_\_cos = cos(l\_\_angle);

        gl\_Position.y -= u\_\_offset;
        gl\_Position.xy -= a\_text\_center;
        gl\_Position = vec4(
            gl\_Position.x \* l\_\_cos - gl\_Position.y \* l\_\_sin,
            gl\_Position.x \* l\_\_sin + gl\_Position.y \* l\_\_cos,
            gl\_Position.z,
            gl\_Position.w
            );
        gl\_Position.xy += a\_text\_center;
        gl\_Position.y += u\_\_offset;
        """,

        u\_\_delay \= 1.0,
        u\_\_offset \= 0,
    )

It can be used witt the following script:

define config.default\_textshader \= "typewriter"

label start:

    "This is a test of the {shader=spin:0.5:-5}spin{/shader} text shader."
