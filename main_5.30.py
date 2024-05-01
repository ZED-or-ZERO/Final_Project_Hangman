import pygame as pg
import math
import random

from setting import *
from button import Button
# import game
# import graphics
# import records
# import sound



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

        # sounds

        self.back_sound = pg.mixer.Sound("sounds/background_sound_01.mp3")
        self.loose_sound = pg.mixer.Sound("sounds/loose_sound_01.mp3")

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
        text = self.fonts[2].render("DEVELOPER HANGMAN", 1, BLACK)
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
            button.draw(self.win, self.fonts[0])  # Передаем LETTER_FONT

        # Hangman image
        self.win.blit(self.images[self.hangman_status], (150, 100))
        pg.display.update()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.game_over = True  # Выход из игр
            elif event.type == pg.MOUSEBUTTONDOWN:
                m_x, m_y = pg.mouse.get_pos()
                for button in self.buttons:
                    if button.clicked((m_x, m_y)) and button.visible:
                        button.visible = False
                        self.guessed.append(button.letter)
                        if button.letter not in self.word:
                            self.hangman_status += 1 
    
    def check_win_loss(self): 
        # Win condition
        won = True
        for letter in self.word:
            if letter not in self.guessed:
                won = False
                break

        if won:
            self.display_message("You WON!")
            self.game_over = True
            self.won = True

        # Loss condition 
        if self.hangman_status == 6:
            self.display_message(f"You LOST! The word was {self.word}")
            self.game_over = True 
            self.won = False
            

    def reset_game(self):
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
            self.handle_events()  # Обработка событий игры
            self.draw()
            self.check_win_loss()

    def display_message(self, message):
        pg.time.delay(1000) 
        self.win.fill(WHITE)
        text = self.fonts[1].render(message, 1, BLACK)
        self.win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2)) 
        pg.display.update()
        pg.time.delay(3000)

    def backround_sound(self):
        self.back_sound.play()





#!===========================================================

def main_menu():
    game = Game() 
    game.backround_sound() # метод воспроизводит фоновую музыку
    game.handle_events()

    while True:
        # отрисовка меню
        game.win.fill(WHITE)
        text = game.fonts[2].render("Click the Mouse to Play", 1, BLACK)
        game.win.blit(text, (WIDTH / 2 - text.get_width() / 2, 200))
        pg.display.update() 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.game_over = True  # Выход из игр
            elif event.type == pg.MOUSEBUTTONDOWN:
                # Проверка, нажата ли кнопка "Играть"
                # if is_play_button_clicked(event.pos):  # Реализуйте эту функцию
                    game.play()
                    if game.game_over:
                        game.reset_game()
                        
    pg.quit()


if __name__ == "__main__":
    main_menu()