import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

TILESIZE = 32
WINWIDTH = TILESIZE * 20
WINHEIGHT = TILESIZE * 20

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT), 0, 32)
pygame.display.set_caption('Game')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
catImg = pygame.image.load('main.png')
catx = 10
caty = 19

keyImg = pygame.image.load('key.png')
keyx = 5
keyy = 15

doorImg = pygame.image.load('door.png')
doorx = 10
doory = 0

got_key = False
game_status = "Playing"

while True: # the main game loop
  DISPLAYSURF.fill(WHITE)

  DISPLAYSURF.blit(catImg, (catx*TILESIZE, caty*TILESIZE))
  DISPLAYSURF.blit(doorImg, (doorx*TILESIZE, doory*TILESIZE))

  if not got_key:
    DISPLAYSURF.blit(keyImg, (keyx*TILESIZE, keyy*TILESIZE))

  if game_status == "Win":
    DISPLAYSURF.fill(GREEN)
    textsurface = font.render('You Win', False, (0, 0, 0))
    DISPLAYSURF.blit(textsurface, (280, 300))
  elif game_status == "Lose":
    DISPLAYSURF.fill(RED)
    textsurface = font.render('You Died', False, (0, 0, 0))
    DISPLAYSURF.blit(textsurface, (280, 300))

  

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == KEYDOWN and game_status == "Playing":
      if event.key == K_LEFT:
        catx -= 1
      elif event.key == K_RIGHT:
        catx += 1
      elif event.key == K_UP:
        caty -= 1
      elif event.key == K_DOWN:
        caty += 1

  if catx == keyx and caty == keyy:
    got_key = True

  if catx == doorx and caty == doory:
    if got_key:
      game_status = "Win"
    else:
      game_status = "Lose"

  pygame.display.update()
  fpsClock.tick(FPS)