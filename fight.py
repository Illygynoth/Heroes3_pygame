import pygame as pg
import sys
import os
import math
class Field(object):
    def __init__(self):
        self.x=10
        self.y=10*math.sqrt(10)
        self.angle=30
        color=(0,255,0)
    def collide(self):
        
class Fight(object):
    def __init__(self,screen):
        pg.init()
        dis = pg.display.Info()
        screen = pg.display.set_mode((dis.current_w, dis.current_h), pg.FULLSCREEN)
        battlefield = pg.transform.scale(pg.image.load(os.path.join("dessert", "dessert_bf.png")).convert_alpha(),(dis.current_w, dis.current_h))
        bg = pg.transform.scale(pg.image.load(os.path.join("dessert", "dessert_bg.png")).convert_alpha(),(dis.current_w, dis.current_h))
        sk = pg.image.load(os.path.join("skeleton_warrior", "skeleton_warrior.png")).convert_alpha()
        bf = [[Field() for x in range(12)] for y in range(15)]
        mouse = pg.transform.scale(pg.image.load(os.path.join("images_title2", "mouse.png")).convert_alpha(),(int(dis.current_w / 120), int(dis.current_h / 40)))
        pg.mouse.set_visible(False)
        width=dis.current_w/17
        height=dis.current_h/7
        while True:
            mx, my = pg.mouse.get_pos()
            screen.blit(battlefield, (0,0))
            screen.blit(bg, (0, 0))
            width = dis.current_w / 17
            for i in range(27):
                pg.draw.polygon(screen, (0, 255, 0), ((width+20, height+40), (width+60, height+20), (width+100, height+40),(width+100,height+100),(width+60, height+120),(width+20, height+100)), 2)
                width+=80
            screen.blit(sk, (dis.current_w / 20, 0))
            screen.blit(mouse, (mx, my))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
