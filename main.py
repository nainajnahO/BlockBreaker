import pygame

# Initialize pygame ####################################################################################################
pygame.init()

# GUI ##################################################################################################################

# Configure window
screen_x = pygame.display.Info().current_w
screen_y = pygame.display.Info().current_h
screen = pygame.display.set_mode((int(screen_x / 2), int(screen_y / 2)))
window_x, window_y = pygame.display.get_window_size()

# Caption
pygame.display.set_caption("Blockbreaker")

# Icon
icon = pygame.image.load("uu_logotyp.jpg")
pygame.display.set_icon(icon)

# Player ###############################################################################################################

# Avatar
player_avatar = pygame.image.load("perspective.png")

# Avatar placement
player_x = (window_x / 2) - player_avatar.get_width() / 2
player_y = window_y - window_y / 7
player_x_change = 0

# Avatar speed
player_speed = 3


def player(x, y):
    screen.blit(player_avatar, (x, y))


# Game loop ############################################################################################################


# System load
fps = 60
clock = pygame.time.Clock()

loop = True
while loop:

    # Load
    clock.tick(fps)

    # Background color
    screen.fill((0, 0, 0))

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        # Keystroke events

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    player(player_x, player_y)
    pygame.display.update()

pygame.quit()
