#!/bin/bash

# Record audio for 30 seconds and save as WAV file
arecord -f cd -t wav -d 30 -r 44100 Sruz_5.wav

# Convert WAV file to MP3 using LAME
lame Sruz_5.wav Sruz_5.mp3
