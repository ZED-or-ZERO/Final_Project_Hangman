import pygame as pg
import math
import random

from setting import *
from button import Button
from sound import *

back_sound = load_back_sound()
class Game:
    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Hangman Game!")
        self.clock = pg.time.Clock()
        self.hangman_status = 0
        self.images = []

        for i in range(7):
            image = pg.image.load(f'images/hangman{i}.png')
            self.images.append(image)

        self.word_list = open("data/Words.txt").read().split()
        self.word = random.choice(self.word_list)
        self.guessed = []
        self.buttons = self.create_buttons()
        self.fonts = self.setup_fonts()
        self.game_over = False
        self.won = False

    def setup_fonts(self):
        LETTER_FONT = pg.font.SysFont('comicsans', LETTER_FONT_SIZE)
        WORD_FONT = pg.font.SysFont('comicsans', WORD_FONT_SIZE)
        TITLE_FONT = pg.font.SysFont('comicsans', TITLE_FONT_SIZE)
        return LETTER_FONT, WORD_FONT, TITLE_FONT

    def create_buttons(self):
        startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
        starty = 400
        letters = []
        A = 65
        for i in range(26):
            x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
            y = starty + ((i // 13) * (GAP + RADIUS * 2))
            letters.append(Button(x, y, chr(A + i)))
        return letters

    def draw(self):
        self.win.fill(WHITE)

        # Title
        text = self.fonts[2].render("Hangman Game", 1, BLACK)
        self.win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

        # Word
        display_word = ""
        for letter in self.word:
            if letter in self.guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        text = self.fonts[1].render(display_word, 1, BLACK)
        self.win.blit(text, (400, 200))

        # Buttons
        for button in self.buttons:
            button.draw(self.win, self.fonts[0]) 

        # Hangman image
        self.win.blit(self.images[self.hangman_status], (150, 100))
        pg.display.update()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.game_over = True  
            elif event.type == pg.MOUSEBUTTONDOWN:
                m_x, m_y = pg.mouse.get_pos()
                for button in self.buttons:
                    play_click_sound()
                    if button.clicked((m_x, m_y)) and button.visible:
                        button.visible = False
                        self.guessed.append(button.letter)
                        if button.letter not in self.word:
                            self.hangman_status += 1 

    def check_win_loss(self):
        won = True
        for letter in self.word:
            if letter not in self.guessed:
                won = False
                break

        if won:
            stop_back_sound(back_sound)
            play_won_sound()
            self.display_message("You WON!")
            self.game_over = True
            self.won = True
            self.reset_game()
            play_back_sound(back_sound)
            

        if self.hangman_status == 6:
            stop_back_sound(back_sound)
            play_lost_sound()
            self.display_message(f"You LOST! The word was {self.word}")
            self.game_over = True
            self.won = False
            self.reset_game()
            play_back_sound(back_sound)
            

    def reset_game(self):
        global hangman_status
        global word
        global guessed
        global letters
        self.hangman_status = 0
        self.word = random.choice(self.word_list)
        self.guessed = []
        for button in self.buttons:
            button.visible = True
        self.game_over = False
        self.won = False

    def play(self):
        while not self.game_over:
            self.clock.tick(60)
            self.handle_events() 
            self.draw()
            self.check_win_loss()

    def display_message(self, message):
        pg.time.delay(1000)
        self.win.fill(WHITE)
        text = self.fonts[1].render(message, 1, BLACK)
        self.win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pg.display.update()
        pg.time.delay(3000)

    def main_menu(self):

        play_back_sound(back_sound)

        play_game = True
        while play_game:
            self.win.fill(WHITE)

            title_text = self.fonts[2].render("Hangman Game", 1, BLACK)
            play_text = self.fonts[1].render("Play", 1, BLACK)

            title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
            play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

            self.win.blit(title_text, title_rect)
            self.win.blit(play_text, play_rect)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    play_game = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    play_game = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    if play_rect.collidepoint(mouse_pos):
                        self.play()
