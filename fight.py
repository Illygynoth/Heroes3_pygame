import pygame as pg
import sys
import os
class Fight(object):
    def __init__(self,screen):
        pg.init()
        dis = pg.display.Info()
        screen = pg.display.set_mode((dis.current_w, dis.current_h), pg.FULLSCREEN)
        bg = pg.transform.scale(pg.image.load(os.path.join("dessert", "dessert.png")).convert(),(dis.current_w, dis.current_h))
        sk = pg.image.load(os.path.join("skeleton_warrior", "skeleton_warrior.png")).convert_alpha()
        while True:
            screen.blit(bg, (0,0))
            screen.blit(sk, (0, 0))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)