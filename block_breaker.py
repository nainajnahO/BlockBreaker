import pygame

pygame.init()

# Variables ############################################################################################################

# Window size
window_x = int(pygame.display.Info().current_w / 2)
window_y = int(pygame.display.Info().current_h / 2)
window = pygame.display.set_mode([window_x, window_y])

# Platform dimensions & position
platform_h = window_y / 60
platform_w = window_x / 20
platform_y = window_y - window_y / 10
platform_x = (window_x / 2) - platform_w / 2

# Tile dimensions & colours
tiles_h = window_y // 20
tiles_w = window_x // 10
tiles_brightness_lower_limit = 50

# Ball dimension & position
ball_r = window_y // 60
ball_y = platform_y
ball_x = window_x // 2


# Ball #################################################################################################################

def draw_ball(x_pos, y_pos, radius):
    pygame.draw.circle(window, (255, 255, 255), (x_pos, y_pos), radius, 0)


# Tiles ################################################################################################################

def generate_tiles():
    lst = []
    for y in range(0, window_y // 3, tiles_h):
        for x in range(0, window_x, tiles_w):
            lst.append(pygame.draw.rect(window, (255, 255, 255), pygame.Rect(x, y, tiles_w, tiles_h)))
    return lst


def update_tiles(list_of_tiles, damaged_tiles):
    for i in damaged_tiles:
        for n in list_of_tiles:
            if i[0] == n[0] and i[1] == n[1]:
                list_of_tiles.remove(n)


def draw_tiles(list_of_tiles):
    global tiles_brightness_lower_limit
    c = tiles_brightness_lower_limit
    for tile in list_of_tiles:
        c += ((255 - (c / 2)) / len(list_of_tiles))
        pygame.draw.rect(window, (c, c, c), pygame.Rect(tile[0], tile[1], tile[2], tile[3]))


def position_tiles(tiles):
    positions = []
    for element in tiles:
        tile_position = (element[0], element[1])
        positions.append(tile_position)
    return positions


def collision_tiles(tile_x, tile_y, x_ball, y_ball):
    return tile_x <= x_ball <= (tile_x + tiles_w) and tile_y <= (y_ball - ball_r) <= (tile_y + tiles_h)


# Game engine ##########################################################################################################

# System load
FPS = 60

# In-game text
my_font = pygame.font.SysFont('Comic Sans MS', 50)
game_over_txt = my_font.render("GAME OVER! Press (r) for restart", True, (255, 255, 255))
you_win_txt = my_font.render("YOU WIN!", True, (255, 255, 255))


def main():

    # Retrieve necessary global variables
    global platform_x, ball_y, ball_x
    clock = pygame.time.Clock()

    # Set game-loop
    run_loop = True

    # Defining object speeds
    ball_speed = 12
    platform_speed = 15

    # Initiating tile variables
    tiles = generate_tiles()
    tiles_pos = position_tiles(tiles)
    removed_tiles = []

    # Initiating ball travel
    flux_y = True
    flux_x = True

    while run_loop:

        # System load control
        clock.tick(FPS)

        # Verifying game-loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_loop = False

        # Platform movement
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_LEFT] and platform_x - platform_speed > 0:
            platform_x -= platform_speed
        if user_input[pygame.K_RIGHT] and platform_x + platform_speed + platform_w < window_x:
            platform_x += platform_speed

        # Wall bounce x-axis & y-axis
        if ball_x - ball_r < 0:
            ball_x, flux_x = ball_x + ball_speed, True
        elif ball_x + ball_r > window_x:
            ball_x, flux_x = ball_x - ball_speed, False
        else:
            if flux_x:
                ball_x += ball_speed
            else:
                ball_x -= ball_speed
        if ball_y - ball_r < 0:
            ball_y, flux_y = ball_y + ball_speed, False

        # Platform bounce
        if platform_x <= ball_x <= platform_x + platform_w and platform_y <= ball_y + ball_r <= platform_y + platform_h:
            ball_y, flux_y = ball_y - ball_speed, True
        else:
            if flux_y:
                ball_y -= ball_speed
            else:
                ball_y += ball_speed

        # Tile collision
        for tile in tiles_pos:
            if collision_tiles(tile[0], tile[1], ball_x, ball_y):
                flux_y = False
                tiles_pos.remove(tile)
                removed_tiles.append(tile)
                update_tiles(tiles, removed_tiles)

        # Losing
        game_over = False
        if ball_y > window_y:
            game_over = True
            ball_speed = 0

        # Winning
        win = False
        if len(tiles) == 0:
            win = True
            ball_speed = 0

        # Update window
        window.fill((0, 0, 0))
        draw_tiles(tiles)
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(platform_x, platform_y, platform_w, platform_h))
        draw_ball(ball_x, ball_y, ball_r)

        if game_over:
            window.blit(game_over_txt, (window_x // 3.5, window_y // 2))
            if user_input[pygame.K_r]:
                return True

        if win:
            window.blit(you_win_txt, (window_x // 3.5, window_y // 2))

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    while main():
        main()
