from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self,):
      self.rect.centerx -= ENTITY_SPEED[self.name] #criou uma velocidade dinamica para cada item do bg parallax
      if self.rect.right <= 0: #se o canto da minha imagem chegar na extrema esquerda 
        self.rect.left = WIN_WIDTH # joga o lado da esquerda para o valor do tamanho da tela  
   
