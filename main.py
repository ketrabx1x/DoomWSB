import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

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
                    self.global_trigger = False
                    self.global_event = pg.USEREVENT + 0
                    pg.time.set_timer(self.global_event, 40)
                    self.new_game()
                    self.music()
                    
        #tworzenie instancji mapy i gracza
          def new_game(self):
                    self.map = Map(self)
                    self.player = Player(self)
                    self.object_renderer = ObjectRenderer(self)
                    self.raycasting = RayCasting(self)
                    self.object_handler = ObjectHandler(self)
                    self.weapon = Weapon(self)
                    self.sound = Sound(self)
                    self.pathfinding = PathFinding(self)

          #aktualizowanie ekranu
          def update(self):
                    self.player.update()
                    self.raycasting.update()
                    self.object_handler.update()
                    self.weapon.update()
                    pg.display.flip()

                    #wyświetlanie ilości kl/s
                    self.delta_time = self.clock.tick(FPS)
                    pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

          #rysowanie ekranu
          def draw(self):
                  #self.screen.fill('black')
                  self.object_renderer.draw()
                  self.weapon.draw()
                  #self.map.draw()
                  #self.player.draw()

          #wychodzenie z gry
          def check_events(self):
                self.global_trigger = False
                for event in pg.event.get():
                        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                                pg.quit()
                                sys.exit()
                        elif event.type == self.global_event:
                                self.global_trigger = True
                        self.player.single_fire_event(event)
                                
          #pętla w której działa gra
          def run(self):
                    while True:
                              self.check_events()
                              self.update()
                              self.draw()
          #muzyka
          def music(self):
                    pg.mixer.music.load('resources/sounds/thunderstruck.mp3')
                    pg.mixer.music.play(-1)
                    pg.mixer.music.set_volume(0.3)

#Uruchamianie gry

if __name__ == '__main__':
          game = Game()
          game.run()