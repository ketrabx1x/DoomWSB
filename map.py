import pygame as pg

#tworzenie mapy 1 = ściana 


_ = False
mini_map = [
          [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,],
          [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
          [1, _, _, 1, _, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _, 1, _, _, 3,],
          [1, _, _, 4, _, 1, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, 1,],
          [1, _, _, 4, _, 1, _, _, _, _, _, _, _, _, 1, _, 1, _, _, 1,],
          [1, _, _, 4, _, 1, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, 1,],
          [1, _, _, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, _, 1, _, _, 1,],
          [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1,],
          [1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1,],
]

#Tworzenie klasy mapa i przypisanie atrybutów
class Map:
          def __init__(self, game):
                    self.game = game
                    self.mini_map = mini_map
                    self.world_map = {}
                    self.get_map()
        
        #pozyskiwanie mapy poprzez zapisywanie koordynatów z cyferką 1 do słownika
          def get_map(self):
                    for j, row in enumerate(self.mini_map):
                              for i, value in enumerate(row):
                                        if value:
                                                  self.world_map[(i, j)] = value
          #rysowanie scian
          def draw(self):
                    [pg.draw.rect(self.game.screen, 'darkgrey', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
                    for pos in self.world_map]