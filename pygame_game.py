import pygame 
pygame.init()
win = pygame.display.set_mode((852, 480))
pygame.display.set_caption("game window")

clock = pygame.time.Clock()

class player(object):
	def __init__(self, x, y, height, width):
		self.x=x
		self.y=y
		self.height=height
		self.width=width
		self.velosity=5
		self.isJump = False 
		self.jumpCount = 10
		self.left = False
		self.right = False
		self.walkCount = 0
		self.screen_width = 852

	def direction_player(self, win):
		if self.walkCount +1 >= 27:
			self.walkCount = 0
		if self.left : 
			win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
			self.walkCount+=1
		elif self.right :
			win.blit(walkRight[self.walkCount//3], (self.x,self.y))
			self.walkCount+=1
		else : 
			win.blit(char, (self.x,self.y))


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')



def DrawGameSpace():
	win.blit(bg, (0,0))
	zoro.direction_player(win)
  	pygame.display.update()

#mainloop
zoro = player(0, 420, 64, 64)
running = True
while running:
  clock.tick(27)
  for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
  keys= pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and zoro.x >= zoro.velosity:
  	 	zoro.x-=zoro.velosity
  	 	zoro.left = True
  	 	zoro.right = False
  elif keys[pygame.K_RIGHT] and zoro.x+zoro.width+zoro.velosity <= zoro.screen_width:
  		zoro.x+=zoro.velosity
  		zoro.left = False
  		zoro.right = True
  else : 
  	zoro.left = False
  	zoro.right = False
  	zoro.walkCount = 0
  if not (zoro.isJump): 
  	if keys[pygame.K_SPACE] :  
  		zoro.isJump = True
  		zoro.left = False
  		zoro.right = False
  		zoro.walkCount = 0
  else : 
  	if zoro.jumpCount >= -10:
  		neg = 1
  		if zoro.jumpCount<0:
  			neg = -1
  		zoro.y-=(zoro.jumpCount**2)*0.5*neg
  		zoro.jumpCount-=1
  	else : 
  		zoro.isJump = False
  		zoro.jumpCount = 10
  DrawGameSpace()
  
pygame.quit()

