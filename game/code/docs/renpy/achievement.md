# Achievements

The Achievement module allows the developer to grant achievements to the player, to clear achievements, and to determine if an achievement has been granted. It also allows the recording of progress towards an achievement.

By default, the achievement stores information in the persistent file. If Steam support is available and enabled, achievement information is automatically synchronized with Steam.

Steam support must be added to Ren'Py, to ensure that it is only distributed by creators that have been accepted to the Steam partner program. To install it, choose "preferences", "Install libraries", "Install Steam Support".

achievement.Sync()

An action that calls achievement.sync(). This is only sensitive if achievements are out of sync.

achievement.clear(_name_)

Clears the achievement with name.

achievement.clear\_all()

Clears all achievements.

achievement.get\_progress(_name_)

Returns the current progress towards the achievement identified with name, or 0 if no progress has been registered for it or if the achievement is not known.

achievement.grant(_name_)

Grants the achievement with name, if it has not already been granted.

achievement.has(_name_)

Returns true if the player has been granted the achievement with name.

achievement.progress(_name_, _complete_)

Reports progress towards the achievement with name, if that achievement has not been granted. The achievement must be defined with a completion amount.

name

The name of the achievement. This should be the name of the achievement, and not the stat.

complete

An integer giving the number of units completed towards the achievement.

achievement.register(_name_, _\*\*kwargs_)

Registers an achievement. Achievements are not required to be registered, but doing so allows one to pass information to the backends.

name

The name of the achievement to register.

The following keyword parameters are optional.

steam

The name to use on steam. If not given, defaults to name.

stat\_max

The integer value of the stat at which the achievement unlocks.

stat\_modulo

If the progress modulo stat\_max is 0, progress is displayed to the user. For example, if stat\_modulo is 10, progress will be displayed to the user when it reaches 10, 20, 30, etc. If not given, this defaults to 0.

achievement.sync()

Synchronizes registered achievements between local storage and other backends. (For example, Steam.)

Variables that control achievements are:

achievement.steam\_position \= None

If not None, this sets the position of the steam notification popup. This must be a string, one of "top left", "top right", "bottom left", or "bottom right".

define config.steam\_appid \= None

If not None, this should be the Steam appid. Ren'Py will automatically set this appid when it starts. This needs to be set using the define statement:

define config.steam\_appid \= 12345

define config.automatic\_steam\_timeline \= True

If true, when run under Steam, the game will automatically update the Steam Timeline.

This currently consists of:

*   Updating the state description to match , if the variables is set.
    
*   Updating the game mode to reflect when the player is inside a menu.
    

## Steamworks API

When Steam is available, a ctypes-based binding to the Steamworks API is available as `achievement.steamapi`. The binding is an instance of the steamapi module, as found , and represents a machine translation of the C++ Steamworks API to Python.

In addition, a large number of functions are available in the achievement.steam object, if and only if the Steamworks API is available.

achievement.steam

If Steam initialized successfully, this is a namespace with high-level Steam methods. If Steam did not initialize, this is None. Always check that this is not None before calling a method.

### Steam Apps

achievement.steam.dlc\_installed(_appid_)

Returns True if dlc is installed, or False otherwise.

achievement.steam.dlc\_progress(_appid_)

Reports the progress towards DLC download completion.

achievement.steam.get\_app\_build\_id()

Returns the build ID of the installed game.

achievement.steam.get\_current\_beta\_name()

Returns the name of the current beta, or None if it can't.

achievement.steam.get\_current\_game\_language()

Return the name of the language the user has selected.

achievement.steam.get\_steam\_ui\_language()

Return the name of the language the steam UI is using.

achievement.steam.install\_dlc(_appid_)

Requests the DLC with appid be installed.

achievement.steam.is\_subscribed\_app(_appid_)

Returns true if the user owns the app with appid, and false otherwise.

achievement.steam.uninstall\_dlc(_appid_)

Requests that the DLC with appid be uninstalled.

### Steam Overlay

achievement.steam.activate\_overlay(_dialog_)

Activates the Steam overlay.

dialog

The dialog to open the overlay to. One of "Friends", "Community", "Players", "Settings", "OfficialGameGroup", "Stats", "Achievements"

achievement.steam.activate\_overlay\_to\_store(_appid_, _flag\=None_)

Opens the steam overlay to the store.

appid

The appid to open.

flag

One of achievement.steam.STORE\_NONE, .STORE\_ADD\_TO\_CART, or .STORE\_ADD\_TO\_CART\_AND\_SHOW.

achievement.steam.activate\_overlay\_to\_web\_page(_url_)

Activates the Steam overlay, and opens the web page at url.

achievement.steam.is\_overlay\_enabled()

Returns true if the steam overlay is enabled. (This might take a while to return true once the game starts.)

achievement.steam.overlay\_needs\_present()

Returns true if the steam overlay is enabled. (This might take a while to return true once the game starts.)

achievement.steam.set\_overlay\_notification\_position(_position_)

Sets the position of the steam overlay. Position should be one of achievement.steam.POSITION\_TOP\_LEFT, .POSITION\_TOP\_RIGHT, .POSITION\_BOTTOM\_LEFT, or .POSITION\_BOTTOM\_RIGHT.

### Steam Stats

achievement.steam.clear\_achievement(_name_)

Clears the achievement with name. Call `_renpysteam.store_stats()` to push this change to the server.

achievement.steam.get\_achievement(_name_)

Gets the state of the achievements with name. This returns True if the achievement has been granted, False if it hasn't, and None if the achievement is unknown or an error occurs.

achievement.steam.get\_float\_stat(_name_)

Returns the value of the stat with name, or None if no such stat exits.

achievement.steam.get\_int\_stat(_name_)

Returns the value of the stat with name, or None if no such stat exits.

achievement.steam.grant\_achievement(_name_)

Grants the achievement with name. Call `_renpysteam.store_stats()` to push this change to the server.

achievement.steam.indicate\_achievement\_progress(_name_, _cur\_progress_, _max\_progress_)

Indicates achievement progress to the user. This does _not_ unlock the achievement.

achievement.steam.list\_achievements()

Returns a list of achievement names.

achievement.steam.retrieve\_stats()

Retrieves achievements and statistics from Steam.

achievement.steam.set\_float\_stat(_name_, _value_)

Sets the value of the stat with name, which must have the type of FLOAT. Call `_renpysteam.store_stats()` to push this change to the server.

achievement.steam.set\_int\_stat(_name_, _value_)

Sets the value of the stat with name, which must have the type of INT. Call `_renpysteam.store_stats()` to push this change to the server.

achievement.steam.store\_stats()

Stores statistics and achievements on the Steam server.

### Steam Timeline

achievement.steam.add\_timeline\_event(_icon_, _title_, _description_, _priority\=0_, _start\_offset\=0.0_, _duration\=0.0_, _possible\_clip\=None_)

Adds an event to the timeline.

icon

The icon to display for the event. This should be a string giving one of the standard steam icons, or one you uploaded to Steam.

title

The title of the event.

description

The description of the event.

priority

The priority of the event, used to resolve conflicts. This should be an interger between 0 and 1000.

start\_offset

The offset of the start of the event from the current time, in seconds.

duration

The duration of the event, in seconds.

possible\_clip

This determines if the event can be clipped. This should be one of the achievement.steam.CLIP\_PRIORITY... constants: CLIP\_PRIORITY\_NONE, CLIP\_PRIORITY\_STANDARD, or CLIP\_PRIORITY\_FEATURED.

achievement.steam.clear\_timeline\_state\_description(_time\_delta_)

Clears the description of the current state in the timeline.

achievement.steam.set\_timeline\_state\_description(_description_, _time\_delta\=0.0_)

Sets the description of the current state in the timeline.

description

A string giving the description of the current state.

time\_delta

The time since the last state change.

### Steam User

achievement.steam.cancel\_ticket()

Cancels the ticket returned by .

achievement.steam.get\_account\_id()

Returns the user's account ID.

achievement.steam.get\_csteam\_id()

Returns the user's full CSteamID as a 64-bit number.

achievement.steam.get\_game\_badge\_level(_series_, _foil_)

Gets the level of the users Steam badge for your game.

achievement.steam.get\_persona\_name()

Returns the user's publicly-visible name.

achievement.steam.get\_session\_ticket(_identity\=None_)

Gets a ticket that can be sent to the server to authenticate this user.

### Steam Workshop

achievement.steam.get\_subscribed\_item\_path(_item\_id_)

Returns the path where an item of user-generated content was installed. Returns None if the item was not installed.

item\_id

The item id.

achievement.steam.get\_subscribed\_items()

Returns a list of the item ids the user has subscribed to in the steam workshop.
