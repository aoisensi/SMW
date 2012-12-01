class Block_dirt_ground_middle(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/dirt_ground_middle/block.png')
    def get_name(self):
        return "dirt_ground_middle"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        if y == 0:
            return 8
        else:
            return 5
block_class = Block_dirt_ground_middle