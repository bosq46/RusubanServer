#!/usr/bin/env python
# -*- cording: utf-8 -*-
import sys
import pygame.mixer
import time


def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(1)
    time.sleep(60)
    pygame.mixer.music.stop()


if __name__ == "__main__":
    # args = sys.argv
    # if len(args) < 2:
    #     print("Please Input MP3 FILE NAME.")
    #     exit(1)
    # play_audio(args[1])
    import glob
    audio_files = glob.glob("./uploads/*")
    if len(audio_files):
        play_audio(audio_files[-1])
