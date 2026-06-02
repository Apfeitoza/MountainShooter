import random
import sys
from code.Const import (
    C_CYAN,
    C_GREEN,
    C_WHITE,
    EVENT_ENEMY,
    EVENT_TIMEOUT,
    MENU_OPTION,
    SPAWN_TIME,
    TIMEOUT_LEVEL,
    TIMEOUT_STEP,
    WIN_HEIGHT,
)
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player

import pygame


class Level:
    def __init__(
        self, window: pygame.Surface, name: str, game_mode: str, player_score: list[int]
    ):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
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
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(
                        14,
                        f'Player 1 - Health: {ent.health} | Score:{ent.score}',
                        C_GREEN,
                        (10, 25),
                    )
                if ent.name == 'Player2':
                    self.level_text(
                        14,
                        f'Player 2 - Health: {ent.health} | Score:{ent.score}',
                        C_CYAN,
                        (10, 45),
                    )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                            
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # printed text
            self.level_text(
                14,
                f'{self.name} - Timeout: {self.timeout / 1000: .1f}s',
                C_WHITE,
                (10, 5),
            )
            self.level_text(
                14, f'fps: {clock.get_fps(): .0f}', C_WHITE, (10, WIN_HEIGHT - 35)
            )
            self.level_text(
                14,
                f'entidades: {len(self.entity_list)}',
                C_WHITE,
                (10, WIN_HEIGHT - 20),
            )
            # faz a mediação de colisões dentro do EntityMediator
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pygame.display.flip()

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
