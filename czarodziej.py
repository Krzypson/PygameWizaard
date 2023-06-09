import pygame as pg
import os
import random

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

pg.init()
pg.font.init()
width = 1000
height=800
window = pg.display.set_mode((width,height),pg.RESIZABLE)
pg.display.set_caption("Czarodziej lmao")
pg.display.set_icon(pg.image.load(os.path.join('Assets','wizhat.png')))
clock=pg.time.Clock()
screen_width = pg.display.Info().current_w
screen_height = pg.display.Info().current_h

#wizard
wizard_sprite = pg.image.load(os.path.join('Assets','wizard.png'))
wizard_width,wizard_height = 100,100
wizard_graph = pg.transform.scale(wizard_sprite,(wizard_width,wizard_height))
wizard = pg.Rect(50,250,wizard_width,wizard_height)
hearts = 3

#fireball
Fireballs=[]
fireball_sprite = pg.image.load(os.path.join('Assets','fireball.png'))
fireball_width,fireball_height = 100,100
fireball_graph = pg.transform.scale(fireball_sprite,(fireball_width,fireball_height))
fireball_movespeed=8

#goblin
Goblins=[]
goblin_ammount = 5
goblin_sprite = pg.image.load(os.path.join('Assets','goblin.png'))
goblin_width,goblin_height=45,75
goblin_graph = pg.transform.scale(goblin_sprite,(goblin_width,goblin_height))

#border
border_left = 0
border_right = screen_width - wizard_width
border_top = 0
border_bottom = screen_height - wizard_height

#UI
heart_icon = pg.image.load(os.path.join('Assets','hearticon.png'))
fireball_icon = pg.image.load(os.path.join('Assets','fireballicon.png'))
score=0
game_over_font=pg.font.SysFont('helvetica',32)
restart_font=pg.font.SysFont('helvetica',18)

Goblin_Hit = pg.USEREVENT+1

Player_Hit = pg.USEREVENT+2

def DrawBack():
    window.fill((119,241,245))
def DrawWiz():
    window.blit(wizard_graph,(wizard.x,wizard.y))
def DrawGoblins():
    for gob in Goblins:
        window.blit(goblin_graph,(gob.x,gob.y))
def DrawFireball():
    for fball in Fireballs:
        window.blit(fireball_graph,(fball.x,fball.y))
def DrawUi():
    game_over = game_over_font.render('GAME OVER',1,(255,0,0))
    score_ui = game_over_font.render(str(score),1,(0,0,0))
    restart_ui = restart_font.render('press r to restart',1,(0,0,0))
    window.blit(score_ui,((screen_width - score_ui.get_width())//2,10))
    match hearts:
        case 1:
            window.blit(heart_icon,(10,10))
        case 2:
            window.blit(heart_icon,(10,10))
            window.blit(heart_icon,(20+heart_icon.get_width(),10))
        case 3:
            window.blit(heart_icon,(10,10))
            window.blit(heart_icon,(15+heart_icon.get_width(),10))
            window.blit(heart_icon,(20+2*heart_icon.get_width(),10))
        #TO BE REPLACED
        case _:
            window.blit(game_over,((screen_width-game_over.get_width())//2,screen_height//2))
            window.blit(restart_ui,((screen_width-restart_ui.get_width())//2,screen_height//2+30))
def Draw():
    DrawBack()
    DrawWiz()
    DrawGoblins()
    DrawUi()
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
                for goblin in Goblins:
                    if fball.colliderect(goblin):
                        pg.event.post(pg.event.Event(Goblin_Hit))
                        Goblins.remove(goblin)
                        Fireballs.remove(fball)
            else:
                Fireballs.remove(fball)
                
def SpawnGoblins():
    global Goblins
    if(len(Goblins)<goblin_ammount):
        goblin = pg.Rect(random.randint(3*screen_width//4,screen_width),random.randint(0,screen_height-goblin_height),goblin_width,goblin_height)
        Goblins.append(goblin)
        
def GoblinMovement():
    global Goblins
    global hearts
    for goblin in Goblins:
        if goblin.colliderect(wizard):
            Goblins.remove(goblin)
            pg.event.post(pg.event.Event(Player_Hit))
        if(goblin.x > border_left):
            goblin.x-=1
        else:
            Goblins.remove(goblin)
            hearts-=1

def Wizard_Damage():
    global hearts
    hearts-=1

def restart():
    global hearts
    global Goblins
    global score
    global wizard
    hearts=3
    Goblins=[]
    score=0
    wizard.x = 50
    wizard.y = 250
    

def main():
    global score
    global hearts
    running = True
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                running = False
            if(event.type == pg.KEYDOWN):
                if(event.key == pg.K_SPACE and hearts>0):
                    fireball = pg.Rect(wizard.x,wizard.y,fireball_width,fireball_height)
                    Fireballs.append(fireball)
                if(event.key == pg.K_r):
                    restart()
            if(event.type == Player_Hit):
                Wizard_Damage()
            if(event.type == Goblin_Hit):
                score+=1
        if hearts>0:
            SpawnGoblins()
            GoblinMovement()
            WizardMovement()
            FireballHandling()
        Draw()

if __name__=="__main__":
    main()