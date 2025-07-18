# Layered Images

When a sprite-set gets to a certain level of complexity, defining every possible combination may become unwieldy. For example, a character with 4 outfits, 4 hairstyles, and 6 emotions already has 96 possible combinations. Creating static images for each possible combination would consume a lot of disk space and programmer time.

To address this use case, Ren'Py introduces a way of defining an image consisting of multiple sprites, organized in layers. (For the purpose of this, consider layers to be the layers in a paint program like Photoshop or the GIMP, and not the layers used elsewhere in Ren'Py.) Elements of these layers can be selected by  provided to the image, or by conditions that are evaluated at runtime.

These images can be declared using the `layeredimage` statement, using a specific language. The  object is its Python alternative, it's not a  but can be assigned to an image statement and used like one.

The bottom of this page contains advice and examples of use.

## Defining Layered Images

The language used to define layered images consists of only a few statements, to introduce the layers. Here is an example which, while not making much practical sense, is technically correct and outlines the layeredimage syntax:

layeredimage augustina:
    zoom 1.4
    at recolor\_transform

    always:
        "augustina\_base"

    attribute base2 default

    group outfit:
        attribute dress default:
            "augustina\_dress"
        attribute uniform

    group face auto:
        pos (100, 100)
        attribute neutral default

label start:
    show augustina \# displaying dress and neutral
    aug "I like this dress."

    show augustina happy \# auto-defined in the auto group
    aug "But what I like even more..."

    show augustina uniform \-happy \# uniform replaces dress, neutral replaces happy
    aug "Is this uniform !"

### Layeredimage

The `layeredimage` statements opens the show. The statement is part of the Ren'Py script language, and runs at . Like the , it takes an image name and opens a block, although what's in the block differs greatly. The image name may contain spaces, just like any other image name in Ren'Py.

Inside the block will fit the statements described further down, as well as the following optional properties.

image\_format

When a given image is a string, and this is supplied, the image name is interpolated into image\_format to make an image file. For example, "sprites/eileen/{image}.png" will look for the image in a subdirectory of sprites. (This is not used by auto groups, which look for defined images and not for image files.)

format\_function

A function that is used instead of  to format the image information into a displayable, during the image definition at init time.

attribute\_function

A function or callable that is used to tweak what attributes end up being displayed. It is called with a set of attributes supplied to the image, and should return the set of attributes that should be used to select layers. It can be used to express complex dependencies between attributes, or to select attributes at random. See  for more information about when and how this is called.

at

A transform or list of transforms that are applied to the layered image.

If given, these are used to construct a transform that is applied to the displayable.

offer\_screen

If this is True, the layeredimage will place its children, and size its children with variable size, like it was given an area matching the whole screen of the game. If it is False, the said behaviors will be done while taking into account the available area, which for example will be smaller in an hbox containing other elements, and the display of the layeredimage will not be consistent every time it is shown.

If None, the default, falls back to , which defaults to True.

### Always

The `always` statement declares an image that is always shown inside the layeredimage, and which will not be attached to an attribute. It must be supplied a displayable, and can also take properties. Both can be placed on the same line or inside a block.

The `always` statement takes the following properties:

if\_all

A string or list of strings giving the names of attributes. If this is given, this layer is only displayed if all of the named attributes are present.

if\_any

A string or list of strings giving the names of attributes. If this is given, this layer is only displayed if any of the named attributes are present.

if\_not

A string or list of strings giving the names of attributes. If this is given, this layer is only displayed if none of the named attributes are present.

If given, these are used to construct a transform that is applied to the displayable.

at

A transform or list of transforms that are applied to the provided displayable.

#### If

The `if` statement (or more fully the if-elif-else statement) allows you to supply one or more conditions that are evaluated at runtime. Each condition is associated with a displayable, with the first true condition being the one that is shown. If no condition is true, the `else` layer is shown if given.

A more complete example of an `if` statement might look like:

if glasses \== "evil":
    "augustina\_glasses\_evil"
elif glasses \== "normal":
    "augustina\_glasses"
elif glasses \== "funky":
    "augustina\_glasses\_clown"
else:
    "augustina\_nose\_mark"

Each clause must be given a displayable. It can also be given these properties:

if\_all

A string or list of strings giving the names of attributes. If this is given, this condition is only considered if all of the named attributes are present.

if\_any

A string or list of strings giving the names of attributes. If this is given, this condition is only considered if any of the named attributes are present.

if\_not

A string or list of strings giving the names of attributes. If this is given, this condition is only considered if none of the named attributes are present.

If present, these are used to construct a transform that is applied to the displayable.

at

A transform or list of transforms that are applied to the displayable.

The `if` statement is transformed to a  when the `layeredimage` statement runs.

layeredimage.predict\_all \= None

Sets the value of predict\_all for the ConditionSwitches produced by layeredimages' `if` statements.

When `predict_all` is not true, changing the condition of the if statement should be avoided while the layered image is shown or about to be shown, as it would lead to an unpredicted image load. It's intended for use for character customization options that don't change often.

### Attribute

The `attribute` statement adds a displayable that is part of the resulting image when the given attribute is used to display it. For example, using the previous example, calling `show augustina dress` will cause the "augustina\_dress" to be shown as part of the "augustina" image.

An `attribute` clause takes an attribute name, which is one word. It can also take two keywords. The `default` keyword indicates that the attribute should be present by default unless an attribute in the same group is called. The `null` keyword prevents this clause from getting attached a displayable, which can be useful for bookkeeping and to build conditional display conditions using if\_all, if\_any, if\_not, attribute\_function,  or `config.default_attributes`.

The same attribute name can be used in multiple `attribute` clauses (and in auto-defined attributes as part of `auto` groups, more about that later), with all the corresponding displayables being shown at the same time (the if\_all, if\_any, and if\_not properties can tweak this).

If the displayable is not explicitly given, it will be computed from the name of the layeredimage, the group (if any), the group's variant (if any), and the attribute. See the  section for more details.

The attribute statement takes the following properties:

if\_all

A string or list of strings giving the names of attributes. If this is present, this layer is only displayed if all of the named attributes are present.

if\_any

A string or list of strings giving the names of attributes. If this is present, this layer is only displayed if any of the named attributes are present.

if\_not

A string or list of strings giving the names of attributes. If this is present, this layer is only displayed if none of the named attributes are present.

If present, these are used to construct a transform that is applied to the layer.

at

A transform or list of transforms that are applied to the layer.

The if\_\* clauses' test is based upon the list of attributes of the resulting image, as explained , but it **does not change** that list.

layeredimage eileen:
    attribute a
    attribute b default if\_not "a"
    attribute c default if\_not "b"

In this example, the `b` and `c` attributes are _always_ part of the attributes list (because of their `default` clause). When calling `show eileen a`, the `a` attribute will be displayed as requested, and the `b` attribute will not, due to its `if_not` property. But even if not displayed, the `b` attribute will still be part of the attributes list, which means the `c` attribute will still not display.

### Group

The `group` statement groups attributes together, making them mutually exclusive. Unless the group is `multiple`, when attributes a and b are in the same group, it is an error to include both of the attributes at the same time, with `show eileen a b` for example. In the same example, calling attribute a will hide attribute b, and vice versa. However, note that it's fine for several `attribute` clauses to be passed the same name, _even within the same group_. In that case, they will be considered as one attribute containing several sprites - more about that at the end of this section.

The `group` statement takes a name. The name isn't used for very much, except to generate the default names of attributes inside the group. That is not the case for `multiple` groups in which the name doesn't have any use or impact.

The name may be followed by the `auto` keyword. If it's present, after any attributes in the group have been declared, Ren'Py will scan its list of images for those that match the group's pattern (see ), with the specificity that in that case, a multiple group's name _is_ part if the pattern, and that the `format_function` passed to the layeredimage is ignored. Any images that are found, except those corresponding to explicitly declared attributes, are then added to the group as if declared using the `attribute` statement inside the group's block. See the  section for a practical demo.

This can be followed by the `multiple` keyword. If present, no incompatibility is applied to the attributes declared inside the block. This is useful to have a group auto-define multiple attributes that are not exclusive, or to apply the same properties to a set of attributes at once. This conflicts with the `default` keyword being given to one of the attributes. Note that `multiple` groups are very different from other, normal groups, and that most of what's true about groups doesn't apply to them.

After these optional keywords, properties can then be declared on the first line of the group, and it can take a block containing properties and attributes.

The group statement takes the properties `attribute` does - such as `if_any`, `at` and so on. Properties supplied to the group are passed to the attributes inside the group, unless overridden by the same property of the attribute itself. In addition, there are two properties which are specific to groups:

variant

If given, this should be a string. If present, it adds an element that becomes part of automatically-generated image names, and of the pattern used to search for images when automatically defining attributes in `auto` groups.

prefix

If given, this is a prefix that is concatenated using an underscore with the manually or automatically defined attribute names. So if prefix is "leftarm", and the attribute name "hip" is encountered, `show eileen leftarm_hip` will display it.

An attribute may also be part of several groups, in which case the attribute is incompatible with every other attribute in every group it's part of. This can be useful for example for a dress attribute, to make it hide both any top and any pants that may be showing when it gets displayed:

layeredimage eileen:
    attribute base default
    group bottom:
        attribute jeans default
        attribute dress null
    group top:
        attribute shirt default
        attribute dress

When several `group` blocks with the same name are defined in the same layeredimage, they are considered to be different parts of a single group. For example:

layeredimage eileen sitting:
    attribute base default
    group arms variant "behind":
        attribute on\_hips
        attribute on\_knees
        attribute mixed
    attribute table default
    group arms variant "infront":
        attribute on\_table default
        attribute holding\_margarita
        attribute mixed

In this example, `eileen_sitting_arms_behind_mixed.png` will contain her left arm behind the table, and `eileen_sitting_arms_infront_mixed.png` will contain her right arm on the table. When calling `show eileen sitting mixed`, the two images will be shown at the same time, respectively behind and in front of the table. In this example, the on\_hips attribute is incompatible with the on\_table attribute, because even though they are not declared in the same block, they are both in the same group.

## Pattern and format function

The pattern, used to find images for attributes when they are not explicitly given one, consists of:

*   The name of the layeredimage, with spaces replaced with underscores.
    
*   The name of the group, if any and if the group is not `multiple`.
    
*   The name of the variant, if there is one.
    
*   The name of the attribute.
    

all combined with underscores. For example, if we have a layered image with the name "augustina work", and the group "eyes", this will match images that match the pattern augustina\_work\_eyes\_attribute. With a variant of blue, it would match the pattern augustina\_work\_eyes\_blue\_attribute. In the following example:

layeredimage augustina work:
    group eyes variant "blue":
        attribute closed

The attribute is linked to the image "augustina\_work\_eyes\_blue\_closed". That can resolve to an image file named `augustina_work_eyes_blue_closed.png`, but it can also be defined explicitly using the  for example.

If you want a `multiple` group's name to be included in the pattern, you can use the following syntax:

group addons multiple variant "addons"

All of the pattern behavior can be changed using a format\_function:  is the function used under the hood to implement the behavior described above. You can see what arguments it takes, in case you want to supply your own format\_function to replace it.

layeredimage.format\_function(_what_, _name_, _group_, _variant_, _attribute_, _image_, _image\_format_, _\*\*kwargs_)

This is called to format the information about an attribute or condition into a displayable. This can be replaced by a creator, but the new function should ignore unknown kwargs.

what

A string giving a description of the thing being formatted, which is used to create better error messages.

name

The name of the layeredimage.

group

The group of an attribute, None if not supplied or if it's part of a condition.

variant

The variant argument to the group, or None if it is not supplied.

attribute

The attribute itself.

image

Either a displayable or string.

image\_format

The image\_format argument of the LayeredImage.

If image is None, then name, group (if not None), variant (if not None), and attribute are combined with underscores to create image, which will then be a string.

If images is a string, and image\_format is not None, image is formatted into the string to get the final displayable.

So if name is "eileen", group is "expression", and attribute is "happy", image would be set to "eileen\_expression\_happy". If image\_format is "images/{image}.png", the final image Ren'Py finds is "images/eileen\_expression\_happy.png". But note that it would have found the same image without the format argument.

## Proxying Layered Images

Sometimes, it can be useful (and even necessary) to proxy a layered image, to use the same layered image in multiple places. One reason for this would be to have a transformed version of a given layeredimage, while another would be to use it as a side image.

The  object does this, taking one layered image and duplicating it somewhere else. For example:

image dupe \= LayeredImageProxy("augustina")

creates a duplicate of the image that can be displayed independently. This also takes a transform argument that makes it useful to position a side image, like this:

image side augustina \= LayeredImageProxy("augustina", Transform(crop\=(0, 0, 362, 362), xoffset\=-80))

See the difference:

image sepia\_augustina\_one \= Transform("augustina", matrixcolor\=SepiaMatrix())
image sepia\_augustina\_two \= LayeredImageProxy("augustina", Transform(matrixcolor\=SepiaMatrix()))

`sepia_augustina_one` will be a sepia version of the _original version_ of the "augustina" layeredimage, in other words what's shown when you don't provide it any attribute. On the contrary, `sepia_augustina_two` will take any attribute "augustina" does, and then apply the sepia effect onto the result. If you can do this:

show augustina happy eyes\_blue dress

then:

show sepia\_augustina\_one happy eyes\_blue dress
\# won't work, because Transform doesn't take attributes

show sepia\_augustina\_two happy eyes\_blue dress
\# will work, and show "augustina happy eyes\_blue dress" in sepia effect

_class_ LayeredImageProxy(_name_, _transform\=None_)

This is an image-like object that proxies attributes passed to it to another layered image.

name

A string giving the name of the layeredimage to proxy to.

transform

If given, a transform or list of transforms that are applied to the image after it has been proxied.

## Selecting attributes to display

Several factors influence what gets displayed following a given . To provide more clarity as to what happens in which order, this section showcases the life of a set of attributes, from the show statement to the on-screen display.

*   The `show` statement provides the initial set of attributes, following the image tag.
    
*   If a  function exists to match the image tag, it is called, and returns a potentially different set of attributes. If so, it replaces the former set, which is forgotten.
    
*   If a  function exists and if its trigger conditions are met, it is called and potentially adds attributes to the set.
    

The previous stages are not specific to layeredimages, because it is only after this stage that renpy determines which image or layeredimage will be called to display. For that reason, the given set of attributes must lead to one, and only one, defined image (or layeredimage, Live2D...), using the behavior described in the .

*   Then, the provided attributes are combined with the attributes defined in the layeredimage, discarding some previously shown attributes and conserving others. This is also the point when unrecognized attributes are detected and related errors are raised. If no such error is raised, the new attributes, along with those which were not discarded, will be recognized by renpy as the set of attributes associated with that image tag. This computing takes some of the incompatibility constraints into account, but not all. For instance incompatibilities due to attributes being in the same non-multiple group will trigger at this point in time, but the if\_any/if\_all/if\_not clauses will not. That's why an attribute called but negated by such a clause will be considered active by renpy, and will for example become visible without having to be called again, if at some point the condition of the if\_x clause is no longer fulfilled.
    
*   If an `attribute_function` has been provided to the layeredimage, it is called with the set of remaining attributes. It returns a potentially different set of attributes.
    
*   This set is once again confronted with the incompatibility constraints of the layeredimage, this time in full. That is the final stage, and remaining attributes are called into display.
    

## Advice

**Use underscores in image filenames.**

By default, Ren'Py's layered images use underscores to separate sections of image names. It might be tempting to use images with spaces between sections, but that could lead to problems later on.

Ren'Py has a rule that if you show an image with the exact name as one that's being shown, it's shown instead. This can bypass the layered image you defined and show the sprite directly on its own, which can lead to weird problems like a pair of eyes floating in space.

By having each sprite have a different tag from the main image, this is no longer a problem.

**Cropping layers isn't necessary.**

Ren'Py optimizes images by cropping them to the bounding box of the non-transparent pixels before loading them into RAM. As a result, assuming the images are being predicted properly, it generally won't improve performance or image size much to crop the images yourself.

**Layered images shouldn't use data that changes at runtime.**

Note that with the exception of the conditions in the `if` statement, all expressions written in a `layeredimage` block are evaluated at init time, when the layered image is first defined. This is not the case for ATL transforms for example, or for anything occurring in , `config.default_attributes` or `attribute_function`, but it is the case for `format_function` which is also only called at layeredimage definition.

**Choosing what syntax to use**

If you want a sprite to be always visible, use either the `always` clause or the `attribute x default` syntax. `always` will require you to provide the displayable explicitly (automatic attribution using the  will not be available), but `attribute` will spend the "x" attribute name which will always be active for that layeredimage.

If you want it to appear depending on the attributes being passed to the layeredimage at the moment of the `show` statement, for example `show eileen happy` instead of `show eileen jeans`, use the `attribute` statement, in or out of a `group` block (or implicitly defined in an `auto` group).

If you want it to appear depending on a python variable or condition, use the `if` statement.

If you want it to depend on both (for example for `show eileen ribbon` to show either a blue or red ribbon depending on a variable, but no ribbon appearing unless you ask for it with the `ribbon` attribute), declare all versions as attributes and use a dedicated  function.

## Examples

**Pattern and auto groups**

From the following files in the images/ directory (or one of its subfolders) and written code:

francis\_base.png
francis\_face\_neutral.png
francis\_face\_angry.png
francis\_face\_happy.png
francis\_face\_very\_happy.png
francis\_face annoyed.png
francis\_supersad.png

layeredimage francis:
    attribute base default
    group face auto
        attribute neutral default
    attribute supersad:
        Solid("#00c3", xysize\=(100, 100))

The `francis` layeredimage will declare the (defaulted) `base` attribute, and associate it the "francis\_base" (auto-defined) image using the  : the layeredimage name ("francis"), the group name (none here), the variant name (none here) and the attribute name ("base"), separated with underscores.

Then, in the `face` group, the explicit `neutral` attribute gets associated the "francis\_face\_neutral" image, following the same pattern but using "face" as the group name and "neutral" as the attribute name.

After all explicit attributes receive their images, `face` being an `auto` group, existing images (auto-defined or not) are scanned for a match with the pattern. Here, three are found : "francis\_face\_angry", "francis\_face\_happy" and "francis\_face\_very\_happy". They are associated with the `angry`, `happy` and `very_happy` attributes respectively, using the same pattern as before. No `annoyed` attribute is defined however, since the "francis\_face annoyed" image contains a space where the pattern expected an underscore.

Finally, the `supersad` attribute is declared, but since a displayable is explicitly provided, the pattern does not look for a matching image.

The "francis\_supersad" and "francis\_face annoyed" images get auto-defined from the filename as part of Ren'Py's ordinary , but these sprites don't find a match with any attribute or auto group, so they end up not being used in the `francis` layeredimage.

As you can see, using the pattern to associate images to attributes and using auto groups shrinks the code considerably. The same layeredimage would have taken 13 lines if everything was declared explicitly (try it!), and this syntax allows for geometric growth of the sprite set - adding any number of new faces wouldn't require any change to the code, for example.

**Dynamism in attributes**

Here is an example for defining attributes depending on variables (as mentioned in the Advice section):

layeredimage eileen:
    attribute base default
    group outfit auto
    group ribbon prefix "ribbon":
        attribute red
        attribute blue

default eileen\_ribbon\_color \= "red"

init python:
    def eileen\_adjuster(names):
        atts \= set(names\[1:\])
        if "ribbon" in atts:
            atts.remove("ribbon")
            atts.add("ribbon\_" + eileen\_ribbon\_color)
        return names\[0\], \*atts

define config.adjust\_attributes\["eileen"\] \= eileen\_adjuster
