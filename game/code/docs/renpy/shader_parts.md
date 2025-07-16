# Default Shader Parts

Shader parts are used by  and . This file contains an index of parts by priority, and the source of each shader part.

## Vertex Part Priorities

How Ren'Py uses vertex part priorities:

*   Priority 0 sets up gl\_Position.
    
*   Priority 10 is used to capture gl\_Position in virtual or drawable coordinates before adjustment.
    
*   Priorities 20-80 adjust gl\_Position in virtual or drawable coordinates.
    
*   Priority 90 is used to capture gl\_Position in virtual or drawable coordinates after adjustment.
    
*   Priority 100 transforms gl\_Position to viewport coordinates.
    
*   Priority 200 stores more information in varying variables, without touching gl\_Position.
    

In order:

0\. 

10\. 

10\. 

20\. 

25\. 

30\. 

35\. 

40\. 

100\. 

200\. 

200\. 

200\. 

200\. 

200\. 

200\. 

200\. 

200\. 

## Fragment Part Priorities

How Ren'Py uses fragment part priorities:

*   Priority 200 determines an original color and stores it in gl\_FragColor.
    
*   Priority 300 multiplies that color with a second texture.
    
*   Priority 325 stores alpha before the text shaders adjust it.
    
*   Priority 350 applies text shaders that adjust alpha.
    
*   Priority 375 can undo part of the effect of these text shaders.
    
*   Priority 400 adjusts the color, applying Transform and displayable-based changes.
    
*   Priority 500 adjusts the alpha channel, applying Transform and displayable-based changes.
    

In order:

200\. 

200\. 

200\. 

200\. 

200\. 

200\. 

300\. 

300\. 

325\. 

350\. 

350\. 

375\. 

400\. 

500\. 

500\. 

## renpy.alpha

Variables:

uniform float u\_renpy\_alpha;
uniform float u\_renpy\_over;

Fragment shader (priority 500):

gl\_FragColor \= gl\_FragColor \* vec4(u\_renpy\_alpha, u\_renpy\_alpha, u\_renpy\_alpha, u\_renpy\_alpha \* u\_renpy\_over);

## renpy.alpha\_mask

Variables:

uniform sampler2D tex0;
uniform sampler2D tex1;
attribute vec2 a\_tex\_coord;
varying vec2 v\_tex\_coord;

Vertex shader (priority 200):

v\_tex\_coord \= a\_tex\_coord;

Fragment shader (priority 500):

vec4 src  \= texture2D(tex0, v\_tex\_coord.xy);
vec4 mask \= texture2D(tex1, v\_tex\_coord.xy);

gl\_FragColor \= vec4(src.r \* mask.r, src.g \* mask.r, src.b \* mask.r, mask.r);

## renpy.blur

Variables:

uniform sampler2D tex0;
attribute vec2 a\_tex\_coord;
varying vec2 v\_tex\_coord;
uniform float u\_renpy\_blur\_log2;

Vertex shader (priority 200):

v\_tex\_coord \= a\_tex\_coord;

Fragment shader (priority 200):

gl\_FragColor \= vec4(0.);
float renpy\_blur\_norm \= 0.;

for (float i \= \-5.; i < 1.; i += 1.) {
    float renpy\_blur\_weight \= exp(\-0.5 \* pow(u\_renpy\_blur\_log2 \- i, 2.));
    renpy\_blur\_norm += renpy\_blur\_weight;
}

gl\_FragColor += renpy\_blur\_norm \* texture2D(tex0, v\_tex\_coord.xy, 0.);

for (float i \= 1.; i < 14.; i += 1.) {

    if (i \>= u\_renpy\_blur\_log2 + 5.) {
        break;
    }

    float renpy\_blur\_weight \= exp(\-0.5 \* pow(u\_renpy\_blur\_log2 \- i, 2.));
    gl\_FragColor += renpy\_blur\_weight \* texture2D(tex0, v\_tex\_coord.xy, i);
    renpy\_blur\_norm += renpy\_blur\_weight;
}

if (renpy\_blur\_norm \> 0.0) {
    gl\_FragColor /= renpy\_blur\_norm;
} else {
    gl\_FragColor \= texture2D(tex0, v\_tex\_coord.xy, 0.0);
}

## renpy.dissolve

Variables:

uniform float u\_lod\_bias;
uniform sampler2D tex0;
uniform sampler2D tex1;
uniform float u\_renpy\_dissolve;
attribute vec2 a\_tex\_coord;
varying vec2 v\_tex\_coord;

Vertex shader (priority 200):

v\_tex\_coord \= a\_tex\_coord;

Fragment shader (priority 200):

vec4 color0 \= texture2D(tex0, v\_tex\_coord.st, u\_lod\_bias);
vec4 color1 \= texture2D(tex1, v\_tex\_coord.st, u\_lod\_bias);

gl\_FragColor \= mix(color0, color1, u\_renpy\_dissolve);

## renpy.geometry

Variables:

uniform mat4 u\_transform;
attribute vec4 a\_position;

Vertex shader (priority 0):

gl\_Position \= a\_position;

Vertex shader (priority 100):

gl\_Position \= u\_transform \* gl\_Position;

## renpy.imagedissolve

Variables:

uniform float u\_lod\_bias;
uniform sampler2D tex0;
uniform sampler2D tex1;
uniform sampler2D tex2;
uniform float u\_renpy\_dissolve\_offset;
uniform float u\_renpy\_dissolve\_multiplier;
attribute vec2 a\_tex\_coord;
varying vec2 v\_tex\_coord;

Vertex shader (priority 200):

v\_tex\_coord \= a\_tex\_coord;

Fragment shader (priority 200):

vec4 color0 \= texture2D(tex0, v\_tex\_coord.st, u\_lod\_bias);
vec4 color1 \= texture2D(tex1, v\_tex\_coord.st, u\_lod\_bias);
vec4 color2 \= texture2D(tex2, v\_tex\_coord.st, u\_lod\_bias);

float a \= clamp((color0.a + u\_renpy\_dissolve\_offset) \* u\_renpy\_dissolve\_multiplier, 0.0, 1.0);
gl\_FragColor \= mix(color1, color2, a);

## renpy.mask

Variables:

uniform float u\_lod\_bias;
uniform sampler2D tex0;
uniform sampler2D tex1;
uniform float u\_renpy\_mask\_multiplier;
uniform float u\_renpy\_mask\_offset;
attribute vec2 a\_tex\_coord;
varying vec2 v\_tex\_coord;

Vertex shader (priority 200):

v\_tex\_coord \= a\_tex\_coord;

Fragment shader (priority 200):

vec4 src \= texture2D(tex0, v\_tex\_coord.st, u\_lod\_bias);
vec4 mask \= texture2D(tex1, v\_tex\_coord.st, u\_lod\_bias);

gl\_FragColor \= src \* (mask.a \* u\_renpy\_mask\_multiplier + u\_renpy\_mask\_offset);

## renpy.matrixcolor

Variables:

uniform mat4 u\_renpy\_matrixcolor;

Fragment shader (priority 400):

gl\_FragColor \= u\_renpy\_matrixcolor \* gl\_FragColor;

## renpy.solid

Variables:

uniform vec4 u\_renpy\_solid\_color;

Fragment shader (priority 200):

gl\_FragColor \= u\_renpy\_solid\_color;

## renpy.texture

Variables:

uniform float u\_lod\_bias;
uniform sampler2D tex0;
attribute vec2 a\_tex\_coord;
varying vec2 v\_tex\_coord;

Vertex shader (priority 200):

v\_tex\_coord \= a\_tex\_coord;

Fragment shader (priority 200):

gl\_FragColor \= texture2D(tex0, v\_tex\_coord.xy, u\_lod\_bias);

## textshader.dissolve

Variables:

uniform float u\_textshader\_dissolve\_duration;
uniform float u\_text\_slow\_duration;
uniform float u\_text\_slow\_time;
attribute float a\_text\_time;
varying float v\_text\_time;

Vertex shader (priority 200):

v\_text\_time \= a\_text\_time;

Fragment shader (priority 350):

float l\_textshader\_dissolve\_duration \= u\_textshader\_dissolve\_duration \* u\_text\_slow\_duration;
float l\_textshader\_dissolve\_done;
if (l\_textshader\_dissolve\_duration \> 0.0) {
    l\_textshader\_dissolve\_done \= clamp((u\_text\_slow\_time \- v\_text\_time) / l\_textshader\_dissolve\_duration, 0.0, 1.0);
} else {
    l\_textshader\_dissolve\_done \= v\_text\_time <= u\_text\_slow\_time ? 1.0 : 0.0;
}
gl\_FragColor \= gl\_FragColor \* l\_textshader\_dissolve\_done;

## textshader.flip

Variables:

uniform float u\_textshader\_flip\_duration;
uniform float u\_text\_slow\_duration;
uniform float u\_text\_slow\_time;
attribute vec2 a\_text\_center;
attribute float a\_text\_min\_time;

Vertex shader (priority 20):

float l\_textshader\_flip\_duration \= u\_textshader\_flip\_duration \* u\_text\_slow\_duration;
float l\_textshader\_flip\_done;

if (l\_textshader\_flip\_duration \> 0.0) {
    l\_textshader\_flip\_done \= clamp((u\_text\_slow\_time \- a\_text\_min\_time) / l\_textshader\_flip\_duration, 0.0, 1.0);
} else {
    l\_textshader\_flip\_done \= a\_text\_min\_time <= u\_text\_slow\_time ? 1.0 : 0.0;
}

gl\_Position.x \= mix(a\_text\_center.x \- (gl\_Position.x \- a\_text\_center.x), gl\_Position.x, l\_textshader\_flip\_done);

## textshader.jitter

Variables:

uniform vec2 u\_textshader\_jitter\_jitter;
uniform vec4 u\_random;
uniform float u\_text\_to\_drawable;

Vertex shader (priority 30):

vec2 l\_textshader\_jitter\_jitter \= u\_textshader\_jitter\_jitter \* u\_text\_to\_drawable;
gl\_Position.xy += l\_textshader\_jitter\_jitter \* u\_random.xy \- l\_textshader\_jitter\_jitter / 2.0;

## textshader.linetexture

Variables:

uniform sampler2D u\_textshader\_linetexture\_texture;
uniform vec2 u\_textshader\_linetexture\_scale;
uniform vec2 u\_textshader\_linetexture\_texture\_res;

uniform float u\_text\_to\_virtual;
uniform float u\_text\_main;

attribute vec2 a\_text\_center;
varying vec2 v\_textshader\_linetexture\_coord;

Vertex shader (priority 10):

v\_textshader\_linetexture\_coord \= vec2( gl\_Position.x, (gl\_Position.y \- a\_text\_center.y)) / u\_textshader\_linetexture\_scale \* u\_text\_to\_virtual / u\_textshader\_linetexture\_texture\_res;
v\_textshader\_linetexture\_coord.y += 0.5;

Fragment shader (priority 300):

if (u\_text\_main \== 1.0) {
    gl\_FragColor \= texture2D(u\_textshader\_linetexture\_texture, v\_textshader\_linetexture\_coord) \* gl\_FragColor;
}

## textshader.offset

Variables:

uniform vec2 u\_textshader\_offset\_offset;
uniform float u\_text\_to\_drawable;

Vertex shader (priority 35):

gl\_Position.xy += u\_textshader\_offset\_offset \* u\_text\_to\_drawable;

## textshader.slowalpha

Variables:

uniform float u\_textshader\_slowalpha\_alpha

Fragment shader (priority 325):

vec4 l\_textshader\_slowalpha\_color \= gl\_FragColor;

Fragment shader (priority 375):

gl\_FragColor \= mix(gl\_FragColor, l\_textshader\_slowalpha\_color, u\_textshader\_slowalpha\_alpha);

## textshader.texture

Variables:

uniform sampler2D u\_textshader\_texture\_texture;
uniform vec2 u\_textshader\_texture\_texture\_res;

uniform float u\_text\_to\_virtual;
uniform float u\_text\_main;
varying vec2 v\_textshader\_texture\_coord;

Vertex shader (priority 10):

v\_textshader\_texture\_coord \= u\_text\_to\_virtual \* gl\_Position.xy / u\_textshader\_texture\_texture\_res;

Fragment shader (priority 300):

if (u\_text\_main \== 1.0) {
    gl\_FragColor \= texture2D(u\_textshader\_texture\_texture, v\_textshader\_texture\_coord) \* gl\_FragColor;
}

## textshader.typewriter

Variables:

uniform float u\_text\_slow\_time;
attribute float a\_text\_min\_time;
varying float v\_text\_min\_time;

Vertex shader (priority 200):

v\_text\_min\_time \= a\_text\_min\_time;

Fragment shader (priority 350):

float l\_textshader\_typewriter\_done \= v\_text\_min\_time <= u\_text\_slow\_time ? 1.0 : 0.0;
gl\_FragColor \= gl\_FragColor \* l\_textshader\_typewriter\_done;

## textshader.wave

Variables:

uniform float u\_textshader\_wave\_amplitude;
uniform float u\_textshader\_wave\_frequency
uniform float u\_textshader\_wave\_wavelength;

uniform float u\_time;
uniform float u\_text\_to\_drawable;
attribute float a\_text\_index;

Vertex shader (priority 40):

gl\_Position.y += cos(2.0 \* 3.14159265359 \* (a\_text\_index / u\_textshader\_wave\_wavelength + u\_time \* u\_textshader\_wave\_frequency)) \* u\_textshader\_wave\_amplitude \* u\_text\_to\_drawable;

## textshader.zoom

Variables:

uniform float u\_textshader\_zoom\_zoom;
uniform float u\_textshader\_zoom\_duration;
uniform float u\_text\_slow\_duration;
uniform float u\_text\_slow\_time;
attribute vec2 a\_text\_center;
attribute float a\_text\_min\_time;

Vertex shader (priority 25):

float l\_textshader\_zoom\_duration \= u\_textshader\_zoom\_duration \* u\_text\_slow\_duration;

if (l\_textshader\_zoom\_duration \> 0.0) {
    float l\_textshader\_zoom\_done \= clamp((u\_text\_slow\_time \- a\_text\_min\_time) / l\_textshader\_zoom\_duration, 0.0, 1.0);
    gl\_Position.xy \= mix(a\_text\_center + (gl\_Position.xy \- a\_text\_center) \* u\_textshader\_zoom\_zoom, gl\_Position.xy, l\_textshader\_zoom\_done);
}

- - -

Built with  using a  provided by .

jQuery(function () { SphinxRtdTheme.Navigation.enable(false); });