# label: ch_1_intro
# This script covers the complete introductory scene, from Morgan's arrival at the manor
# through her initial interactions with Ash, Ignatius, and Princess Pinkpaws.

label intro:
    scene bg manor exterior with dissolve
    #TODO: Add ambient sounds (wind, distant crows?)

    "[mcn] [mcl] stood at the front door staring at her hand."

    "It was balled into a fist, ready to knock, but her nerves held it back."

    mct "Is this a huge mistake?"

    "This thought bounced through her head, bullying any other thoughts into a silence that dared to change the topic."

    mct "Think this through, [mcn]. This is a creepy ass house in the middle of the woods."
    
    mct "You've never even met this Ash guy in person and you get this random invite to his spooky murder mansion to do what? Just talk about what's happening to Roan?"
    
    mct "{i}If{/i} anything is even happening."
    
    mct "That new girlfriend of his sucks and has him wrapped around her iced-up finger, but that doesn't mean she has some spell cast on him."
    
    mct "Ash is a crazy person and I'm being crazy just entertaining his accusations."
    
    "Even with that logic firmly planted in her mind, she didn't leave right away."
    
    "She didn't leave because there was a chance, even a slim one, that this was true."
    
    "It had started with an email she saw on Roan's laptop, left open by mistake. A shipping confirmation for Heather, from some sketchy-sounding Glamour shop called 'Foxglove Finery.' Weekly deliveries."
    
    "Her first instinct was to dig deeper. But 'Foxglove Finery' was a digital ghost. No website, no business registration, no digital footprint whatsoever. The sender's email was a dead end, routed through a server that no longer existed. It was an anomaly that defied every rule of the internet she knew."
    
    "Then there were the 'Glamour' posts... He used to post raid memes and blurry pictures of his cat. Now it was all flowery, purple prose captions about his 'luminous love' for Heather. It was like he was replaced by a bad romance novelist."
    
    "He started ghosting their regular 'Neph' sessions. Ditched the whole guild. For her."
    
    "Each piece was weird on its own, but together... together they almost painted the picture Ash described. A picture of someone being controlled."
    
    "This could be real, and Ash could be the only one able to help her save Roan."
    
    "Even if he was just an online friend until now."

    call screen personality_choice_screen with dissolve

    mct "Okay, pull yourself together and accept your fate of being every dumb white girl in a slasher film."

    "[mcn] finally knocked. Right before realizing there was a doorbell and intercom on the side of the door."

    # The door opens.
    show ash happy at center with dissolve
    
    a "There you are. The pizza's getting cold."

    "Ash's voice was the most familiar part about him. It had a casual but confident cadence that tended to make people want to confide in him."

    mc "{assertive}Yeah, um, sorry.{/assertive}{shy}I've just been standing out here waiting for someone in a mask to cut me in half with a machete.{/shy}"

    "{assertive}Ash smiled sympathetically.{/assertive}{shy}Ash laughed.{/shy}"

    show ash happy at left with ease
    # Ash moves to the side to let her in.

    a "{assertive}No need to apologize.{/assertive}{shy}They're way more likely to do that {i}inside{/i} the house.{/shy}"
    
    a "Come on in."

    "At his behest, [mcn] went inside."

    scene bg manor hallway with dissolve
    show ash neutral at left with moveinleft

    a "Welcome to our humble abode."

    "Ash gestured wide and spun around as he walked down the hallway."

    a "Pepperoni was your favorite, right? Or was that Roan's? Anyway, it doesn't matter, we got a variety."

    mc "You have a nice place."

    a "Nah, it's not mine, I'm just crashing."

    scene bg manor kitchen with dissolve
    show ash happy at left with moveinleft
    show ignatius neutral at right with moveinright

    a "And this is my roomie, Nate."

    i "Ignatius."

    menu:
        "Call him Nate.":
            $ set_use_nate_nickname(True)
            mc "Nice to meet you, Nate."
            show ash happy at left
            a "See? Much better."
            show ignatius angry at right
            i "I prefer Ignatius."
        "Call him Ignatius.":
            $ set_use_nate_nickname(False)
            mc "Nice to meet you, Ignatius."
            show ash worried at left
            a "Oh come on, lighten up."
            show ignatius happy at right
            i "Thank you for being respectful."
    show ash neutral at left with ease
    show ignatius neutral at right with ease
    
    i "Yes. Well. Greetings aside. Who are you and why are you in my home?"
    a "This is [mcn]. Remember? I told you about them."
    i "You didn't say they'd be coming here."
    a "This is the best place for them to be. It's where all the magic is."
    i "Right. Well... Miss? Mister? Mx?"
    a "Miss."
    mc "It's [mcn] [mcl]."
    i "Ms. [mcl], I understand that you're concerned about your friend, but we can't help you."
    show ash angry at left
    a "Hey, {i}I'm{/i} concerned too."
    i "And you barely know this person."
    a "And she barely knows me, and yet here she is. Trying to save her friend, and we are the only ones that can help her."
    i "Trust me."
    mc "Wait, why are you saying it like that? How are {i}you{/i} involved in this?"
    a "Are {i}we{/i}?"
    i "What do you mean {i}we{/i}?"
    show ash happy at left
    a "Come on Nate. Let's eat this delicious pizza I went all the way into town to get."
    
    menu:
        "Tch, fine, but you're explaining yourself after.":
            $ personality_trait = 0 # Assertive
            pass
        "I mean I wouldn't mind some explanation. You're being really cryptic.":
            $ personality_trait = 1 # Shy
            pass

    i "It's going to be a lot, and you should probably hear it on a full stomach."
    mct "I guess he's not wrong. I haven't eaten since this morning."
    mc "Okay."

    scene bg manor living room with fade
    show ash neutral at center with moveincenter
    show ignatius neutral at right with moveinright
    
    "After some quiet slices of pizza and clean up, the three migrated to a livingroom that looked like a set piece for a mystery novel."
    mc "You're really into RP, huh?"
    "[mcn]'s comment got a bright laugh out of Ash."
    show ash happy at center
    a "I mean, yeah, but that's not why the decor looks like this."
    a "All of Nate's stuff is just really old."
    i "Most of it is inherited."
    mc "Ah."
    mct "So this guy is old money. Got it."
    mc "Well, Ash? Are you going to explain yourself now?"
    a "I'm getting to it."
    show ignatius angry at right
    i "Well get to it faster, Ash."
    "Ash's laugh lit up the room again."
    show ash happy at center
    a "Okay, unbunch your britches."
    show ash angry at center
    a "So, you know how Roan has been devoted to that new girlfriend of his? So into her that he's basically an entirely different person."
    mc "Yes, but how do you know that? He's been dating her a year, and we met you three months ago on Neph and he basically stopped playing a week later."
    a "I might have been keeping up with Roan for a month and a half after he started dating Heather Rose Cromwell?"
    mct "Oh fuck. Okay, I'm basically alone in the woods with Roan's cyber stalker."
    mct "Or, hell, maybe a real stalker."
    "[mcn] felt cold, and was struck dumb with how in danger she might just be, and it was evident on her face."

    a "It's not as creepy as it sounds, I promise."
    mc "Shit, you're delusional. You saying it was magic should have been a huge red flag and I'm an idiot."
    mc "Hang on. Magic? Is that why you're roping me into this?"
    a "Well, I'm roping you in because I think it's {i}our{/i} magic."
    mc "Bullshit! I'd know if it was ours!"
    mct "Oh no. It's both of them. I'm in danger."
    "[mcn] started scanning the room to try to spot a clear exit."
    show ignatius worried at right
    i "Damn it, Ash, you spooked her!"
    show ash angry at center
    a "Hey! You invited a stranger to our house and told her that magic is why her friend is being gaslit by his girlfriend!"
    show ignatius angry at right
    i "I did, and she came! The magic explanation didn't shut her brain down and I believe that we're partly responsible for what happened to her friend!"
    
    "[mcn] saw an opening and bolted towards the door."
    
    show ignatius angry at right
    i "You're absolutely sure."
    show ash angry at center
    a "Yes!"
    show ignatius worried at right
    i "Miss, wait!"
    
    "[mcn] swung open the door and dashed down the hallway."
    "The two men didn't give a swift pursuit, and she found out it was because the front door was locked."
    
    a worried "Okay, miss. I know you feel like you're in a lot of danger, but you're not. If you would just calm down I can prove it."
    mc "Right..."
    mct "I'm still questioning if this was a good idea or not."
    a "We really are the best chance you have of helping Roan."
    a "I know I'm being pretty cryptic, but if I explain too much too fast it can actually hurt you."
    mc "I felt okay earlier. It was more disorienting than anything."
    a "Well let's not push our luck too much."
    mc "I appreciate the concern."
    a "Oh, you have your laptop, right?"
    mc "Yes, I brought it with me."
    a "Smart girl, let's get you set up with a room."
    mc "Thanks."
    mct "I had left unceremoniously."
    a "Don't mind Nate. He's a good guy but is cripplingly socially awkward. Homeschooled."
    "Ash led [mcn] through more of the house, and despite places that were really showing their age, like the occasional faded soggy wallpaper or cracking paint, it was very clean, orderly, and well kept."
    "The same could be said of the room [mcn] was brought to."
    "The room was decorated in rose patterns and gold accents. It felt way more posh than the other rooms she'd seen."
    a "She whistled to indicate this."
    a "Pretty nice, right? Nate's mom always did have the nicest room in the house."
    mc "She had... splendid taste, yeah."
    a "Yeah, and she's probably not haunting it."
    mc "Is that... a joke?"
    a "Sure."

    a "Plug it in by the bed. The other outlet is a bit fussy. I don't trust it."
    mc "Got it."
    "Ash stood there awkwardly for a moment before seeing himself out."
    "[mcn] stood there awkwardly because she left all her stuff in the car and would need to go out and get it."
    "When she stepped into the hall she was greeted by a tall poodle, holding one of her bags in its teeth, setting it down gently next to her other bags."
    "The dog looked at her with dark brown eyes that seemed entirely too intelligent."
    "[mcn] stepped over as the dog wagged at her and checked the ornate golden tag hanging off the loose set of pearls the dog wore instead of a collar."
    mct "Princess Pinkpaws."
    mc "Well hello there, Princess."
    p "Hello, miss." # 'p' is the character variable for Princess Pinkpaws
    "[mcn] paled and felt her stomach churn."
    p "Wow, you don't look so good."
    mc "Ah! You can talk!"
    p "Ah! You can hear me!"
    mc "How?"
    p "Why?!"
    a "What's going on?"
    mc "Talking dog."
    a "Oh shit, really?"
    p "Ash!"
    a "Sorry, sorry. This is just Nate's assistant and familiar. I guess showing you that spell jostled some filters out of your brain."
    mc "Is that good?"
    a "Sort of. It means we can expose you at a bit of a faster pace."
    p "I'm going to go tell master."
    a "Sure, Princess."
    "The dog trotted off."
    mc "Princess is a... cute dog."
    a "Yeah, and really chill for a poodle. They're a lot less neurotic when they can actually understand the concept of context."
    mc "That makes sense."
    "[mcn] found herself mentally bouncing back faster this time."
    a "Looks like Nate had her getting you your stuff. Is this all of it?"
    mc "It looks like it."
    a "Alright, cool. I'm gonna go check on... something. Make yourself at home. Bathroom's down the hall if you need it."
    "Ash gave her a small, reassuring smile before turning and disappearing back towards the living room, leaving her alone with the talking poodle and her luggage."
    mct "Right. Make myself at home in the possibly-haunted house of a talking dog's master. Totally normal."
    "With a sigh that carried the weight of the entire day, [mcn] picked up her bags and headed into the guest room, the heavy door clicking shut behind her."
    "She didn't bother unpacking much, just the essentials. The absurdity of it all was draining, and the plush-looking bed was calling her name."



    scene bg manor bedroom with fadeinblack 
    "[mcn] woke up wondering if she'd just had the most bizarre dream."
    "When Princess came in, pulling a tray cart with her teeth via a scarf tied to the handle, it sank in quietly that it hadn't been."
    p "Good morning, guest."
    "Princess greeted [mcn] with a thumping tail wag after she set."
    mc "Morning."
    p "Master made you some breakfast."
    mc "Pancakes?"
    p "Yes, ma'am."
    mc "They look good."
    "The breakfast on the cart looked like something you would get at a five star hotel as room service."
    mc "He must really know how to cook."
    p "He's a scientist, mostly."
    mc "Oh. I thought maybe he was a magician. I guess?"
    p "Well, yes and no. See, he's an alchemist by trade, and that requires a lot more science than it does magic."
    mc "Oh. Of course."
    p "Master is very talented."
    "Princess wagged harder and puffed up her wooly chest."
    p "If anyone can help Ash's friend it's master. Oh, I guess that's your friend too. That's why you're here."
    mc "I've definitely known Roan for a lot longer than Ash has."
    p "Not many people can say that about Ash. He's usually the one that's known someone the longest."
    p "How long have you known your friend?"
    mc "Since high school. So about fifteen years."
    p "That's a long time for a friendship."
    mc "He's definitely one of my oldest and closest friends."
    p "It must really hurt to be losing him to an enchantment."
    mc "It's hurt to be losing him in general, but I always knew it would one day. He'd get married, have kids, and then just have less and less free time."
    mc "But I could be more okay with that if he was with a woman that treated him well. This woman though, she's horrible. She doesn't respect him or his interests. She refuses to let him go anywhere by himself, hits him if she sees him talking to other women, she totally controls where he goes, what he does, she only likes him because she has a Korean fetish too, I'm sure of it."
    "[mcn] took a breath not realizing she'd said all of that as one long, heated, sentence."
    p "? You're really upset. Would you like to pet me? Or have me sit my head in your lap? I am a trained emotional support and service animal."
    mc "Thanks."
    "[mcn] reached out and pet the dog."
    
    mc "I still don't know if I fully believe it's magic that's responsible. I mean if all of it is like what he showed me, it's not subtle."
    p "Spell casting is pretty dramatic, but potions are very subtle."
    mc "Potions, huh? And he's an expert on those."
    p "Yes, master is very talented but he doesn't make potions that would do the things you're describing."
    mc "But he could? I mean, potions could, but they'd need to be really strong. I know that master always makes his really weak."
    mc "So that it can't be abused? Why even make them at all?"
    p "Because they can be fun! Master makes silly potions that only last an hour."
    mc "Silly potions, huh?"
    p "Sure! Like ones that change your sense of taste and smell or make you super smart or funny at a party. Novelty stuff."
    mc "Nothing that would turn you into a slave though."
    p "Oh no! Definitely nothing like that. That's so invasive and cruel! Not to mention illegal."

    mc "So then there are magical laws about it?"
    p "Of course! Magic is powerful, and people who seek it aren't always good. To protect innocents, magic is highly regulated."
    mc "So there really is just a whole secret magical society."
    p "It's not secret, but to know about it could cause mass hysteria and widespread madness."
    mc "It's that serious, huh?"
    p "Definitely. You're really lucky. Or related to a magical creature, but you smell really normal to me."
    mct "Not being totally human is an option? How many only part humans have I met?"
    "[mcn] could feel her heart start to pound as panic slowly started to drain blood from her face and chill her bones."
    p "Oh, you're getting a strange look in your eyes. Hang on."
    "Princess barked a few times, which caused [ig] to come rushing in."   
    "Ash was soon behind."
    show ignatius neutral at right
    i "Are you okay?"
    show ash neutral at center
    "[mcn] nodded and swallowed."
    mct "Okay. Okay. Just calm down [mcn]."
    mct "{emo}This is scary, but we don't need to panic now.{/emo}{log}Panicking now wouldn't help him. Especially not Roan.{/log}"


    # End of transcribed scene
    jump ch_1_end

# ============================================================================
# CHAPTER 1 END
# ============================================================================

label ch_1_end:
    # This label marks the end of Chapter 1
    # You can add any end-of-chapter logic here, such as:
    # - Saving the game
    # - Showing chapter completion screen
    # - Transitioning to the next chapter
    
    "Chapter 1 Complete"
    
    # Return to main menu or continue to next chapter
    return
