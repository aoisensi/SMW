class Block_dirt_ground_left(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/dirt_ground_left/block.png')
    def get_name(self):
        return "dirt_ground_left"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        collision = Collision()
        if y == 0:
            collision.top = True
            if x == 0:
                collision.left = True
        return collision
block_class = Block_dirt_ground_left