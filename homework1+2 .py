import pygame
from pygame.locals import *
from sys import exit

# initialize
pygame.init()

# Setup Screen
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=RESIZABLE)
pygame.display.set_caption("Flappy Bird Phake")

# fps
clock = pygame.time.Clock()
fps = 60

# load sprites
background = []
base = pygame.image.load('asset/base.png').convert_alpha()
base2 = pygame.image.load('asset/base.png').convert_alpha()
bg_sky = pygame.image.load('asset/background_sky.png').convert_alpha()
bg_mountain = pygame.image.load('asset/background_rock.png').convert_alpha()
bg_cloud = pygame.image.load('asset/background_cloud.png').convert_alpha()
bg_tree = pygame.image.load('asset/background_tree.png').convert_alpha()
bg_cake = pygame.image.load('asset/background_cake.png').convert_alpha()
background.extend([bg_sky, bg_mountain, bg_cloud, bg_tree, bg_cake])
#base = pygame.image.load('assets/base.png').convert()


# define variables
run = True
ground_scroll = 0 
ground_scroll2 = 1920
scroll_spd = 60


# Sprites bird

        
while run:
   
    # setup background position
    for i in range(5):
        screen.blit(background[i], (0,0))
        
    # setup scrolling ground
    ground_scroll2 -= scroll_spd
    if ground_scroll2 < 0:
       ground_scroll2 = 1920
    screen.blit(base2, (ground_scroll2, 0))
    
    
    ground_scroll -= scroll_spd
    if ground_scroll < -1920:
       ground_scroll = 0
    screen.blit(base, (ground_scroll, 0))
        
    # setup event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(fps) # fps frame per second

