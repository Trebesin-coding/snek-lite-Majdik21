import pygame as pg
from sys import exit
import random 

pg.init()

screen_width = 800
screen_height = 800

screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
running = True

player_surf = pg.image.load('img/player.png').convert_alpha()
player_x = 150
player_y = 50
player_rect = player_surf.get_rect(midbottom=(player_x,player_y))
player_speed = 2
player_score = 0


coinr_surf = pg.image.load('img/coinr.png').convert_alpha()
coinr_x = random.randint(0, screen_width)
coinr_y = random.randint(0, screen_height)
coinr_rect = coinr_surf.get_rect(midbottom=(coinr_x,coinr_y))

font = pg.font.Font('img/AmaticSC-Regular.ttf', 25)

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            exit()
    
    key = pg.key.get_pressed()
    if key[pg.K_d]:
        player_rect.right += player_speed
    if key[pg.K_a]:
        player_rect.left -= player_speed
    if key[pg.K_w]:
        player_rect.top -= player_speed
    if key[pg.K_s]:
        player_rect.bottom += player_speed

    
    screen.fill('white')

    score = font.render(f'score: {player_score}', False, '#ffffff')

    screen.blit(player_surf, (player_rect))
    screen.blit(coinr_surf, (coinr_rect))

    if player_rect.colliderect(coinr_rect):
        player_score += 1
        coinr_x = random.randint(0, screen_width)
        coinr_y = random.randint(0, screen_height)
        coinr_rect = coinr_surf.get_rect(midbottom=(coinr_x,coinr_y))
