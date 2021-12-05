import pygame
import random
import time

# inheritance for guest class
# use a class from a level for interaction with account database

class Account(object):
    def __init__(self, name):
        self.username = name

class Guest(Account):
     pass

def get_text():
    with open('texts.txt', 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        print(line)

    return lines

def sign_in():
    pygame.init()
    screen = pygame.display.set_mode((800,800))

    titlefont = pygame.font.SysFont('Arial', 50)
    title = titlefont.render('Sign In', True, (255,255,0))
    screen.blit(title,(470,50))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    
    titlefont = pygame.font.SysFont('Arial', 50)
    title = titlefont.render('Fast Fingers', True, (255,255,0))
    screen.blit(title,(470,50))

    menu_font = pygame.font.SysFont('Arial', 40)
    start = menu_font.render('Start', True, (0,0,0))
    account = menu_font.render('Account', True, (0,0,0))
    quitt = menu_font.render('Quit', True, (0,0,0))

    
    
    pygame.draw.rect(screen, (255,255,0), (500, 200, 200,100), 0)
    pygame.draw.rect(screen, (255,255,0), (500, 350, 200,100), 0)
    pygame.draw.rect(screen, (255,255,0), (500, 500, 200,100), 0)

    screen.blit(start,(550, 225))
    screen.blit(account,(525,375))
    screen.blit(quitt,(550, 525))


    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                print(mx,my)

                if (500 <= mx <= 700) and (200 <= my <= 300):
                    run = False
                    account = sign_in()
                
                elif (500 <= mx <= 700) and (350 <= my <= 450):
                    print('account')

                elif (500 <= mx <= 700) and (450 <= my <= 600):
                    run = False


        pygame.display.update()

    


main()

