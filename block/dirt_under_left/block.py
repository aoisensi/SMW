class Block_dirt_under_left(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/dirt_under_left/block.png')
    def get_name(self):
        return "dirt_under_left"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        collision = Collision()
        return collision
block_class = Block_dirt_under_left