import pygame as pg 

def load_back_sound():
    pg.mixer.init()
    back_sound = pg.mixer.Sound("sounds/background_sound_01.mp3")
    return back_sound

def play_back_sound(back_sound):
    back_sound.play()

def stop_back_sound(back_sound):
    back_sound.stop()

def play_lost_sound():
    pg.mixer.music.stop()
    pg.mixer.music.load("sounds\lost_sound_01.mp3")
    pg.mixer.music.play()

def play_won_sound():
    pg.mixer.music.stop()
    pg.mixer.music.load("sounds\win_sound.mp3")
    pg.mixer.music.play()

def play_click_sound():
    pg.mixer.music.load("sounds\click_sound.mp3")
    pg.mixer.music.play(fade_ms=1)