class Hero():

    def __init__(self,pos,manager):

        self.hero = loader.loadModel("smiley")
        self.manager = manager

        self.hero.setPos(pos)
        self.hero.setScale(0.3)
        self.hero.setColor(1,0,0)

        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos((0,0,1.5))

    def accept_events(self):
        base.accept("a",self.turn_left)
        base.accept("a"+"-repeat",self.turn_left)
        base.accept("d",self.turn_right)
        base.accept("d"+"-repeat",self.turn_right)
        base.accept("w",self.move)
        base.accept("w"+"-repeat",self.move)
        base.accept("s",self.move_back)
        base.accept("s"+"-repeat",self.move_back)
        base.accept("q",self.build)
        base.accept("e",self.is_empty)
        base.accept("i",self.manager.save_map)
        base.accept("o",self.manager.load_pickle_map)
        base.accept("1",self.manager.set_brick)
        base.accept("2",self.manager.set_stone)

    def is_empty(self):
        x,y = self.check_angle()
        now = self.hero.getPos()
        res = (now[0]+x,now[1]+y,now[2])
        return not self.manager.check_position(res)

    def up_is_empty(self):
        x,y = self.check_angle()
        now = self.hero.getPos()
        res = now[0]+x,now[1]+y,now[2] + 1
        return not self.manager.check_position(res)

    def down_is_empty(self):
        x,y = self.check_angle()
        now = self.hero.getPos()
        res = now[0],now[1],now[2] -1 
        return not self.manager.check_position(res)

    
    def gravity(self):
        i = 0
        while self.down_is_empty():
            i += 1
            if i >= 5000:
                exit()
            now = self.hero.getPos()
            res = now[0],now[1],now[2] - 1
            self.hero.setPos(res)

    def move(self):
        self.gravity()
        x,y = self.check_angle()
        now  =self.hero.getPos()
        res = (now[0]+x,now[1]+y,now[2])

        if self.is_empty():
            self.hero.setPos(res)
        else:
            if self.up_is_empty():
                res = now[0]+x,now[1]+y,now[2] + 1
                self.hero.setPos(res)

    def move_back(self):
        x,y = self.check_angle()
        now = self.hero.getPos()
        res = (now[0]-x,now[1]-y,now[2])
        self.hero.setPos(res)

    def build(self):
        now = self.hero.getPos()
        x,y = self.check_angle()
        block_pos = now[0]+x,now[1]+y,now[2]
        self.manager.addBlock(block_pos)

    def turn_left(self):
        self.hero.setH((self.hero.getH()+5)%360)

    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)%360)

    def check_angle(self):
        angle = self.hero.getH()
        if 0 <= angle <= 20:
            return 0,1
        if 20 <= angle <= 65:
            return -1,1
        if 65 <= angle <= 110:
            return -1,0
        if 110 <= angle <= 155:
            return -1,-1
        if 155 <= angle <= 200:
            return 0, -1
        if 200 <= angle <= 245:
            return 1, -1
        if 245 <= angle <= 290:
            return 1, 0
        if 290 <= angle <= 355:
            return 1, 1

