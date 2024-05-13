import os
import pygame

def play_mp3(mp3_file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

def main():
    mp3_file = '/home/sruthi_32/Sruz_3.mp3'  # Absolute path to your MP3 file
    play_mp3(mp3_file)

if __name__ == "__main__":
    main()
