# In-Game Menus

In many visual novels, the player is asked to make choices that control the outcome of the story. The Ren'Py language contains a `menu` statement that makes it easy to present choices to the user.

Here's an example of a `menu` statement:

menu:
     "What should I do?"

     "Drink coffee.":
         "I drink the coffee, and it's good to the last drop."

     "Drink tea.":
         $ drank\_tea \= True

         "I drink the tea, trying not to make a political statement as I do."

     "Genuflect.":
         jump genuflect\_ending

label after\_menu:

     "After having my drink, I got on with my morning."

The `menu` statement begins with the keyword `menu`. This may be followed by a label name, in which case it's equivalent to preceding the menu with that label. For example:

menu drink\_menu:
    ...

The menu statement is followed by an indented block. This block may contain a , and must contain at least one menu choice. If the say statement is present, it is displayed on the screen at the same time as the menu.

**Menu Choices.** A menu choice is an option the user can select from the in-game menu. A menu choice begins with a string. The string may be followed by an if-clause, which makes the choice conditional. The menu choice ends with a colon, and must be followed by a block of Ren'Py statements.

When the choice is selected, the block of statements is run. If execution reaches the end of the block, it continues with the statement after the end of the menu statement.

An if-clause consists of the keyword `if`, followed by a Python expression. The menu choice is only displayed if the expression is true. In the following menu:

menu:
    "Go left.":
        ...
    "Go right.":
        ...
    "Fly above." if drank\_tea:
        ...

The third choice will only be presented if the `drank_tea` variable is true. (However if, the  variable is set to True, it will be shown as a disabled button.)

If all menu options have their if conditions unfulfilled, the menu will be skipped and control will advance to the statement following it.

## Menu Set

A menu can take a set clause, on a line by itself. If present, only items with captions that are not in the set are displayed as part of the menu. When a choice is selected, the caption of that choice can be added to the set.

As with if clauses, if no choice is available, control advances to the statement after the menu.

For historical reasons, the set can be either a set object or a list.

default menuset \= set()

menu chapter\_1\_places:

    set menuset
    "Where should I go?"

    "Go to class.":
        jump go\_to\_class

    "Go to the bar.":
        jump go\_to\_bar

    "Go to jail.":
        jump go\_to\_jail

label chapter\_1\_after\_places:

    "Wow, that was one heck of a Tuesday."

## Menu Arguments

It's possible to pass arguments to the menu itself, and to the individual choices in a menu. To pass arguments to the menu, add them to the menu line, after the optional name, and immediately before the colon. To pass arguments to a menu choice, put them after the menu string and before the `if` keyword or colon.

menu ("jfk", screen\="airport"):

    "Chicago, IL" (200):
        jump chicago\_trip

    "Dallas, TX" (150, sale\=True):
        jump dallas\_trip

    "Hot Springs, AR" (300) if secret\_unlocked:
        jump hot\_springs\_trip

Menu arguments passed to the menu itself become arguments to the screen, except the screen argument which selects the screen, and the nvl argument that selects the .

See the documentation for  and .
