# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.


import numpy as np
import matplotlib.pyplot as plt


def count_neighbours(grid, bordergrid):
    neighbour_array = np.zeros((len(grid[0]), len(grid[0])), dtype=int)
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] >= 1:
                grid[row][column] = 1
            else:
                grid[row][column] = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            total = 0
            # topleft
            total += bordergrid[row][column]
            # topmid
            total += bordergrid[row][column+1]
            # topright
            total += bordergrid[row][column+2]
            # midleft
            total += bordergrid[row+1][column]
            # midright
            total += bordergrid[row+1][column+2]
            # botleft
            total += bordergrid[row+2][column]
            # botmid
            total += bordergrid[row+2][column+1]
            # botright
            total += bordergrid[row+2][column+2]

            neighbour_array[row][column] = total

    return neighbour_array


def update_gamestate(grid, neighbour_array):
    for i in range(len(neighbour_array)):
        for j in range(len(neighbour_array[i])):
            # if a live cell
            if grid[i][j] == 1:
                # has the 2 or 3  neighbours
                if neighbour_array[i][j] == 2 or neighbour_array[i][j] == 3:
                    # it lives
                    grid[i][j] = 1
                # otherwise it dies
                else:
                    grid[i][j] = -1
            # if a dead cell has 3 neighbours it comes to life
            else:
                if neighbour_array[i][j] == 3:
                    grid[i][j] = 2
                elif grid[i][j] == -1:
                    grid[i][j] = 0

    return grid


def next_generation(gameState):
    neighbour_array = count_neighbours(gameState, np.pad(gameState, pad_width=1, mode='constant', constant_values=0))
    return update_gamestate(gameState, neighbour_array)


def reset_game(gameState, N):
    gameState = np.random.choice((1, 0),  N * N, p=[0.4, 0.6]).reshape(N, N)
    return  gameState

