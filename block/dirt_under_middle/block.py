class Block_dirt_under_middle(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/dirt_under_middle/block.png')
    def get_name(self):
        return "dirt_under_middle"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        return 5
block_class = Block_dirt_under_middle