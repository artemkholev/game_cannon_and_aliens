import pygame, controls
import sys
from gan import Gan
from pygame.sprite import Group
from status import Stats
from score import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption('Космические защитники')
    bg_color = (0, 0, 0)
    gan = Gan(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gan, bullets)
        if stats.run_game == True:
            gan.update_gan()
            controls.update_film(bg_color, screen, stats, sc, gan, inos, bullets)
            controls.bullets_update(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gan, inos, bullets)
run()