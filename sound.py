import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.mp3')
        self.npc_pain = pg.mixer.Sound(self.path + 'pain.mp3')
        self.npc_shot = pg.mixer.Sound(self.path + 'attack.mp3')
        self.npc_death = pg.mixer.Sound(self.path + 'death.mp3')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.mp3')