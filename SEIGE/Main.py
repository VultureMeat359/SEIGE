"""
          _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \               \:::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \               \:::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \               \:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \               \:::\    \        /:::/  \:::\    \        /:::/__\:::\    \    
    \:::\   \:::\    \      /::::\   \:::\    \              /::::\    \      /:::/    \:::\    \      /::::\   \:::\    \   
  ___\:::\   \:::\    \    /::::::\   \:::\    \    ____    /::::::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \  
 /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /\   \  /:::/\:::\    \  /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \ 
/::\   \:::\   \:::\____\/:::/__\:::\   \:::\____\/::\   \/:::/  \:::\____\/:::/____/  ___\:::|    |/:::/__\:::\   \:::\____\
\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /\:::\  /:::/    \::/    /\:::\    \ /\  /:::|____|\:::\   \:::\   \::/    /
 \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \:::\/:::/    / \/____/  \:::\    /::\ \::/    /  \:::\   \:::\   \/____/ 
  \:::\   \:::\    \       \:::\   \:::\    \       \::::::/    /            \:::\   \:::\ \/____/    \:::\   \:::\    \     
   \:::\   \:::\____\       \:::\   \:::\____\       \::::/____/              \:::\   \:::\____\       \:::\   \:::\____\    
    \:::\  /:::/    /        \:::\   \::/    /        \:::\    \               \:::\  /:::/    /        \:::\   \::/    /    
     \:::\/:::/    /          \:::\   \/____/          \:::\    \               \:::\/:::/    /          \:::\   \/____/     
      \::::::/    /            \:::\    \               \:::\    \               \::::::/    /            \:::\    \         
       \::::/    /              \:::\____\               \:::\____\               \::::/    /              \:::\____\        
        \::/    /                \::/    /                \::/    /                \::/____/                \::/    /        
         \/____/                  \/____/                  \/____/                                           \/____/

"""
import pygame, time, math, random, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("SEIGE")
win = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
x = 0
y = 700
player_width = 40
player_height = 60
vel = 5
sprint = 200
isSprinting = False
#TODO: FIND A DECENT SOUND FILE FOR FOOTSTEPS
# footsteps = pygame.mixer.Sound("")

run = True
x = 0
while run:
    pygame.time.delay(30)
    if sprint < 200:
        sprint = sprint + 0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
        #footsteps.play()
        if keys[pygame.K_SPACE] and sprint > 5:
            x -= 6
            sprint = sprint - 3
            isSprinting = True
        else:
            isSprinting = False
    if keys[pygame.K_RIGHT]:
        x += vel
        #footsteps.play()
        if keys[pygame.K_SPACE] and sprint > 5:
            x += 6
            sprint = sprint - 3
            isSprinting = True
        else:
            isSprinting = False
    if keys[pygame.K_UP]:
        y -= vel
        #footsteps.play()
        if keys[pygame.K_SPACE] and sprint > 5:
            y -= 6
            sprint = sprint - 3
            isSprinting = True
        else:
            isSprinting = False
    if keys[pygame.K_DOWN]:
        y += vel
        #footsteps.play()
        if keys[pygame.K_SPACE] and sprint > 5:
            y += 6
            sprint = sprint - 3
            isSprinting = True
        else:
            isSprinting = False
    win.fill((0,0,0))
    font = pygame.font.SysFont("pixel", 30, True)
    text = font.render("SPRINT:", 1, (255,255,255))
    win.blit(text, (25, 3))
    pygame.draw.rect(win, (0,128,0), (25, 50, sprint, 20))
    pygame.draw.rect(win, (255,255,0), (x, y, player_width, player_height))
    pygame.display.update()
    
pygame.quit()
