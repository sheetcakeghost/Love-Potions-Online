label testing:
menu optional_name:
    "Effects Testing":
        jump individual_effects_test
    "Character Testing":
        jump character_testing
    

label character_testing:
    scene bg room
    show ash at left
    show morgen at right
    morgen "Hello, Ash."
    ash "Hello, Morgan."
    morgen "How are you?"
    ash "I'm good, thanks."
    morgen "What are you doing?"
    ash "I'm just testing the character testing."
    morgen "What are you testing?"
    ash "I'm testing the character testing."
    morgen "What are you testing?"
    return