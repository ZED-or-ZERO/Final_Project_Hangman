import pygame as pg
import math

from setting import *

class Button:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter
        self.radius = RADIUS
        self.visible = True

    def draw(self, win, font):
        if self.visible:
            pg.draw.circle(win, BLACK, (self.x, self.y), self.radius, 3)
            text = font.render(self.letter, 1, BLACK)
        else:
            pg.draw.circle(win, BLACK, (self.x, self.y), self.radius)
            text = font.render(self.letter, 1, WHITE)

        win.blit(text, (self.x - text.get_width() / 2, self.y - text.get_height() / 2))

    def clicked(self, mouse_pos):
        x, y = mouse_pos
        dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dis < self.radius