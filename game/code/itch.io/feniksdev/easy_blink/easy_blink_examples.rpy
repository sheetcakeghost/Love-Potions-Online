################################################################################
##
## Easy Blinking for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com) v1.1
##
################################################################################
## This file contains an example declaration and demo label for the declaring
## blinking attributes using the EasyBlink class. You can jump to the label
## "test_blinks" to see the blinking in action e.g.
##
# jump test_blinks
##
## Explanatory comments have been added all throughout this file.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
## EXAMPLE 1
## This example shows how you can directly declare blinking attributes using
## the EasyBlink class. It's useful if you only want one or two blinking
## attributes, or if you aren't using a layered image (so you can't use
## the layered image format function in the extras file).
layeredimage agustina_not_auto:

    always "agustina_base"

    ## Note: You should set up the default values of EasyBlink at the top of
    ## easy_blink.rpy to be the values you use most often. Then you can omit
    ## a lot of repeated arguments from your declarations. These attributes
    ## assume the following defaults:
    ##   blink_framerate = 0.04
    ##   numbered = False
    ##   reverse = False
    ##   start_no_num = False
    ##   automatic_blink_frames = []
    group eyes:
        ## Instead of an image like "agustina_eyes_normal", you will use the
        ## EasyBlink class to declare the blinking attributes.
        ## See the top of easy_blink.rpy for explanations on each property.
        ## The only required parts are the path and img properties.
        ## These are used as follows:
        ##   path : The path where the eye images are found, so the image path
        ##          can be put together with path + img substitutions. It should
        ##          include the substitution {img} which will be replaced with
        ##          the image name. e.g. "characters/eileen/{img}.webp"
        ##          or an auto-declared one like "eileen_eyes_{img}"
        ##          If numbered=True, it should also include a {num} substitution
        ##          which will be replaced with the number of the image.
        ##          e.g. "characters/eileen/{img}{num}.webp"
        ##          or an auto-declared one like "eileen_eyes_{img}{num}"
        ##          If it doesn't include any {img} substitutions, then your
        ##          mid_blink_frames will need to be direct image paths too.
        ##   img : The name of the first frame of the animation/the open eye
        ##         image. It's substituted in as the value for {img} in the path.
        ##         e.g. "happy_e"
        ##         Not used if `path` does not have an {img} substitution.
        attribute normal default EasyBlink(
            path="agustina_eyes_{img}", img="normal",
            ## This will go normal->semi->closed->semi->normal
            ## The mid-eye frames are also substituted in for {img} in the path.
            ## So this finds "agustina_eyes_semi" and "agustina_eyes_closed"
            ## along with the open eye image, "agustina_eyes_normal"
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        attribute cry EasyBlink(
            path="agustina_eyes_{img}{num}", img="cry",
            ## These images use a numbering scheme, from 0-2
            ## agustina_eyes_cry0, agustina_eyes_cry1, agustina_eyes_cry2
            reverse=True, numbered=True,
        )
        attribute surprised EasyBlink(
            path="agustina_eyes_{img}", img="surprised",
            ## This attribute lacks the "semi" frame, so it goes from open
            ## to closed with no other in-between frames.
            mid_eye_frames=["closed"],
        )
        attribute surprised2 EasyBlink(
            ## The path can also be a direct image path with no {img}, in
            ## which case the mid_eye_frames should also be direct image paths.
            ## If you're using numbered frames, you still need to include
            ## the {num} substitution in the path, but the mid_eye_frames
            ## won't matter (since they aren't used for numbered animations).
            path="easy_blink/agustina_eyes_surprised.png",
            mid_eye_frames=["easy_blink/agustina_eyes_semi.png",
                "easy_blink/agustina_eyes_closed.png"],
            ## Note that you can also use image names declared with the `image`
            ## statement or through Ren'Py's auto image declaration rules e.g.
            # path="agustina_eyes_surprised",
            # mid_eye_frames=["agustina_eyes_semi", "agustina_eyes_closed"],
        )
        attribute side_eyes EasyBlink(
            path="agustina_eyes_{img}", img="side_eyes",
            ## This attribute gets an automatically generated mid-blink frame,
            ## since it's looking to the side. The open eye image has all
            ## transparency at the bottom trimmed away so that the eyes are
            ## at the bottom of the image. In this case it'll get squished
            ## down to 85% (0.85) of its usual height to provide an extra frame
            ## between "open" and "closed".
            automatic_blink_frames=[0.85],
            ## The "semi" frame is omitted because we're auto-generating it,
            ## above.
            mid_eye_frames=["closed"],
            ## We'll linger for a shorter time on the mid-blink frame and longer
            ## on the closed and open eye frames.
            blink_framerate=[0.04, 0.02, 0.04],
        )
        attribute semi EasyBlink(
            path="agustina_eyes_{img}", img="semi",
            ## The "semi" frame is omitted because the eye already
            ## is semi-closed.
            mid_eye_frames=["closed"],
        )

        ## This is just a regular, non-blinking attribute
        attribute closed "agustina_eyes_closed"


        attribute normal_dissolve EasyBlink(
            path="agustina_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
            ## This is the same as normal eyes, but with a dissolve transition
            ## between each frame. You can either provide just a transition,
            ## as seen here, or a list of transitions, in which case you need
            ## at least one transition for each frame (including a transition
            ## between the last and first frames when it loops).
            ## If reverse=True and you provide a list of transitions, the
            ## transitions will be reversed as well (e.g. so the transition
            ## between mid-to-closed is the same as the one for closed-to-mid),
            ## and you need one less than the number of frames.
            transitions=Dissolve(0.4),
            ## The transition always takes the full amount of time to play out,
            ## so 0.4 seconds dissolve from one frame to another, and then it
            ## waits on that frame for 0.1 seconds before starting to dissolve
            ## to the next.
            blink_framerate=0.1,
        )

        ## These two attributes show two different ways of declaring the same
        ## thing. This is an expression with a "startup animation", where the
        ## character's eyes go wide for a moment before they look to the side
        ## and loop blinking.
        attribute short_surprise EasyBlink(
            path="agustina_eyes_{img}", reverse=True,
            ## This declaration uses the special `sequence` argument instead
            ## of img, mid_eye_frames, blink_framerate, and transitions.
            ## It takes a list of tuples, each with the following format:
            ##   (img, <time>, <transition>)
            ## img : Required. The name of the image to use, provided in the
            ##       same format as mid_eye_frames.
            ## <time> : Optional. The amount of time to wait on this frame.
            ##          If omitted, it defaults to blink_framerate.
            ## <transition> : Optional. The transition to use when moving to
            ##                the next frame. If omitted, it defaults to None.
            sequence=[("normal", 0.25, Dissolve(0.1)),
                ("surprised", 0.5, Dissolve(0.3)), ("side_eyes", 0.2),
                ("side_eyes", 0.04), ([0.85], 0.03), ("closed", 0.04)],
                ## You might have noticed "side_eyes" in here twice - this is
                ## so the looped blinking doesn't have a long pause on the first
                ## frame, but we also want to linger on side_eyes for a moment
                ## after the surprised eyes.
                ## There's also a tuple that starts with [0.85] - this is
                ## interpreted as an automatic_blink_frames argument. It will
                ## use the eye image immediately before it (the side_eyes) at
                ## 85% of its usual height.

            ## Lastly, this says that the actual blink looping starts at frame
            ## 3, aka on ("side_eyes", 0.04) - remember that indices start at 0.
            loop_start_frame=3,
        )

        ## This declares the same thing as earlier, but through separate
        ## arguments. Both do the same thing, so it's up to you which format
        ## is easier to use.
        attribute short_surprise2 EasyBlink(
            path="agustina_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["surprised", "side_eyes", "side_eyes",
                [0.85], "closed"],
            blink_framerate=[0.25, 0.5, 0.2, 0.04, 0.03, 0.04],
            transitions=[Dissolve(0.1), Dissolve(0.3), None, None, None],
            loop_start_frame=3,
        )

## This is a short screen that shows how you can make a preference toggle
## to turn blinking on/off on a global basis.
screen toggle_blinking():
    textbutton "Turn blinking {}".format("off" if persistent.blinking_on else "on"):
        background "#000" text_color "#fff" text_hover_color "#bbb"
        align (0.5, 0.0)
        action ToggleField(persistent, "blinking_on")

label test_blinks():
    scene expression "#21212d"
    ## This screen has a button to toggle blinking on and off. It's for
    ## demonstration purposes; usually you'd have this in your settings screen.
    show screen toggle_blinking()
    show agustina_not_auto at truecenter:
        ysize int(config.screen_height*0.9) fit "contain"
    with dissolve
    "Blink test, normal expression."
    show agustina_not_auto cry with dict(master=Dissolve(5.0))
    "This is a long transition to show the blinking doesn't happen while transitioning."
    show agustina_not_auto surprised with dissolve
    "Blink test, surprised expression without a mid-blink frame."
    show agustina_not_auto surprised2 with dissolve
    "Blink test, surprised expression with another mid-blink frame."
    show agustina_not_auto side_eyes with dissolve
    "Blink test, side eyes expression with auto-generated mid-blink frame."
    show agustina_not_auto semi with dissolve
    "Semi-closed eyes, no mid-blink frames."
    show agustina_not_auto closed with dissolve
    "Closed eyes, no blinking."
    show agustina_not_auto normal_dissolve with dissolve
    "You can also use transitions between blink frames. This uses a dissolve for 0.4 seconds between each frame so you can see it."
    show agustina_not_auto short_surprise with dissolve
    "You can also have a \"startup animation\" before the blinking begins to loop."
    "In this case, we dissolve between a few frames of surprised eyes, and then begin looping the side_eyes."
    "If you roll back to the previous line, the animation also will not start over until you get to the line where it was first shown."
    show agustina_not_auto short_surprise2 with dissolve
    "There are multiple ways to declare more complicated animations with transitions and startup animations; this is a second method that does the same thing."
    ## Jump to the examples for the extra files, if present.
    if renpy.has_label("test_blinks_auto"):
        call test_blinks_auto()

    jump test_blinks
