import pygame

pygame.init()
screen = pygame.display.set_mode((950, 555))
pygame.display.set_caption('PyGame')
icon = pygame.image.load('files/i.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('files/background.png')
player = pygame.image.load('files/left/1.png')

running = True
while running:

    screen.blit(bg, (0, 0))
    screen.blit(player, (300, 400))



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
