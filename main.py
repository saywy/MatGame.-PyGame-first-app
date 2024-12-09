import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((950, 555))
pygame.display.set_caption('PyGame')
icon = pygame.image.load('files/i.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('files/background.png')

# подгружаем ходьбу

walk_left = [
    pygame.image.load('files/left/1.png'),
    pygame.image.load('files/left/2.png'),
    pygame.image.load('files/left/3.png'),
    pygame.image.load('files/left/4.png')
]

walk_right = [
    pygame.image.load('files/right/1.png'),
    pygame.image.load('files/right/2.png'),
    pygame.image.load('files/right/3.png'),
    pygame.image.load('files/right/4.png')
]


player_anim_count = 0


running = True
while running:

    screen.blit(bg, (0, 0))
    screen.blit(walk_right[player_anim_count], (300, 400))

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(8)
