"""Contains constants used in the program."""

import pyaudio


# Audio stream settings (see
# https://people.csail.mit.edu/hubert/pyaudio/docs/ for more details on
# any of these)
FRAMES_PER_BUFFER = 1024    # number of audio frames per buffer
FORMAT = pyaudio.paInt16    # sampling size and format
CHANNELS = 1                # number of audio channels
RATE = 44100                # sampling rate in Hz

# This is a list of frequency ranges of interest, based mostly on
# intuition and testing, and also information online. Tweaking these may
# lead to better results. There must be exactly 6 frequency bins (for
# now), and their upper limit  must never exceed the sampling rate.
FREQUENCY_BINS = ((60, 150),    # bass (consider going further than 150)
                  (250, 500),   # low midrange
                  (500, 2e3),   # midrange
                  (2e3, 4e3),   # upper midrange
                  (4e3, 6e3),   # "presence"
                  (6e3, 20e3),  # "brilliance"
                 )

# Raspberry Pi GPIO pins to use. The order here matters, and for now
# there must be exactly 6 pins. More on this later.
GPIO_PINS = (12, 18, 22, 36, 38, 40)
