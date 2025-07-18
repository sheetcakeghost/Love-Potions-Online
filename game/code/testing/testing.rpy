label testing:
    menu optional_name:
        "FX Testing":
            jump fx_testing
        "Layered Background Testing":
            jump test_layered_backgrounds
        "General Testing":
            jump general_testing
        

    # Widget Sprite LayeredImage

    layeredimage pw:

        always:
            "images/CHA/pw/base.png"

        group emotes:

            attribute tears:
                "images/CHA/pw/acc/cry.png"

            attribute questionmark:
                "images/CHA/pw/acc/question.png"

            attribute sweatdrop:
                "images/CHA/pw/acc/sweat.png"

            attribute emoteclear:
                "images/CHA/pw/acc/blank.png"

        group eyes:

            attribute eyesneutral default:
                "images/CHA/pw/face/eyes/neutral.png"
                #default True

            attribute closed:
                "images/CHA/pw/face/eyes/close.png"

            attribute crying:
                "images/CHA/pw/face/eyes/cry.png"

            attribute crying:
                "images/CHA/pw/face/eyes/cry.png"

            attribute closedhappy:
                "images/CHA/pw/face/eyes/happy.png"

            attribute closedpain:
                "images/CHA/pw/face/eyes/pain.png"

    #    group eyebrows:

    #        attribute normal default:
    #            "augustina_eyebrows_normal"

    #        attribute oneup:
    #            "augustina_eyebrows_oneup"

        group mouth:

            #pos (100, 100)

            attribute mouthneutral default:
                "/images/CHA/pw/face/mouth/flat.png"

            attribute mouthloud:
                "/images/CHA/pw/face/mouth/loud.png"

        group spec:

            #pos (100, 100)

            attribute wat:
                "/images/CHA/pw/face/spec/wat.png"

            attribute yeah:
                "/images/CHA/pw/face/spec/yeah.png"

    layeredimage spw:

        always:
            "images/CHA/pw/sbase.png"

        group spec:

            attribute glitter:
                "images/CHA/pw/face/spec/glitter.png"

            attribute surprise:
                "images/CHA/pw/face/spec/surprise.png"

            attribute tableflip:
                "images/CHA/pw/face/spec/table.png"

    init:
        define pwn = "Pixie Widget"
        define dpw = "Pixie Widget"
        define pw = Character("[pwn]")
        define tpw = Character("[pwn]")
        define bpw = Character("[pwn]")




    label general_testing:
        scene bg matrix with dissolve
        "This is where the introduction to the game will be. Normally we'd have the intro playing right now, but you decided to test things instead."
        "I'm going to test the maximum amount of text that can fit in a box now by filling this with a lot of babble. I thought about just using the same sentence over and over again for this, but then I thought \"Nah, I bet I can string some unnecessary words together.\" Of course, this little test is more to help work out the spacing. I rarely ever put this much text on the same line."
        define testname1 = Character("Name Here")
        define testname2 = Character("The Honorable Name McHerengton the 3rd Esquire")
        define testname3 = Character("The Honorable Name McHerengton")
        define testname4 = Character("Name McHerengton")
        testname1 "And now we're going to test the name box."
        testname2 "Well that did it for a short name, but how about a long one?"
        testname3 "Let's try another one."
        testname3 "Still a little long, but not too badly. Let's try something more reasonably sized."
        testname4 "Like this one."
        testname4 "Yeah, see. This fits well enough."

        "{i}Let's see how the italics look{/i} next to some normal text. Maybe just {i}one{/i} word this time."
        "Okay, now let's test our choices. How about a riddle."
        menu:
            "You throw away the outside and cook the inside. Then you eat the outside and throw away the inside. What did you eat?"

            "An ear of corn.":
                $ answer = "corn"
                "Yep, that's it. Though, I prefer my corn already off the cob so it doesn't get stuck in my teeth as badly."
                jump end

            "A chicken.":
                $ answer = "chicken"
                "You got it. These are pretty easy when you can see the answers though, huh?"
                jump end

            "A candy bar!":
                $ answer = "chocolate"
                "Uh, I appreciate the enthusiasm, but no. ... Well, I guess if you include the wrapper? But even if you do include that, who cooks a candy bar? You, I guess."
                jump end
    label end:

        "Okay, now let's try getting a character in here."

        show spw glitter with dissolve:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        bpw "Hello!"
        hide spw
        show pw closedhappy mouthneutral with dissolve:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        bpw "Thank you for inviting me."
        "We're gonna use Pixie Widget to test all the things that require having a character on screen."
        bpw "I'm looking forward to it."
        "For now let's see if it can remember what your answer was to that riddle from before."
        show pw closedhappy mouthneutral sweatdrop with dissolve
        bpw "But I wasn't there to hear the riddle."
        "I don't think we need to worry about story consistency during this test, okay?"
        show pw eyesneutral mouthneutral emoteclear with dissolve
        bpw "Well, okay then. If you don't mind."
        if answer == "corn":
            bpw "I'm pretty sure they said corn. Then you complained about it getting stuck in your teeth."
        if answer == "chicken":
            bpw "They said chicken. Technically correct, if a little bit mean to the chicken."
        if answer == "chocolate":
            show pw closedhappy mouthneutral with dissolve
            bpw "They answered a candy bar! That's my favorite too!"
        show pw eyesneutral mouthneutral with dissolve
    #    "Good, that's that squared away then."
    #    "I'm gonna test nvl mode real quick."
    #    novel "This should be in a big ol' box that takes the whole screen. I can fill this with all kinds of text, but I don't know if I'll actually use this in the game proper. I just like covering my bases."
    #    novel "And if I keep going like this it'll keep adding to this screen."
    #    novel "See?"
    #    novel "Now give me a second while I try and fill this screen with as much text as I can."
    #    novel "I'm gonna cheat a little and use lorem ipsum. That's pretty standard for placeholder text."
    #    novel "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    #    novel "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
    #    novel "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    #    novel "You wanna know what \"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet consectetur adipisci velit\" means?"
    #    novel "Neither is there anyone who loves, pursues or desires pain itself because it is pain."
    #    novel "It's from Cicero's De finibus bonorum et malorum (On the Ends of Goods and Evils)."
    #    novel "That's pretty cool, isn't it?"
    #    novel "I think so."
    #    novel "I wonder why people use it as placeholder text?"
    #    novel "It was first used in the 1960s in advertisements for Letraset transfer sheets."
    #    novel "Why people keep using it I have no idea."
    #    novel "Oh no! This line is falling off of the frame! What will we do?! Wanna see a trick? I can make all this text disappear!"
    #    nvl clear
    #    novel "Disappear!"
    #    novel "I can make the whole window disappear too."
    #    "Boom!"
    #    "Okay, that's enough of that."
        "Now let's try and give the pixie widget a new name."
        $ pwn = renpy.input("Why don't you pick one?", default = 'Widdy')
        $ pwn = pwn.strip()
        if pwn == "":
            $ pwn="Widdy"
        show pw closedhappy mouthneutral with dissolve
        pw "I like that name! But then I'm programmed to."
        "Alright, now let's give your widget a personality. This is being implemented with If statements, and while I won't be using a \"pick their personality\" feature in the game, this does let me get the swing of the coding."

        menu:
            "Do we go with nice or naughty? Keep in mind that nice is already installed on [pwn]."
            "Nice":
                $ chose = "nice"
            "Naughty":
                $ chose = "naughty"

        if chose == "nice":
            "Yeah, that's the one I'd have gone with. Why mess with a classic, right? Plus I don't want my digital assistant getting uppity."

        if chose == "naughty":
            "You picked [chose] Really? Well it's your call. It's a bad one, but it's yours."

        show pw closedhappy mouthneutral with dissolve
        if chose == "naughty":
            tpw "Fuck you, fuck your mom, and fuck the horse you rode in on after your mom blew it."
            jump transitionskip
        if chose == "nice":
            pw "Phew, I'm glad I'm still me."
            jump transitionskip

    label transitiontesting:
        "Okay, let's test out some transitions. You up for it, [pwn]?"
        if chose == "nice":
            pw "Sure am!"
        if chose == "naughty":
            tpw "Shove your transitions up your gaping asshole!"
        "Awesome. You sure made the right choice on those personalities."
        "First let's try out the circle transition. This'll change the scene so it'll toss the widget out, but we'll bring it back with the transition."
        scene bg bluegrid with circeout
        "That's circeout. We'll recall [pwn] with circin."
        show pw closedhappy mouthneutral with circin:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "Next is the iris transition."
        scene bg bluegrid with irisout
        "That was irisout. Let's pull the widget back with irisin."
        show pw closedhappy mouthneutral with irisin:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "You doing okay, [pwn]?"
        if chose == "naughty":
            tpw "Eat a bag of dicks!"
            "Yep, this personality choice was a {i}great{/i} call. Not at all annoying."
        if chose == "nice":
            pw "Uhuh, thanks for asking!"

        "Okay then. Let's try out some of those teleporting transitions I worked up. We won't change the scene with these since they're meant to be a special effect."
        "You ready, [pw]?"
        if chose == "nice":
            pw "Sure am!"
            "Good, now let's get going."
        if chose == "naughty":
            tpw "I'd like to shove a blunt splintery pole up your ass!"
            "Yeeeeah. Let's just move on, shall we?"

        "First teleport out with teleout."
        hide pw with teleout
        "And then teleport in with telein."
        show pw closedhappy mouthneutral with telein:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "Working okay so far. Let's do the second teleport out with teleout2."
        hide pw with teleout2
        "And second with telein2."
        show pw closedhappy mouthneutral with telein2:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "Alright. Let's do the third one with teleout3."
        hide pw with teleout3
        "And bring it back with telein3."
        show pw closedhappy mouthneutral with telein3:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "teleout4."
        hide pw with teleout4
        "telein4."
        show pw closedhappy mouthneutral with telein4:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "teleout5."
        hide pw with teleout5
        "telein5."
        show pw closedhappy mouthneutral with telein5:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "teleout6."
        hide pw with teleout6
        "telein6."
        show pw closedhappy mouthneutral with telein6:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "teleout7."
        hide pw with teleout7
        "telein7."
        show pw closedhappy mouthneutral with telein7:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "teleout8."
        hide pw with teleout8
        "telein8."
        show pw closedhappy mouthneutral with telein8:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "teleout9."
        hide pw with teleout9
        "telein9."
        show pw closedhappy mouthneutral with telein9:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "teleout10."
        hide pw with teleout10
        "telein10."
        show pw closedhappy mouthneutral with telein10:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
            repeat
        "Now I want to try to make it rain."
        show rain with dissolve
        "Hmm, does this look okay? Maybe I'll adjust the image later. At least it works."
        hide rain with dissolve
        "How about this scanline effect?"
        show scanlines with dissolve
        "Not bad. It flickers and I can probably use some flickering effects later."
        hide scanlines with dissolve
        "Okay, that's all of them."
        if chose == "nice":
            pw "I liked them."
        if chose == "naughty":
            tpw "I thought they were shit."
        "Your programing isn't sophisticated enough for you to have a real opinion, [pwn]."
        if chose == "nice":
            pw "That's true."
        if chose == "naughty":
            tpw "Smoke a dried up horse cock stuffed with lye."
            jump testend


    label transitionskip:
        "Normally right now I'd test transitions, but I haven't made any for this game to test yet. They'll probably be magic
        based though."
        jump testend


    label testend:
        "Anyway, looks like we've got all the testing squared away for now. Might as well go back to the menu."
        "You ready to go?"
        hide pw
        show spw glitter with dissolve:
            xalign 0.5 yalign 0.5
            ease 2.0 yoffset 5
            ease 2.0 yoffset 0
        if chose == "nice":
            pw "Yep! Bye!"
        if chose == "naughty":
            tpw "See you later, cockwipes!"
        hide spw with dissolve
        "And back to the menu we go."
        return
