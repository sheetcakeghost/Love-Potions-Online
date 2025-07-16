# Image Manipulators

An image manipulator is a displayable that takes an image or image manipulator, and either loads it or performs an operation on it. Image manipulators can only take images or other image manipulators as input.

An image manipulator can be used any place a displayable can, but not vice-versa. An  is a kind of image manipulator, so an Image can be used whenever an image manipulator is required.

Warning

The use of image manipulators is historic. A number of image manipulators that had been documented in the past should no longer be used, as they suffer from inherent problems, and in general (except for ), the  displayable provides similar functionality while fixing the problems.

_class_ im.AlphaMask(_base_, _mask_, _\*\*properties_)

An image manipulator that takes two image manipulators, base and mask, as arguments. It replaces the alpha channel of base with the red channel of mask.

This is used to provide an image's alpha channel in a second image, like having one jpeg for color data, and a second one for alpha. In some cases, two jpegs can be smaller than a single png file.

Note that this takes different arguments from , which uses the mask's alpha channel.

The two images need to have the same size, and the same oversampling factor.

_class_ im.Blur(_im_, _xrad_, _yrad\=None_, _\*\*properties_)

An image manipulator that blurs the image manipulator im using an elliptical kernel described by xrad and optionally yrad.

If yrad is None, it will take the value of xrad resulting in a circular kernel being used.

image logo blurred \= im.Blur("logo.png", 1.5)

Deprecated since version 7.4.0: Use the  transform property.

_class_ im.Crop(_im_, _rect_)

An image manipulator that crops rect, a (x, y, width, height) tuple, out of im, an image manipulator.

image logo crop \= im.Crop("logo.png", (0, 0, 100, 307))

Deprecated since version 7.4.0: Use the  transform property.

_class_ im.Data(_data_, _filename_, _\*\*properties_)

This image manipulator loads an image from binary data.

data

A string of bytes, giving the compressed image data in a standard file format.

filename

A "filename" associated with the image. This is used to provide a hint to Ren'Py about the format of data. (It's not actually loaded from disk.)

_class_ im.FactorScale(_im_, _width_, _height\=None_, _bilinear\=True_, _\*\*properties_)

An image manipulator that scales im (a second image manipulator) to width times its original width, and height times its original height. If height is omitted, it defaults to width.

If bilinear is true, then bilinear interpolation is used for the scaling. Otherwise, nearest neighbor interpolation is used.

image logo doubled \= im.FactorScale("logo.png", 1.5)

Deprecated since version 7.4.0: Use the , or the  and  transform properties.

_class_ im.Flip(_im_, _horizontal\=False_, _vertical\=False_, _\*\*properties_)

An image manipulator that flips im (an image manipulator) vertically or horizontally. vertical and horizontal control the directions in which the image is flipped.

image eileen flip \= im.Flip("eileen\_happy.png", vertical\=True)

Deprecated since version 7.4.0: Set  (for horizontal flip) or  (for vertical flip) to a negative value.

im.Grayscale(_im_, _\*\*properties_)

An image manipulator that creates a desaturated version of the image manipulator im.

Deprecated since version 7.4.0: Set the  transform property to .

im.Sepia(_im_, _\*\*properties_)

An image manipulator that creates a sepia-toned version of the image manipulator im.

Deprecated since version 7.4.0: Set the  transform property to 

_class_ im.Tile(_im_, _size\=None_, _\*\*properties_)

An image manipulator that tiles the image manipulator im, until it is size.

size

If not None, a (width, height) tuple. If None, this defaults to (, ).

Deprecated since version 7.4.0: Use .

## im.MatrixColor

Warning

The im.MatrixColor image manipulator has been replaced by Transforms and ATL transforms that specify the matrixcolor property. Each im.matrix generator has been given a new Matrix equivalent, which can be found in the .

The im.MatrixColor image manipulator is an image manipulator that uses a matrix to control how the colors of an image are transformed. The matrix used can be an im.matrix object, which encodes a 5x5 matrix in an object that supports matrix multiplication, and is returned by a series of functions. im.matrix objects may be multiplied together to yield a second object that performs both operations. For example:

image city blue \= im.MatrixColor(
    "city.jpg",
    im.matrix.desaturate() \* im.matrix.tint(0.9, 0.9, 1.0))

first desaturates the image, and then tints it blue. When the intermediate image is not needed, multiplying matrices is far more efficient, in both time and image cache space, than using two im.MatrixColors.

Warning

The new Matrix objects multiply in the opposite order as the im.Matrixcolor ones. With X being the Matrix corresponding to im.Matrixcolor.x, `C*B*A` will be the Matrix corresponding to `im.a*im.b*im.c`.

_class_ im.MatrixColor(_im_, _matrix_, _\*\*properties_)

An image operator that uses matrix to linearly transform the image manipulator im.

Matrix should be a list, tuple, or  that is 20 or 25 elements long. If the object has 25 elements, then elements past the 20th are ignored.

When the four components of the source color are R, G, B, and A, which range from 0.0 to 1.0; the four components of the transformed color are R', G', B', and A', with the same range; and the elements of the matrix are named:

\[ a, b, c, d, e,
  f, g, h, i, j,
  k, l, m, n, o,
  p, q, r, s, t \]

the transformed colors can be computed with the formula:

R' = (a \* R) + (b \* G) + (c \* B) + (d \* A) + e
G' = (f \* R) + (g \* G) + (h \* B) + (i \* A) + j
B' = (k \* R) + (l \* G) + (m \* B) + (n \* A) + o
A' = (p \* R) + (q \* G) + (r \* B) + (s \* A) + t

The components of the transformed color are clamped to the range \[0.0, 1.0\].

Deprecated since version 7.4.0: Use `Transform(im, matrixcolor=matrix, **properties)`. See  and .

_class_ im.matrix

Constructs an im.matrix object from matrix. im.matrix objects support The operations supported are matrix multiplication, scalar multiplication, element-wise addition, and element-wise subtraction. These operations are invoked using the standard mathematical operators (\*, \*, +, and -, respectively). If two im.matrix objects are multiplied, matrix multiplication is performed, otherwise scalar multiplication is used.

matrix is a 20 or 25 element list or tuple. If it is 20 elements long, it is padded with (0, 0, 0, 0, 1) to make a 5x5 matrix, suitable for multiplication.

Deprecated since version 7.4.0: Use .

im.matrix.brightness(_b_)

Returns an im.matrix that alters the brightness of an image.

b

The amount of change in image brightness. This should be a number between -1 and 1, with -1 the darkest possible image and 1 the brightest.

Deprecated since version 7.4.0: Use  with the  transform property.

im.matrix.colorize(_black\_color_, _white\_color_)

Returns an im.matrix that colorizes a black and white image. black\_color and white\_color are Ren'Py style colors, so they may be specified as strings or tuples of (0-255) color values.

\# This makes black colors red, and white colors blue.
image logo colored \= im.MatrixColor(
    "bwlogo.png",
    im.matrix.colorize("#f00", "#00f"))

Deprecated since version 7.4.0: Use  with the  transform property.

im.matrix.contrast(_c_)

Returns an im.matrix that alters the contrast of an image. c should be greater than 0.0, with values between 0.0 and 1.0 decreasing contrast, and values greater than 1.0 increasing contrast.

Deprecated since version 7.4.0: Use  with the  transform property.

im.matrix.desaturate()

Returns an im.matrix that desaturates the image (makes it grayscale). This is equivalent to calling im.matrix.saturation(0).

Deprecated since version 7.4.0: Use  with the  transform property.

im.matrix.hue(_h_)

Returns an im.matrix that rotates the hue by h degrees, while preserving luminosity.

Deprecated since version 7.4.0: Use  with the  transform property.

im.matrix.identity()

Returns an identity matrix, one that does not change color or alpha.

Deprecated since version 7.4.0: Use  with the  transform property.

im.matrix.invert()

Returns an im.matrix that inverts the red, green, and blue channels of the image without changing the alpha channel.

Deprecated since version 7.4.0: Use  with the  transform property.

im.matrix.opacity(_o_)

Returns an im.matrix that alters the opacity of an image. An o of 0.0 is fully transparent, while 1.0 is fully opaque.

Deprecated since version 7.4.0: Use  with the  transform property.

im.matrix.saturation(_level_, _desat\=(0.2126, 0.7152, 0.0722)_)

Returns an im.matrix that alters the saturation of an image. The alpha channel is untouched.

level

The amount of saturation in the resulting image. 1.0 is the unaltered image, while 0.0 is grayscale.

desat

This is a 3-element tuple that controls how much of the red, green, and blue channels will be placed into all three channels of a fully desaturated image. The default is based on the constants used for the luminance channel of an NTSC television signal. Since the human eye is mostly sensitive to green, more of the green channel is kept then the other two channels.

Deprecated since version 7.4.0: Use  with the  transform property.

im.matrix.tint(_r_, _g_, _b_)

Returns an im.matrix that tints an image, without changing the alpha channel. r, g, and b should be numbers between 0 and 1, and control what fraction of the given channel is placed into the final image. (For example, if r is .5, and the value of the red channel is 100, the transformed color will have a red value of 50.)

Deprecated since version 7.4.0: Use  with the  transform property.

- - -

Built with  using a  provided by .

jQuery(function () { SphinxRtdTheme.Navigation.enable(false); });