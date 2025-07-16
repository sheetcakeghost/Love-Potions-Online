# Audio Filters

Audio filters allow a game to change the sound on a channel from what is present in an audio file. This can be used to add effects to the sound, including reverb, delay/echo, and high-pass/low-pass filters.

Audio filters are placed in the renpy.audio.filter module. Although not strictly required, it is recommended that module be aliased to something shorter, like `af`, using:

define af \= renpy.audio.filter

The filters can then be invoked using the  function, like:

$ renpy.music.set\_audio\_filter("music", af.Reverb(0.5))

By default, the filter takes effect at the start of the next audio file queued or played. If you want to apply the filter to the currently playing and queued audio, you can use the replace argument:

$ renpy.music.set\_audio\_filter("music", af.Lowpass(440), replace\=True)

This will apply the filter to the audio as soon as possible.

Finally, you can remove a filter from a channel by passing None as the filter:

$ renpy.music.set\_audio\_filter("music", None)

(It's also possible to give None with replace set to True.)

## Filter Reuse

When a filter is set on a channel, it will filter all audio played on that channel. Specifically, the Comb, Delay, and Reverb filters will continue to output information from old audio files for some time after a new audio file has started playing, provided the filter is not changed.

This means that Ren'Py is storing audio information inside the filter object. Because of this, it is generally not a good idea to share filter objects between channels, or to use a filter object multiple times with a single channel.

## Silence Padding

When an audio filter is active and the last queued sound on a channel finises playing, Ren'Py will add 2 seconds of silence to the channel, to ensure that delay and reverb filters have time to finish playing.

If you need more silence, it can be queued with:

queue sound "<silence 10"\>

## Audio Filters

Whenever a filter is accepted, a list may be given instead, to represent a  of those filters. So writing:

renpy.music.set\_audio\_filter("music", \[af.Reverb(0.5), af.Lowpass(440)\])

is equivalent to:

renpy.music.set\_audio\_filter("music",
    af.Sequence(\[
        af.Reverb(0.5),
        af.Lowpass(440),
        \]))

Apart from that, the audio filters consist of the following classes. It's not possible to define your own, for performance reasons.

renpy.audio.filter.Allpass(_frequency\=350_, _q\=1.0_)

An allpass filter allows all frequencies through, but changes the phase relationship between the various frequencies.

frequency

The frequency at the center of the phase change.

q

Controls the sharpness of the phase shift. The higher the value, the sharper the phase shift.

renpy.audio.filter.Bandpass(_frequency\=350_, _q\=1.0_)

A bandpass filter.

frequency

The center frequency.

q

Controls the width of the band. The width becomes narrower as the value of Q increases.

_class_ renpy.audio.filter.Comb(_delay_, _filter\=None_, _multiplier\=1.0_, _wet\=True_)

A comb filter. A comb filter consists of a delay that is filtered and mutiplied, mixed with its input, and then fed back into the delay, causing the filter to be applied multiple times.

delay

The delay, in seconds. If a list of delays is provided, each subchannel will be delayed by the corresponding amount. Each delay must be at least 0.01 seconds.

filter

The filter to apply to the delayed signal. If None, the Null filter is used.

multiplier

The amount to multiply the filtered signal by.

wet

If True, the output of the filter is the sum of the input and the filtered and multiplied signal. If False, the output is just the filtered and muliplied signal.

_class_ renpy.audio.filter.Delay(_delay_)

This filter implements a delay. Samples that are provided to the input emerge from the output after delay seconds.

delay

The delay, in seconds. If a list of delays is provided, each subchannel will be delayed by the corresponding amount. Each delay must be at least 0.01 seconds.

renpy.audio.filter.Highpass(_frequency\=350_, _q\=1.0_)

A highpass filter with 12/dB octave rolloff.

frequency

The cutoff frequency.

q

Controls how peaked the response will be in decibels. For this filter type, this value is not a traditional Q, but is a resonance value in decibels.

renpy.audio.filter.Highshelf(_frequency\=350_, _gain\=0_)

A highshelf filter that allows all frequencies through, but boosts those above a certain frequency by a certain amount.

frequency

The lower frequency.

gain

The amount to boost the frequencies above the lower frequency, in decibels.

renpy.audio.filter.Lowpass(_frequency\=350_, _q\=1.0_)

A lowpass filter with 12/dB octave rolloff.

frequency

The cutoff frequency.

q

Controls how peaked the response will be in decibels. For this filter type, this value is not a traditional Q, but is a resonance value in decibels.

renpy.audio.filter.Lowshelf(_frequency\=350_, _gain\=0_)

A lowshelf filter that allows all frequencies through, but boosts those below a certain frequency by a certain amount.

frequency

The upper frequency.

gain

The amount to boost the frequencies below the upper frequency, in decibels.

_class_ renpy.audio.filter.Mix(_\*filters_)

An audio filter that splits its input into multiple streams, applies each of its arguments to a stream, and mixes those streams by summing them together.

For example:

init python:

    import renpy.audio.filter as af

    \# This mixes the unchanged input with a delay.
    $ echo \= af.Mix(af.Null(), af.Delay(.3))

_class_ renpy.audio.filter.Multiply(_multiplier_)

An audio filter that multiplies its input by multiplier.

renpy.audio.filter.Notch(_frequency\=350_, _q\=1.0_)

The opposite of a bandpass filter. Frequencies inside a range surrounding frequency are suppressed, while other frequences are passed through.

frequency

The center frequency.

q

Controls the width of the notch. The width becomes narrower as the value of q increases.

_class_ renpy.audio.filter.Null

An audio filter that passes it's input through to its output unchanged.

renpy.audio.filter.Peaking(_frequency\=350_, _q\=1.0_, _gain\=0_)

A peaking filter that allows all frequencies through, but boosts those around a certain frequency by a certain amount.

frequency

The center frequency.

q

Controls the sharpness of the peak. The higher the value, the sharper the peak.

gain

The amount to boost the frequencies around the center frequency, in decibels.

renpy.audio.filter.Reverb(_resonance\=.5_, _dampening\=880_, _wet\=1.0_, _dry\=1.0_, _delay\_multiplier\=1.0_, _delay\_times\=\

An artificial reverb filter that simulates the sound of a room or hall, somewhat inspired by Freeverb.

resonance

The amount of feedback in the reverb. This should be between 0 and 1. Larger numbers make the reverb last longer. Too large values will cause the reverb to go out of control.

dampening

This applies a lowpass filter to each reverberation, simulating the lost of high frequences as sound passes through the air.

wet

A multiplier that is applied to the reverb signal before it is passed to the output.

dry

A multiplier that is applied to the input signal before it is passed to the output. Set this to 0.0 to only hear the reverb, not the original sound.

delay\_multiplier

A multiplier that is applied to the delay times. This can be used to adjust the length of the reverb.

delay\_times

A list of delay times, in seconds, that are used to create the early reflections. These are used to create comb filters.

delay\_subchannel

The amount of time, in seconds, that is added to each delay time to create a second subchannel. This is used to create a stereo effect.

allpass\_frequences

A list of frequences, in hertz, that are used to create allpass filters that simulate late reflections.

_class_ renpy.audio.filter.Sequence(_\*filters_)

An AudioFilter that applies its input to a sequence of filters, in order. This is used internally when a list of audiofilters is given, so it should be rare to use this directly.

_class_ renpy.audio.filter.WetDry(_filter_, _wet\=1.0_, _dry\=1.0_)

A filter that mixes its input with the output of a filter.

filter

The filter to apply to the input.

wet

A multiplier, generally between 0.0 and 1.0, that controls the amount of the filter that is mixed in.

dry

A multiplier, generally between 0.0 and 1.0, that controls the amount of the input that is mixed in.
