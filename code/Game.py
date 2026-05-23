from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu

import pygame


class Game:
    def __init__(self):
        pygame.init()
        # Criar janela do jogo(surface)
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            # aqui ele abre o menu
            menu = Menu(self.window)
            menu.run()
            pass
