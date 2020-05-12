import pygame as pg
import sys
import os
from fight import Fight
pg.init()
screen=pg.display.set_mode((pg.display.Info().current_w,pg.display.Info().current_h),pg.FULLSCREEN)
dis=pg.display.Info()
bg = pg.transform.scale(pg.image.load(os.path.join("images_title2", "background.png")).convert(), (dis.current_w, dis.current_h))
ng=pg.image.load(os.path.join("images_title2", "new_game.png")).convert_alpha()
ng_mask=pg.mask.from_surface(ng)
lg=pg.image.load(os.path.join("images_title2", "load_game.png")).convert_alpha()
lg_mask=pg.mask.from_surface(lg)
h=pg.image.load(os.path.join("images_title2", "highscore.png")).convert_alpha()
h_mask=pg.mask.from_surface(h)
a=pg.image.load(os.path.join("images_title2", "authors.png")).convert_alpha()
a_mask=pg.mask.from_surface(a)
q=pg.image.load(os.path.join("images_title2", "quit.png")).convert_alpha()
q_mask=pg.mask.from_surface(q)
nbg=pg.image.load(os.path.join("images_title2", "new_game_bg.png")).convert_alpha()
mouse=pg.image.load(os.path.join("images_title2", "mouse.png")).convert_alpha()
mouse_mask=pg.mask.from_surface(mouse)
def load(name1,name2,name3,name4,name5,name6,name7):
    global bg,ng,lg,h,a,q,nbg,ng_mask,lg_mask,h_mask,a_mask,q_mask
    bg = pg.transform.scale(pg.image.load(os.path.join("images_title2", name1)).convert(), (dis.current_w, dis.current_h))
    ng = pg.transform.scale(pg.image.load(os.path.join("images_title2", name2)).convert_alpha(), (int(dis.current_w/6), int(dis.current_h/5)))
    ng_mask = pg.mask.from_surface(ng)
    lg = pg.transform.scale(pg.image.load(os.path.join("images_title2", name3)).convert_alpha(), (int(dis.current_w/6), int(dis.current_h/5)))
    lg_mask = pg.mask.from_surface(lg)
    h = pg.transform.scale(pg.image.load(os.path.join("images_title2", name4)).convert_alpha(), (int(dis.current_w/6), int(dis.current_h/5)))
    h_mask = pg.mask.from_surface(h)
    a = pg.transform.scale(pg.image.load(os.path.join("images_title2", name5)).convert_alpha(), (int(dis.current_w/6), int(dis.current_h/5)))
    a_mask = pg.mask.from_surface(a)
    q = pg.transform.scale(pg.image.load(os.path.join("images_title2", name6)).convert_alpha(), (int(dis.current_w/6), int(dis.current_h/5)))
    q_mask = pg.mask.from_surface(q)
    nbg = pg.transform.scale(pg.image.load(os.path.join("images_title2", name7)).convert_alpha(), (dis.current_w, dis.current_h))
def disp(b,n,l,h,a,q,g,m,count,type,x,y):
    screen.blit(b, (0, 0))
    screen.blit(n, (int(dis.current_w*6/8), int(dis.current_h/50)))
    screen.blit(l, (int(dis.current_w*6/8), int(dis.current_h*10/50)))
    screen.blit(h, (int(dis.current_w*6/8), int(dis.current_h*20/50)))
    screen.blit(a, (int(dis.current_w*6/8), int(dis.current_h*30/50)))
    screen.blit(q, (int(dis.current_w*6/8), int(dis.current_h*40/50)))
    screen.blit(m, (x, y))
    if count ==1 and (type=="new" or type=="load"):
        screen.blit(g, (0,0))
    pg.display.update()
load("background.png","new_game.png","load_game.png","highscore.png","authors.png","quit.png","new_game_bg.png")
count = 0
type=""
while True:
    pg.mouse.set_visible(False)
    mx,my=pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            newgame=ng.get_rect()
            newgame[0]=int(dis.current_w*6/8)
            newgame[1]=int(dis.current_h/50)
            if newgame.collidepoint(x, y) and count == 0:
                load("background.png","single_player.png","multi_player.png","campaign.png","training.png","back.png","new_game_bg.png")
                type="new"
                count=1
            elif newgame.collidepoint(x, y) and count == 1:
                if type=="new":
                    Fight()
            newgame[1] = int(dis.current_h * 10 / 50)
            if newgame.collidepoint(x,y) and count == 0:
                load("background.png", "single_player.png", "multi_player.png", "campaign.png", "training.png", "back.png", "load_game_bg.png")
                type="load"
                count=1
            newgame[1]=int(dis.current_h*40/50)
            if newgame.collidepoint(x,y) and count == 1:
                load("background.png", "new_game.png", "load_game.png", "highscore.png", "authors.png", "quit.png","new_game_bg.png")
                count=0
            elif newgame.collidepoint(x, y) and count == 0:
                sys.exit(0)
    disp(bg, ng, lg, h, a, q, nbg, mouse, count,type,mx,my)
