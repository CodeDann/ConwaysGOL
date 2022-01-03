from logic import *
from graphics import *


N = int(input("Input the size of the grid: "))
gameState = np.random.choice((1, 0),  N * N, p=[0.4, 0.6]).reshape(N, N)
play_GOL(gameState, N)

