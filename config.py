from os import path

# Pastas onde estão os assets
IMG_DIR = path.join(path.dirname(__file__), "assets", "images") # Pasta de imagens
SND_DIR = path.join(path.dirname(__file__), "assets", "sounds") # Pasta de sons

# Dados gerais do jogo
WIDTH = 500    # Largura da tela
HEIGHT = 600   # Altura da tela
FPS = 45       # Frames por segundo

# Define tamanhos
PLAYER_WIDTH = 51
PLAYER_HEIGHT = 51
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 100

# Define cores
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Quantidade de inimigos e outros
PLATFORM_NUMBER = 1

# Estados do jogo
INIT = 0
LEVEL1 = 1
LEVEL2 = 2
LEVEL3 = 3
END_SCREEN = 4
QUIT = 5