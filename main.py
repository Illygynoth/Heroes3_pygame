import pygame as pg
import sys
import os
pg.init()
screen=pg.display.set_mode((pg.display.Info().current_w,pg.display.Info().current_h),pg.FULLSCREEN)
bg = pg.image.load(os.path.join("images_title", "background.png")).convert()
bg = pg.transform.scale(bg, (pg.display.Info().current_w, pg.display.Info().current_h))
ng = pg.image.load(os.path.join("images_title", "new_game.png")).convert_alpha()
ng = pg.transform.scale(ng, (pg.display.Info().current_w, pg.display.Info().current_h))
lg = pg.image.load(os.path.join("images_title", "load_game.png")).convert_alpha()
lg = pg.transform.scale(lg, (pg.display.Info().current_w, pg.display.Info().current_h))
h = pg.image.load(os.path.join("images_title", "highscore.png")).convert_alpha()
h = pg.transform.scale(h, (pg.display.Info().current_w, pg.display.Info().current_h))
a = pg.image.load(os.path.join("images_title", "authors.png")).convert_alpha()
a = pg.transform.scale(a, (pg.display.Info().current_w, pg.display.Info().current_h))
q = pg.image.load(os.path.join("images_title", "quit.png")).convert_alpha()
q = pg.transform.scale(q, (pg.display.Info().current_w, pg.display.Info().current_h))
count=0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
    screen.blit(bg, (0, 0))
    if count == 0:
        screen.blit(ng, (0, 0))
        screen.blit(lg, (0, 0))
        screen.blit(h, (0, 0))
        screen.blit(a, (0, 0))
        screen.blit(q, (0, 0))
        pg.display.update()
    if pg.mouse.get_pressed()[0]:
        ng = pg.image.load(os.path.join("images_title", "single_player.png")).convert_alpha()
        ng = pg.transform.scale(ng, (pg.display.Info().current_w, pg.display.Info().current_h))
        lg = pg.image.load(os.path.join("images_title", "multi_player.png")).convert_alpha()
        lg = pg.transform.scale(lg, (pg.display.Info().current_w, pg.display.Info().current_h))
        h = pg.image.load(os.path.join("images_title", "campaign.png")).convert_alpha()
        h = pg.transform.scale(h, (pg.display.Info().current_w, pg.display.Info().current_h))
        a = pg.image.load(os.path.join("images_title", "training.png")).convert_alpha()
        a = pg.transform.scale(a, (pg.display.Info().current_w, pg.display.Info().current_h))
        q = pg.image.load(os.path.join("images_title", "back.png")).convert_alpha()
        q = pg.transform.scale(q, (pg.display.Info().current_w, pg.display.Info().current_h))
        count=1
    if count == 1:
        screen.blit(ng, (0, 0))
        screen.blit(lg, (0, 0))
        screen.blit(h, (0, 0))
        screen.blit(a, (0, 0))
        screen.blit(q, (0, 0))
        pg.display.update()
