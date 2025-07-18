# Matrixcolor

Ren'Py supports recoloring images using the  transform property. This property can take either a  or a ColorMatrix object.

## Premultiplied Alpha Color

When an image is loaded, Ren'Py decompresses the image, and then copies it to the GPU of your computer or mobile device. As part of the copying, each of the four color channels (red, green, blue, and alpha - with alpha representing opacity) is scaled to a number between 0.0 and 1.0. In this system, 1.0 represents the full level of a color or fully opaque, while 0.0 represents the absence of the color or the pixel being fully transparent.

Ren'Py doesn't stop there, though. Once the values have been scaled, the red, green, and blue channels are multiplied by the alpha channel. This means that an opaque white pixel will have the value (1.0, 1.0, 1.0, 1.0), a 50% transparent red pixel will have the value (0.5, 0.0, 0.0, 0.5), and a transparent pixel will have the value (0.0, 0.0, 0.0, 0.0).

Premultiplied alph allows Ren'Py to scale images up and down without causing dark artifacts that come from representing colors more directly. Scaling images is similar to averaging two pixels together. Without premultiplied alpha, we might have a solid white pixel and a transparent pixel - (1.0, 1.0, 1.0, 1.0) and (0.0, 0.0, 0.0, 0.0), respectively. Average those together gets (0.5, 0.5, 0.5, 0.5). But that's not right - averaging solid white and transparent black should get 50% opaque white, not 50% opaque gray.

In the premultiplied alpha system, the starting value is the same, and so is the result - except now, (0.5, 0.5, 0.5, 0.5) has been pre-defined to be 50% opaque white. By storing colors in this way, Ren'Py can draw them to the screen correctly, and not get weird artifacts when scaling.

## Using a Matrix to Change Colors

The  objects used to change colors can consist of 16 numbers, which can in turn be arranged into a 4x4 grid. Here's a way of doing this that assigns a letter to each number:

define mymatrix \= Matrix(\[ a, b, c, d,
                           e, f, g, h,
                           i, j, k, l,
                           m, n, o, p, \])

While they're represented as letters here, realize these are really numbers, either given directly or computed.

These values are applied to the red (R), green (G), blue (B), and alpha (A) channels of the original color to make a new color, (R', G', B', A'). The formulas to do this are:

R' = R \* a + G \* b + B \* c + A \* d
G' = R \* e + G \* f + B \* g + A \* h
B' = R \* i + G \* j + B \* k + A \* l
A' = R \* m + G \* n + B \* o + A \* p

While this might seem complex, there's a pretty simple structure to it - the first row creates the new red channel, the second the new green channel and so on. So if we wanted to make a matrix that swapped red and green for some reason, we'd write:

transform swap\_red\_and green:
    matrixcolor Matrix(\[ 0.0, 1.0, 0.0, 0.0,
                         1.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 1.0, 0.0,
                         0.0, 0.0, 0.0, 1.0, \])

While this is a simple example, there is a lot of color theory that can be expressed in this way. Matrices can be combined by multiplying them together, and when that happens the matrices are combined right to left.

## ColorMatrix

While Matrix objects are suitable for static color changes, they're not useful for animating color changes. It's also useful to have a way of taking common matrices and encapsulating them in a way that allows the matrix to be parameterized.

The ColorMatrix is a base class that is is extended by a number of Matrix-creating classes. Instances of ColorMatrix are called by Ren'Py, and return Matrixes. ColorMatrix is well integrated with ATL, allowing for matrixcolor animations.

transform red\_blue\_tint:
    matrixcolor TintMatrix("#f00")
    linear 3.0 matrixcolor TintMatrix("#00f")
    linear 3.0 matrixcolor TintMatrix("#f00")
    repeat

The ColorMatrix class can be subclassed, with the subclasses replacing its `__call__` method. This method takes:

*   An old object to interpolate off of. This object may be of any class, and may be None if no old object exists.
    
*   A value between 0.0 and 1.0, representing the point to interpolate. 0.0 is entirely the old object, and 1.0 is entirely the new object.
    

And should return a .

As an example of a ColorMatrix, here is the implementation of Ren'Py's TintMatrix class.

class TintMatrix(ColorMatrix):
    def \_\_init\_\_(self, color):

        \# Store the color given as a parameter.
        self.color \= Color(color)

    def \_\_call\_\_(self, other, done):

        if type(other) is not type(self):

            \# When not using an old color, we can take
            \# r, g, b, and a from self.color.
            r, g, b \= self.color.rgb
            a \= self.color.alpha

        else:

            \# Otherwise, we have to extract from self.color
            \# and other.color, and interpolate the results.
            oldr, oldg, oldb \= other.color.rgb
            olda \= other.color.alpha
            r, g, b \= self.color.rgb
            a \= self.color.alpha

            r \= oldr + (r \- oldr) \* done
            g \= oldg + (g \- oldg) \* done
            b \= oldb + (b \- oldb) \* done
            a \= olda + (a \- olda) \* done

        \# To properly handle premultiplied alpha, the color channels
        \# have to be multiplied by the alpha channel.
        r \*= a
        g \*= a
        b \*= a

        \# Return a Matrix.
        return Matrix(\[ r, 0, 0, 0,
                        0, g, 0, 0,
                        0, 0, b, 0,
                        0, 0, 0, a \])

### Structural Similarity

In ATL, interpolating a the  property requires the use of ColorMatrixes that have structural similarity. That means the same types of ColorMatrix, multiplied together in the same order.

As an example, the following will interpolate from normal to a desaturated blue tint, and then return to normal.

show eileen happy at center:
    matrixcolor TintMatrix("#ffffff") \* SaturationMatrix(1.0)
    linear 2.0 matrixcolor TintMatrix("#ccccff") \* SaturationMatrix(0.0)
    linear 2.0 matrixcolor TintMatrix("#ffffff") \* SaturationMatrix(1.0)

While the first setting of matrixcolor may seem unnecessary, it is required to provide a base for the first linear interpolation. If it wasn't present, that interpolation would be skipped.

## Built-In ColorMatrix Subclasses

The following is the list of ColorMatrix subclasses that are built into Ren'Py.

_class_ BrightnessMatrix(_value\=1.0_)

A ColorMatrix that can be used with  to change the brightness of an image, while leaving the Alpha channel alone.

value

The amount of change in image brightness. This should be a number between -1 and 1, with -1 the darkest possible image and 1 the brightest.

_class_ ColorizeMatrix(_black\_color_, _white\_color_)

A ColorMatrix that can be used with  to colorize black and white displayables. It uses the color of each pixel in the black and white to interpolate between the black color and the white color.

The alpha channel is not touched.

This is inteded for use with a black and white image (or one that has been desaturated with ), and will yield strange results when used with images that are not black and white.

black\_color, white\_color

The colors used in the interpolation.

_class_ ContrastMatrix(_value\=1.0_)

A ColorMatrix that can be used with  to change the brightness of an image, while leaving the Alpha channel alone.

value

The contrast value. Values between 0.0 and 1.0 decrease the contrast, while values above 1.0 increase the contrast.

_class_ HueMatrix(_value\=1.0_)

A ColorMatrix that can be used with  to rotate the hue by value degrees. While value can be any number, positive or negative, 360 degrees makes a complete rotation. The alpha channel is left alone.

_class_ IdentityMatrix

A ColorMatrix that can be used with  that does not change the color or alpha of what is supplied to it.

_class_ InvertMatrix(_value\=1.0_)

A ColorMatrix that can be used with  to invert each of the color channels. The alpha channel is left alone.

value

The amount to inverty by. 0.0 is not inverted, 1.0 is fully inverted. Used to animate inversion.

_class_ OpacityMatrix(_value\=1.0_)

A ColorMatrix that can be used with  to change the opacity of an image, while leaving color channels alone.

value

The amount the alpha channel should be multiplied by, a number between 0.0 and 1.0.

_class_ SaturationMatrix(_value_, _desat\=(0.2126, 0.7152, 0.0722)_)

A ColorMatrix that can be used with  that alters the saturation of an image, while leaving the alpha channel alone.

value

The amount of saturation in the resulting image. 1.0 is the unaltered image, while 0.0 is grayscale.

desat

This is a 3-element tuple that controls how much of the red, green, and blue channels will be placed into all three channels of a fully desaturated image. The default is based on the constants used for the luminance channel of an NTSC television signal. Since the human eye is mostly sensitive to green, more of the green channel is kept than the other two channels.

SepiaMatrix(_tint\='#ffeec2'_, _desat\=(0.2126, 0.7152, 0.0722)_)

A function that returns a ColorMatrix that can be used with  to sepia-tone a displayable. This is the equivalent of:

TintMatrix(tint) \* SaturationMatrix(0.0, desat)

_class_ TintMatrix(_color_)

A ColorMatrix can be used with  to tint an image, while leaving the alpha channel alone.

color

The color that the matrix will tint things to. This is passed to , and so may be anything that Color supports as its first argument.
