import pygame.font
from pygame import font
from gan import Gan
from pygame.sprite import Group

class Scores():
    '''вывод игровой информации'''
    def __init__(self, screen, stats):
        '''инициализируем подсчёт очков'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 30)
        self.image_score()
        self.image_hight_score()
        self.image_life_gans()

    def image_score(self):
        '''преобразовывает текст в изображение'''
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_hight_score(self):
        '''рекордная сумма баллов на игре'''
        self.hight_score_image = self.font.render(str(self.stats.hight_score), True, self.text_color, (0, 0, 0))
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.screen_rect.top + 20

    def image_life_gans(self):
        '''количество жизней'''
        self.gans = Group()
        for gan_namber in range(self.stats.gans_left):
            gan = Gan(self.screen)
            gan.rect.x = 15 + gan_namber * gan.rect.width
            gan.rect.y = 20
            self.gans.add(gan)

    def show_score(self):
        '''вывод счёта на экран'''
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.gans.draw(self.screen)