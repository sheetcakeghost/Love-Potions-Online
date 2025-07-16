################################################################################
## Animations
################################################################################

# Slide in entrance randomizes whether it slides from the left or right. You can adjust this.
transform slidein_entrance():
    alpha 0.0
    choice:
        xoffset -50
    choice:
        xoffset 50
    easein 0.6 alpha 1.0 xoffset 0

# A smaller bounce entrance
transform bounce_entrance():
    alpha 0.0
    yoffset -20
    easein 0.3 alpha 1.0 yoffset 5
    easeout 0.2 yoffset 0

# A larger bounce entrance
transform big_bounce_entrance():
    alpha 0.0
    yoffset -30
    easein 0.3 alpha 1.0 yoffset 10
    easeout 0.2 yoffset -5
    easein 0.15 yoffset 5
    easeout 0.1 yoffset -2
    easein 0.1 yoffset 2
    easeout 0.1 yoffset 0

# Floats up from below.
transform float_entrance():
    alpha 0.0
    yoffset 20
    easein 0.5 alpha 1.0 yoffset 0
    ease 0.2 yoffset 5
    ease 0.2 yoffset 0

# A very exaggerated entrance. You can adjust the zoom to make it subtler.
transform zoom_pop_entrance():
    alpha 0.0 zoom 0.5
    easein 0.4 alpha 1.0 zoom 1.1
    easeout 0.2 zoom 1.0

# Similar to the bounce entrances, but drops further
transform drop_entrance():
    alpha 0.0 yoffset -100
    easein 0.4 alpha 1.0 yoffset 10
    easeout 0.3 yoffset -5
    ease 0.2 yoffset 0


