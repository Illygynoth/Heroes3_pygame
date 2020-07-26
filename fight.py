#Note: there are no turns for now, so movement range in the program can be different than the value in the monsters base
import pygame as pg
import sys
import os
from monsters import monsters
from heroes import heroes
#not important for now, could be done with variables
class Field(object):
    def __init__(self):
        self.x=20
        self.color=(0,255,0)
def quicksort(tab,l,p):
    v = tab[int((l+p)/2)]["spd"]
    i=l
    j=p
    while True:
        while tab[i]["spd"]>v:
            i+=1
        while tab[j]["spd"]<v:
            j-=1
        if i<=j:
            x=tab[i]
            tab[i]=tab[j]
            tab[j]=x
            i+=1
            j-=1
        if i>j:
            break
    if j > l:
        quicksort(tab,l,j)
    if i < p:
        quicksort(tab,i,p)
    else:
        return tab
def move(j,value_of_y,i,value_of_x,name):
    #c is value returning, help is number of grids that must be deleted from movement,speed is for checking if number of row is even and speed2 is only to eliminate problem with odd speed of unit
    c=0
    help=0
    speed=0
    speed2=speed+2
    while speed <= monsters[name]["spd"]:
        if abs(j - value_of_y) <= speed2 and abs(j - value_of_y) > speed:
            if value_of_y % 2 == 0 and j % 2 == 1 and i > value_of_x or value_of_y % 2 == 1 and j % 2 == 0 and i < value_of_x:
                c = help
            else:
                c = help+1
        help=help+1
        speed=speed+2
        if monsters[name]["spd"]-speed==1:
            speed2=speed+1
        else:
            speed2=speed+2
    return c
class Fight(object):
    def __init__(self,screen):
        pg.init()
        dis = pg.display.Info()
        #initializing size of battlefield to fullscreen and convering alpha channel
        battlefield = pg.transform.scale(pg.image.load(os.path.join("dessert", "dessert_bf.png")).convert_alpha(),(dis.current_w, dis.current_h))
        bg = pg.transform.scale(pg.image.load(os.path.join("dessert", "dessert_bg.png")).convert_alpha(),(dis.current_w, dis.current_h))
        sk = pg.image.load(os.path.join("skeleton_warrior", "skeleton_warrior.png")).convert_alpha()
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
        h=[]
        h.append(heroes["Sandro"])
        iAMamonster = []
        monsters_pic = []
        monsters_xy=[]
        value_of_xy=[]
        for i in h[0]["slot"]:
            #loading names of monsters to not write all of this all the time
            iAMamonster.append(h[0]["slot"][i])
        for i in range(len(iAMamonster)):
            #loading pictures of monsters
            monsters_pic.append(pg.image.load(os.path.join(iAMamonster[i]["name"],iAMamonster[i]["name"]+".png")).convert_alpha())
        #initializing hitbox for every tile
        for j in range(sizeY):
            if type == "odd":
                type = "even"
                width = dis.current_w / 17
            elif type == "even":
                type = "odd"
                width = dis.current_w / 26
            new=[]
            for i in range(count):
                new.append([width+b.x,width+b.x*5,height+b.x*2,height+b.x*5])
                width+=b.x*4
            bf.append(new)
            height+=b.x*4
        #initializing current pos for unit, and coordinates of tiles it's standing on
        for i in range(len(iAMamonster)):
            monsters_xy.append((bf[5][0][0] - 5, bf[5][i*2][2] - 50,h[0]["slot"][str(i+1)]["name"]))
            value_of_xy.append((0,i*2))
        print(monsters_xy)
        current_posX, current_posY = bf[5][0][0] - 5, bf[5][5][2] - 50
        value_of_x=0
        value_of_y=5
        iAMamonster=quicksort(iAMamonster,0,len(iAMamonster)-1)
        while True:
            mx, my = pg.mouse.get_pos()
            screen.blit(battlefield, (0,0))
            screen.blit(bg, (0, 0))
            type = "even"
            height = dis.current_h / 7
            for j in range(sizeY):
                if type=="odd":
                    type = "even"
                    width = dis.current_w / 17
                elif type=="even":
                    type="odd"
                    width = dis.current_w / 25
                for i in range(count):
                    c = 0
                    #drawing tiles, in different colour if it's in range of unit's movement
                    c=move(j,value_of_y,i,value_of_x,iAMamonster[1]["name"])
                    if abs(j-value_of_y)+abs(i-value_of_x)-c < monsters[iAMamonster[1]["name"]]["spd"]+1:
                        pg.draw.polygon(screen, (0,0,255), ((width+b.x, height+b.x*2), (width+b.x*3, height+b.x), (width+b.x*5, height+b.x*2),(width+b.x*5,height+b.x*5),(width+b.x*3, height+b.x*6),(width+b.x, height+b.x*5)), 2)
                    else:
                        pg.draw.polygon(screen, b.color, ((width + b.x, height + b.x * 2), (width + b.x * 3, height + b.x),(width + b.x * 5, height + b.x * 2), (width + b.x * 5, height + b.x * 5), (width + b.x * 3, height + b.x * 6), (width + b.x, height + b.x * 5)), 2)
                    width+=b.x*4
                height+=b.x*4
            screen.blit(monsters_pic[1], (monsters_xy[0][0], monsters_xy[0][1]))
            screen.blit(mouse, (mx, my))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit(0)
                if event.type == pg.MOUSEBUTTONUP:
                    for j in range(sizeY):
                        #checking if which tile has been clicked (if has) and determining if it was in unit's range
                        #PROBLEM SOLVED: to go left/right unit has to move up/down taking movement point which doesn't make sense at that grid
                        #PROBLEM SOLVED: redundancy
                        #PROBLEM SOLVED: unit can go further
                        c=0
                        for i in range(15):
                            c=move(j,value_of_y,i,value_of_x,iAMamonster[1]["name"])
                            if bf[j][i][2] < my and bf[j][i][3] > my and bf[j][i][0] < mx and bf[j][i][1] > mx and  abs(abs(j-value_of_y) + abs(i-value_of_x)-c) < monsters[iAMamonster[1]["name"]]["spd"]+1:
                                #PROBLEM: tuple cannot be assigned
                                monsters_xy[0][0],monsters_xy[0][1]=bf[j][i][0]-5,bf[j][i][2]-50
                                value_of_xy[0][0],value_of_xy[0][1]=j,i
