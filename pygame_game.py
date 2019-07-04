import pygame 
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("game window")
running = True
while running:
  for event in pygame.event.get():
    	if event.type == pygame.QUIT:
      		running = False