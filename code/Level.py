import random
import sys
from code.EntityMediator import EntityMediator
from code.Const import COLOR_WHITE, EVENT_ENEMY, MENU_OPTION, SPAWN_TIME, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory

import pygame


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

        self.timeout = 20000  # 20 segundos

    def run(
        self,
    ):
        pygame.mixer_music.load((f'./asset/{self.name}.mp3'))
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # taxa de frames(?)
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(
                    source=ent.surf, dest=ent.rect
                )  # blit - desenhar imagem na tela
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # printed text
            self.level_text(
                14,
                f'{self.name} - Timeout: {self.timeout / 1000: .1f}s',
                COLOR_WHITE,
                (10, 5),
            )
            self.level_text(
                14, f'fps: {clock.get_fps(): .0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35)
            )
            self.level_text(
                14,
                f'entidades: {len(self.entity_list)}',
                COLOR_WHITE,
                (10, WIN_HEIGHT - 20),
            )
            #faz a mediação de colisões dentro do EntityMediator
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pygame.display.flip()
        pass

    def level_text(
        self, text_size: int, text: str, text_color: tuple, text_position: tuple
    ):
        text_font: pygame.Font = pygame.font.SysFont(
            name='IBM Plex Mono', size=text_size
        )
        text_surf: pygame.Surface = text_font.render(
            text, True, text_color
        ).convert_alpha()  # converte o texto em uma surface
        text_rect: pygame.Rect = text_surf.get_rect(
            left=text_position[0], top=text_position[1]
        )  # cria um retangulo para colocar o texto
        self.window.blit(source=text_surf, dest=text_rect)
