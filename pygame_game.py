import pygame 
pygame.init()
win = pygame.display.set_mode((852, 480))
pygame.display.set_caption("game window")
clock = pygame.time.Clock()

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


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
		self.standing = True

	def direction_player(self, win):

		if self.walkCount +1 >= 27:
			self.walkCount = 0
		if not (self.standing): 
			if self.left : 
				win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
				self.walkCount+=1
			elif self.right :
				win.blit(walkRight[self.walkCount//3], (self.x,self.y))
				self.walkCount+=1
		else : 
			if self.right:
				win.blit(walkRight[0],(self.x,self.y))
			else : 
				win.blit(walkLeft[0],(self.x,self.y))


class projectile(object):
	def __init__(self, x,y,radius,color,facing):
		self.x = x
		self.y = y
		self.radius = radius 
		self.color = color 
		self.facing = facing
		self.velosity = 8 * facing 
	def draw (self, win):
		pygame.draw.circle(win, self.color, (int(self.x),int(self.y)), self.radius)

def DrawGameSpace():
	win.blit(bg, (0,0))
	zoro.direction_player(win)
	for bullet in bullets:
		bullet.draw(win)
  	pygame.display.update()

#mainloop
zoro = player(0, 420, 64, 64)
bullets= []
running = True
while running:
  clock.tick(27)
  for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
  for  bullet  in bullets: 
  	if bullet.x <500 and bullet.x >0:
  		bullet.x += bullet.velosity
  	else : 
  		bullets.pop(bullets.index(bullet))

  keys= pygame.key.get_pressed()
  if keys[pygame.K_SPACE] :
  	if zoro.left:
  		facing=-1
  	else:
  		facing = 1 
  	if len(bullets) < 5:
  		bullets.append(projectile(round(zoro.x+zoro.width // 2), round(zoro.y+zoro.height //2),6,(0,0,0),facing))
  if keys[pygame.K_LEFT] and zoro.x >= zoro.velosity:
  	 	zoro.x-=zoro.velosity
  	 	zoro.left = True
  	 	zoro.right = False
  	 	zoro.standing = False
  elif keys[pygame.K_RIGHT] and zoro.x+zoro.width+zoro.velosity <= zoro.screen_width:
  		zoro.x+=zoro.velosity
  		zoro.left = False
  		zoro.right = True
  		zoro.standing = False
  else : 
  	zoro.standing = True
  	zoro.walkCount = 0
  if not (zoro.isJump): 
  	if keys[pygame.K_UP] :  
  		zoro.isJump = True
  		zoro.left = False
  		zoro.right = False
  		zoro.standing = True
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

