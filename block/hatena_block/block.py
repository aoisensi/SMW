class Block_hatena_block(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/hatena_block/block.png')
    def get_name(self):
        return "hatena_block"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        if x==0:
            if y==0:
                return 7
            elif y==15:
                return 1
            else:
                return 4
        elif x==15:
            if y==0:
                return 9
            elif y==15:
                return 3
            else:
                return 6
        else:
            if y==0:
                return 8
            elif y==15:
                return 2
            else:
                return 5
block_class = Block_hatena_block