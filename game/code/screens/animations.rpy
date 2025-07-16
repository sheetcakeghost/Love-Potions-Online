transform side_float():
    on show:
        xoffset 400
        easein .3 xoffset 0
    on hide:
        easeout .2 xoffset 400

transform button_fade():
    alpha .7
    on idle:
        alpha .7
    on hover:
        alpha 1
    on insensitive:
        alpha .3
    on selected_idle:
        alpha 1
    on selected_hover:
        alpha 1

transform return_slide():
    xoffset 50
    on idle:
        easein .3 xoffset 50
    on hover:
        easein .3 xoffset 0


transform wiggle():
    subpixel True

    on idle:
        linear 0.3 rotate 0

    on hover:
        linear .3 rotate 5
        linear .3 rotate 0
        linear .3 rotate -5
        linear .3 rotate 0
        repeat


transform wiggle_heavy():
    subpixel True

    on idle:
        parallel:
            linear .3 rotate 0
        parallel:
            linear .3 alpha 1.0

    on hover:
        parallel:
            linear .3 rotate 10
            linear .3 rotate 0
            linear .3 rotate -10
            linear .3 rotate 0
            repeat
        parallel:
            linear .3 alpha 1.0

    on insensitive:
        rotate 0
        alpha .5

transform slot_hover:
    alpha 0.0

    on idle:
        linear .3 alpha 0.0
    on hover:
        linear .3 alpha .7

transform slot_hover_text:
    alpha 0.0

    on idle:
        linear .3 alpha 0.0
    on hover:
        linear .3 alpha 1.0

transform page_wiggle_heavy():
    subpixel True

    on idle:
        linear .3 rotate 0

    on hover:
        linear .2 rotate 10
        linear .2 rotate 0
        linear .2 rotate -10
        linear .2 rotate 0
        repeat
    on insensitive:
        rotate 0
        alpha .5
    on selected_idle:
        linear .2 rotate 10
        linear .2 rotate 0
        linear .2 rotate -10
        linear .2 rotate 0
        repeat
    on selected_hover:
        linear .2 rotate 10
        linear .2 rotate 0
        linear .2 rotate -10
        linear .2 rotate 0
        repeat