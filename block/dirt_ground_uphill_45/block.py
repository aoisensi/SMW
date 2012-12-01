class Block_dirt_ground_uphill_45(object):
    image = None
    def __init__(self):
        self.image = pygame.image.load('./block/dirt_ground_uphill_45/block.png')
    def get_name(self):
        return "dirt_ground_uphill_45"
    def get_picture(self):
        return self.image
    def get_collision(self, x, y):
        collision = Collision()
        if(15-x==y):
            collision.up = True
        return collision
block_class = Block_dirt_ground_uphill_45