from code.Const import COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, MENU_OPTION, WIN_WIDTH

import pygame.image
from pygame import Rect, Surface
from pygame.font import Font


class Menu:
    def __init__(self, window):
        self.window = window
        # 1 etapa: carregar a imagem
        self.surf = pygame.image.load('asset/MenuBg.png').convert_alpha()
        # criar um retangulo para posicionar a imagem (olhar doc do pygame)
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(
        self,
    ):
        menu_option = 0
        # Inserção do Som
        pygame.mixer_music.load('asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # se usar o parametro -1 a musica roda em loop

        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            # Texto do Menu
            self.menu_text(
                40, 'Mountain', COLOR_ORANGE, ((WIN_WIDTH / 2), 70)
            )  # tamanho do texto, texto, cor do texto, centralização
            self.menu_text(40, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            # Para o texto do menu ele criou uma tupla com varias strings e um laço para colocar elas no menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(
                        20,
                        MENU_OPTION[i],
                        COLOR_YELLOW,
                        ((WIN_WIDTH / 2), 200 + 25 * i),
                    )
                else:
                    self.menu_text(
                        20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i)
                    )

            pygame.display.flip()

            #  Check for all events
            for event in pygame.event.get():  # sem essa linha ele não roda no mac
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if (
                        event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER
                    ):  # ENTER KEY
                        return MENU_OPTION[menu_option]

    def menu_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple
    ):
        text_font: Font = pygame.font.SysFont(
            name='IBM Plex Mono', size=text_size
        )  # cria o texto (vira imagem)
        text_surf: Surface = text_font.render(
            text, True, text_color
        ).convert_alpha()  # converte o texto em uma surface
        text_rect: Rect = text_surf.get_rect(
            center=text_center_pos
        )  # cria um retangulo para colocar o texto
        self.window.blit(source=text_surf, dest=text_rect)
