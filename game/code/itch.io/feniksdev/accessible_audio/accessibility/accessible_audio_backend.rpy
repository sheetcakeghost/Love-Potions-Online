################################################################################
##
## Sound Disabler and Captions Tool for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## and Alaric (just-write-studios.itch.io) v1.0
##
################################################################################
## This file contains the code for the backend of the accessible audio system.
## It has a backend to store information on audio files. It has two main
## functions: first, it can display audio captions to the player. Second, a
## special screen allows players to toggle off individual audio files.
##
## This file is just the backend; you don't need to understand everything in
## this file. Check out accessible_audio_frontend.rpy for examples and code you
## can modify!
##
## If you use this tool, credit us as Feniks and Alaric @ feniksdev.com.
##
## Leave a comment on the tool page on itch.io if you run into any issues!
################################################################################
init -100 python:

    class AAudioData():
        """
        A class which stores and categorizes information on an audio file
        so it can be used with audio captions and an audio filtering system.
        """
        ## A dictionary of categories to lists of AAudioData objects
        category_dict = { }
        ## A dictionary of paths to AAudioData objects
        path_to_data = { }
        def __init__(self, name, caption, description=None, categories=None,
                path=None, replacement_file="audio/special_silence.ogg"):
            """
            A class to store information on an audio file for use with audio
            captions and categorization.

            Parameters:
            -----------
            name : str
                The name of the audio file. Optional, but used for easier
                organization. If provided and it's a valid variable name, it
                will also declare this in the audio namespace.
            caption : str
                A caption that will be used with audio captions e.g. "footsteps"
            description : str
                Optional. A description of the audio file, for categorization.
                If not provided, defaults to the caption. You may wish to be
                more descriptive here e.g. "footsteps on a wet surface".
            categories : list of str
                A list of categories this sound belongs to. Used for
                categorizing sounds to be toggled off individually.
            path : str
                The path to the audio file. If not provided, it will be
                constructed out of the DEFAULT_FOLDER, the first category in
                the list, and the name of the audio file.
            replacement_file : str
                If provided, this is an audio file that should play instead of
                this file if it is turned off. Usually this is just 1.0 seconds
                of silence, but you may wish to change it to a particular length
                of silence instead so as not to throw off animation timing.
                e.g. "<silence 1.2>"
                Note that "<silence 1.0>" can only be used for in-game sounds,
                not for UI played via activate_sound or hover_sound. The
                included special_silence.ogg file is 1 second of silence and
                can be used to replace UI sounds.
            """
            self.name = name
            self.caption = caption
            self.description = description or self.caption
            self.categories = categories or [ ]
            self.replacement_file = replacement_file
            if path is not None:
                self.path = path
            else:
                if self.categories:
                    cat_name = self.categories[0] + "/"
                else:
                    cat_name = ""
                self.path = "{}/{}{}.{}".format(aaudio.DEFAULT_FOLDER, cat_name,
                    self.name.lower(), aaudio.DEFAULT_EXTENSION)
            for cat in self.categories:
                AAudioData.category_dict.setdefault(cat, set()).add(self)
            AAudioData.path_to_data[self.path] = self
            ## Declare this in the audio namespace
            audio.__dict__.setdefault(self.name, self.path)

        def __repr__(self):
            return "<AAudioData: {}>".format(self.name)

    def find_missing_audio_declarations():
        """
        A function which searches through files in the DEFAULT_FOLDER and
        alerts the developer if there are any audio files which are not
        declared as AAudioData or whose category name is undefined.
        """
        files = renpy.list_files()
        undeclared = [ ]
        for file in files:
            if file.startswith(aaudio.DEFAULT_FOLDER):
                if (file not in AAudioData.path_to_data):
                    undeclared.append(file)

        ## Make a pretty print of the text to declare the files which can
        ## be copied to the clipboard.
        pretty = [ ]
        for file in undeclared:
            import os
            basename = os.path.basename(file)
            base, ext = os.path.splitext(basename)

            if not ext.lower() in [ ".wav", ".mp2", ".mp3", ".ogg", ".opus", ".flac" ]:
                continue

            if base == "special_silence" and ext.lower() == ".ogg":
                ## No need to label the special silence file
                continue

            base = base.lower()
            ## Check if it's in a sub-folder and use that as the category
            ## name if so.
            split = file.split("/")
            cat_name = split[-2] if len(split) > 2 else ""
            pretty.append("    AAudioData(\"{}\", categories=[\"{}\"], path=\"{}\",".format(
                base, cat_name, file))
            pretty.append("        caption=_(\""
                ## We have to split up the line here or translation won't
                ## work because it's trying to identify this as a translatable
                ## string.
                + "\"), description=None)")

        if pretty:
            pretty.insert(0, "init python:")

        ## Now check if there are any missing category names
        missing_categories = []
        for cat in AAudioData.category_dict.keys():
            if cat not in aaudio.CATEGORY_NAMES:
                missing_categories.append("define aaudio.CATEGORY_NAMES[\"{}\"] = _(".format(cat)
                    ## The split is necessary here also.
                    + "\"{}\")".format(cat.capitalize()))

        if pretty:
            pretty_text = "\n".join(pretty)
        else:
            pretty_text = ""

        if missing_categories:
            pretty_text += "\n" + "\n".join(missing_categories)

        if pretty_text:
            store.persistent.missing_audio_declarations = pretty_text
        else:
            store.persistent.missing_audio_declarations = None
        return

    def display_audio_caption(info):
        """
        info is a dictionary with information on filename, fadeout, fadein,
        loop, channel, and relative_volume (and optionally if_changed). This
        function will display an audio caption for the file, if it is available.
        """
        if not persistent.audio_captions_on:
            return
        audio_caption_notify(info['filename'], info["channel"], )

    def audio_caption_notify(filename, channel=None):
        """
        A function which displays an audio caption for the provided filename
        on the provided channel, if there is an AAudioData declaration for it.
        """
        adata = AAudioData.path_to_data.get(filename, None)
        if adata is None:
            return
        if adata.caption:
            prefix = aaudio.CHANNEL_TO_CAPTION_PREFIX.get(channel, "")
            if prefix:
                caption = "{} {}".format(renpy.translate_string(prefix), renpy.translate_string(adata.caption))
            else:
                caption = renpy.translate_string(adata.caption)
            renpy.notify(caption)

    def replace_audio_files(filename):
        """
        A function which will replace the provided filename with silence if
        the player has this sound toggled off.
        """
        adata = AAudioData.path_to_data.get(filename, None)
        if adata is None:
            return filename
        if adata.path in persistent.excluded_sounds:
            return adata.replacement_file
        return filename

    def toggle_category_membership(category):
        """
        A function which will toggle all sounds in a category on or off.
        """
        is_on = all([ aa.path in persistent.excluded_sounds for aa in AAudioData.category_dict[category] ])
        for aa in AAudioData.category_dict[category]:
            if is_on:
                persistent.excluded_sounds.remove(aa.path)
            else:
                persistent.excluded_sounds.add(aa.path)

    def stop_all_audio(channels=None):
        """
        Stop the music on the provided channels, and add any songs playing
        on them to the excluded sounds set. Ensure the periodic callback is set
        up to stop this music upon resuming the game.
        """
        for channel in channels:
            playing = renpy.music.get_playing(channel)
            renpy.music.stop(channel)
            if playing:
                ## Try to add this to the excluded sounds set
                persistent.excluded_sounds.add(playing)
        store.channels_to_stop.update(channels)
        if stop_excluded_sounds not in config.periodic_callbacks:
            config.periodic_callbacks.append(stop_excluded_sounds)

    def check_stop_sounds(excluded):
        """
        Checks if any new sounds were added to the excluded list. If so,
        sets up the periodic callback to ensure they are stopped.
        """
        if persistent.excluded_sounds == excluded:
            return
        else:
            ## Need to make sure none of these sounds are playing when
            ## the game resumes.
            store.sounds_to_stop = persistent.excluded_sounds - excluded
        if store.sounds_to_stop and stop_excluded_sounds not in config.periodic_callbacks:
            config.periodic_callbacks.append(stop_excluded_sounds)

    def stop_excluded_sounds():
        """
        A callback called periodically by Ren'Py. Used to stop unwanted
        sounds from playing.
        """
        if _menu:
            return
        if store.channels_to_stop:
            to_check = set(aaudio.USED_CHANNELS) - store.channels_to_stop
            for channel in store.channels_to_stop:
                renpy.music.stop(channel)
            store.channels_to_stop.clear()
        else:
            to_check = aaudio.USED_CHANNELS

        if store.sounds_to_stop:
            for channel in to_check:
                playing = renpy.music.get_playing(channel)
                if playing and playing in store.sounds_to_stop:
                    renpy.music.stop(channel)
            store.sounds_to_stop.clear()

        ## Remove itself from the periodic callbacks, as its job is done
        ## so there's no need to keep calling it.
        config.periodic_callbacks.remove(stop_excluded_sounds)

    def capitalize_first(s):
        """
        Capitalize the first letter of a string, and leave the rest of
        the capitalization untouched.
        """
        return s[0].upper() + s[1:]

    class TurnOffAudio(Action):
        """
        A screen action which turns off all currently playing audio on the
        provided channels, and queues up the periodic function to ensure
        they are stopped when the game resumes. Also adds these sounds to the
        excluded sounds set.
        """
        def __init__(self, channels):
            self.channels = channels
        def get_sensitive(self):
            return any(renpy.music.get_playing(channel) for channel in self.channels)
        def __call__(self):
            stop_all_audio(self.channels)
            renpy.restart_interaction()


init 100 python:
    if config.developer:
        ## Check for missing audio declarations
        find_missing_audio_declarations()

init -200 python in aaudio:
    _constant = True
    ## The default folder for any audio declarations
    DEFAULT_FOLDER = "audio"
    ## The default extension for audio files
    DEFAULT_EXTENSION = "ogg"
    ## The channels used for sounds the player can turn off. Add custom
    ## channels to this.
    USED_CHANNELS = [ "music", "sound" ]
    CATEGORY_NAMES = dict()
    CHANNEL_TO_CAPTION_PREFIX = dict()

default persistent.missing_audio_declarations = None
default persistent.audio_captions_on = False
default persistent.excluded_sounds = set()
default channels_to_stop = set()
default sounds_to_stop = set()

define PLAY_CALLBACKS += [ display_audio_caption ]
define config.audio_filename_callback = replace_audio_files

## License
## THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.