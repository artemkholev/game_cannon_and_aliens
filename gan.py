import pygame
from pygame.sprite import Sprite

class Gan(Sprite):
    '''инициализация пушки'''
    def __init__(self, screen):
        super(Gan, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('фото/пушка.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        '''отрисовка пушки'''
        self.screen.blit(self.image, self.rect)

    def update_gan(self):
        '''обновление позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.5
        elif self.mleft and self.rect.left > 0:
            self.center -= 0.5

        self.rect.centerx = self.center

    def create_gan(self):
        '''размещает пушку по центру'''
        self.center = self.screen_rect.centerx