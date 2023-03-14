import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *

class Game:
          def __init__(self):
                    #inicjacja modułu pyGame
                    pg.init()
                    #wyłączenie widoczności kursora
                    pg.mouse.set_visible(False)
                    #utworzenie ekranu i ustawienie rozdzielczości
                    self.screen = pg.display.set_mode(RES)
                    #Utworzenie zegara (do utrzymywania konkretnej ilości kl/s)
                    self.clock = pg.time.Clock()
                    self.delta_time = 1
                    self.new_game()
                    self.music()
                    
        #tworzenie instancji mapy i gracza
          def new_game(self):
                    self.map = Map(self)
                    self.player = Player(self)
                    self.object_renderer = ObjectRenderer(self)
                    self.raycasting = RayCasting(self)

          #aktualizowanie ekranu
          def update(self):
                    self.player.update()
                    self.raycasting.update()
                    pg.display.flip()

                    #wyświetlanie ilości kl/s
                    self.delta_time = self.clock.tick(FPS)
                    pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

          #rysowanie ekranu
          def draw(self):
                  #self.screen.fill('black')
                  self.object_renderer.draw()
                  #self.map.draw()
                  #self.player.draw()

          #wychodzenie z gry
          def check_events(self):
                    for event in pg.event.get():
                              if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                                        pg.quit()
                                        sys.exit()
          #pętla w której działa gra
          def run(self):
                    while True:
                              self.check_events()
                              self.update()
                              self.draw()
          #muzyka
          def music(self):
                    pg.mixer.music.load('thunderstruck.mp3')
                    pg.mixer.music.play(-1)
                    pg.mixer.music.set_volume(0.5)

#Uruchamianie gry

if __name__ == '__main__':
          game = Game()
          game.run()