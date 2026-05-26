from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Level import Level
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
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, "Level1", menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close window
                quit()  # end pygame
            else:
                pass
