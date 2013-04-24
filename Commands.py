import pygame, sys
from pygame import *
from weapon import *

def inv(player, args):
  for name, item in player.inventory:
		print("{0} x{1}".format(item.name, item.quantity))


def exit(player, exit):
	pygame.quit()
	sys.exit()
	
def movement(player, args):
	print ("W = Moves Up\n" "S = Moves Down\n" "A = Moves Left\n" "D = Moves Right")

def startDisplay(player, args):
	pygame.init()
	mainClock = pygame.time.Clock()

	WINDOWHEIGHT = 640
	WINDOWWIDTH = 480
	screen = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH), 0, 32)

	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)

	moveLeft = False
	moveRight = False
	moveUp = False
	moveDown = False

	MOVESPEED = 2
	playerrect = pygame.Rect(300, 100, 30, 30)

	while True:
	    # check for events
	    for event in pygame.event.get():
	        if event.type == KEYDOWN:
	            # change the keyboard variables
	            if event.key == K_LEFT or event.key == ord('a'):
	                moveRight = False
	                moveLeft = True
	            if event.key == K_RIGHT or event.key == ord('d'):
	                moveLeft = False
	                moveRight = True
	            if event.key == K_UP or event.key == ord('w'):
	                moveDown = False
	                moveUp = True
	            if event.key == K_DOWN or event.key == ord('s'):
	                moveUp = False
	                moveDown = True
	        if event.type == KEYUP:
	            if event.key == K_ESCAPE:
	                pygame.quit()
	                sys.exit()
	            if event.key == K_LEFT or event.key == ord('a'):
	                moveLeft = False
	            if event.key == K_RIGHT or event.key == ord('d'):
	                moveRight = False
	            if event.key == K_UP or event.key == ord('w'):
	                moveUp = False
	            if event.key == K_DOWN or event.key == ord('s'):
	                moveDown = False
	                
	    screen.fill(BLACK)
	    # move the player
	    if moveDown and playerrect.bottom < WINDOWHEIGHT:
	        playerrect.top += MOVESPEED
	    if moveUp and playerrect.top > 0:
	        playerrect.top -= MOVESPEED
	    if moveLeft and playerrect.left > 0:
	        playerrect.left -= MOVESPEED
	    if moveRight and playerrect.right < WINDOWWIDTH:
	        playerrect.right += MOVESPEED
	    
	    # draw the player onto the surface
	    pygame.draw.rect(screen, WHITE, playerrect)
	    
	    pygame.display.update()
	    mainClock.tick(120)
