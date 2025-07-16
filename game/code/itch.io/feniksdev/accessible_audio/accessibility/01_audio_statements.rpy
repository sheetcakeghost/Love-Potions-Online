################################################################################
##
## Sound Disabler and Captions Tool for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## and Alaric (just-write-studios.itch.io) v1.0
##
################################################################################
## This file contains the code for overwriting the play sound / play music
## and play statements in Ren'Py to allow for callbacks. The Sound Disabler
## and Captions Tool uses this callback to include audio captions.
##
## This file is just the backend; you don't need to understand everything in
## this file. Check out accessible_audio_frontend.rpy for examples and code you
## can modify!
##
## If you use this tool, credit us as Feniks and Alaric @ feniksdev.com.
##
## Leave a comment on the tool page on itch.io if you run into any issues!
################################################################################
python early:

    def custom_execute_play_music(p):
        """
        Run when the play music statement is executed. This is a replacement
        for the one found in the engine which runs callbacks.
        """

        if p["channel"] is not None:
            channel = eval(p["channel"])
        else:
            channel = "music"

        new_dict = dict(filename=_audio_eval(p["file"]),
                        fadeout=eval(p["fadeout"]),
                        fadein=eval(p["fadein"]),
                        channel=channel,
                        loop=p.get("loop", None),
                        if_changed=p.get("if_changed", False),
                        relative_volume=eval(p.get("volume", "1.0")))

        for cb in PLAY_CALLBACKS:
            cb(new_dict)
        filename = new_dict.pop("filename")
        renpy.music.play(filename, **new_dict)

    def custom_execute_play_sound(p):
        """
        Run when the play sound statement is executed. This is a replacement
        for the one found in the engine which runs callbacks.
        """

        if p["channel"] is not None:
            channel = eval(p["channel"])
        else:
            channel = "sound"

        fadeout = eval(p["fadeout"]) or None

        loop = p.get("loop", False)

        if loop is None:
            loop = config.default_sound_loop

        new_dict = dict(filename=_audio_eval(p["file"]),
                        fadeout=fadeout,
                        fadein=eval(p["fadein"]),
                        loop=loop,
                        channel=channel,
                        relative_volume=eval(p.get("volume", "1.0")))

        for cb in PLAY_CALLBACKS:
            cb(new_dict)
        filename = new_dict.pop("filename")
        renpy.sound.play(filename, **new_dict)


    renpy.statements.registry[("play","music")]["execute"] = custom_execute_play_music
    renpy.statements.registry[("play","sound")]["execute"] = custom_execute_play_sound
    renpy.statements.registry[("play",)]["execute"] = custom_execute_play_music

## Callbacks which are called with information on the file which is set to play
define -100 PLAY_CALLBACKS = [ ]

## License
## THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.