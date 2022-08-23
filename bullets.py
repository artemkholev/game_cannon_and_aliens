import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gan):
        '''Создание пули из пушки'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 10)
        self.color = (139, 195, 74)
        self.speed = 10
        self.rect.centerx = gan.rect.centerx
        self.rect.top = gan.rect.top
        self.y = float(self.rect.y)

    def update(self):
        '''Перемещение пули вверх'''
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''отрисовка пули'''
        pygame.draw.rect(self.screen, self.color, self.rect)