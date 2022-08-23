import pygame, sys
from bullets import Bullet
from ino import Ino
import time

def events(screen, gan, bullets):
    '''обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Вправо
            if event.key == pygame.K_RIGHT:
                gan.mright = True
            # Влево
            elif event.key == pygame.K_LEFT:
                gan.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gan)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Вправо
            if event.key == pygame.K_RIGHT:
                gan.mright = False
            # Влево
            if event.key == pygame.K_LEFT:
                gan.mleft = False
def update_film(bg_color, screen, stats, sc, gan, inos, bullets):
    '''обновление экрана'''
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gan.output()
    inos.draw(screen)
    pygame.display.flip()

def bullets_update(screen, stats, sc, inos, bullets):
    '''обновление позиции пули'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    colisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if colisions:
        for ino in colisions.values():
            stats.score += 10 * len(ino)
        sc.image_score()
        check_hight_score(stats, sc)
        sc.image_life_gans()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def gan_kill(stats, screen, sc, gan, inos, bullets):
    '''столкновение пушки и армии'''
    if stats.gans_left > 0:
        stats.gans_left -= 1
        sc.image_life_gans()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gan.create_gan()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, sc, gan, inos, bullets):
    '''обновляет позицию пришельцев'''
    inos.update()
    if pygame.sprite.spritecollideany(gan, inos):
        gan_kill(stats, screen, sc, gan, inos, bullets)
    inos_check(stats, screen, sc, gan, inos, bullets)

def inos_check(stats, screen, sc, gan, inos, bullets):
    '''проверка края'''
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gan_kill(stats, screen, sc, gan, inos, bullets)
            break

def create_army(screen, inos):
    '''создании армии'''
    ino = Ino(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    number_ino_x = int((700 - (2 * ino_width)) / ino_width) - 25
    number_ino_y = int((600 - (2 * ino_height)) / ino_height) - 25

    for row_number in range(number_ino_y):
        for ino_namber in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + 10 + ino_width * ino_namber + (ino_namber * 9)
            ino.y = ino_height + (ino_height * row_number) + 50
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)

def check_hight_score(stats, sc):
    '''проверка новых рекордов'''
    if stats.score > stats.hight_score:
        stats.hight_score = stats.score
        sc.image_hight_score()
        with open('record.txt', 'w') as f:
            f.write(str(stats.hight_score))
