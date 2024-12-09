import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('PyGame')
icon = pygame.image.load('files/i.png')
pygame.display.set_icon(icon)

player = pygame.image.load('files/i.png')

running = True
while running:

    screen.blit(player, (200, 200))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
