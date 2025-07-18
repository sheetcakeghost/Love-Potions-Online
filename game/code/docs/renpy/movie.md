# Movie

Ren'Py is capable of using FFmpeg (included) to play movies using the video codecs:

*   AV1
    
*   VP9
    
*   VP8
    
*   Theora
    
*   MPEG-4 part 2 (including Xvid and DivX)
    
*   MPEG-2
    
*   MPEG-1
    

and the following audio codecs:

*   Opus
    
*   Vorbis
    
*   MP3
    
*   MP2
    
*   FLAC
    
*   PCM
    

inside the following container formats:

*   WebM
    
*   Matroska
    
*   Ogg
    
*   AVI
    
*   Various kinds of MPEG stream.
    

(Note that using some of these formats may require patent licenses. When in doubt, and especially for commercial games, we recommend using AV1, VP9, VP8, or Theora; Opus or Vorbis; and WebM, Matroska, or Ogg.)

Movies can be displayed fullscreen or in a displayable. Fullscreen movies are more efficient. YUV444 movies are not hardware accelerated, use YUV420 or YUV422 instead.

Ren'Py's movie decoder does not support movies with alpha channels, but the side\_mask parameter of the  displayable can be used for that purpose. Here is an example of how to use ffmpeg to create a webm file with a side-by-side mask from a mov file with an alpha channel.

ffmpeg \-i original.mov \-filter:v alphaextract mask.mov
ffmpeg \-i original.mov \-i mask.mov \-filter\_complex "hstack" \-codec:v vp8 \-crf 10 output.webm

Movies are supported on the Web platform, but the list of supported codecs differs from browser to browser. For cross-browser compatibility (especially to support Safari), the most efficient combination is H.264 with MP3 (or AAC) in a MP4 file. However, Ren'Py does not support H.264 decoding (or AAC), so this combination can only work on the Web platform.

## Fullscreen Movies

The easiest and most efficient way to display a movie fullscreen is to use the  function. This function displays the movie fullscreen until it either ends, or the player clicks to dismiss it.

$ renpy.movie\_cutscene("On\_Your\_Mark.webm")

## Movie Displayables and Movie Sprites

The Movie displayable can be used to display a movie anywhere Ren'Py can show a displayable. For example, a movie can be displayed as the background of a menu screen, or as a background.

The Movie displayable can also be used to define a movie sprite, which is a sprite that is backed by two movies. The primary movie provides the color of the sprite. A second movie, the mask movie, provides the alpha channel, with white being full opacity and black being full transparency.

Movies played by the Movie displayable loop automatically.

Here's an example of defining a movie sprite:

image eileen movie \= Movie(play\="eileen\_movie.webm", side\_mask\=True)

The movie sprite can be shown using the show statement, which automatically starts the movie playing. It will be automatically stopped when the displayable is hidden.

show eileen movie

e "I'm feeling quite animated today."

hide eileen

e "But there's no point on wasting energy when I'm not around."

A Movie displayable can also be used as part of a screen, provided it is created during the init phase (for example, as part of an image statement.)

image main\_menu \= Movie(play\="main\_menu.ogv")

screen main\_menu:
    add "main\_menu"
    textbutton "Start" action Start() xalign 0.5 yalign 0.5

Multiple movie displayables or sprites can be displayed on the screen at once, subject to system performance, and provided all share the same framerate. The behavior of Ren'Py when displaying movies with different framerates is undefined, but will likely include a significant amount of frame drop.

## Python Functions

renpy.movie\_cutscene(_filename_, _delay\=None_, _loops\=0_, _stop\_music\=True_)

This displays a movie cutscene for the specified number of seconds. The user can click to interrupt the cutscene. Overlays and Underlays are disabled for the duration of the cutscene.

filename

The name of a file containing any movie playable by Ren'Py.

delay

The number of seconds to wait before ending the cutscene. Normally the length of the movie, in seconds. If None, then the delay is computed from the number of loops (that is, loops + 1) \* the length of the movie. If -1, we wait until the user clicks.

loops

The number of extra loops to show, -1 to loop forever.

Returns True if the movie was terminated by the user, or False if the given delay elapsed uninterrupted.

_class_ Movie(_\*_, _size\=None_, _channel\='movie'_, _play\=None_, _side\_mask\=False_, _mask\=None_, _mask\_channel\=None_, _start\_image\=None_, _image\=None_, _play\_callback\=None_, _loop\=True_, _group\=None_, _\*\*properties_)

This is a displayable that shows the current movie.

size

This should be specified as either a tuple giving the width and height of the movie, or None to automatically adjust to the size of the playing movie. (If None, the displayable will be (0, 0) when the movie is not playing.)

channel

The audio channel associated with this movie. When a movie file is played on that channel, it will be displayed in this Movie displayable. If this is left at the default of "movie", and play is provided, a channel name is automatically selected, using  and .

play

If given, this should be the path to a movie file, or a list of paths to movie files. These movie files will be automatically played on channel when the Movie is shown, and automatically stopped when the movie is hidden.

side\_mask

If true, this tells Ren'Py to use the side-by-side mask mode for the Movie. In this case, the movie is divided in half. The left half is used for color information, while the right half is used for alpha information. The width of the displayable is half the width of the movie file.

Where possible, side\_mask should be used over mask as it has no chance of frames going out of sync.

mask

If given, this should be the path to a movie file, or a list of paths to movie files, that are used as the alpha channel of this displayable. The movie file will be automatically played on movie\_channel when the Movie is shown, and automatically stopped when the movie is hidden.

mask\_channel

The channel the alpha mask video is played on. If not given, defaults to channel\_mask. (For example, if channel is "sprite", mask\_channel defaults to "sprite\_mask".)

start\_image

An image that is displayed when playback has started, but the first frame has not yet been decoded.

image

An image that is displayed when play has been given, but the file it refers to does not exist. (For example, this can be used to create a slimmed-down mobile version that does not use movie sprites.) Users can also choose to fall back to this image as a preference if video is too taxing for their system. The image will also be used if the video plays, and then the movie ends, unless group is given.

play\_callback

If not None, a function that's used to start the movies playing. (This may do things like queue a transition between sprites, if desired.) It's called with the following arguments:

old

The old Movie object, or None if the movie is not playing.

new

The new Movie object.

A movie object has the play parameter available as `_play`, while the `channel`, `loop`, `mask`, and `mask_channel` fields correspond to the given parameters.

Generally, this will want to use  to start the movie playing on the given channel, with synchro\_start=True. A minimal implementation is:

def play\_callback(old, new):

    renpy.music.play(new.\_play, channel\=new.channel, loop\=new.loop, synchro\_start\=True)

    if new.mask:
        renpy.music.play(new.mask, channel\=new.mask\_channel, loop\=new.loop, synchro\_start\=True)

loop

If False, the movie will not loop. If image is defined, the image will be displayed when the movie ends. Otherwise, the displayable will become transparent.

group

If not None, this should be a string. If given, and if the movie has not yet started playing, and another movie in the same group has played in the previous frame, the last frame from that movie will be used for this movie. This can prevent flashes of transparency when switching between two movies.

keep\_last\_frame

If true, and the movie has ended, the last frame will be displayed, rather than the movie being hidden. This only works if loop is false. (This behavior will also occur if group is set.)
