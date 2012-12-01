class Block_glass(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/glass/glass.png')
    def get_name(self):
        return "glass"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        collision = Collision()
        return collision
block_class = Block_glass