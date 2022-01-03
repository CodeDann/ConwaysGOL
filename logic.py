# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.


import numpy as np
import matplotlib.pyplot as plt


def count_neighbours(grid, bordergrid):
    neighbour_array = np.zeros((len(grid[0]), len(grid[0])), dtype=int)
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
            if grid[i][j]:
                if (neighbour_array[i][j] == 2 or neighbour_array[i][j] == 3):
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0
            else:
                if neighbour_array[i][j] == 3:
                    grid[i][j] = 1

    return grid


def next_generation(gameState):
    neighbour_array = count_neighbours(gameState, np.pad(gameState, pad_width=1, mode='constant', constant_values=0))
    return update_gamestate(gameState, neighbour_array)




