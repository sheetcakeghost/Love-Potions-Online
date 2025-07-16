https://feniksdev.itch.io/inline-conditions-for-renpy

# Inline Conditions for Ren'Py by Feniks (feniksdev.com)

Adding this file to your game will allow you to write dialogue that includes conditional checks to show enclosed text only if the provided condition(s) are met. This can help avoid multiple repeated lines with small tweaks or excessive variable declarations. If you use this file in your project, credit me as Feniks @ feniksdev.com There are three text tags included, which have slightly different behaviour for how they are treated while the player is skipping if they have the preference setting to only skip seen text on.

`{skip_if}`

- This tag (and any attached `{elif}` or `{else}` tags) means that all variants of this line are treated as the same line for skipping. If the player has seen this line once in any playthrough, regardless of which of the conditions were met when it was seen, it will be skipped if the player is skipping only seen text. It also has a "pretty" form - `{same: if}`. This has the exact same behaviour, but is intended to be more readable. It communicates that all variants of this line are the same when it comes to skipping unread text only.

`{stop_if}`

- This tag (and any attached `{elif}` or `{else}` tags) means that all variants of this line are treated as separate lines for skipping. If the first time the player encounters this line, the `{stop_if}` condition is True, if on a second playthrough they encounter this line again but the condition is False, the game will stop skipping at this line. If the player has seen a particular variant of the line before, it is treated as "seen" and does not stop skipping. It also has a "pretty" form - `{diff: if}`. This has the exact same behaviour, but is intended to be more readable. It communicates that all variants of this line are different when it comes to skipping unread text only.

`{if}`

- This tag can have the behaviour of either `{skip_if}` or `{stop_if}`. You will set which one in the `init python in myconfig` block below. It is intended as a convenience, so you can assign `{if}` to whichever behaviour your project will need more often. You cannot change this behaviour in the middle of gameplay, so if you require the opposite behaviour, use `{skip_if}` or `{stop_if}` directly (or their "pretty" forms).

## Usage

`{skip_if}`, `{stop_if}`, `{if}`, and `{elif}` all require a condition to work. The condition can be any arbitrary expression, including function calls, so long as it can be evaluated in Python. It is evaluated just before the line is shown, but may be evaluated occasionally beforehand for prediction, so you should be sure to declare any values you're using with define or default as appropriate and ensure your function calls do not cause side effects. The structure of a tag with a condition looks like:

`"{if condition}This text will only show if the condition is True.{/if}"`

The condition comes after the `if` and is evaluated as a Python expression. The condition may take many forms:

- `{if num_apples > 5}`
- `{diff: if pronouns == 'she/her'}`
- `{same: if xia_points > 2 and zoran_points < 10}`
- `{if persistent.good_end}...{elif persistent.bad_end}...`

While `{if}`, `{same: if}`, and `{diff: if}` can all be used to start a conditional statement, (as with the `{skip_if}` and `{stop_if}` versions), `{elif}` and `{else}` can only be used after an initial if tag of some kind. `{elif}` and `{else}` work as they do in Python, so if a previous clause in an if/elif/else chain is True, the rest of the chain is False and skipped. The `{else}` tag does not take any condition. It is shown only if none of the previous conditions were True.

These text tags ONLY work inside dialogue and choice menus. If you would like similar behaviour for screens or inside functions, you should use the more flexible fstring notation from Python: https://realpython.com/python-f-strings/ You may also be interested in https://feniksdev.itch.io/inline-python-for-renpy, which brings general Python expressions to Ren'Py dialogue and choices.

## Examples

1. `"You set {same: if apples == 1}it{else}them{/else} on the table."`

If the player has more than one apple, the dialogue changes slightly to indicate it is plural. This is nearly inconsequential, so `{same: if}` is specified so the game does not stop skipping for any variant of this line once the player has seen one version of it. (This may also be the default behaviour for a regular `{if}` tag, if desired). The `{/else}` tag closes the conditional statement so the two possible versions of this line are:

```py
"You set it on the table." (if apples == 1)
"You set them on the table." (if apples != 1)
```

2. `"Zoran slowly walked away.{if perception > 10} His gait was awkward, as though from an injury."`

Here, there is some bonus dialogue if the player is perceptive. Whether the game considers a variant of this line to be "seen" or not depends on how you set up the behaviour of `{if}` at the top of inline_conditions.rpy. The `{if}` tag does not need to be closed at the end of this line, as reaching the end of the line automatically closes it.

1. `"You have {if apples>1}many{elif apples==1}one{else}no{/else} apple{if apples!=1}s{/if}."`

Another example using an if/elif/else structure. The three possibilities for this line are:

```py
"You have many apples." (if apples > 1)
"You have one apple." (if apples == 1)
"You have no apples." (if apples < 1)
```

You can add as many elif statements as needed for your conditional. The full condition is closed with an `{/else}` tag, as that's the final text tag used in the if/elif/else chain.

4. `"You checked, and it was locked.{if has_key or has_lockpick} That wouldn't be an issue.{if has_key} The key fit smoothly into the lock.{else} Your lockpick made quick work of it."`

You can also nest conditions. Here, the nesting is roughly equivalent to:

```py
"You checked, and it was locked."
if has_key or has_lockpick:
    extend " That wouldn't be an issue."
    if has_key:
            extend " The key fit smoothly into the lock."
    else:
        extend " Your lockpick made quick work of it."
```

Unlike the above code, however, the inline conditional version does not require clicks to advance through each line.

5. `"You mean you don't{same: if is_drunk} {i}*hic*{/i}{/if} {diff: if zoran_points<5}hate me?{else}think I'm a bother?"`

A single line can have multiple inline conditions, and they don't have to have the same structure. Both conditions can be tracked differently for skipping purposes, if you want. So for this line, whether the player is drunk or not will not matter when the line is considered for skipping, only whether they have more or less than 5 points with Zoran. This behaviour can be particularly helpful for translation, where some languages may need to break up sentences in different ways to communicate the same point. The above line is approximately equivalent to:

```py
if is_drunk:
    if zoran_points < 5:
        "You mean you don't {i}*hic*{/i} hate me?"
    else:
        "You mean you don't {i}*hic*{/i} think I'm a bother?"
else:
    if zoran_points < 5:
        "You mean you don't hate me?"
    else:
        "You mean you don't think I'm a bother?"
```

As you can see, the inline conditions clean this up considerably.

6. `"It's a{if gift == 'apron'}n{elif gift == 'earrings'} pair of{/elif} [gift]."`
To use string values in your conditions, you have to use whichever quotations you're not using for the dialogue (so, in this case, single quotes since double quotes are used for the dialogue). To close an if/elif conditional which doesn't have an {else}, you'll use {/elif} to close it. You can interpolate variables regularly inside dialogue with [var]. The possible outcomes of this line are:

```py
"It's an apron." (if gift == "apron")
"It's a pair of earrings." (if gift == "earrings")
"It's a [gift]." (if gift is anything else e.g. "It's a camera.")
```

## Final notes

You can also use the `skip_if` and `stop_if` special tags as described earlier instead of the `same: if` and `diff: if` format e.g.

`"You mean you don't{same: if is_drunk} {i}*hic*{/i}{/if} {diff: if zoran_points<5}hate me?{else}think I'm a bother?"`

is equivalent to:

`"You mean you don't{skip_if is_drunk} {i}*hic*{/i}{/if} {stop_if zoran_points<5}hate me?{else}think I'm a bother?"`

Which one you use doesn't matter, it's just what makes more sense to you.

You can check out my website, https://feniksdev.com for more Ren'Py tutorials, and subscribe to feniksdev.itch.io so you don't miss out on future Ren'Py tool releases!








Overview
Consider the following situation:

if apples == 1:
  "You set it on the table."
else:
  "You set them on the table."
This is a lot of code for an extremely minor line variation. Some other engines for text-based projects like Twine Sugarcube have inline conditional statement syntax to reduce this sort of thing down to one line of dialogue. And now you can have this functionality in Ren'Py too, using this addon!

"You set {if apples == 1}it{else}them{/else} on the table."
Description
This Ren'Py addon provides:

Text tag-like syntax to use conditions in dialogue and in choice menus
Skip seen text only compatibility - two different syntax variations let you decide whether the line should be considered unseen if the player hasn't seen a particular combination of conditions, or if it's still considered the same line for skipping.
Choose which behaviour you want as the default, with the option to use the other behaviour on a per-condition basis
Any combination of if/elif/else is possible
Compatible with translations
An optional lint file is included for a small additional fee. This file performs a regular lint check, but with additional options for linting the inline conditional statements for correctness + a count of how many inline conditions you're using across your whole project.

Features
Free File
Extra Paid File
{if}, {elif}, {else} text tags, and special {skip_if} and {stop_if} variants

Explanatory comments and examples

Code to remember which versions of the line have been viewed, for use with the "skip unseen" setting

An updated Skip screen action which behaves correctly for use with inline conditionals and the "skip unseen" setting
A special lint function which can be executed in-game. Produces a regular lint file, but cleans up false positives you'd get when running Lint from the launcher.

This function will check your inline conditionals for correctness - it will let you know if you have a poorly-formed condition that would cause an error.

Optionally, you can set the lint function to also report variables which are used in your inline conditionals but are not declared beforehand.

The produced lint file also includes a count at the bottom of the number of inline conditional statements in the project.

The condition correctness check and number of inline conditional checks will also work when Lint is used from the launcher, but note that a regular Lint will (as of 8.1/7.6) incorrectly report inline conditionals as erroneous text tags.


Use
Simply place inline_conditions.rpy into your game folder and you can start writing inline conditional statements. Near the top of the file, after the examples, you can set inline_conditions_same_for_skipping to True or False to control what behaviour the inline conditions have by default for skipping.

"It's a{if gift == 'apron'}n{elif gift == 'earrings'} pair of{/elif} [gift]."
This code is roughly equivalent to:

if gift == 'apron':
  "It's an [gift]."
elif gift == 'earrings':
  "It's a pair of [gift]."
else:
  "It's a [gift]."
Because the condition is inline, unlike the very verbose version above, you have the option of treating it as a singular line when it comes to skipping. It's also treated as a single line for translation - this can even reduce unneeded lines, particularly in cases where a line would not need to have a variation due to one language not differentiating between plural and singular nouns. Inline conditions cut down on unnecessary variable declarations, and provide a smoother experience for readers who won't find skipping suddenly stops for a minuscule line difference.

Compatibility
This code has been tested for compatibility with Ren'Py 7.5-7.6 and Ren'Py 8.0-8.2. It is expected to be compatible with earlier and later Ren'Py versions, and I'll maintain compatibility at least until Ren'Py adds a similar feature to the engine itself.

For 8.1 and Earlier:
Inline conditions will cause lint errors in versions earlier than 8.2, as presently Lint does not account for text filters when linting text, thus it does not recognize the text tags. Lint also does not check the conditions for correctness in any way. You can safely ignore lint errors which complain of unrecognized text tags. 

An additional file is also available for a small fee which adds a custom lint function to properly account for inline conditions - this fee is so I can continue to maintain the linter even if the engine updates how linting is handled. You will run the lint in-game instead of from the launcher.

For 8.2 and Later:
Linting has been updated in 8.2 to apply filters to the text before reporting errors. This means that if you have the additional lint files in your project, you can use Lint from the launcher and the additional lint tests for conditions will work as a regular lint hook.

Terms of Use
Both the free version and any paid addons have the same terms of use.

You may:

Use this code in commercial and noncommercial projects, provided it is packaged into an archived .rpa file. The code to do so is included in the code files.
Modify and edit the code to suit your needs.
You may not:

Resell all or part of the code as-is or sell it with modifications
Release any projects created using this code without providing attribution
Attribution must be credited to Feniks, with a link to either the page with this code or to https://feniksdev.com

Final Notes
If you pay the minimum price for the lint file, it also includes functions for linting inline Python, which you can find linked below. Both inline conditions and  inline Python use the same approach to correctly lint the added formatting. Whether you download the bonus lint file here or on the other page, both contain the same files, so you do not have to pay twice!



Consider looking at my other Ren'Py tools, which I've added to a collection here: https://itch.io/c/3491447/my-renpy-tools and follow me to be sure you're notified of new releases and updates. I also release tutorials on my website, https://feniksdev.com
