import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((950, 555))
pygame.display.set_caption('MatGame')
icon = pygame.image.load('files/left/1.png').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load('files/background.png').convert()

# подгружаем ходьбу

walk_left = [
    pygame.image.load('files/left/1.png').convert_alpha(),
    pygame.image.load('files/left/2.png').convert_alpha(),
    pygame.image.load('files/left/3.png').convert_alpha(),
    pygame.image.load('files/left/4.png').convert_alpha()
]
walk_right = [
    pygame.image.load('files/right/1.png').convert_alpha(),
    pygame.image.load('files/right/2.png').convert_alpha(),
    pygame.image.load('files/right/3.png').convert_alpha(),
    pygame.image.load('files/right/4.png').convert_alpha()
]

sigma = pygame.image.load('files/sigma.png').convert_alpha()
sigma_x = 955

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 400

is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('files/SigmaSong.mp3')
bg_sound.play()

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 950, 0))
    screen.blit(sigma, (sigma_x, 400))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_x > 50:
        player_x -= player_speed
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_x < 200:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2

            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == -950:
        bg_x = 0

    sigma_x -= 10

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(15)