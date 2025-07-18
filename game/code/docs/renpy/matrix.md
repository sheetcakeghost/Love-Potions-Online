# Matrix

_class_ Matrix(_l_)

This represents a 4x4 matrix, that is used in various places in Ren'Py.

When used to transform coordinates, the 16 elements of this matrix are:

xdx, xdy, xdz, xdw,
ydx, ydy, ydz, ydw,
zdx, zdy, zdz, zdw,
wdx, wdy, wdz, wdw

where x' = xdx \* x + xdy \* y + xdz \* z + xdw \* w, where x is the original value of x and x' is the transformed value, and similarly for x, y, z, and w. This is usually applied to a position where w is 1, allowing any combination of translation, rotation, and scaling to be expressed in a single matrix.

When used to transform colors, the 16 elements of this matrix are:

rdr, rdg, rdb, rda,
gdr, gdg, gdg, gda,
bdr, bdg, bdb, bda,
adr, adg, adb, ada,

For the red, green, blue, and alpha channels.

Matrix objects can be multiplied using the Python multiplication operator, to generate a matrix that performs both operations. The order in which the matrixes appear can matter. Assuming v is a position or color being transformed:

(step2 \* step1) \* v

is equivalent to:

step2 \* (step1 \* v)

l

This can be a list of 4, 9, or 16 numbers that is used to introduce this matrix. If not the full 16, the top-left corner of the matrix is initialized, with zdz and wdw set to 1.0 if not given. For example:

Matrix(\[ 1, 2, 3, 4 \])

would result in the Matrix:

1.0, 2.0, 0.0, 0.0,
3.0, 4.0, 0.0, 0.0,
0.0, 0.0, 1.0, 0.0,
0.0, 0.0, 0.0, 1.0,

Matrix.identity()

Returns an identity matrix.

Matrix.offset(_x_, _y_, _z_)

Returns a matrix that offsets the vertex by a fixed amount.

Matrix.perspective(_w_, _h_, _n_, _p_, _f_)

Returns a matrix suitable for the perspective projection of an image in the Ren'Py coordinate system. This is a view into the a coordinate system where, where when z=0, (0, 0) corresponds to the top-left corner of the screen, and (w, h) corresponds to the bottom-right corner of the screen.

w, h

The width and height of the input plane, in pixels.

n

The distance of the near plane from the camera.

p

How far the z=0 plane is from the camera. This is also where one virtual pixel is one coordinate unit in x and y.

f

The distance of the far plane from the camera.

Matrix.rotate(_x_, _y_, _z_)

Returns a matrix that rotates the displayable around the origin.

x, y, z

The amount to rotate around the origin, in degrees.

The rotations are applied in order:

*   A clockwise rotation by x degrees in the Y/Z plane.
    
*   A clockwise rotation by y degrees in the Z/X plane.
    
*   A clockwise rotation by z degrees in the X/Y plane.
    

Matrix.scale(_x_, _y_, _z_)

Returns a matrix that scales the displayable.

x, y, z

The factor to scale each axis by.
