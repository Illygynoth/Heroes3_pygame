import pygame as pg
import sys
import os
pg.init()
screen=pg.display.set_mode((pg.display.Info().current_w,pg.display.Info().current_h),pg.FULLSCREEN)
dis=pg.display.Info()
bg = pg.image.load(os.path.join("images_title2", "background.png")).convert()
bg = pg.transform.scale(bg, (dis.current_w, dis.current_h))
ng = pg.image.load(os.path.join("images_title2", "new_game.png")).convert_alpha()
ng = pg.transform.scale(ng, (dis.current_w, dis.current_h))
lg = pg.image.load(os.path.join("images_title2", "load_game.png")).convert_alpha()
lg = pg.transform.scale(lg, (dis.current_w, dis.current_h))
h = pg.image.load(os.path.join("images_title2", "highscore.png")).convert_alpha()
h = pg.transform.scale(h, (dis.current_w, dis.current_h))
a = pg.image.load(os.path.join("images_title2", "authors.png")).convert_alpha()
a = pg.transform.scale(a, (dis.current_w, dis.current_h))
q = pg.image.load(os.path.join("images_title2", "quit.png")).convert_alpha()
q = pg.transform.scale(q, (dis.current_w, dis.current_h))
def disp(b,n,l,h,a,q):
    screen.blit(b, (0, 0))
    screen.blit(n, (0, 0))
    screen.blit(l, (0, 0))
    screen.blit(h, (0, 0))
    screen.blit(a, (0, 0))
    screen.blit(q, (0, 0))
    pg.display.update()
count = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if ng.get_rect().collidepoint(x, y):
                print("hej")
    if pg.mouse.get_pressed()[2]:
        if count == 0:
            sys.exit(0)
        count-=1
        ng = pg.image.load(os.path.join("images_title2", "new_game.png")).convert_alpha()
        ng = pg.transform.scale(ng, (dis.current_w, dis.current_h))
        lg = pg.image.load(os.path.join("images_title2", "load_game.png")).convert_alpha()
        lg = pg.transform.scale(lg, (dis.current_w, dis.current_h))
        h = pg.image.load(os.path.join("images_title2", "highscore.png")).convert_alpha()
        h = pg.transform.scale(h, (dis.current_w, dis.current_h))
        a = pg.image.load(os.path.join("images_title2", "authors.png")).convert_alpha()
        a = pg.transform.scale(a, (dis.current_w, dis.current_h))
        q = pg.image.load(os.path.join("images_title2", "quit.png")).convert_alpha()
        q = pg.transform.scale(q, (dis.current_w, dis.current_h))
    if pg.mouse.get_pressed()[0]:
        count += 1
        ng = pg.image.load(os.path.join("images_title2", "single_player.png")).convert_alpha()
        ng = pg.transform.scale(ng, (dis.current_w, dis.current_h))
        lg = pg.image.load(os.path.join("images_title2", "multi_player.png")).convert_alpha()
        lg = pg.transform.scale(lg, (dis.current_w, dis.current_h))
        h = pg.image.load(os.path.join("images_title2", "campaign.png")).convert_alpha()
        h = pg.transform.scale(h, (dis.current_w, dis.current_h))
        a = pg.image.load(os.path.join("images_title2", "training.png")).convert_alpha()
        a = pg.transform.scale(a, (dis.current_w, dis.current_h))
        q = pg.image.load(os.path.join("images_title2", "back.png")).convert_alpha()
        q = pg.transform.scale(q, (dis.current_w, dis.current_h))
    disp(bg, ng, lg, h, a, q)
