import pygame

pygame.init()


screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('PyGame')

icon = pygame.image.load('files/i.png')

pygame.display.set_icon(icon)



square = pygame.Surface((100, 250))
square.fill('Blue')

myfont = pygame.font.Font('files/shadow-whisper-demo.regular.ttf', 40)
text_surface = myfont.render('Matvey', True, 'White')

player = pygame.image.load('files/i.png')

running = True
while running:

    screen.blit(square, (10, 0))
    screen.blit(text_surface, (300, 100))
    pygame.draw.circle(screen, 'Orange', (20, 20), 20)
    screen.blit(player, (200, 200))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()