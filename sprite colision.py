import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED = 5
FONT_SIZE = 72


pygame.init()
background_image = pygame.transform.scale(pygame.image.load("bj.jpg"),
                                          (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color,height,width):
        super().__init__()
        self.image=pygame.surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect=self.image.get_rect()
        def move(self,x_change, y_change)