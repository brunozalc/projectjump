# ===== Inicialização =====
# --- Importando e inicializando pacotes
import pygame, random, math, sys
from config import *
from funcs import *
from init_screen import init_screen
from menu import menu
from level1 import level1
from level2 import level2
from level3 import level3
from end_screen import game_over
 
pygame.init()
pygame.mixer.init()

# --- Gerando a tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project Jump")

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    if state == MENU:
        main_menu = menu(window)
        state = main_menu[0]
        dificuldade = main_menu[1]
    elif state == LEVEL1:
        lvl1 = level1(window, dificuldade)
        state = lvl1[0]
        tempo = lvl1[1]
        dificuldade = lvl1[2]
        if state == END_SCREEN:
            state = game_over(window, "level1", tempo, dificuldade)
    elif state == LEVEL2:
        lvl2 = level2(window, dificuldade)
        state = lvl2[0]
        tempo = lvl2[1]
        dificuldade = lvl2[2]
        if state == END_SCREEN:
            state = game_over(window, "level2", tempo, dificuldade)
    elif state == LEVEL3:
        lvl3 = level3(window, dificuldade)
        state = lvl3[0]
        tempo = lvl3[1]
        dificuldade = lvl3[2]
        if state == END_SCREEN:
            state = game_over(window, "level3", tempo, dificuldade)

# ===== Finalização =====
pygame.quit() # Função do pygame que finaliza os recursos inicializados