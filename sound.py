import pygame as pg 

def play_back_sound():
    pg.mixer.music.load("sounds/background_sound_01.mp3")
    pg.mixer.music.play(-1)

def play_lost_sound():
    pg.mixer.music.stop()
    pg.mixer.music.load("sounds\lost_sound_01.mp3")
    pg.mixer.music.play()

def play_won_sound():
    pg.mixer.music.stop()
    pg.mixer.music.load("sounds\win_sound.mp3")
    pg.mixer.music.play()