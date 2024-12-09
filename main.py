import pygame

pygame.init()
screen = pygame.display.set_mode((950, 555))
pygame.display.set_caption('PyGame')
icon = pygame.image.load('files/i.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('files/background.png')

running = True
while running:

    screen.blit(bg, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
