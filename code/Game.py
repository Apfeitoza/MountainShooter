from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Level import Level
from code.Menu import Menu

import pygame

from code.Score import Score


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
            #aqui ele recebe o score
            score = Score(self.window)

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0,0] #[Player1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close window
                quit()  # end pygame
            else:
                pass
