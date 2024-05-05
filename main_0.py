
#!   ЭТО НУЛЕВОЙ ВАРИАНТ  ! 


import pygame as pg 
import math
import random

from setting import *

# setup display
pg.init()
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hangman Game!")

# button variables
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
letters = []
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pg.font.SysFont('comicsans', LETTER_FONT_SIZE)
WORD_FONT = pg.font.SysFont('comicsans', WORD_FONT_SIZE)
TITLE_FONT = pg.font.SysFont('comicsans', TITLE_FONT_SIZE)

# load images.
images = []
for i in range(7):
    image = pg.image.load('D:\Learning Python\PythonFinalProject\image_text/hangman' + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
word_list = open("D:\Learning Python\PythonFinalProject\image_text/Words.txt").read().split()
word = random.choice(word_list) 
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)


def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pg.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
        else:
            pg.draw.circle(win, BLACK, (x, y), RADIUS)
            text = LETTER_FONT.render(ltr, 1, 'white')

        win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pg.display.update()


def display_message(message):
    pg.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pg.display.update()
    pg.time.delay(3000)

def hidden_word(word):
    win.fill(WHITE)
    pg.mixer.music.stop()
    pg.mixer.music.load("D:\Learning Python\PythonFinalProject\Music\loose.mp3")
    pg.mixer.music.play(0)
    text_real = WORD_FONT.render("Hidden word is ", 1, BLACK)
    text_word = WORD_FONT.render(word, 1, RED)
    
    # Define coordinates to centralize
    text_real_x = (WIDTH - (text_real.get_width() + text_word.get_width())) / 2
    text_word_x = text_real_x + text_real.get_width()
    text_y = (HEIGHT - max(text_real.get_height(), text_word.get_height())) / 2
    
    # Output
    win.blit(text_real, (text_real_x, text_y))
    win.blit(text_word, (text_word_x, text_y))
    pg.display.update()
    pg.time.delay(4000)

#Restart game 
def reset_game():
    global hangman_status
    global word
    global guessed
    global letters
    hangman_status = 0
    word_list = open("D:\Learning Python\PythonFinalProject\image_text/Words.txt").read().split() 
    word = random.choice(word_list)
    guessed = []
    for letter in letters:
        letter[3] = True

def main():
    
    global hangman_status
    FPS = 60
    clock = pg.time.Clock()

    pg.mixer.music.load("D:\Learning Python\PythonFinalProject\Music\elevator ahh type beat.mp3")
    pg.mixer.music.play()

    while True:
        clock.tick(FPS)
        
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                m_x, m_y = pg.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            pg.mixer.music.stop()
            pg.mixer.music.load("D:\Learning Python\PythonFinalProject\Music\win.mp3")
            pg.mixer.music.play(0)
            display_message("You WON!")
            reset_game()


        if hangman_status == 6:
            hidden_word(word)
            display_message("You LOST! Try again!")
            reset_game()
        
    
def main_menu():
    play_game = True
    while play_game:
        win.fill(WHITE)
        text = TITLE_FONT.render("Click the Mouse to Play", 1, BLACK)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, 200))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                play_game = False
            if event.type == pg.MOUSEBUTTONDOWN:
                main()
    pg.quit()

main_menu()
pg.quit()
