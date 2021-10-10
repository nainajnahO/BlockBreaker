import pygame

# Initialize pygame ####################################################################################################
pygame.init()

# GUI ##################################################################################################################

# Configure window
screen_x = pygame.display.Info().current_w
screen_y = pygame.display.Info().current_h
screen = pygame.display.set_mode((int(screen_y / 2 * 1.618), int(screen_y / 2)))
window_x, window_y = pygame.display.get_window_size()

# Background color
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)

# Caption
pygame.display.set_caption("Blockbreaker")

# Icon
icon = pygame.image.load("uu_logotyp.jpg")
pygame.display.set_icon(icon)


def draw_window(player_x, player_y, rect_w, rect_h):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, pygame.Rect(player_x, player_y, rect_w, rect_h))
    pygame.display.update()


# Player ###############################################################################################################

# Avatar & position
rect_x = 64
rect_y = 8 * 1.618
avatar_x = (window_x / 2) - rect_x / 2
avatar_y = window_y - window_y / 8

# Avatar speed
avatar_speed = 10

# Ball #################################################################################################################


# Game engine ##########################################################################################################

# FPS
FPS = 60


def main(player_x, player_y):
    clock = pygame.time.Clock()
    loop = True
    while loop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_LEFT] and player_x - avatar_speed > 0:
            player_x -= avatar_speed
        if user_input[pygame.K_RIGHT] and player_x + avatar_speed + rect_x < window_x:  # elif
            player_x += avatar_speed

        draw_window(player_x, player_y, rect_x, rect_y)

    pygame.quit()


if __name__ == '__main__':
    main(avatar_x, avatar_y)
