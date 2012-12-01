class Block_dirt_ground_right(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/dirt_ground_right/block.png')
    def get_name(self):
        return "dirt_ground_left"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        if y == 0:
            if x == 15:
                return 9
            else:
                return 8
        else:
            return 5
block_class = Block_dirt_ground_right