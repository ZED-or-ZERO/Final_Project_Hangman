import pygame as py
from game import Game


def main_menu():
    game = Game() 
    game.main_menu() 
    pg.quit()

if __name__ == "__main__":
    main_menu()