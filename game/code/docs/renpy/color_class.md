# Color Class

Ren'Py has a Color class that can be used for converting from one color space to another, or performing various color theory operations. Colors are immutable, and can be used wherever a color tuple can be used.

Color tuples operate in one of three color spaces.

*   RGB - Red, Green, Blue
    
*   HLS - Hue, Lightness, Saturation
    
*   HSV - Hue, Saturation, Value
    

As an example of some of the calculations that can be performed, all of the following colors are bright green:

\# Standard Ren'Py Colors.
Color("#0f0")
Color("#00ff00")
Color((0, 255, 0, 255))

\# Convert from other color spaces.
Color(hls\=(.333, 0.5, 1.0))
Color(hsv\=(.333, 1.0, 1.0))

\# Turns red into green via a method that returns a new color.
Color("#f00").rotate\_hue(.333)

_class_ Color(_color\=None_, _hls\=None_, _hsv\=None_, _rgb\=None_, _alpha\=1.0_)

The Color class is used to represent and manipulate colors and convert between various color spaces. It also represents opacity in the form of an alpha.

When creating a Color, at most one of the color, hls, hsv, or rgb arguments should be supplied. (If all are None, None is returned.)

color

The color, in one of the standard formats Ren'Py understands. These are:

*   A Color object.
    
*   An (r, g, b) or (r, g, b, a) tuple, in which all the numbers are between 0 and 255.
    
*   A string giving a hexadecimal color, in the form "#rgb", "#rgba", "#rrggbb", or "#rrggbbaa".
    

hls

A color in the hue-lightness-saturation color space. This should be supplied a three-component tuple, where each component is between 0.0 and 1.0.

hsv

A color in the hue-saturation-value color space. This should be supplied a three-component tuple, where each component is between 0.0 and 1.0.

rgb

A color in the red-green-blue color space. This should be supplied a three-component tuple, where each component is between 0.0 and 1.0.

If the supplied color does not contain an alpha value, alpha is used. alpha must be between 0.0 and 1.0.

Color objects can be used as 4-component tuples, where the components are (red, green, blue, and alpha). When used as a tuple, the value of each component is between 0 and 255.

Color objects support the +, -, and \* operators, representing component-wise addition, subtraction, and multiplication. Some uses of these operators can cause the creation of colors with components that are not in the supported range. Such colors should not be passed to other parts of Ren'Py. (The normalize method can be called to return a new color with the components limited to the proper range.)

A Color object has the following properties:

hls

Returns the color as a tuple of three floating point numbers giving hue, lightness, and saturation. Each component ranges between 0.0 and 1.0.

hsv

Returns the color as a tuple of three floating point numbers giving hue, saturation, and value. Each component ranges between 0.0 and 1.0.

rgb

Returns the color as a tuple of three floating point numbers giving the red, green, and blue components. Each component ranges between 0.0 and 1.0.

rgba

Returns the color as a tuple of four floating point numbers giving the red, green, blue and alpha components as 0.0 to 1.0 values.

premultiplied

Returns the color as a tuple of four floating point numbers giving the red, green, blue and alpha components as 0.0 to 1.0 values, with the red, green, and blue components premultiplied by the alpha.

alpha

Returns the alpha (opacity) of this Color as a number between 0.0 and 1.0, where 0.0 is transparent and 1.0 is opaque.

hexcode

Returns a string containing a hex color code of the form #rrggbbaa or #rrggbb.

Color objects have the following methods. Since Colors are immutable, these methods always return a new Color object.

interpolate(_other_, _fraction_)

Interpolates between this Color and other in the RGB color space, returning a new Color as the result. If fraction is 0.0, the result is the same as this color, if 1.0, it is the same as other.

interpolate\_hls(_other_, _fraction_)

Interpolates between this Color and other in the HLS color space, returning a new Color as the result. If fraction is 0.0, the result is the same as this color, if 1.0, it is the same as other.

other may be a string, Color or an HLS tuple.

interpolate\_hsv(_other_, _fraction_)

Interpolates between this Color and other in the HSV color space, returning a new Color as the result. If fraction is 0.0, the result is the same as this color, if 1.0, it is the same as other.

other may be a string, Color or an HSV tuple.

multiply\_hls\_saturation(_saturation_)

Multiplies this color's saturation by saturation, and returns the result as a new Color. This is performed in the HLS color space.

multiply\_hsv\_saturation(_saturation_)

Multiplies this color's saturation by saturation, and returns the result as a new Color. This is performed in the HSV color space.

multiply\_value(_value_)

Multiples this color's value by value and returns the result as a new Color. This is performed in the HSV color space.

normalize()

Returns a normalized version of this Color where all components fall between 0 and 255.

opacity(_opacity_)

Multiplies the alpha channel of this color by opacity, and returns the new color.

replace\_hls\_saturation(_saturation_)

Replaces this color's saturation with saturation, and returns the result as a new Color. This is performed in the HLS color space.

replace\_hsv\_saturation(_saturation_)

Replace this color's saturation with saturation, and returns the result as a new Color. This is performed in the HSV color space.

replace\_hue(_hue_)

Replaces this color's hue with hue, which should be between 0.0 and 1.0. Returns the new Color.

replace\_lightness(_lightness_)

Replaces this color's lightness with lightness, and returns the result as a new Color. This is performed in the HLS color space.

replace\_opacity(_opacity_)

Replaces this color's alpha channel with opacity, and returns the result as a new Color.

replace\_value(_value_)

Replaces this color's value with value and returns the result as a new Color. This is performed in the HSV color space.

rotate\_hue(_rotation_)

Rotates this color's hue by rotation, and returns the new Color. rotation is a fraction of a full rotation (between 0.0 and 1.0). Divide by 360.0 to convert to degrees.

shade(_fraction_)

Creates a shade of this color by mixing it with black. fraction is the fraction of this color that is in the new color. If fraction is 1.0, the color is unchanged, if 0.0, black is returned.

The alpha channel is unchanged.

tint(_fraction_)

Creates a tint of this color by mixing it with white. fraction is the fraction of this color that is in the new color. If fraction is 1.0, the color is unchanged, if 0.0, white is returned.

The alpha channel is unchanged.
