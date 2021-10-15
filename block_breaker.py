import pygame
import random

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

# Player ###############################################################################################################

# Avatar & position
rect_x = 64
rect_y = 8 * 1.618
avatar_x = (window_x / 2) - rect_x / 2
avatar_y = window_y - window_y / 8

# Avatar speed
avatar_speed = 10


def draw_rect(pos_x, pos_y, rect_w, rect_h):
    pygame.draw.rect(screen, WHITE, pygame.Rect(pos_x, pos_y, rect_w, rect_h))


# Ball #################################################################################################################
circle_r = 13
circle_x = (window_x / 2)
circle_y = avatar_y - circle_r


def draw_ball(pos_x, pos_y):
    pygame.draw.circle(screen, WHITE, (pos_x, pos_y), circle_r, 0)


# Blocks ###############################################################################################################

tiles_width = window_x // 9
tiles_height = window_x // 19


def tiles():
    lst = []
    for y in range(0, window_y // 4, tiles_height):
        for x in range(0, window_x - tiles_width, tiles_width):
            lst.append([x, y, tiles_width, tiles_height])
    return lst


def draw_tiles():
    for i in range(len(tiles())):
        c = random.randint(50, 255)
        pygame.draw.rect(screen, (c, c, c), pygame.Rect(tiles()[i]))


# Game engine ##########################################################################################################

# FPS
FPS = 60


def main():
    global avatar_x, avatar_y, circle_x, circle_y

    clock = pygame.time.Clock()
    loop = True

    flux_x = True
    flux_y = True

    while loop:
        # FPS
        clock.tick(FPS)

        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # Rectangle movement
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_LEFT] and avatar_x - avatar_speed > 0:
            avatar_x -= avatar_speed
        if user_input[pygame.K_RIGHT] and avatar_x + avatar_speed + rect_x < window_x:  # elif
            avatar_x += avatar_speed

        # Ball boarders & movement
        # x-movement
        if circle_x - circle_r / 2 - avatar_speed > 0 and flux_x:
            circle_x -= avatar_speed
        else:
            flux_x = False
            circle_x += avatar_speed
            if circle_x + circle_r / 2 + avatar_speed > window_x:
                flux_x = True

        # y-movement
        if circle_y - circle_r / 2 - avatar_speed > 0 and flux_y:
            circle_y -= avatar_speed
        else:
            flux_y = False
            circle_y += avatar_speed
            if circle_y + circle_r / 2 + avatar_speed > window_y:
                flux_y = True

        # Output
        screen.fill(BLACK)
        draw_rect(avatar_x, avatar_y, rect_x, rect_y)
        draw_ball(circle_x, circle_y)
        draw_tiles()
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
