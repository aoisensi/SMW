class Sprite_kinoko(Sprite):

    image = None
    #落下速度
    fall = 0
    #移動方向(右ならTrue 左ならFalse)
    dir = True
    on_ground = True
    coordinate = None

    def __init__(self, id, stage, coordinate):
        self.stage = stage
        self.coordinate = coordinate

    @staticmethod
    def get_name():
        return 'kinoko'

    @staticmethod
    def load_sprite():
        Sprite_kinoko.image = pygame.image.load('./sprite/kinoko/kinoko.png')

    def render(self):
        return (Sprite_kinoko.image, self.coordinate)

    def update(self):
        x = self.coordinate[0]
        y = self.coordinate[1]
        if(self.dir):
            #右向きなう
            col_x = x + 15
            for col_y in range(0, 16):
                col_y += y
                collision = stage.get_collision(col_x, col_y)
                if(collision.left and not collision.up):
                    self.dir = False
                    is_break = True
                    break
            else:
                x += 1
        else:
            #左向きなう
            col_x = x
            for col_y in range(0, 16):
                col_y += y
                collision = stage.get_collision(col_x, col_y)
                if(collision.right and not collision.up):
                    self.dir = True
                    is_break = True
                    break
            else:
                x -= 1
        #落下判定
        col_down_x = x + (self.dir if 8 else 7)
        if(self.on_ground):
            for col_down_y_l in range(-2, 3):
                col_down_y = y + 16 + col_down_y_l
                if(self.stage.get_collision(col_down_x, col_down_y).up):
                    y += col_down_y_l
                    self.on_ground = True
                    break
            else:
                self.on_ground = False
        elif(self.fall > 0):
            for col_down_y_l in range(0, int(self.fall)):
                col_down_y = y + 16 + col_down_y_l
                if(self.stage.get_collision(col_down_x, col_down_y).up):
                    y += col_down_y_l
                    self.on_ground = True
                    self.fall = 0
                    break

        if self.fall < 3 and not self.on_ground:
            self.fall += 0.2
        y += self.fall



        self.coordinate = (x, y)








sprite_class = Sprite_kinoko
