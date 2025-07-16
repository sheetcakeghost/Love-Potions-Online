# Gestures

Ren'Py includes a gesture recognizer that is enabled when a touchscreen is used. This makes it possible for gestures to functions that would otherwise require a keyboard and mouse.

The gesture recognizer first classifies swipes into 8 compass directions, "n", "ne", "e", "se", "s", "sw", "w", "nw". North is considered to be towards the top of the screen. It then concatenates the swipes into a string using the "\_" as a delimiter. For example, if the player swipes down and to the right, the string "s\_e" will be produced.

Assuming  is None, what happens next is that gesture is mapped to an event using . If it is found, it is queued using . Otherwise, the gesture is ignored.

Gesture recognition is only enabled when "touch" is present in , which should be the case when running on a touchscreen device.

define config.gestures \= { "n\_s\_w\_e\_w\_e" : "progress\_screen" }

A map from gesture to the event activated by the gesture.

define config.dispatch\_gesture : Callable

The function that is used to dispatch gestures. This function is passed the raw gesture string. If it returns non-None, the interaction ends.

renpy.cancel\_gesture()

Cancels the current gesture, preventing the gesture from being recognized. This should be called by displayables that have gesture-like behavior.
