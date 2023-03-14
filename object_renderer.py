import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
    
    def draw(self):
        self.render_game_objects()

    #reenderowanie obiektów
    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    #statyczna metoda pozyskująca i ustaljąca rozdzielczość tekstur
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    #przypisujemy teksture do numerka
    def load_wall_textures(self):
        return{
            1: self.get_texture('resources/textures/1.png'),            
        }