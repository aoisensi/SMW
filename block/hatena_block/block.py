class Block_hatena_block(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/hatena_block/block.png')
    def get_name(self):
        return "hatena_block"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        collision = Collision()
        collision.left = x == 0
        collision.right = x == 15
        collision.up = y == 0
        collision.down = y == 15
        return collision
block_class = Block_hatena_block