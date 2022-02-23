######################################################################################################
# Name : Switch 5 Game
# Description : In this game you have 10 pegs (5 yellow and 5 green) and 11 holes, each color is on a
# side and there are 2 rules: 
# - Pegs can only move forward (to left for yellow pegs and to right for green pegs)
# - Pegs can go if there is a blank space after or, if there is an other peg, you need to have a free 
# space after. The goal is to switch green and yellow pegs.
# Author : Vivien Chambe
# Date : 23/02/2022
# ##################################################################################################### 

import pygame
from sys import exit

#Initialisation of the window

pygame.init()

width = 800
height = 400 
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Switch 5 Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

background = pygame.image.load("./graphics/bg.png")
text_surface = test_font.render("Switch game", False, "Black")
fill_surface = pygame.Surface((200,50))
fill_surface.fill("White")
background = pygame.image.load("./graphics/bg.png")
restart_surface= pygame.image.load("./graphics/restart_button.png")
end_surface = test_font.render("Congratulations", False, "Black")

class Pion:
    def __init__(self,x,y,couleur):
        self.x = x
        self.y = y
        self.image = pygame.image.load("./graphics/rond_"+couleur+".png")
        self.couleur = couleur

def is_finished():
    return pj[0].x == final_coord_j[0] and pj[1].x == final_coord_j[1] and pj[2].x == final_coord_j[2] and pj[3].x == final_coord_j[3] and pj[4].x == final_coord_j[4] and pv[0].x == final_coord_v[0] and pv[1].x == final_coord_v[1] and pv[2].x == final_coord_v[2] and pv[3].x == final_coord_v[3] and pv[4].x == final_coord_v[4]
    
def tracer_points():
    screen.blit(background,(0,0))
    for i in range (5):
        screen.blit(pj[i].image,(pj[i].x,pj[i].y))
        screen.blit(pv[i].image,(pv[i].x,pv[i].y))

def couleur(x,y): # To know if a case is free or not
    for i in range (5):
        if x>143 and x<600 and y>170 and y<200:
            for i in range (5) :
                if x>pv[i].x and x<pv[i].x+35:
                    return pv[i].couleur
                
            for i in range (5) :
                if x>pj[i].x and x<pj[i].x+35:
                    return pj[i].couleur 
        else:
            return "blanc"

def setup():
    screen.blit(background,(0,0))
    global pv, pj, final_coord_v, final_coord_j
    final_coord_j = []
    final_coord_v = []
    pv = []
    pj = []
    for i in range (5):
        pj.append(Pion(137+i*42,164,"jaune"))
        pv.append(Pion(389+i*42,164,"vert"))
        final_coord_j.append(pv[i].x)
        final_coord_v.append(pj[i].x)
    tracer_points()

setup()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        elif event.type == pygame.KEYUP: #To reset game
            if event.key == pygame.K_r:
                setup()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            is_finished()
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            if x>350 and x<390 and y>250 and y<290: #clic on reset button
                setup()

            elif couleur(x,y) == "blanc" : #There is no peg here so do nothing
                pass

            else:
                if couleur(x,y) == "jaune": 
                    for i in range (5):
                        if x>pj[i].x and x<pj[i].x+35:
                            if couleur(x+42,y) == None:
                                pj[i].x += 42
                            elif couleur(x+2*42,y) == None: 
                                pj[i].x += 2*42
                            else: print ("Mouvement impossible")
                            tracer_points()

                if couleur(x,y) == "vert":
                    for i in range (5):
                        if x>pv[i].x and x<pv[i].x+35:
                            if couleur(x-42,y) == None:
                                pv[i].x -= 42
                            elif couleur(x-2*42,y) == None: 
                                pv[i].x -= 2*42
                            else: print ("Mouvement impossible")
                            tracer_points()
    
    if is_finished():
        print ("terminé")
        screen.blit(end_surface,(240,30)) 

    screen.blit(restart_surface,(350,250))

    # Tracking Cursor ###############################
    # position_surface = test_font.render(str(pygame.mouse.get_pos()), False, "Black")
    # screen.blit(fill_surface,(0,0))
    # screen.blit(position_surface,(0,0))
    # screen.blit(text_surface,(275,100))
    #################################################

    pygame.display.update()
    clock.tick(60)