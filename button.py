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

    def draw(self, win, font):  # Добавляем аргумент font
        if self.visible:
            pg.draw.circle(win, BLACK, (self.x, self.y), self.radius, 3)
            text = font.render(self.letter, 1, BLACK)  # Используем font
        else: 
            pg.draw.circle(win, BLACK, (self.x, self.y), self.radius)
            text = font.render(self.letter, 1, WHITE)  # Используем font

        win.blit(text, (self.x - text.get_width() / 2, self.y - text.get_height() / 2))

    def clicked(self, mouse_pos):
        x, y = mouse_pos
        dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dis < self.radius



    def play_button_clicked(self, mouse_pos):
        # 1. Определите координаты и размеры кнопки "Играть"
        play_button_x = self.x / 10  # X-координата левого верхнего угла кнопки
        play_button_y = self.y / 10  # Y-координата левого верхнего угла кнопки
        play_button_width = 50       # Ширина кнопки
        play_button_height = 10      # Высота кнопки

        m_x, m_y = mouse_pos

        if (play_button_x <= mouse_x <= play_button_x + play_button_width and
            play_button_y <= mouse_y <= play_button_y + play_button_height):
            return True
        else:
            return False

