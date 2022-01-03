from logic import next_generation
import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEAL = (0, 128, 128)
RED = (255, 0, 0)


def clear_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = 0

    return grid


def play_GOL(grid, N):
    
    # This sets the margin between each cell
    MARGIN = 2
    # This sets the WIDTH and HEIGHT of each grid location and screen

    WINDOW_SIZE = [500+((N-1)*MARGIN), 500+((N-1)*MARGIN)]
    # WINDOW_SIZE = [500,500]
    WIDTH = round(500/N)
    HEIGHT = round(500/N)


    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen

    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Conways Game of Life")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # toggle the state of that location
                grid[row][column] = not(grid[row][column])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    grid = next_generation(grid)
                if event.key == pygame.K_c:
                    grid = clear_grid(grid)


        # Set the screen background
        screen.fill(TEAL)

        # Draw the grid
        for row in range(N):
            for column in range(N):
                color = BLACK
                if grid[row][column] == 1:
                    color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
