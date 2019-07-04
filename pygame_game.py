import pygame 
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("game window")
running = True
x = 50
y =50
width = 40
height = 60
velosity = 5

while running:
  pygame.time.delay(100)
  pygame.draw.rect(win, (255,12,4), (x, y, width, height))
  pygame.display.update()

  keys= pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
  		x-=velosity
  if keys[pygame.K_RIGHT]:
  		x+=velosity
  if keys[pygame.K_UP]:
  		y-=velosity
  if keys[pygame.K_DOWN]:
  		y+=velosity	
  #win.fill((0,0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      	running = False

   
pygame.quit()