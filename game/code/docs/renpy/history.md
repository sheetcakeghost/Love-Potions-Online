# Dialogue History

Ren'Py includes a dialogue history system that stores each line of dialogue after it has been shown to the player. This stored dialogue can then be retrieved and re-shown to the player.

The dialogue history system is controlled by two variables. The  variable controls the maximum number of history entries that are stored, and must be set to enable history at all. The  variable can be used to disable and re-enable history storage.

Finally, the  variable stores the actual history, as a list of HistoryEntry objects. HistoryEntry objects contain data in their fields, as defined below.

_class_ HistoryEntry

kind

The kind of character that created this history. Ren'Py sets this to "current" while a line of dialogue is displaying, and then to either "adv" or "nvl".

who

A string giving the name of the character that is speaking, or None if no such string exists.

what

A string giving the dialogue text.

who\_args

A dictionary giving the properties that were supplied to the who text widget when the dialogue was originally shown.

what\_args

A dictionary giving the properties that were supplied to the what text widget when the dialogue was originally shown.

window\_args

A dictionary giving the properties that were supplied to the dialogue window when the dialogue was originally shown.

show\_args

A dictionary giving the properties that were supplied to the say screen when the dialogue was originally shown.

image\_tag

The image tag given to the , or None if no such tag was given.

voice

This is the object returned from , storing information about the voice that is being played.

rollback\_identifier

This is an identifier that can be passed to the  action, to cause a rollback to the line of script that generated this history entry. The rollback only occurs if the location is still in the script log, otherwise the action is insensitive.

Once a HistoryEntry has been created, it is passed to each of the callbacks in , which allows creator-written code to add new fields.
