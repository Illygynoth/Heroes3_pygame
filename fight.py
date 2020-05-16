import pygame as pg
import sys
import os

class Field(object):
    def __init__(self):
        self.x=20
        self.color=(0,255,0)

class Fight(object):
    def __init__(self,screen):
        pg.init()
        dis = pg.display.Info()
        battlefield = pg.transform.scale(pg.image.load(os.path.join("dessert", "dessert_bf.png")).convert_alpha(),(dis.current_w, dis.current_h))
        bg = pg.transform.scale(pg.image.load(os.path.join("dessert", "dessert_bg.png")).convert_alpha(),(dis.current_w, dis.current_h))
        sk = pg.image.load(os.path.join("skeleton_warrior", "skeleton_warrior.png")).convert_alpha()
        bf = Field()
        mouse = pg.transform.scale(pg.image.load(os.path.join("images_title2", "mouse.png")).convert_alpha(),(int(dis.current_w / 120), int(dis.current_h / 40)))
        pg.mouse.set_visible(False)
        width=dis.current_w/17
        height=dis.current_h/7
        type="odd"
        count=15
        while True:
            mx, my = pg.mouse.get_pos()
            screen.blit(battlefield, (0,0))
            screen.blit(bg, (0, 0))
            height = dis.current_h / 7
            for j in range(10):
                if type=="odd":
                    count = 15
                    type = "even"
                    width = dis.current_w / 17
                elif type=="even":
                    count = 16
                    type="odd"
                    width = dis.current_w / 26
                for i in range(count):
                    pg.draw.polygon(screen, bf.color, ((width+bf.x, height+bf.x*2), (width+bf.x*3, height+bf.x), (width+bf.x*5, height+bf.x*2),(width+bf.x*5,height+bf.x*5),(width+bf.x*3, height+bf.x*6),(width+bf.x, height+bf.x*5)), 2)
                    width+=80
                height+=80
            screen.blit(sk, (dis.current_w / 20, 0))
            screen.blit(mouse, (mx, my))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit(0)
