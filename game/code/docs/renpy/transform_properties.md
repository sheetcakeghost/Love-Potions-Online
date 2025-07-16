# Transform Properties

Transform properties are used by  to influence how a displayable is drawn. They are usually set using  or the  class.

## List of Transform Properties

The following transform properties exist.

When the type is given as a , its relative component is interpreted as a fraction of the size of the containing area (for ) or of the displayable (for ).

Note that not all properties are independent. For example,  and  both update some of the same underlying data. In a `parallel` statement, not more than one block should adjust properties sharing the same data. The angle and radius properties set both horizontal and vertical positions.

### Positioning

pos

Type:

(position, position)

Default:

(0, 0)

The position, relative to the top-left corner of the containing area.

xpos

Type:

position

Default:

0

The horizontal position, relative to the left side of the containing area.

ypos

Type:

position

Default:

0

The vertical position, relative to the top of the containing area.

anchor

Type:

(position, position)

Default:

(0, 0)

The anchor position, relative to the top-left corner of the displayable.

xanchor

Type:

position

Default:

0

The horizontal anchor position, relative to the left side of the displayable.

yanchor

Type:

position

Default:

0

The vertical anchor position, relative to the top of the displayable.

align

Type:

(float, float)

Default:

(0.0, 0.0)

Equivalent to setting pos and anchor to the same value.

xalign

Type:

float

Default:

0.0

Equivalent to setting xpos and xanchor to this value.

yalign

Type:

float

Default:

0.0

Equivalent to setting ypos and yanchor to this value.

offset

Type:

(absolute, absolute)

Default:

(0, 0)

The number of pixels the displayable is offset by in each direction. Positive values offset towards the bottom-right.

xoffset

Type:

absolute

Default:

0

The number of pixels the displayable is offset by in the horizontal direction. Positive values offset toward the right.

yoffset

Type:

absolute

Default:

0

The number of pixels the displayable is offset by in the vertical direction. Positive values offset toward the bottom.

xycenter

Type:

(position, position)

Default:

(0.0, 0.0)

Equivalent to setting pos to the value of this property, and anchor to (0.5, 0.5).

xcenter

Type:

position

Default:

0.0

Equivalent to setting xpos to the value of this property, and xanchor to 0.5.

ycenter

Type:

position

Default:

0.0

Equivalent to setting ypos to the value of this property, and yanchor to 0.5.

subpixel

Type:

boolean

Default:

False

If True, causes the child to be placed using subpixel positioning.

Subpixel positioning effects the colors (including transparency) that are drawn into pixels, but not which pixels are drawn. When subpixel positioning is used in combination with movement (the usual case), the image should have transparent borders in the directions it might be moved in, if those edges are visible on the screen.

For example, if a character sprite is being moved horizontally, it makes sense to have transparent borders on the left and right. These might not be necessary when panning over a background that extends outside the visible area, as the edges will not be seen.

### Rotation

rotate

Type:

float or None

Default:

None

If None, no rotation occurs. Otherwise, the image will be rotated by this many degrees clockwise. Rotating the displayable causes it to be resized, according to the setting of rotate\_pad, below. This can cause positioning to change if xanchor and yanchor are not 0.5.

rotate\_pad

Type:

boolean

Default:

True

If True, then a rotated displayable is padded such that the width and height are equal to the hypotenuse of the original width and height. This ensures that the transform will not change size as its contents rotate. If False, the transform will be given the minimal size that contains the transformed displayable. This is more suited to fixed rotations.

transform\_anchor

Type:

boolean

Default:

False

If true, the anchor point is located on the cropped child, and is scaled and rotated as the child is transformed. Effectively, this makes the anchor the point that the child is rotated and scaled around.

### Zoom and Flip

zoom

Type:

float

Default:

1.0

This causes the displayable to be zoomed by the supplied factor.

xzoom

Type:

float

Default:

1.0

This causes the displayable to be horizontally zoomed by the supplied factor. A negative value causes the image to be flipped horizontally.

yzoom

Type:

float

Default:

1.0

This causes the displayable to be vertically zoomed by the supplied factor. A negative value causes the image to be flipped vertically.

### Pixel Effects

nearest

Type:

boolean

Default:

None

If True, the displayable and its children are drawn using nearest-neighbor filtering. If False, the displayable and its children are drawn using bilinear filtering. If None, this is inherited from the parent, or , which defaults to False.

alpha

Type:

float

Default:

1.0

This controls the opacity of the displayable.

The alpha transform is applied to each image comprising the child of the transform independently. This can lead to unexpected results when the children overlap, such as seeing a character through clothing. The  displayable can help with these problems.

additive

Type:

float

Default:

0.0

This controls how much additive blending Ren'Py performs. When 1.0, Ren'Py draws using the ADD operator. When 0.0, Ren'Py draws using the OVER operator.

Additive blending is performed on each child of the transform independently.

Fully additive blending doesn't alter the alpha channel of the destination, and additive images may not be visible if they're not drawn directly onto an opaque surface. (Complex operations, like viewport, , , and certain transitions may cause problems with additive blending.)

matrixcolor

Type:

None or Matrix or MatrixColor

Default:

None

If not None, the value of this property is used to recolor everything that children of this transform draw. Interpolation is only supported when MatrixColors are used, and the MatrixColors are structurally similar. See  for more information.

blur

Type:

None or float

Default:

None

This blurs the child of this transform by blur pixels, up to the border of the displayable. The precise details of the blurring may change between Ren'Py versions, and the blurring may exhibit artifacts, especially when the image being blurred is changing.

### Polar Positioning

around

Type:

(position, position)

Default:

(0.0, 0.0)

This specifies the starting point, relative to the upper-left corner of the containing area, from where the polar vector (computed from  and ) will be drawn. The sum of the two gives the resulting .

angle

Type:

float

This gives the angle component of a position specified in polar coordinates. This is measured in degrees, with 0 being to the top of the screen, and 90 being to the right.

Ren'Py clamps this angle to between 0 and 360 degrees, including 0 but not 360. If a value is set outside this range, it will be set to the equivalent angle in this range before being used. (Setting this to -10 is the equivalent of setting it to 350.)

radius

Type:

position

The radius component of the position given in polar coordinates.

If a float, this will be scaled to the smaller of the width and height available to the transform.

### Polar Positioning of the Anchor

Note

While using polar coordinates to position the anchor is possible, it's often more convenient to simply set  to (0.5, 0.5), and position the center of your displayable.

anchoraround

Type:

(position, position)

This specifies the starting point, relative to the upper-left corner of the displayable, from where the polar vector (computed from  and ) will be drawn. The sum of the two gives the resulting .

anchorangle

Type:

(float)

The angle component of the polar coordinates of the anchor. This is specified in degrees, with 0 being to the top and 90 being to the right.

Ren'Py clamps this angle to between 0 and 360 degrees, including 0 but not 360. If a value is set outside this range, it will be set to the equivalent angle in this range before being used. (Setting this to -10 is the equivalent of setting it to 350.)

anchorradius

Type:

(position)

The radius component of the polar coordinates of the anchor.

If a float, it is scaled horizontally and vertically to the size and shape of the displayable: if the height is not equal to the width, a radius that is not strictly absolute will result in elliptical motion when varying the anchorangle. For that reason, it is recommended to only pass `int` or  values to this property.

### Cropping and Resizing

crop

Type:

None or (position, position, position, position)

Default:

None

If not None, causes the displayable to be cropped to the given box. The box is specified as a tuple of (x, y, width, height), with x and y being the coordinates of the box's top-left corner relative to the top-left corner of the child. All values can expand outside of the bounds of the original image, with the area outside being transparent, though width and height must be positive.

If corners and crop are given, crop takes priority over corners.

corner1

Type:

None or (position, position)

Default:

None

If not None, gives the upper-left corner of the crop box. The values can expand outside of the bounds of the original image. Crop takes priority over corners.

corner2

Type:

None or (position, position)

Default:

None

If not None, gives the lower-right corner of the crop box. The values can expand outside of the bounds of the original image, but they should not be inferior to . Crop takes priority over corners.

xysize

Type:

None or (position, position)

Default:

None

If not None, causes the displayable to be scaled to the given size. This is equivalent to setting the  and  properties to the first and second components.

This is affected by the  property.

xsize

Type:

None or position

Default:

None

If not None, causes the displayable to be scaled to the given width.

This is affected by the  property.

ysize

Type:

None or position

Default:

None

If not None, causes the displayable to be scaled to the given height.

This is affected by the  property.

fit

Type:

None or string

Default:

None

Causes the displayable to be sized according to the table below. In the context of the table below, the "dimensions" are:

*   If both  and  are not None, both sizes are used as the dimensions.
    
*   If only one of those properties is not None, it is used as the sole dimension.
    
*   Otherwise, if fit is not None the area that the Transform is contained in is used as the dimensions.
    

If fit, xsize, and ysize are all None, this property does not apply.

 
| Value | Description |
| --- | --- |
| `contain` | As large as possible, without exceeding any dimensions. Maintains aspect ratio. |
| `cover` | As small as possible, while matching or exceeding all dimensions. Maintains aspect ratio. |
| None or `fill` | Stretches/squashes displayable to exactly match dimensions. |
| `scale-down` | As for `contain`, but will never increase the size of the displayable. |
| `scale-up` | As for `cover`, but will never decrease the size of the displayable. |

### Panning and Tiling

xpan

Type:

None or float

Default:

None

If not None, this interpreted as an angle that is used to pan horizontally across a 360 degree panoramic image. The center of the image is used as the zero angle, while the left and right edges are -180 and 180 degrees, respectively.

ypan

Type:

None or float

Default:

None

If not None, this interpreted as an angle that is used to pan vertically across a 360 degree panoramic image. The center of the image is used as the zero angle, while the top and bottom edges are -180 and 180 degrees, respectively.

xtile

Type:

int

Default:

1

The number of times to tile the image horizontally.

ytile

Type:

int

Default:

1

The number of times to tile the image vertically.

### Transitions

See .

delay

Type:

float

Default:

0.0

If this transform is being used as a transition, then this is the duration of the transition. See .

events

Type:

boolean

Default:

True

If True, events are passed to the child of this transform. If False, events are blocked. (This can be used in ATL transitions to prevent events from reaching the old\_widget.)

### Other

fps

Type:

float or None

Default:

None

If not None, this alters time inside the transform so that it is discrete. For example, if a transform has an fps of 10, then times inside the transform will be rounded down to the nearest multiple of 0.1. This can be used to simulate a lower frame rate.

show\_cancels\_hide

Type:

boolean

Default:

True

Normally, when a displayable or screen with the same tag or name as one that is hiding is shown, the hiding displayable or screen is removed, cancelling the hide transform. If this property is False in the hide transform, this cancellation will not occur, and the hide transform will proceed to completion.

There are also several sets of transform properties that are documented elsewhere:

3D Stage properties:

, , , , , , , , , 

Model-based rendering properties:

, , , 

GL Properties:

The .

Uniforms:

Properties beginning with `u_` are uniforms that can be used by .

## Property Order

Transform properties are applied in the following order:

1.  fps
    
2.  mesh, blur
    
3.  tile
    
4.  pan
    
5.  crop, corner1, corner2
    
6.  xysize, size, maxsize
    
7.  zoom, xzoom, yzoom
    
8.  point\_to
    
9.  orientation
    
10.  xrotate, yrotate, zrotate
    
11.  rotate
    
12.  zpos
    
13.  matrixtransform, matrixanchor
    
14.  zzoom
    
15.  perspective
    
16.  nearest, blend, alpha, additive, shader
    
17.  matrixcolor
    
18.  GL Properties, Uniforms
    
19.  position properties
    
20.  show\_cancels\_hide
    

## Deprecated Transform Properties

Warning

The following properties should not be used in modern games, as they may conflict with more recent features. They are only kept here for compatibility, along with the new way of achieving the same behavior.

alignaround

Type:

(float, float)

This sets , , and  to the same value.

crop\_relative

Type:

boolean

Default:

True

If False, float components of ,  and  are interpreted as an absolute number of pixels, instead of a fraction of the width and height of the source image.

If an absolute number of pixel is to be expressed,  instances should be provided to these properties instead of using the crop\_relative property. If necessary, values of dubious type can be wrapped in the  callable.

size

Type:

None or (int, int)

Default:

None

This is an older version of  interpreting floating-point values as an absolute number of pixels.

maxsize

Type:

None or (int, int)

Default:

None

If not None, causes the displayable to be scaled so that it fits within a box of this size, while preserving aspect ratio. (Note that this means that one of the dimensions may be smaller than the size of this box.)

To achieve the same result, give the values to the  property, and set the  property to the value "contain".
