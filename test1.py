import pygame as pg
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

pg.init()
width = 800
height = 600
window = pg.display.set_mode((width,height),pg.RESIZABLE)
pg.display.set_caption("nienawidzę kobiet")
clock=pg.time.Clock()

#wizard
wizard_sprite = pg.image.load(os.path.join('Assets','wizard.png'))
wizard_width,wizard_height = 100,100
wizard_graph = pg.transform.scale(wizard_sprite,(wizard_width,wizard_height))
wizard = pg.Rect(50,250,wizard_width,wizard_height)

#fireball
fireball_sprite = pg.image.load(os.path.join('Assets','fireball.png'))
fireball_width,fireball_height = 100,100
fireball_graph = pg.transform.scale(fireball_sprite,(fireball_width,fireball_height))
fireball = pg.Rect(500,250,fireball_width,fireball_height)

def DrawBack():
    window.fill((119,241,245))
def DrawWiz(wizard):
    window.blit(wizard_graph,(wizard.x,wizard.y))
def DrawFireball(fireball):
    window.blit(fireball_graph,(fireball.x,fireball.y))
    pg.display.update()
    
def Draw():
    DrawBack()
    DrawWiz(wizard)
    pg.display.update()

def WizardAction():
    wizard_movespeed=4
    keys_pressed = pg.key.get_pressed()
    if(keys_pressed[pg.K_w]):wizard.y-=wizard_movespeed
    if(keys_pressed[pg.K_s]):wizard.y+=wizard_movespeed
    if(keys_pressed[pg.K_a]):wizard.x-=wizard_movespeed
    if(keys_pressed[pg.K_d]):wizard.x+=wizard_movespeed
    if(keys_pressed[pg.K_SPACE]):DrawFireball(fireball)
        

def main():
    running = True
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                running = False

        Draw()
        WizardAction()

if __name__=="__main__":
    main()