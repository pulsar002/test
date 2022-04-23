# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
import pickle

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.Mapmanager = Mapmanager()
        #self.Mapmanager.create_floor()
        #self.Mapmanager.create_walls()
        #self.Mapmanager.rand_map()
        self.Mapmanager.load_map()
        gg = Hero((1,10,2),self.Mapmanager)

test = Game()
test.run()