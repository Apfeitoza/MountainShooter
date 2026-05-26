from abc import ABC, abstractmethod
import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png') #ja puxamos aqui a surface e o rect abaixo, quando criar as entidades não precisa fazer.
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod #precisa definir o abstract method 
    def move(self, ): #movimento é implementado pela classes filhas
        pass
