https://feniksdev.itch.io/in-depth-pronouns-for-renpy
# README

Thank you for downloading In-Depth Pronouns for Ren'Py! I hope this code will help you add more customization to your game.

There are a lot of bits and bobs that make up this code, so here is an overview of your next steps:

1. Make sure all the pronouns rpy files are inside your game/ folder somewhere. You can keep them in the pronouns/ subfolder, like YourGame/game/pronouns/pronoun_setup.rpy
2. If you're using a version of Ren'Py before 7.5 (e.g. 7.4.11 or earlier), you will need to remove or comment out some code in `pronoun_screens.rpy`. At the bottom of `screen term_customization` is a line that looks like `if GetFocusRect("term_drop"):`. You will need to remove/comment that code until the end of the screen. Slightly earlier in that same screen is the screen action `CaptureFocus("term_drop")`. You will also need to replace that with the action `CycleCustomTerm(current_key, term)`. This will allow you to click to cycle through pronouns instead of using a dropdown.
3. Otherwise, you're ready to go! Add the line `jump test_select_pronouns` somewhere early on in your script so you can test out the features.

The `test_one_pronoun_set` label demonstrates the simplest version of this code, where the player picks between pre-set pronouns without any further customization options.

The `test_custom_pronouns` brings up a screen where players can input their own pronouns. Players can then separately select which sorts of terms they want to use.

The `multiple_pronouns` label has two versions. The first is set up using a series of choice menus, most suited for if you're unfamiliar with screen language but still want to give players more involved customization. This label allows players to choose multiple pronoun sets, including the option to enter their own. They can then choose which terms they want to use, and how frequently they would like the game to randomize their pronouns.

Absent from the choice menu options is:

- The ability to customize pronoun randomization percentages. By default, all pronouns are weighted equally likely to be chosen when the game randomizes pronouns.
- The ability to fine-tune term preferences. This choice menu only allows players to set a general preference which will be used for all terms, with no options to fine-tune words for particular term groups.

These are both adjustable in the `pick_multiple_pronouns` screen, but are omitted from the choice menu approach due to it being very cumbersome to implement as a series of choices. However, the choice menu approach is an extremely suitable option if you want to allow players more control over their terms and also have multiple pronouns, while keeping the required coding very minimal.

Finally, there is the screen version of the `multiple_pronouns` label. It calls a special screen, `pick_multiple_pronouns`. This screen unleashes the full potential of the pronouns systems - not only can players mix and match pronoun sets, enter their own, adjust the frequency each pronoun set will be used, but they can also use the *Advanced* option for terms to fine-tune the words people use to refer to them.

## Adding Pronouns to your Project

If the options presented in the label demos above suit your project's needs, you can simply pop that code wherever your game needs it, and optionally update any of the screens in `pronoun_screens.rpy` to suit the styling of your game.

To add to or adjust existing pronoun values, head over to `pronoun_setup.rpy`. This file has the code where you can declare different pronoun sets, verbs, and any terms you might need for your game. There are plenty of examples to demonstrate how to add and adjust them to your needs.

You can also adjust any of the screens in `pronoun_screens.rpy` for your project. Where possible, custom actions have been added to simplify a lot of the buttons and inputs. You need to keep a lot of the logical stuff the same (button actions, input values), but the styling and positioning is up to you!

## Final Notes

Thanks for reading through this README! If you use this code in your project, you can credit me as Feniks with a link to my website https://feniksdev.com/ - I also post Ren'Py tutorials on there! You can follow me on itch.io at https://feniksdev.itch.io/ to be notified of any future tool releases as well. You might also consider looking at https://feniksdev.itch.io/multi-thumb-bar-for-renpy - a tool which adds the ability to include bars with multiple thumbs, perfect for letting players visually adjust pronoun frequencies.

If you found this code useful, consider dropping me a ko-fi at https://ko-fi.com/fen/ I appreciate the support to help me keep releasing useful Ren'Py tools!









Overview
This tool for Ren'Py provides a comprehensive way of adding player-selectable pronouns to your game, including rarely-seen features such as:

Choose multiple pronoun sets, and determine how frequently you would like each set to be used
Customize how frequently pronouns are switched, with the option to randomize pronouns every line, every scene, or only manually
Enter your own set of custom pronouns, which can be used alongside any other pronoun sets
Select term preferences separately from pronouns – players can use they/them but still be called “sister”, “daughter”, “girlfriend”, or use he/him but be referred to as “sibling”, “child”, “partner”.
Enter your own terms to be referred to by, and fine-tune specific preferences. Maybe you use she/they but prefer "person" to "woman" and "sister" to "sibling" - that's possible.
Incredibly simple set up for not only pronouns but also verbs and gendered terms, with easily readable scripting. You can include or exclude as much functionality as you need.
This code is also available on GitHub!

Description
This code will add several new classes, functions, and screens to your game, all included inside several files inside a pronouns folder. The code is initially set up to support the pronouns they/them, she/her, he/him, and one player-inputted custom pronoun set, but can be modified to the needs of your project. The project supports players having just one pronoun set, and also supports players choosing multiple pronoun sets which the game will switch between based on player preference. It also has a comprehensive customization system for choosing preferences for terms like "sister", "brother", "sibling".

Instructions
Download pronouns.zip and unzip it to get the pronouns/ folder. Place the folder into your Ren’Py game folder. I suggest you begin with a jump to the test label, test_select_pronouns, in your script so you can test it e.g. jump test_select_pronouns in the start label will let you test this code. The code is extensively documented so you can follow along and adapt it to suit the needs of your project.

Read the README included first for a quick overview of what's in each file and what to look at.

Use
Roughly, set up includes lines like the following:

define they = Pronoun("they", "she", "he", custom="they")
define them = Pronoun("them", "her", "him", custom="them")
define are = PronounVerb("are", "is")
define were = PronounVerb("were", "was")
define person = Term("person", "woman", "man", id="person")
define sibling = Term("sibling", "sister", "brother", id="sibling")

This will allow you to write lines in script like:

"[they!c] [are] my [sibling]."

This will appear in-game with the player-chosen pronouns and terms. The most common ways this will read are “She is my sister.”, “He is my brother.”, “They are my sibling.”.

Compatibility
This code has been tested for compatibility with Ren’Py 7.5-7.6 and Ren’Py 8.0-8.2. One of the screens, screen term_customization, uses the nearrect displayable and GetFocus actions to create a dropdown, which was introduced in 7.5/8.0. If you are on an older version, you will need to update, remove, or refactor this screen to not use dropdowns in this manner. A description of which code to remove and replace for backwards compatibility with 7.4.11 and earlier is included in the README inside the zip file.

The screens have also been coded with 1920x1080 project dimensions in mind. You will likely need to adapt the screens and styles to use in projects with different dimensions, though the code and logic is portable for any project dimensions.

Otherwise, this code is expected to be compatible with any Ren’Py version past 7.4 (please leave a reply in the forums below if you encounter issues). It is also expected to remain compatible with future versions of Ren’Py, and I intend to support it into the future as well.

Terms of Use
You may:

Use this code in commercial and noncommercial projects.
Modify and edit this code to suit your needs
You may not:

Resell all or part of this code as-is or sell it with modifications
Attribution should be credited as Feniks, with either a link to this page or to https://feniksdev.com

Author’s Notes
This code is adapted from the code I wrote for Our Life: Now & Forever by GB Patch Games. Try the free demo to see how we handled character customization!


I also have a listing for “multi-thumb bar” code, with code included so you can adapt it to be used for determining pronoun frequency for randomization. You can find it here!





And if you're using pronouns for a character customization system, you might also consider my Better Colorize tool, which allows you to recolour images in-engine with far more flexibility than default Ren'Py:



For more Ren'Py tutorials, check out my website https://feniksdev.com!