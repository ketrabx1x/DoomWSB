import pygame as pg

#tworzenie mapy 1 = ściana 


_ = False
mini_map = [
        #  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19
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
                    self.rows = len(self.mini_map)
                    self.cols = len(self.mini_map[0])
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