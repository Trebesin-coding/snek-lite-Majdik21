import pygame as pg
from sys import exit
import random 
import datetime as dt

pg.init()

screen_width = 800
screen_height = 800

screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
now = dt.datetime.now()
running = True

speed_boost = True
speed_boost_time = 0
cooldown = 0


def animation(direction):
    global player_index, player_img
    frame_count = 2
 
    player_index += 0.1
    if player_index >= frame_count:
        player_index = 0
     
    player_img = image_cutter(player_spritesheet, int(player_index), direction, 17, 17, 3)

def image_cutter(sheet, frame_x, frame_y, width, height, scale):
    img = pg.Surface((width, height)).convert_alpha()
    img.blit(sheet, (0,0), ((frame_x * width), (frame_y * height), width, height))
    img = pg.transform.scale(img, (width*scale, height*scale))
    img.set_colorkey((0, 0, 0))
    return img


player_spritesheet = pg.image.load("img/player_spritesheet.png").convert_alpha()
player_img = image_cutter(player_spritesheet, 0, 0, 17, 17, 3)
player_x = 150
player_y = 50
player_rect = player_img.get_rect(midbottom=(player_x,player_y))
player_speed = 2
player_index = 0
player_score = 0


coinr_surf = pg.image.load('img/coinr.png').convert_alpha()
coinr_surf = pg.transform.rotozoom(coinr_surf, 0, 1.5)
coinr_x = random.randint(0, screen_width)
coinr_y = random.randint(0, screen_height)
coinr_rect = coinr_surf.get_rect(midbottom=(coinr_x,coinr_y))




font = pg.font.Font('img/AmaticSC-Regular.ttf', 25)
i=0

while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            exit()
    
    
    key = pg.key.get_pressed()
    
    if key[pg.K_d]:
        animation(4)
        player_rect.right += player_speed
    if key[pg.K_a]:
        animation(3)
        player_rect.left -= player_speed
    if key[pg.K_w]:
        animation(1)
        player_rect.top -= player_speed
    if key[pg.K_s]:
        animation(2)
        player_rect.bottom += player_speed
    
    if key[pg.K_LSHIFT] and speed_boost:
        speed_boost_time = 5000
        speed_boost = False
    

    if speed_boost_time > 0:
        player_speed = 5
        speed_boost_time -= clock.get_time()
    else:
        player_speed = 2
        
    if speed_boost_time <= 0 and not speed_boost:
        cooldown += clock.get_time()

    if cooldown >= 20000:
        cooldown = 0
        speed_boost = True
    
    
    screen.fill('black')

    score = font.render(f'score: {player_score}', False, '#ffffff')

    screen.blit(player_img, (player_rect))
    screen.blit(coinr_surf, (coinr_rect))
    screen.blit(score, (screen_width - 80, 30))

    if player_rect.colliderect(coinr_rect):
        player_score += 1
        coinr_x = random.randint(0, screen_width)
        coinr_y = random.randint(0, screen_height)
        coinr_rect = coinr_surf.get_rect(midbottom=(coinr_x,coinr_y))

    pg.display.update()
    clock.tick(60)