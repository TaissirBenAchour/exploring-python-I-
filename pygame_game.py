import pygame 
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("game window")
running = True
x = 50
y =450
width = 40
height = 60
velosity = 5
isJump = False
jumpCount = 10

while running:
  pygame.time.delay(100)
  pygame.draw.rect(win, (255,12,4), (x, y, width, height))
  pygame.display.update()

  keys= pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and x >= velosity:
  		x-=velosity
  if keys[pygame.K_RIGHT] and x+width+velosity <= 500:
  		x+=velosity

  if not (isJump):
  	if keys[pygame.K_UP] and y>= velosity:
  		y-=velosity
  	if keys[pygame.K_DOWN] and y+height+velosity <= 500:
  		y+=velosity	
  	if keys[pygame.K_SPACE] :  
  		isJump = True
  else : 
  	if jumpCount >= -10:
  		neg = 1
  		if jumpCount<0:
  			neg = -1
  		y-=(jumpCount**2)*0.5*neg
  		jumpCount-=1
  	else : 
  		isJump = False
  		jumpCount = 10

  win.fill((0,0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      	running = False

   
pygame.quit()