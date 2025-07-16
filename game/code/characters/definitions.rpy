## Character Definitions for Love Potions Online
## Based on the official GDD - these are the actual characters from the game

### Main Character (Player)
define mc = Character("[mcn] [mcl]", 
    color="#d4a8b0",  # Dusty Rose from GDD palette
    what_prefix='"',
    what_suffix='"',
    who_prefix='[',
    who_suffix=']')

### Key Characters (Love Interests)

## Ignatius "Nate" Thornwick - The Alchemist
define ignatius = Character("Ignatius",
    color="#c5b0d9",  # Wisteria from GDD palette
    what_prefix='"',
    what_suffix='"',
    image="ignatius")

define nate = Character("Nate",
    color="#c5b0d9",  # Wisteria from GDD palette
    what_prefix='"',
    what_suffix='"',
    image="ignatius")

## Ashketharon "Ash" Zephyrius Voidrender the Eternal - The Dragon
define ash = Character("Ash",
    color="#4d9fff",  # Dodger Blue from GDD palette
    what_prefix='"',
    what_suffix='"',
    image="ash")

### Supporting Characters

## Roan Song - The Victim (Best Friend)
define roan = Character("Roan",
    color="#b0c8bc",  # Ash Grey from GDD palette
    what_prefix='"',
    what_suffix='"',
    image="roan")

## Heather Rose Cromwell - The Antagonist
define heather = Character("Heather",
    color="#e74c3c",  # Red for antagonist
    what_prefix='"',
    what_suffix='"',
    image="heather")

## Obsidian Foxglove - The Hidden Antagonist
define obsidian = Character("Obsidian",
    color="#2a2a2a",  # Charcoal from GDD palette
    what_prefix='"',
    what_suffix='"',
    image="obsidian")

## Princess Pinkpaws - The Familiar
define pinkpaws = Character("Princess Pinkpaws",
    color="#f7f2e8",  # Eggshell from GDD palette
    what_prefix='"',
    what_suffix='"',
    image="pinkpaws")

### Layered Character Images
## Using the layered image system from images/cha/

# Ignatius/Nate layered images
layeredimage ignatius:
    always "images/cha/Nate/Base.PNG"
    
    group brows:
        attribute neutral default "images/cha/Nate/Brows/Neutral.PNG"
        attribute sad "images/cha/Nate/Brows/Sad.PNG"
        attribute worried "images/cha/Nate/Brows/Worried.PNG"
        attribute annoyed "images/cha/Nate/Brows/Annoyed.PNG"
        attribute angry "images/cha/Nate/Brows/Angry.PNG"
        attribute curious "images/cha/Nate/Brows/Curious.PNG"
        attribute raised "images/cha/Nate/Brows/Raised.PNG"
        attribute really "images/cha/Nate/Brows/Really.PNG"
        attribute questioning "images/cha/Nate/Brows/Questioning.PNG"
    
    group eyes:
        attribute open default "images/cha/Nate/Eyes/Open.PNG"
        attribute closed "images/cha/Nate/Eyes/Closed.PNG"
        attribute closed_happy "images/cha/Nate/Eyes/Closed Happy.PNG"
        attribute wide "images/cha/Nate/Eyes/Wide.PNG"
        attribute terrified "images/cha/Nate/Eyes/Terrified.PNG"
        attribute lidded "images/cha/Nate/Eyes/Lidded.PNG"
    
    group mouth:
        attribute flat default "images/cha/Nate/Mouth/Flat.PNG"
        attribute smile "images/cha/Nate/Mouth/Smile.PNG"
        attribute smile_teeth "images/cha/Nate/Mouth/Smile Teeth.PNG"
        attribute smile_open "images/cha/Nate/Mouth/Smile Open.PNG"
        attribute frown "images/cha/Nate/Mouth/Frown.PNG"
        attribute smirk "images/cha/Nate/Mouth/Smirk.PNG"
        attribute open "images/cha/Nate/Mouth/Open.PNG"
        attribute o "images/cha/Nate/Mouth/O.PNG"
        attribute shout "images/cha/Nate/Mouth/Shout.PNG"
        attribute yell "images/cha/Nate/Mouth/Yell.PNG"
        attribute hmph "images/cha/Nate/Mouth/Hmph.PNG"
        attribute grimace "images/cha/Nate/Mouth/Grimace.PNG"

# Ash layered images
layeredimage ash:
    always "images/cha/Ash/Base.PNG"
    
    group brows:
        attribute neutral default "images/cha/Ash/Brows/Neutral.PNG"
        attribute sad "images/cha/Ash/Brows/Sad.PNG"
        attribute worried "images/cha/Ash/Brows/Worried.PNG"
        attribute annoyed "images/cha/Ash/Brows/Annoyed.PNG"
        attribute angry "images/cha/Ash/Brows/Angry.PNG"
        attribute curious "images/cha/Ash/Brows/Curious.PNG"
        attribute raised "images/cha/Ash/Brows/Raised.PNG"
        attribute really "images/cha/Ash/Brows/Really.PNG"
        attribute questioning "images/cha/Ash/Brows/Questioning.PNG"
    
    group eyes:
        attribute open default "images/cha/Ash/Eyes/Open.PNG"
        attribute closed "images/cha/Ash/Eyes/Closed.PNG"
        attribute closed_happy "images/cha/Ash/Eyes/Closed Happy.PNG"
        attribute wide "images/cha/Ash/Eyes/Wide.PNG"
        attribute terrified "images/cha/Ash/Eyes/Terrified.PNG"
        attribute lidded "images/cha/Ash/Eyes/Lidded.PNG"
    
    group mouth:
        attribute flat default "images/cha/Ash/Mouth/Flat.PNG"
        attribute smile "images/cha/Ash/Mouth/Smile.PNG"
        attribute smile_teeth "images/cha/Ash/Mouth/Smile Teeth.PNG"
        attribute smile_open "images/cha/Ash/Mouth/Smile Open.PNG"
        attribute frown "images/cha/Ash/Mouth/Frown.PNG"
        attribute smirk "images/cha/Ash/Mouth/Smirk.PNG"
        attribute open "images/cha/Ash/Mouth/Open.PNG"
        attribute o "images/cha/Ash/Mouth/O.PNG"
        attribute shout "images/cha/Ash/Mouth/Shout.PNG"
        attribute yell "images/cha/Ash/Mouth/Yell.PNG"
        attribute hmph "images/cha/Ash/Mouth/Hmph.PNG"
        attribute grimace "images/cha/Ash/Mouth/Grimace.PNG"

# Roan layered images
layeredimage roan:
    always "images/cha/Roan/Base.PNG"
    
    group brows:
        attribute neutral default "images/cha/Roan/Brows/Neutral.PNG"
        attribute sad "images/cha/Roan/Brows/Sad.PNG"
        attribute worried "images/cha/Roan/Brows/Worried.PNG"
        attribute annoyed "images/cha/Roan/Brows/Annoyed.PNG"
        attribute angry "images/cha/Roan/Brows/Angry.PNG"
        attribute curious "images/cha/Roan/Brows/Curious.PNG"
        attribute raised "images/cha/Roan/Brows/Raised.PNG"
        attribute really "images/cha/Roan/Brows/Really.PNG"
        attribute questioning "images/cha/Roan/Brows/Questioning.PNG"
    
    group eyes:
        attribute open default "images/cha/Roan/Eyes/Open.PNG"
        attribute closed "images/cha/Roan/Eyes/Closed.PNG"
        attribute closed_happy "images/cha/Roan/Eyes/Closed Happy.PNG"
        attribute wide "images/cha/Roan/Eyes/Wide.PNG"
        attribute terrified "images/cha/Roan/Eyes/Terrified.PNG"
        attribute lidded "images/cha/Roan/Eyes/Lidded.PNG"
    
    group mouth:
        attribute flat default "images/cha/Roan/Mouth/Flat.PNG"
        attribute smile "images/cha/Roan/Mouth/Smile.PNG"
        attribute smile_teeth "images/cha/Roan/Mouth/Smile Teeth.PNG"
        attribute smile_open "images/cha/Roan/Mouth/Smile Open.PNG"
        attribute frown "images/cha/Roan/Mouth/Frown.PNG"
        attribute smirk "images/cha/Roan/Mouth/Smirk.PNG"
        attribute open "images/cha/Roan/Mouth/Open.PNG"
        attribute o "images/cha/Roan/Mouth/O.PNG"
        attribute shout "images/cha/Roan/Mouth/Shout.PNG"
        attribute yell "images/cha/Roan/Mouth/Yell.PNG"
        attribute hmph "images/cha/Roan/Mouth/Hmph.PNG"
        attribute grimace "images/cha/Roan/Mouth/Grimace.PNG"

# Heather layered images
layeredimage heather:
    always "images/cha/Heather/Base.PNG"
    
    group brows:
        attribute neutral default "images/cha/Heather/Brows/Neutral.PNG"
        attribute sad "images/cha/Heather/Brows/Sad.PNG"
        attribute worried "images/cha/Heather/Brows/Worried.PNG"
        attribute annoyed "images/cha/Heather/Brows/Annoyed.PNG"
        attribute angry "images/cha/Heather/Brows/Angry.PNG"
        attribute curious "images/cha/Heather/Brows/Curious.PNG"
        attribute raised "images/cha/Heather/Brows/Raised.PNG"
        attribute really "images/cha/Heather/Brows/Really.PNG"
        attribute questioning "images/cha/Heather/Brows/Questioning.PNG"
    
    group eyes:
        attribute open default "images/cha/Heather/Eyes/Open.PNG"
        attribute closed "images/cha/Heather/Eyes/Closed.PNG"
        attribute closed_happy "images/cha/Heather/Eyes/Closed Happy.PNG"
        attribute wide "images/cha/Heather/Eyes/Wide.PNG"
        attribute terrified "images/cha/Heather/Eyes/Terrified.PNG"
        attribute lidded "images/cha/Heather/Eyes/Lidded.PNG"
    
    group mouth:
        attribute flat default "images/cha/Heather/Mouth/Flat.PNG"
        attribute smile "images/cha/Heather/Mouth/Smile.PNG"
        attribute smile_teeth "images/cha/Heather/Mouth/Smile Teeth.PNG"
        attribute smile_open "images/cha/Heather/Mouth/Smile Open.PNG"
        attribute frown "images/cha/Heather/Mouth/Frown.PNG"
        attribute smirk "images/cha/Heather/Mouth/Smirk.PNG"
        attribute open "images/cha/Heather/Mouth/Open.PNG"
        attribute o "images/cha/Heather/Mouth/O.PNG"
        attribute shout "images/cha/Heather/Mouth/Shout.PNG"
        attribute yell "images/cha/Heather/Mouth/Yell.PNG"
        attribute hmph "images/cha/Heather/Mouth/Hmph.PNG"
        attribute grimace "images/cha/Heather/Mouth/Grimace.PNG"

# Obsidian layered images
layeredimage obsidian:
    always "images/cha/Obsidian/Base.PNG"
    
    group brows:
        attribute neutral default "images/cha/Obsidian/Brows/Neutral.PNG"
        attribute sad "images/cha/Obsidian/Brows/Sad.PNG"
        attribute worried "images/cha/Obsidian/Brows/Worried.PNG"
        attribute annoyed "images/cha/Obsidian/Brows/Annoyed.PNG"
        attribute angry "images/cha/Obsidian/Brows/Angry.PNG"
        attribute curious "images/cha/Obsidian/Brows/Curious.PNG"
        attribute raised "images/cha/Obsidian/Brows/Raised.PNG"
        attribute really "images/cha/Obsidian/Brows/Really.PNG"
        attribute questioning "images/cha/Obsidian/Brows/Questioning.PNG"
    
    group eyes:
        attribute open default "images/cha/Obsidian/Eyes/Open.PNG"
        attribute closed "images/cha/Obsidian/Eyes/Closed.PNG"
        attribute closed_happy "images/cha/Obsidian/Eyes/Closed Happy.PNG"
        attribute wide "images/cha/Obsidian/Eyes/Wide.PNG"
        attribute terrified "images/cha/Obsidian/Eyes/Terrified.PNG"
        attribute lidded "images/cha/Obsidian/Eyes/Lidded.PNG"
    
    group mouth:
        attribute flat default "images/cha/Obsidian/Mouth/Flat.PNG"
        attribute smile "images/cha/Obsidian/Mouth/Smile.PNG"
        attribute smile_teeth "images/cha/Obsidian/Mouth/Smile Teeth.PNG"
        attribute smile_open "images/cha/Obsidian/Mouth/Smile Open.PNG"
        attribute frown "images/cha/Obsidian/Mouth/Frown.PNG"
        attribute smirk "images/cha/Obsidian/Mouth/Smirk.PNG"
        attribute open "images/cha/Obsidian/Mouth/Open.PNG"
        attribute o "images/cha/Obsidian/Mouth/O.PNG"
        attribute shout "images/cha/Obsidian/Mouth/Shout.PNG"
        attribute yell "images/cha/Obsidian/Mouth/Yell.PNG"
        attribute hmph "images/cha/Obsidian/Mouth/Hmph.PNG"
        attribute grimace "images/cha/Obsidian/Mouth/Grimace.PNG"

# Princess Pinkpaws layered images
layeredimage pinkpaws:
    always "images/cha/Princess/Base.png"
    
    group brows:
        attribute neutral default "images/cha/Princess/Brows/Neutral.PNG"
        attribute sad "images/cha/Princess/Brows/Sad.PNG"
        attribute worried "images/cha/Princess/Brows/Worried.PNG"
        attribute annoyed "images/cha/Princess/Brows/Annoyed.PNG"
        attribute angry "images/cha/Princess/Brows/Angry.PNG"
        attribute curious "images/cha/Princess/Brows/Curious.PNG"
        attribute raised "images/cha/Princess/Brows/Raised.PNG"
        attribute really "images/cha/Princess/Brows/Really.PNG"
        attribute questioning "images/cha/Princess/Brows/Questioning.PNG"
    
    group eyes:
        attribute open default "images/cha/Princess/Eyes/Open.PNG"
        attribute closed "images/cha/Princess/Eyes/Closed.PNG"
        attribute closed_happy "images/cha/Princess/Eyes/Closed Happy.PNG"
        attribute wide "images/cha/Princess/Eyes/Wide.PNG"
        attribute terrified "images/cha/Princess/Eyes/Terrified.PNG"
        attribute lidded "images/cha/Princess/Eyes/Lidded.PNG"
    
    group mouth:
        attribute flat default "images/cha/Princess/Mouth/Flat.PNG"
        attribute smile "images/cha/Princess/Mouth/Smile.PNG"
        attribute smile_teeth "images/cha/Princess/Mouth/Smile Teeth.PNG"
        attribute smile_open "images/cha/Princess/Mouth/Smile Open.PNG"
        attribute frown "images/cha/Princess/Mouth/Frown.PNG"
        attribute smirk "images/cha/Princess/Mouth/Smirk.PNG"
        attribute open "images/cha/Princess/Mouth/Open.PNG"
        attribute o "images/cha/Princess/Mouth/O.PNG"
        attribute shout "images/cha/Princess/Mouth/Shout.PNG"
        attribute yell "images/cha/Princess/Mouth/Yell.PNG"
        attribute hmph "images/cha/Princess/Mouth/Hmph.PNG"
        attribute grimace "images/cha/Princess/Mouth/Grimace.PNG"

### Character Background Information

## Ignatius "Nate" Thornwick - The Alchemist
# Personality: Reclusive, socially awkward, brilliant, aromantic/asexual
# Background: Lives in a remote manor, creates harmless "novelty" potions
# Appearance: Wears simple black hoodie (oversized "modern-day wizard robe")
# Key Traits: Horrified that his potions are being perverted, adores Princess Pinkpaws
# Relationship: Aromantic/asexual - focuses on friendship and intellectual connection

## Ashketharon "Ash" Zephyrius Voidrender the Eternal - The Dragon
# Personality: Ancient, pansexual, relaxed and open
# Background: Ancient dragon in human form, power source for Ignatius's alchemy
# Appearance: Modern and casual, signature tropical shirts
# Key Traits: "Hoard" is digital assets in MMO Nephilim, online friend of protagonist
# Relationship: Pansexual - can pursue romantic relationships

## Roan Song - The Victim (Best Friend)
# Personality: Trendy Korean-American, original personality being overwritten
# Background: Protagonist's best friend, under love potion influence
# Key Traits: Distant, abandoned shared hobbies, "bruised purple prose" social media
# Status: Personality being erased by corrosive magic (1 month deadline)

## Heather Rose Cromwell - The Antagonist
# Personality: Wealthy, clever, privileged, sees Roan as possession
# Background: Roan's girlfriend, uses resources to control him
# Key Traits: Enforces "no-sodium" diet on Roan, weekly deliveries from sketchy shop
# Role: Primary antagonist, controlling relationship

## Obsidian Foxglove - The Hidden Antagonist
# Personality: Social media scammer with weak magical talent
# Background: Enhances Ignatius's potions, sells through "Glamour" app
# Key Traits: Responsible for dangerous enhanced potions (3-5 weeks duration)
# Role: Hidden antagonist, source of the problem

## Princess Pinkpaws - The Familiar
# Personality: Highly intelligent poodle-mix service animal
# Background: Ignatius's familiar, can speak
# Appearance: Elegant, tall poodle mix with string of pearls instead of collar
# Key Traits: Surprised protagonist can understand her (unusual for non-magical person)
# Role: Emotional support, reveals magical world information

### Character Stats (for relationship tracking)
default ignatius_affection = 0
default ash_affection = 0

### Player Name Variables (from GDD)
default mcn = "Morgan"  # First name
default mcl = "Casey"   # Last name

### Common Emotion Combinations
## These are pre-defined combinations for easy use in scripts

# Happy expressions
image ignatius happy = "ignatius"
image ash happy = "ash"
image roan happy = "roan"
image heather happy = "heather"
image pinkpaws happy = "pinkpaws"

# Sad expressions
image ignatius sad = "ignatius"
image ash sad = "ash"
image roan sad = "roan"
image heather sad = "heather"
image pinkpaws sad = "pinkpaws"

# Angry expressions
image ignatius angry = "ignatius"
image ash angry = "ash"
image roan angry = "roan"
image heather angry = "heather"
image pinkpaws angry = "pinkpaws"

# Surprised expressions
image ignatius surprised = "ignatius"
image ash surprised = "ash"
image roan surprised = "roan"
image heather surprised = "heather"
image pinkpaws surprised = "pinkpaws"

# Neutral expressions
image ignatius neutral = "ignatius"
image ash neutral = "ash"
image roan neutral = "roan"
image heather neutral = "heather"
image pinkpaws neutral = "pinkpaws"

# Special expressions
image ignatius exasperated = "ignatius"
image heather smug = "heather"
image obsidian neutral = "obsidian"
image obsidian angry = "obsidian"
image obsidian smug = "obsidian"

### Usage Examples
## In your script files, you can use these in several ways:

# Method 1: Using the layered image directly with attributes
# show ignatius brows neutral eyes open mouth smile
# ignatius "Welcome to the manor!"

# Method 2: Using layered image attributes directly
# show ignatius brows annoyed eyes wide mouth shout
# ignatius "Please don't call me Nate!"

# Method 3: Mixing and matching attributes
# show ash brows curious eyes open mouth smile_teeth
# ash "I'm glad you decided to visit!"

# Method 4: Using the character name with attributes
# show roan brows sad eyes lidded mouth frown
# roan "I don't feel like myself lately..."

# Method 5: Using the character name alone (shows default expression)
# show ignatius
# ignatius "Hello there."
