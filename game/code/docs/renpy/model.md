# Model-Based Rendering

While Ren'Py is primarily used with two dimensional rectangular images that are common in visual novels, underneath the hood it has a model-based renderer intended to to take advantage of features found in modern GPUs. This allows for a number of visual effects that would not otherwise be possible.

As a warning, this is one of the most advanced features available in Ren'Py. In many cases, it's not necessary to understand how model-based rendering works behind the scenes - features like  and Live2D support can be used without understanding how Model-Based rendering works, and more such features will be added to the understanding. This documentation is intended for very advanced creators, and for developers looking to add to Ren'Py itself.

Model-Based Rendering is one of the most advanced features in Ren'Py, and this documentation may be hard to understand without first looking at the OpenGL, OpenGL ES, GLSL, and GLSL ES manual. What's more, since there are portions of the models that are passed directly to your GPU drivers, which may accept erroneous inputs, it's important to check on multiple kinds of hardware.

## Models, Renders, and Drawing Operations

The fundamental thing that Ren'Py draws to the screen is a Model. A model consists of the following things:

*   A Mesh of one or more triangles. A triangle consists of three vertices (corners), each of which contains a position in two or three-dimensional space, and may contain additional information, most commonly texture coordinates.
    
*   Zero or more textures, with the precise number allowed being limited by the GPUs your game can run on. All GPUs should support at least three textures per model. A texture is a rectangle containing image data that's been loaded on the GPU, either directly or using a render-to-texture operation.
    
*   A list of shader part names. Ren'Py uses these shader parts to create shaders, which are programs that are run on the GPU to render the model. Shader part names can be prefixed with a "-" to prevent that shader part from being used.
    
*   Uniform values. A uniform is additional data that is the same throughout the model. For example, when a model represents a solid color, the color is a uniform.
    
*   GL properties. GL properties are flags that further control how things are rendered, such as the minification/magnification modes and the color mask.
    

As Ren'Py usually draws more than one thing to the screen, it creates a tree of `Render` objects. These Render objects may have Models or other Renders as children. (A Render object can also be turned into a Model. as described below.) A Render contains:

*   A list of children, including a 2-dimensional offset that is applied to each child.
    
*   A  that describes how the children are transformed in three-dimensional space.
    
*   Lists of shader part names, uniforms, and GL properties that are applied to the Models when being drawn.
    
*   Flags that determine if the drawable-space clipping polygon should be updated.
    

Ren'Py draws the screen by performing a depth-first walk through the tree of Renders, until a Model is encountered. During this walk, Ren'Py updates a matrix transforming the location of the Model, a clipping polygon, and lists of shader parts, uniforms, and GL properties. When a Model is encountered as part of this walk, the appropriate shader program is activated on the GPU, all information is transferred, and a drawing operation occurs.

## Where Models are Created

Ren'Py creates Models automatically as part of its normal operation. The main reason to understand where models are created is that models correspond to drawing operations, and hence are the units that shaders are applied to.

Images and Image Manipulators

These create a model with a mesh containing two triangles that cover the rectangle of the image. The mesh contains texture coordinates. The model uses the "renpy.texture" shader.

The Solid displayable creates a mesh containing two triangles, and no texture coordinates. The model uses the "renpy.solid" shader, with the color placed in the `u_renpy_solid_color` uniform.

, , , , , 

Each of these transforms and displayables creates a Model with a mesh, shaders, and uniforms as is needed for its purposes.

Live2D

Live2D displayables may created multiple Models when rendered, generally one Model for each layer.

 and ATL

A Transform creates a model if  is True, or if  is being used. In this case, the children of the Transform are rendered to textures, with the mesh of the first texture being used for the mesh associated with the model.

Not every transform creates a Model. Some transforms will simply add shaders and uniforms to a Render (such as transforms that use  or ). Other transforms simply affect geometry.

`Render`

A Transform creates a model if its `mesh` attribute is True. In this case, the children of the Render are rendered to textures, with the mesh of the first texture being used for the mesh associated with the model.

It's expected that Ren'Py will add more ways of creating models in the future.

## Shader Program Generation

Ren'Py generates a shader program by first assembling a list of shader part names. This list consists of "renpy.geometry", the list of shader parts taken from Renders, and the list of shader parts found in the Model being drawn.

The shader parts are then deduplicated. If a shader part begins with "-", it is removed from the list, as is the rest of that part without the leading "-". (So "-renpy.geometry" will cause itself and "renpy.geometry" to be removed.)

Ren'Py then takes the list of shader parts, and retrieves lists of variables, functions, vertex shader parts, and fragment shader parts. These are, in turn, used to generate the source code for shaders, with the parts of the vertex and fragement shaders being included in low-number to high-number priority order.

This means that any variable created by one of the shaders will be accessible by every other fragment from any other shader in the list of shader parts. There is no scope like in Python functions to protect interference between shaders.

Ren'Py keeps a cache of all combinations of shader parts that have ever been used in game/cache/shaders.txt, and loads them at startup. If major changes in shader use occur, this file should be edited or deleted so it can be re-created with valid data.

## Creating a Custom Shader

New shader parts can be created by calling the renpy.register\_shader function and supplying portions of GLSL shaders.

Generally, shader parts should be of the form "namespace.part", such as "mygame.recolor" or "mylibrary.warp". Names beginning with "renpy." or "live2d." are reserved for Ren'Py, as are names beginning with \_.

renpy.register\_shader(_name_, _\*\*kwargs_)

This registers a shader part. This takes name, and then keyword arguments.

name

A string giving the name of the shader part. Names starting with an underscore or "renpy." are reserved for Ren'Py.

variables

The variables used by the shader part. These should be listed one per line, a storage (uniform, attribute, or varying) followed by a type, name, and semicolon. For example:

variables\='''
uniform sampler2D tex0;
attribute vec2 a\_tex\_coord;
varying vec2 v\_tex\_coord;
'''

vertex\_functions

If given, a string containing functions that will be included in the vertex shader.

fragment\_functions

If given, a string containing functions that will be included in the fragment shader.

Other keyword arguments should start with `vertex_` or `fragment_`, and end with an integer priority. So "fragment\_200" or "vertex\_300". These give text that's placed in the appropriate shader at the given priority, with lower priority numbers inserted before higher priority numbers.

Ren'Py supports only the following variable types:

*   float (a Python float)
    
*   vec2 (a tuple of 2 floats)
    
*   vec3 (a tuple of 3 floats)
    
*   vec4 (a tuple of 4 floats)
    
*   mat4 (a )
    
*   sampler2D (supplied by Ren'Py)
    

Uniform variables should begin with u\_, attributes with a\_, and varying variables with v\_. Names starting with u\_renpy\_, a\_renpy, and v\_renpy are reserved, as are the standard variables given below.

As a general sketch for priority levels, priority 100 sets up geometry, priority 200 determines the initial fragment color (gl\_FragColor), and higher-numbered priorities can apply effects to alter that color.

Here's an example of a custom shader part that applies a gradient across each model it is used to render:

init python:

    renpy.register\_shader("example.gradient", variables\="""
        uniform vec4 u\_gradient\_left;
        uniform vec4 u\_gradient\_right;
        uniform vec2 u\_model\_size;
        varying float v\_gradient\_done;
        attribute vec4 a\_position;
    """, vertex\_300\="""
        v\_gradient\_done = a\_position.x / u\_model\_size.x;
    """, fragment\_300\="""
        float gradient\_done = v\_gradient\_done;
        gl\_FragColor \*= mix(u\_gradient\_left, u\_gradient\_right, gradient\_done);
    """)

The custom shader can then be applied using a transform:

transform gradient:
    shader "example.gradient"
    u\_gradient\_left (1.0, 0.0, 0.0, 1.0)
    u\_gradient\_right (0.0, 0.0, 1.0, 1.0)

show eileen happy at gradient

As stated before, the `gradient_done` variable from the example.gradient shader will be accessible by any and all other shaders applied from the same list. This can be useful when having optional parts in a given shader system, but it can also lead to name collisions when using two independent shaders.

There is a variable that can help in debugging custom shaders:

define config.log\_gl\_shaders \= False

If true, source code for the GLSL shader programs will be written to log.txt on start.

## Shader Part Local Variables

Variables can be declared shader-local by using one of `u__`, `a__`, `v__`, or `l__` as a prefix. When this is done, the double underscores are filled in with the shader name with all dots replaced with underscores. For example, if the shader name is `example.gradient`, the prefix `u__` will be replaced with `u_example_gradient_`.

The main use of this is with , where most uniforms are shader-local. Also, local variables inside the shader should be declared with `l__`.

## Transforms and Model-Based Rendering

Model-Based rendering adds the following properties to ATL and :

mesh

Type:

None or True or tuple

Default:

None

If not None, this Transform will be rendered as a model. This means:

*   A mesh will be created. If this is a 2-component tuple, it's taken as the number of points in the mesh, in the x and y directions. (Each dimension must be at least 2.) If True, the mesh is taken from the child.
    
*   The child of this transform will be rendered to a texture.
    
*   The renpy.texture shader will be added.
    

mesh\_pad

Type:

None or tuple

Default:

None

If not None, this can either be a 2 or 4-component tuple. If mesh is True and this is given, this applies padding to the size of the textures applied to the textures used by the mesh. A 2-component tuple applies padding to the right and bottom, while a 4-component tuple applies padding to the left, top, right, and bottom.

This can be used, in conjunction with the `gl_pixel_perfect` property, to render text into a mesh. In Ren'Py, text is rendered at the screen resolution, which might overflow the boundaries of the texture that will be applied to the mesh. Adding a few pixels of padding makes the texture bigger, which will display all pixels. For example:

transform adjust\_text:
    mesh True
    mesh\_pad (10, 0)
    gl\_pixel\_perfect True
    shader "shaders.adjust\_text"

will ensure that the texture passed to the shader contains all of the pixels of the text.

shader

Type:

None or str or list of str

Default:

None

If not None, a shader part name or list of shader part names that will be applied to this Render (if a Model is created) or the Models reached through this Render.

blend

Type:

None or str

Default:

None

if not None, this should be a string. This string is looked up in  to get the value for the gl\_blend\_func property. It's used to use alternate blend modes.

The default blend modes this supports are "normal", "add", "multiply", "min", and "max".

In addition, uniforms that start with u\_ but not with u\_renpy are made available as Transform properties. GL properties are made available as transform properties starting with gl\_. For example, the color\_mask property is made available as gl\_color\_mask.

## Blend Functions

define config.gl\_blend\_func \= { ... }

A dictionary used to map a blend mode name to a blend function. The blend modes are supplied to the gl\_blend\_func property, given below.

The default blend modes are:

gl\_blend\_func\["normal"\] \= (GL\_FUNC\_ADD, GL\_ONE, GL\_ONE\_MINUS\_SRC\_ALPHA, GL\_FUNC\_ADD, GL\_ONE, GL\_ONE\_MINUS\_SRC\_ALPHA)
gl\_blend\_func\["add"\] \= (GL\_FUNC\_ADD, GL\_ONE, GL\_ONE, GL\_FUNC\_ADD, GL\_ZERO, GL\_ONE)
gl\_blend\_func\["multiply"\] \= (GL\_FUNC\_ADD, GL\_DST\_COLOR, GL\_ONE\_MINUS\_SRC\_ALPHA, GL\_FUNC\_ADD, GL\_ZERO, GL\_ONE)
gl\_blend\_func\["min"\] \= (GL\_MIN, GL\_ONE, GL\_ONE, GL\_MIN, GL\_ONE, GL\_ONE)
gl\_blend\_func\["max"\] \= (GL\_MAX, GL\_ONE, GL\_ONE, GL\_MAX, GL\_ONE, GL\_ONE)

As Ren'Py uses premultiplied alpha, the results of some of these may be counterintuitive when a pixel is not opaque. In the GPU, the color (r, g, b, a) is represented as (r \* a, g \* a, b \* a, a), and the blend function uses these premultiplied colors. This may be a different result that you get for these blend modes in a paint program, when what is drawn is not fully opaque.

## Uniforms and Attributes

The following uniforms are made available to all Models.

`vec2 u_model_size`

The width and height of the model.

`float u_lod_bias`

The level of detail bias to apply to texture lookups. This may be set in a Transform. The default value, taken from  and defaulting to -0.5, biases Ren'Py to always pick the next bigger level and scale it down.

`mat4 u_transform`

The transform used to project virtual pixels to the OpenGL viewport.

`float u_time`

The time of the frame. The epoch is undefined, so it's best to treat this as a number that increases by one second a second. The time is modulo 86400, so it will reset to 0.0 once a day.

`vec4 u_random`

Four random numbers between 0.0 and 1.0 that are (with incredibly high likelyhood) different from frame to frame.

`vec4 u_viewport`

This gives the current viewport being drawn into. u\_viewport.xy is are the coordinates of the bottom-left corner of the viewport, relative to the bottom-left corner of the window. u\_viewport.pq is the width and height of the viewport.

`vec2 u_virtual_size`

> This is the virtual size of the game (, ). This can be used to convert from gl\_Position to virtual coordinates using:
> 
> v\_position \= u\_virtual\_size \* vec2(gl\_Position.x \* .5 + .5, \-gl\_Position.y \* .5 + .5)

`vec2 u_drawable_size`

The size of the drawable are of the windows, in pixels, at the resolution the game is running at. For example, if a 1280x720 game is scaled up to 1980x1080, this will be (1920, 1080).

`sampler2D tex0`, `sampler2D tex1`, `sampler2D tex2`

If textures are available, the corresponding samplers are placed in this variable.

`vec2 res0`, `vec2 res1`, `vec2 res2`

If textures are available, the size of the textures are placed in these variables. When the texture is loaded from disk, this is the size of the image file. After a render to texture, it's the number of drawable pixels the rendered texture covered.

The following attributes are available to all models:

`vec4 a_position`

The position of the vertex being rendered. This is in virtual pixels, relative to the upper left corner of the texture.

If textures are available, so is the following attribute:

`vec2 a_tex_coord`

The coordinate that this vertex projects to inside the textures.

## GL Properties

GL properties change the global state of OpenGL, or the Model-Based renderer. These properties can be used with a Transform, or with the `Render.add_property()` function.

`gl_blend_func`

If present, this is expected to be a six-component tuple, which is used to set the equation used to blend the pixel being drawn with the pixel it is being drawn to, and the parameters to that equation.

Specifically, this should be (rgb\_equation, src\_rgb, dst\_rgb, alpha\_equation, src\_alpha, dst\_alpha). These will be used to call:

glBlendEquationSeparate(rgb\_equation, alpha\_equation)
glBlendFuncSeparate(src\_rgb, dst\_rgb, src\_alpha, dst\_alpha)

Please see the OpenGL documentation for what these functions do. OpenGL constants can be imported from renpy.uguu:

init python:
    from renpy.uguu import GL\_ONE, GL\_ONE\_MINUS\_SRC\_ALPHA

The  transform property is generally an easy way to use this.

`gl_color_mask`

This is expecting to be a 4-tuple of booleans, corresponding to the four channels of a pixel (red, green, blue, and alpha). If a given channel is True, the draw operation will write to that pixel. Otherwise, it will not.

`gl_depth`

If True, this will clear the depth buffer, and then enable depth rendering for this displayable and the children of this displayable.

Note that drawing any pixel, even transparent pixels, will update the depth buffer. As a result, using this with images that have transparency may lead to unexpected problems. (As an alternative, consider the `zorder` and `behind` clauses of the `show` statement.)

`gl_pixel_perfect`

When True, Ren'Py will move the mesh such that the first vertex is aligned with a pixel on the screen. This is mostly used in conjunction with text, to ensure that the text remains sharp.

The following properties only take effect when a texture is being created, by a Transform with  set, or by , where these can be supplied the property method.

`gl_drawable_resolution`

If True or not set, the texture is rendered at the same resolution as the window displaying the game. If False, it's rendered at the virtual resolution of the displayable.

`gl_anisotropic`

If supplied, this determines if the textures applied to a mesh are created with anisotropy. Anisotropy is a feature that causes multiple texels (texture pixels) to be sampled when a texture is zoomed by a different amount in X and Y.

This defaults to True. Ren'Py sets this to False for certain effects, like the Pixellate transition.

`gl_mipmap`

If supplied, this determines if the textures supplied to a mesh are created with mipmaps. This defaults to True.

`gl_texture_wrap`

When supplied, this determines how the textures applied to a mesh are wrapped. This expects a 2-component tuple, where the first component is used to set GL\_TEXTURE\_WRAP\_S and the second component is used to set GL\_TEXTURE\_WRAP\_T, which conventionally are the X and Y axes of the created texture.

The values should be OpenGL constants imported from renpy.uguu:

init python:
    from renpy.uguu import GL\_CLAMP\_TO\_EDGE, GL\_MIRRORED\_REPEAT, GL\_REPEAT

This can also be customized for specific textures. gl\_texture\_wrap\_tex0 controls the first texture, gl\_texture\_wrap\_tex1 the second, gl\_texture\_wrap\_tex2, the third, and gl\_texture\_wrap\_tex3 the fourth. While only these four are avalable through Transforms, it's possibe to supply "texture\_wrap\_tex4" or "texture\_wrap\_myuniform" to Render.add\_property.

## Model Displayable

The Model displayable acts as a factory to created models for use with the model-based renderer.

_class_ Model(_size\=None_, _\*\*properties_)

This is a displayable that causes Ren'Py to create a 2D or 3D model for use with the model-based renderer, that will be drawn in a single operation with the shaders given here, or selected by an enclosing Transform or Displayable.

size

If not None, this should be a width, height tuple, that's used to give the size of the Model. If not given, the model is the size of the area provided to it. The fit parameter to a texture takes precedence.

If no mesh method is called, a mesh that sets a\_position and a\_tex\_coord to match the way Ren'Py loads textures is created if at least one texture is supplied. Otherwise, a mesh that only sets a\_position is used.

All methods on this calls return the displayable the method is called on, making it possible to chain calls.

child(_displayable_, _fit\=False_)

This is the same as the texture method, except that the focus and main parameters are set to true.

grid\_mesh(_width_, _height_)

Creates a mesh that consists of a width x height grid of evenly spaced points, connecting each point to the closest points vertically and horizontally, and dividing each rectangle in the grid so created into triangles.

width, height

The number of points in the horizontal vertical directions, a integer that is at least 2.

property(_name_, _value_)

Sets the value of a gl property.

name

A string giving the name of the GL property, including the "gl\_" prefix.

value

The value of the gl property.

shader(_shader_)

Adds a shader to this model.

shader

A string given the name of a shader to use with this model.

texture(_displayable_, _focus\=False_, _main\=False_, _fit\=False_, _texture\_wrap\=None_)

Add a texture to this model, by rendering the given displayable. The first texture added will be `tex0`, the second `tex1`, a and so on.

focus

If true, focus events are passed to the displayable. It's assumed that coordinate relative to the model map 1:1 with coordinates relative to the displayable.

main

If true, this is marked as a main child of this displayable, which allows it to be inspected using the displayable inspector.

fit

If true, the Model is given the size of the displayable. This may only be true for one texture.

texture\_wrap

If not None, this is the  that will be applied to this texture.

uniform(_name_, _value_)

Sets the value of a uniform that is passed to the shaders.

name

A string giving the name of the uniform to set, including the "u\_" prefix.

value

The value of the uniform. Either a float, a 2, 3, or 4 element tuple of floats, or a Matrix.

### Model Displayable Examples

The Model displayable can be used in conjunction with an ATL transform and a built-in shader to create the Dissolve transform:

transform dt(delay\=1.0, new\_widget\=None, old\_widget\=None):
    delay delay
    Model().texture(old\_widget).child(new\_widget)
    shader \[ 'renpy.dissolve' \]

    u\_renpy\_dissolve 0.0
    linear delay u\_renpy\_dissolve 1.0

Using the Model displayable as the child of a displayable is incompatible with , as the two both create models inside Ren'Py.

## Animated Shaders

When using shaders that depend on `u_time` to animate, one must be aware, that even though every shader on screen will run on every frame displayed, Ren'Py does not run on constant FPS, and will fall back to the minimum frame rate of 5 FPS if no displayables require to be redrawn.

When using an animating shader in an ATL transform, this can cause that shader to "stutter" and only animate properly while some other object on screen animates as well, in case the transform you're using it in does not cause redraws otherwise. In this case, an empty ATL loop can be introduced to force redraws to happen:

transform fancy\_shader:
    shader 'my\_fancy\_shader'
    pause 0
    repeat

`pause 0` will cycle the frames as fast as possible. You can also set different values for `pause` to specify a minimum frame rate, like `pause 1.0/30`.

## Shader Parts

For a list of shader parts that Ren'Py uses, see the .
