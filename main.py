from math import trunc

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
sigma_list_in_game = []

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 400

is_jump = False
jump_count = 9

bg_sound = pygame.mixer.Sound('files/SigmaSong.mp3')
bg_sound.play()

sigma_timer = pygame.USEREVENT + 1
pygame.time.set_timer(sigma_timer, 2500)

label = pygame.font.Font('files/karedoks-demo.regular.ttf', 40)
lose_lable = label.render("You've lost", False, (193, 196, 199))
restart_lable = label.render("RESTART", False, (115, 132, 148))

restart_lable_rect = restart_lable.get_rect(topleft=(400, 500))

bullets_left = 5

bullet = pygame.image.load('files/патрон.png').convert_alpha()
bullets = []

gameplay = True

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 950, 0))

    if gameplay:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if sigma_list_in_game:
            for (i, el) in enumerate(sigma_list_in_game):
                screen.blit(sigma, el)
                el.x -= 10

                if el.x < -20:
                    sigma_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_x > 50:
            player_x -= player_speed
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_x < 850:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -9:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2

                jump_count -= 1
            else:
                is_jump = False
                jump_count = 9

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -950:
            bg_x = 0

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4

                if el.x > 955:
                    bullets.pop(i)

                if sigma_list_in_game:
                    for (index, sigma_el) in enumerate(sigma_list_in_game):
                        if el.colliderect(sigma_el):
                            sigma_list_in_game.pop(index)
                            bullets.pop(i)


    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_lable, (400, 250))
        screen.blit(restart_lable, restart_lable_rect)

        mouse = pygame.mouse.get_pos()
        if restart_lable_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            sigma_list_in_game.clear()
            bullets.clear()
            bullets_left = 5

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == sigma_timer:
            sigma_list_in_game.append(sigma.get_rect(topleft=(955, 400)))

        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
            bullets_left -= 1

    clock.tick(15)

