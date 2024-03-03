import pygame as pg
import os
from pygame import key

FPS = 60
WIDTH, HEIGHT = 1000, 700
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FLASH_COOLDOWN = 5000
enemy_last_flash_time = 0
hero_last_flash_time=0

PLAYER_HEIGHT, PLAYER_WIDTH = 70, 40
WHITE = (255, 255, 255)
HERO_IMAGE = pg.image.load(os.path.join("/Users/icloud/Documents/joc/shooter/imagini/erou.png"))
ENEMY_IMAGE = pg.image.load(os.path.join("/Users/icloud/Documents/joc/shooter/imagini/inamic.png"))
HERO_IMAGE = pg.transform.scale(
    HERO_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT))
ENEMY_IMAGE = pg.transform.scale(
    ENEMY_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT))

def hero_handle_movement(hero_movement, hero,current_time):
    global hero_last_flash_time
    if hero_movement[pg.K_w]:
        hero.y -= 2
    if hero_movement[pg.K_s]:
        hero.y += 2
    if hero_movement[pg.K_a]:
        hero.x -= 2
    if hero_movement[pg.K_d]:
        hero.x += 2
    if hero_movement[pg.K_f] and current_time - hero_last_flash_time >= FLASH_COOLDOWN:
        flash_performed = False
        if hero_movement[pg.K_a]:
            hero.x -= 70
            flash_performed = True
        if hero_movement[pg.K_d]:
            hero.x += 70
            flash_performed = True
        if hero_movement[pg.K_w]:
            hero.y -= 70
            flash_performed = True
        if hero_movement[pg.K_s]:
            hero.y += 70
            flash_performed = True
        if flash_performed:
            hero_last_flash_time = current_time

def enemy_handle_movement(enemy_movement,enemy,current_time):
    global enemy_last_flash_time
    if enemy_movement[pg.K_UP]:
        enemy.y -= 2
    if enemy_movement[pg.K_DOWN]:
        enemy.y += 2
    if enemy_movement[pg.K_LEFT]:
        enemy.x -= 2
    if enemy_movement[pg.K_RIGHT]:
        enemy.x += 2
    if enemy_movement[pg.K_l] and current_time - enemy_last_flash_time >= FLASH_COOLDOWN:
        flash_performed = False
        if enemy_movement[pg.K_LEFT]:
            enemy.x -= 70
            flash_performed = True
        if enemy_movement[pg.K_RIGHT]:
            enemy.x += 70
            flash_performed = True
        if enemy_movement[pg.K_UP]:
            enemy.y -= 70
            flash_performed = True
        if enemy_movement[pg.K_DOWN]:
            enemy.y += 70
            flash_performed = True
        if flash_performed:
            enemy_last_flash_time = current_time
def draw_window(hero,enemy):
    WIN.fill(WHITE)
    WIN.blit(HERO_IMAGE, (hero.x,hero.y))
    WIN.blit(ENEMY_IMAGE, (enemy.x,enemy.y))
    pg.display.update()

def main():
    run = True
    hero = pg.Rect(200,400,PLAYER_WIDTH,PLAYER_HEIGHT)
    enemy = pg.Rect(700, 400, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pg.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        draw_window(hero,enemy)

        current_time = pg.time.get_ticks()
        hero_movement = key.get_pressed()
        hero_handle_movement(hero_movement,hero,current_time)

        enemy_movement = key.get_pressed()
        enemy_handle_movement(enemy_movement, enemy, current_time)

    pg.quit()
if __name__ == "__main__":
    main()