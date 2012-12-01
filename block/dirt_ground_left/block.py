class Block_dirt_ground_left(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/dirt_ground_left/block.png')
    def get_name(self):
        return "dirt_ground_left"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        if y == 0:
            if x == 0:
                return 7
            else:
                return 8
        else:
            return 5
block_class = Block_dirt_ground_left