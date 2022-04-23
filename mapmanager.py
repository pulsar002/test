# напиши здесь код создания и управления картой

import pickle

class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.startNew()

    def set_brick(self):
        self.texture = "brick.png"

    def set_stone(self):
        self.texture = "stone.png"

    def startNew(self):
        self.land = render.attachNewNode("Land")
    
    def clear(self):
        self.land.removeNode()
        self.startNew()

    def addBlock(self, position, texture=None):
        block = loader.loadModel(self.model)
        if texture is None:
            texture = loader.loadTexture(self.texture)

        block.setPos(position)
#        print(block.getTag("at"))
        block.reparentTo(self.land)

    def check_position(self, position):
        position = position[0], position[1], position[2] 
        for block in self.land.getChildren():
            if position == block.getPos():
                return True
        return False

    def create_floor(self):
        self.texture = 'brick.png'
        for x in range(10):
            for y in range(10):
                self.addBlock((x,y,0))

    def create_walls(self):
        self.texture = 'wood.png'
        for x in range(10):
            for y in range(0,10):
                for z in range(3):
                    self.addBlock((x,y,z))

    def save_map(self):
        all_blocks = self.land.getChildren()
        with open("map.dat","wb") as file:
            pickle.dump(len(all_blocks),file)
            for block in all_blocks:
                x,y,z = list(block.getPos())
                pickle.dump(x,file)
                pickle.dump(y,file)
                pickle.dump(z,file)
                pickle.dump(block.getTexture(),file)

    def load_pickle_map(self):
        self.clear()
        with open("map.dat","rb") as file:
            n_blocks = pickle.load(file)
            for i in range(n_blocks):
                x = pickle.load(file)
                y = pickle.load(file)
                z = pickle.load(file)
                texture = pickle.load(file)
                self.addBlock((x,y,z),texture)

    def load_map(self):
        with open("map.txt","r") as file:
            date = file.readlines()

        x = 0
        for str in date:
            y = 0
            temp = str.split(" ")[:-1]
            for max_z in temp:
                for z in range(int(max_z)+1):
                    self.addBlock((x,y,z))
                y += 1
            x += 1

    def rand_map(self):
        for x in range(10):
            for y in range(10):
                for z in range(10):
                    if random() > z*0.1:
                        self.addBlock((x,y,z))