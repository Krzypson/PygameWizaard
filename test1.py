import pygame as pg
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

pg.init()
width = 1000
height=800
window = pg.display.set_mode((width,height),pg.RESIZABLE)
pg.display.set_caption("Czarodziej lmao")
pg.display.set_icon(pg.image.load(os.path.join('Assets','wizhat.png')))
clock=pg.time.Clock()

#wizard
wizard_sprite = pg.image.load(os.path.join('Assets','wizard.png'))
wizard_width,wizard_height = 100,100
wizard_graph = pg.transform.scale(wizard_sprite,(wizard_width,wizard_height))
wizard = pg.Rect(50,250,wizard_width,wizard_height)

#fireball
Fireballs=[]
fireball_sprite = pg.image.load(os.path.join('Assets','fireball.png'))
fireball_width,fireball_height = 100,100
fireball_graph = pg.transform.scale(fireball_sprite,(fireball_width,fireball_height))
fireball_movespeed=8

#border
border_left = 0
border_right = pg.display.Info().current_w - wizard_width
border_top = 0
border_bottom = pg.display.Info().current_h - wizard_height

def DrawBack():
    window.fill((119,241,245))
def DrawWiz():
    window.blit(wizard_graph,(wizard.x,wizard.y))
def DrawFireball():
    for fball in Fireballs:
        window.blit(fireball_graph,(fball.x,fball.y))
def Draw():
    DrawBack()
    DrawWiz()
    DrawFireball()
    pg.display.update()

def WizardMovement():
    wizard_movespeed=4
    keys_pressed = pg.key.get_pressed()
    if(keys_pressed[pg.K_w] and wizard.y > border_top):wizard.y-=wizard_movespeed
    if(keys_pressed[pg.K_s]and wizard.y < border_bottom):wizard.y+=wizard_movespeed
    if(keys_pressed[pg.K_a] and wizard.x > border_left):wizard.x-=wizard_movespeed
    if(keys_pressed[pg.K_d] and wizard.x < border_right):wizard.x+=wizard_movespeed
    
def FireballHandling():
    if(len(Fireballs)>0):
        for fball in Fireballs:
            if fball.x < border_right:
                fball.x+=fireball_movespeed
            else:
                Fireballs.remove(fball)

def main():
    FB=0
    running = True
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                running = False
            if(event.type == pg.KEYDOWN):
                if(event.key == pg.K_SPACE):
                    fireball = pg.Rect(wizard.x,wizard.y,fireball_width,fireball_height)
                    Fireballs.append(fireball)
        WizardMovement()
        Draw()
        FireballHandling()

if __name__=="__main__":
    main()