import pygame as pg
import sys
import os
import time
from monsters import monsters
from heroes import heroes
#not important for now, could be done with variables
class Field(object):
    def __init__(self):
        self.x=20
        self.color=(0,255,0)

class Fight(object):
    def __init__(self,screen):
        pg.init()
        dis = pg.display.Info()
        #initializing size of battlefield to fullscreen and convering alpha channel
        battlefield = pg.transform.scale(pg.image.load(os.path.join("dessert", "dessert_bf.png")).convert_alpha(),(dis.current_w, dis.current_h))
        bg = pg.transform.scale(pg.image.load(os.path.join("dessert", "dessert_bg.png")).convert_alpha(),(dis.current_w, dis.current_h))
        sk = pg.image.load(os.path.join("skeleton_warrior", "skeleton_warrior1.png")).convert_alpha()
        sk_mask = pg.mask.from_surface(sk)
        b = Field()
        mouse = pg.transform.scale(pg.image.load(os.path.join("images_title2", "mouse.png")).convert_alpha(),(int(dis.current_w / 120), int(dis.current_h / 40)))
        mouse_mask = pg.mask.from_surface(mouse)
        pg.mouse.set_visible(False)
        #Initializing width and height on the screen for battlefield (actual hexes)
        width=dis.current_w/17
        height=dis.current_h/7
        #How much tiles will be in battlefield in width and height
        count=15
        sizeY=11
        type="even"
        bf=[]
        h=(heroes["Sandro"],heroes["Sandro"])
        #initializing hitbox for every tile
        for j in range(sizeY):
            if type == "odd":
                count = 15
                type = "even"
                width = dis.current_w / 17
            elif type == "even":
                count = 16
                type = "odd"
                width = dis.current_w / 26
            new=[]
            for i in range(count):
                new.append([width+b.x,width+b.x*5,height+b.x*2,height+b.x*5])
                width+=80
            bf.append(new)
            print(bf[j][0])
            height+=80
        #initializing current pos for unit, and numbers of tiles it's standing on
        current_posX, current_posY = bf[5][0][0] + 10, bf[5][5][2] - 20
        value_of_x=0
        value_of_y=5
        while True:
            mx, my = pg.mouse.get_pos()
            screen.blit(battlefield, (0,0))
            screen.blit(bg, (0, 0))
            type = "even"
            height = dis.current_h / 7
            for j in range(sizeY):
                if type=="odd":
                    count = 15
                    type = "even"
                    width = dis.current_w / 17
                elif type=="even":
                    count = 16
                    type="odd"
                    width = dis.current_w / 26
                for i in range(count):
                    #drawing tiles, in different colour if it's in range of unit's movement
                    if abs(j-value_of_y)+abs(i-value_of_x) < monsters["skeleton_warrior"]["spd"]+1:
                        pg.draw.polygon(screen, (0,0,255), ((width+b.x, height+b.x*2), (width+b.x*3, height+b.x), (width+b.x*5, height+b.x*2),(width+b.x*5,height+b.x*5),(width+b.x*3, height+b.x*6),(width+b.x, height+b.x*5)), 2)
                    else:
                        pg.draw.polygon(screen, b.color, ((width + b.x, height + b.x * 2), (width + b.x * 3, height + b.x),(width + b.x * 5, height + b.x * 2), (width + b.x * 5, height + b.x * 5), (width + b.x * 3, height + b.x * 6), (width + b.x, height + b.x * 5)), 2)
                    width+=80
                height+=80
            screen.blit(sk, (current_posX, current_posY))
            screen.blit(mouse, (mx, my))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit(0)
                if event.type == pg.MOUSEBUTTONUP:
                    for i in range(11):
                        #checking if which tile has been clicked (if has) and determining if it was in unit's range
                        #PROBLEM: to go left/right unit has to move up/down taking movement point which doesn't make sense at that grid
                        if i%2==0:
                            for j in range(16):
                                if bf[i][j][2] < my and bf[i][j][3] > my and bf[i][j][0] < mx and bf[i][j][1] > mx and abs(i-value_of_y)+abs(j-value_of_x) <= monsters["skeleton_warrior"]["spd"]+1:
                                    current_posX,current_posY=bf[i][j][0]+10,bf[i][j][2]-20
                                    value_of_y,value_of_x=i,j
                        else:
                            for j in range(15):
                                if bf[i][j][2] < my and bf[i][j][3] > my and bf[i][j][0] < mx and bf[i][j][1] > mx and abs(i-value_of_y)+abs(j-value_of_x) < monsters["skeleton_warrior"]["spd"]+1:
                                    current_posX,current_posY=bf[i][j][0]+10,bf[i][j][2]-20
                                    value_of_y, value_of_x = i, j
